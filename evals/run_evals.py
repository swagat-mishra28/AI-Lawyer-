"""Run every test case end-to-end and save UNEDITED outputs + an automatic scorecard.

    python -m evals.run_evals                         # all cases, default model from .env
    python -m evals.run_evals --only dep-hinglish     # one case
    python -m evals.run_evals --provider groq --model llama-3.3-70b-versatile

Writes outputs/<model>/<case>.json (full trace), <case>.md (readable), summary.md, summary.csv.
Automatic checks are objective (category, language, escalation, deadline maths, forbidden patterns,
guard). Answer quality (helpfulness, tone, legal soundness) is reviewed by a human: see
outputs/<model>/REVIEW.md.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
import time
import traceback
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from nyaya import drafter  # noqa: E402
from nyaya.assistant import LANG_OVERRIDES, Session  # noqa: E402
from nyaya.config import llm_settings  # noqa: E402
from nyaya.llm import LLM  # noqa: E402
from nyaya.notice import explain  # noqa: E402
from nyaya.sparring import Sparring  # noqa: E402


def run_case(case: dict, llm: LLM, today: dt.date) -> dict:
    out: dict = {"id": case["id"], "title": case["title"], "input": {k: case[k] for k in case if k not in ("expect",)}}
    if case.get("notice_text"):
        lang = LANG_OVERRIDES.get(case.get("notice_language", "English")) or ("en", "English")
        res = explain(llm, case["notice_text"], lang, received_on=dt.date.fromisoformat(case["notice_received"]), today=today)
        out.update(kind="notice", reply=res["reply_markdown"], reply_rendered=res["reply_rendered"], rules=res["rules"],
                   extract=res["extract"], guard=res["guard_log"], kb_ids=res["kb_ids"], case={"category": "notice"})
        return out
    sess = Session(llm=llm, today=today)
    turns = []
    for t in case["turns"]:
        r = sess.turn(t)
        turns.append({"user": t, "reply": r.reply_markdown, "case": r.case, "rules": r.rules, "kb_ids": r.kb_ids,
                      "guard": r.guard_log, "sources": r.sources})
    last = turns[-1]
    out.update(kind="chat", turns=turns, reply=last["reply"], rules=last["rules"], guard=last["guard"],
               case=last["case"], kb_ids=last["kb_ids"])
    if case.get("draft") and last["case"].get("category") in drafter.DOCS:
        try:
            out["draft"] = drafter.draft(llm, last["case"], case["draft"], today=today)
        except ValueError as e:
            out["draft_error"] = str(e)
    if case.get("spar"):
        sp = Sparring(llm, last["case"])
        for line in case["spar"]:
            sp.say(line)
        coach_text, coach_guard = sp.coach()
        out["spar"] = {"transcript": sp.transcript, "coach": coach_text, "coach_guard": coach_guard}
    return out


def score(case: dict, out: dict) -> dict:
    exp = case.get("expect", {})
    reply = out.get("reply", "") or ""
    reply_l = reply.lower()
    levels = {e["level"] for e in out["rules"]["escalations"]}
    checks: dict[str, bool] = {}
    if "category" in exp:
        checks["category"] = out["case"].get("category") == exp["category"]
    if "language" in exp:
        checks["language"] = out["case"].get("language") == exp["language"]
    for lvl in exp.get("escalation", []):
        checks[f"escalates:{lvl}"] = lvl in levels
    if exp.get("no_escalation"):
        checks["no_false_alarm"] = not (levels & {"emergency", "lawyer_now"})
    if exp.get("deadline"):
        checks["deadline_computed"] = bool(out["rules"]["deadlines"])
    if exp.get("deadline_date"):
        checks["deadline_date"] = any(d["date"] == exp["deadline_date"] for d in out["rules"]["deadlines"])
    if exp.get("forum"):
        checks["forum"] = exp["forum"].lower() in ((out["rules"].get("forum") or {}).get("forum", "").lower())
    for i, group in enumerate(exp.get("mention_any", [])):
        checks[f"mentions:{group[0]}"] = any(str(g).lower() in reply_l for g in group)
    for rx in exp.get("not_regex", []):
        checks[f"absent:{rx}"] = not re.search(rx, reply)
    checks["guard_clean"] = out["guard"]["final_violations"] == 0
    if out.get("draft"):
        checks["draft_no_legal_refs_in_facts"] = not out["draft"]["facts_guard"]["violations"]
    return checks


def to_markdown(case: dict, out: dict, checks: dict) -> str:
    L = [f"# {out['id']} - {out['title']}", ""]
    if out["kind"] == "notice":
        L += ["## Input notice", "```", case["notice_text"].strip(), "```", "", "## Extracted",
              "```json", json.dumps(out["extract"], ensure_ascii=False, indent=1), "```", "", "## Reply (unedited)", out["reply"]]
    else:
        for i, t in enumerate(out["turns"], 1):
            L += [f"## Turn {i} - user", "> " + t["user"].replace("\n", "\n> "), "", f"## Turn {i} - Nyaya Saathi (unedited)",
                  t["reply"], ""]
        L += ["## Case file (intake)", "```json", json.dumps(out["case"], ensure_ascii=False, indent=1), "```"]
    L += ["", "## Computed by code", "```json",
          json.dumps({k: out["rules"].get(k) for k in ("deadlines", "forum", "fee", "escalations")}, ensure_ascii=False, indent=1), "```",
          "", f"## Guard: first pass {len(out['guard']['first_pass']['violations'])} violation(s), repaired={out['guard']['repaired']}, "
          f"scrubbed={out['guard']['scrubbed']}, final={out['guard']['final_violations']}"]
    for v in out["guard"]["first_pass"]["violations"]:
        L.append(f"- {v['kind']}: `{v['text']}` - {v['detail']}")
    if out.get("draft"):
        L += ["", f"## Draft: {out['draft']['title']}", out["draft"]["markdown"]]
    if out.get("spar"):
        L += ["", "## Practice mode"]
        for m in out["spar"]["transcript"]:
            L.append(f"- **{'User' if m['role'] == 'user' else 'Other side'}:** {m['content']}")
        L += ["", "### Coach feedback", out["spar"]["coach"]]
    L += ["", "## Automatic checks"] + [f"- {'PASS' if ok else 'FAIL'} {k}" for k, ok in checks.items()]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider")
    ap.add_argument("--model")
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--today", default="2026-11-21")
    ap.add_argument("--out", default=None)
    ap.add_argument("--pause", type=float, default=4.0, help="seconds between cases (free-tier rate limits)")
    args = ap.parse_args()

    settings = llm_settings(args.provider, args.model)
    llm = LLM(settings)
    today = dt.date.fromisoformat(args.today)
    cases = yaml.safe_load((ROOT / "evals" / "cases.yaml").read_text(encoding="utf-8"))
    if args.only:
        cases = [c for c in cases if c["id"] in args.only]
    slug = re.sub(r"[^a-zA-Z0-9.\-]+", "_", settings.label)
    out_dir = Path(args.out) if args.out else ROOT / "outputs" / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    for c in cases:
        print(f"-> {c['id']}", flush=True)
        n_before = len(llm.calls)
        t0 = time.time()
        try:
            out = run_case(c, llm, today)
            checks = score(c, out)
            out["checks"] = checks
            (out_dir / f"{c['id']}.md").write_text(to_markdown(c, out, checks), encoding="utf-8")
        except Exception as e:  # noqa: BLE001 - record failures honestly
            out = {"id": c["id"], "error": repr(e), "traceback": traceback.format_exc()}
            checks = {"ran": False}
        out["calls"] = [vars(x) for x in llm.calls[n_before:]]
        out["seconds"] = round(time.time() - t0, 1)
        (out_dir / f"{c['id']}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
        g = out.get("guard", {})
        rows.append({"id": c["id"], "title": c["title"], "passed": sum(checks.values()), "total": len(checks),
                     "failed": ";".join(k for k, v in checks.items() if not v),
                     "first_pass_violations": len(g.get("first_pass", {}).get("violations", [])) if g else "",
                     "repaired": g.get("repaired", ""), "final_violations": g.get("final_violations", ""),
                     "seconds": out["seconds"]})
        print(f"   {rows[-1]['passed']}/{rows[-1]['total']} {rows[-1]['failed']}", flush=True)
        time.sleep(args.pause)

    with (out_dir / "summary.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    usage = llm.usage_summary()
    tp, tt = sum(r["passed"] for r in rows), sum(r["total"] for r in rows)
    caught = sum(r["first_pass_violations"] or 0 for r in rows)
    md = [f"# Eval run - {settings.label}", "", f"- Date pinned to: {args.today}", f"- Cases: {len(rows)}",
          f"- Automatic checks passed: **{tp}/{tt}** ({100 * tp / max(tt, 1):.0f}%)",
          f"- Cases with all checks passing: {sum(r['passed'] == r['total'] for r in rows)}/{len(rows)}",
          f"- Unverified legal references caught by the guard on first draft: {caught}; shown to users after guard: "
          f"{sum(r['final_violations'] or 0 for r in rows)}",
          f"- Model usage: {usage['calls']} calls, {usage['input_tokens']:,} input + {usage['output_tokens']:,} output tokens, "
          f"{usage['seconds']} s total model time ({usage['failed_attempts']} rate-limited/failed attempts retried)", "",
          "| case | checks | failed | guard caught (1st pass) | repaired |", "|---|---|---|---|---|"]
    md += [f"| {r['id']} | {r['passed']}/{r['total']} | {r['failed'] or '-'} | {r['first_pass_violations']} | {r['repaired']} |" for r in rows]
    (out_dir / "summary.md").write_text("\n".join(md), encoding="utf-8")
    (out_dir / "run_meta.json").write_text(json.dumps({"model": settings.label, "today": args.today, "usage": usage,
                                                       "run_at": dt.datetime.now().isoformat(timespec="seconds")}, indent=1))
    print("\n".join(md[:8]))


if __name__ == "__main__":
    main()
