"""Explain a notice the person received: extract (LLM) -> compute deadlines and severity (code)
-> explain in their language (LLM, grounded) -> guard."""
from __future__ import annotations

import datetime as dt
import json
import re

from . import guard, prompts, rules
from .assistant import grounded_generate, script_hint
from .kb import load_kb
from .llm import LLM

SEVERITY = {
    "court_summons": ("high", "court_summons"),
    "police_notice": ("high", "police_or_arrest"),
    "cheque_bounce_notice": ("high", "cheque_bounce_against_user"),
    "eviction_notice": ("medium", "eviction_threat"),
    "legal_demand_notice": ("medium", None),
    "reply_notice": ("low", None),
    "other": ("unknown", None),
}


def read_document(data: bytes, filename: str) -> str:
    if filename.lower().endswith(".pdf"):
        from pypdf import PdfReader
        import io

        return "\n".join((p.extract_text() or "") for p in PdfReader(io.BytesIO(data)).pages)
    return data.decode("utf-8", errors="ignore")


def quoted_refs(laws_mentioned: list[str]) -> list[tuple[str | None, str]]:
    """Sections the notice itself cites - the explanation may repeat these (marked as 'the notice mentions')."""
    kb = load_kb()
    aliases = guard._alias_index(kb)
    out = []
    for s in laws_mentioned or []:
        act = next((k for a, k in aliases if a in s.lower()), None)
        for n in re.findall(r"\d{1,4}[A-Z]?", s):
            if not re.fullmatch(r"(19|20)\d\d", n):
                out.append((act, n))
    return out


def explain(llm: LLM, doc_text: str, language: tuple[str, str] = ("en", "English"),
            received_on: dt.date | None = None, today: dt.date | None = None) -> dict:
    today = today or dt.date.today()
    kb = load_kb()
    ext = llm.json("You extract facts from legal documents precisely. Never invent.",
                   [{"role": "user", "content": prompts.NOTICE_EXTRACT.format(today=today.isoformat(), doc=doc_text[:12000])}],
                   purpose="notice_extract")
    doc_type = ext.get("doc_type") or "other"
    severity, flag = SEVERITY.get(doc_type, ("unknown", None))
    case = {"category": "notice", "sub_type": doc_type.replace("_", " "),
            "user_role": "notice recipient", "red_flags": [flag] if flag else [],
            "amounts": {"disputed": ext.get("amount_demanded")},
            "dates": {"notice_received": (received_on or today).isoformat()}}
    # deadline written in the notice: N days from receipt
    if ext.get("deadline_days"):
        try:
            case["dates"]["notice_deadline"] = ((received_on or today) + dt.timedelta(days=int(ext["deadline_days"]))).isoformat()
        except (TypeError, ValueError):
            pass
    if ext.get("hearing_date"):
        case["dates"]["notice_deadline"] = ext["hearing_date"]
    computed = rules.compute(case, today)

    text_for_triggers = doc_type + " " + doc_text[:3000]
    entries = kb.retrieve("notice", text_for_triggers)
    q = quoted_refs(ext.get("laws_mentioned") or [])
    system = prompts.NOTICE_EXPLAIN.format(
        doc_type=doc_type.replace("_", " "), language_name=language[1] + script_hint(language[0]),
        knowledge=kb.format_for_prompt(entries), extract=json.dumps(ext, ensure_ascii=False, indent=1),
        facts=json.dumps({k: computed[k] for k in ("today", "deadlines", "escalations")}, ensure_ascii=False, indent=1))
    text, glog = grounded_generate(llm, system, [{"role": "user", "content": "Please explain this notice to me."}], kb,
                                   entries, purpose="notice_explain", quoted_refs=q, max_tokens=2000)
    rendered, sources = guard.render_citations(text, kb)
    return {"extract": ext, "severity": severity, "rules": computed, "reply_markdown": text,
            "reply_rendered": rendered, "sources": sources, "guard_log": glog, "kb_ids": [e.id for e in entries]}
