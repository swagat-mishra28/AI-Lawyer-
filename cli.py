"""Terminal interface - handy for running on a new input during an interview.

    python cli.py chat                                 # interactive conversation
    python cli.py ask "landlord not returning my deposit..."
    python cli.py notice path/to/notice.txt --lang Hindi
    python cli.py chat --provider groq --model llama-3.3-70b-versatile
"""
from __future__ import annotations

import argparse
import json
import re
import sys

from nyaya import drafter
from nyaya.assistant import LANG_OVERRIDES, Session
from nyaya.config import llm_settings
from nyaya.llm import LLM
from nyaya.notice import explain, read_document

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def plain(md: str) -> str:
    return re.sub(r"<sup>\[(\d+)\]</sup>", r"[\1]", md)


def show(res):
    for e in res.rules["escalations"]:
        print(f"!! [{e['level']}] {e['reason']} {e['action']}")
    print("\n" + plain(res.reply_rendered) + "\n")
    for s in res.sources:
        print(f"  [{s['n']}] {s['title']} - {s['law']}" + ("" if s["confidence"] == "high" else " (verify)"))
    for d in res.rules["deadlines"]:
        print(f"  ⏰ {d['label']}: {d['date']} ({d['days_left']} days left)")
    g = res.guard_log
    print(f"  [guard] refs checked {g['first_pass']['refs_checked']}, caught {len(g['first_pass']['violations'])}, "
          f"shown unverified {g['final_violations']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["chat", "ask", "notice"])
    ap.add_argument("text", nargs="?")
    ap.add_argument("--provider")
    ap.add_argument("--model")
    ap.add_argument("--lang", default="auto", choices=list(LANG_OVERRIDES))
    ap.add_argument("--draft", help="after 'ask', draft this document type (e.g. legal_notice)")
    a = ap.parse_args()
    llm = LLM(llm_settings(a.provider, a.model))
    print(f"(model: {llm.label})")

    if a.mode == "notice":
        with open(a.text, "rb") as f:
            doc = read_document(f.read(), a.text)
        lang = LANG_OVERRIDES.get(a.lang) or ("en", "English")
        r = explain(llm, doc, lang)
        for e in r["rules"]["escalations"]:
            print(f"!! [{e['level']}] {e['reason']} {e['action']}")
        print(plain(r["reply_rendered"]))
        return

    sess = Session(llm=llm, language_override=a.lang)
    if a.mode == "ask":
        res = sess.turn(a.text)
        show(res)
        print(json.dumps(res.case, ensure_ascii=False, indent=1))
        if a.draft:
            print(drafter.draft(llm, res.case, a.draft)["markdown"])
        return
    print("Describe your problem (empty line to quit).")
    while True:
        try:
            t = input("\nYou: ").strip()
        except EOFError:
            break
        if not t:
            break
        show(sess.turn(t))


if __name__ == "__main__":
    main()
