"""The conversation pipeline. One user turn =

    1. INTAKE   (LLM -> JSON)   messy story -> structured case file
    2. RULES    (code)          deadlines, forum, fee, escalations, missing evidence
    3. RETRIEVE (code)          pick verified knowledge entries for this category
    4. ADVISE   (LLM)           plain-language answer grounded ONLY in those entries
    5. GUARD    (code)          strip/repair any unverified legal reference

Two model calls per turn (three if the guard asks for a repair).
"""
from __future__ import annotations

import datetime as dt
import json
from dataclasses import dataclass, field
from typing import Any

from . import guard, prompts, rules
from .kb import Entry, KnowledgeBase, load_kb
from .llm import LLM

CATEGORIES = {"deposit", "consumer", "wages", "notice", "other"}
LANG_OVERRIDES = {"auto": None, "English": ("en", "English"), "Hindi": ("hi", "Hindi"),
                  "Hinglish": ("hinglish", "Hinglish"), "Tamil": ("ta", "Tamil"), "Bengali": ("bn", "Bengali"),
                  "Marathi": ("mr", "Marathi"), "Telugu": ("te", "Telugu"), "Kannada": ("kn", "Kannada"),
                  "Gujarati": ("gu", "Gujarati"), "Malayalam": ("ml", "Malayalam"), "Punjabi": ("pa", "Punjabi")}


def script_hint(lang: str) -> str:
    if lang == "hinglish":
        return " (Hindi written in English/Latin letters, exactly like the person writes - do NOT use Devanagari)"
    if lang == "hi":
        return " (Devanagari script)"
    return ""


def grounded_generate(llm: LLM, system: str, messages: list[dict], kb: KnowledgeBase, entries: list[Entry], *,
                      purpose: str, quoted_refs=None, max_tokens: int = 3000) -> tuple[str, dict]:
    """Generate, check every legal reference, ask the model to fix once, then scrub what remains."""
    text = guard.normalize_tags(llm.chat(system, messages, purpose=purpose, max_tokens=max_tokens))
    first = guard.check(text, kb, entries, quoted_refs)
    log = {"first_pass": first.to_dict(), "repaired": False, "scrubbed": False}
    if not first.ok:
        fix_msgs = messages + [{"role": "assistant", "content": text},
                               {"role": "user", "content": prompts.ADVISOR_FIX.format(violations=first.as_feedback())}]
        text = guard.normalize_tags(llm.chat(system, fix_msgs, purpose=purpose + ":repair", max_tokens=max_tokens))
        log["repaired"] = True
        second = guard.check(text, kb, entries, quoted_refs)
        log["second_pass"] = second.to_dict()
        if not second.ok:
            text = guard.scrub(text, second)
            log["scrubbed"] = True
    final = guard.check(text, kb, entries, quoted_refs)
    log["final_violations"] = len(final.violations)
    return text, log


@dataclass
class TurnResult:
    reply_markdown: str          # with [K:id] tags
    reply_rendered: str          # tags turned into footnote numbers
    sources: list[dict]
    case: dict
    rules: dict
    kb_ids: list[str]
    guard_log: dict


@dataclass
class Session:
    llm: LLM
    today: dt.date = field(default_factory=dt.date.today)
    language_override: str = "auto"
    case: dict = field(default_factory=dict)
    history: list[dict] = field(default_factory=list)   # [{"role","content"}] - content is the final reply
    trace: list[dict] = field(default_factory=list)
    kb: KnowledgeBase = field(default_factory=load_kb)

    # ----------------------------------------------------------------- intake
    def intake(self, user_text: str) -> dict:
        convo = "\n".join(f"{m['role'].upper()}: {m['content']}" for m in self.history[-8:])
        convo += f"\nUSER: {user_text}"
        system = prompts.INTAKE.format(today=self.today.isoformat(),
                                       previous=json.dumps(self.case, ensure_ascii=False) if self.case else "(none yet)")
        case = self.llm.json(system, [{"role": "user", "content": "CONVERSATION:\n" + convo}], purpose="intake")
        case = normalise_case(case)
        ov = LANG_OVERRIDES.get(self.language_override)
        if ov:
            case["language"], case["language_name"] = ov
        return case

    # ----------------------------------------------------------------- one turn
    def turn(self, user_text: str) -> TurnResult:
        self.case = self.intake(user_text)
        convo_text = user_text + " " + " ".join(m["content"] for m in self.history if m["role"] == "user")
        corroborate_flags(self.case, convo_text)
        computed = rules.compute(self.case, self.today)
        category = self.case["category"]
        entries = self.kb.retrieve(category, convo_text)
        lang, lang_name = self.case.get("language", "en"), self.case.get("language_name", "English")
        facts = {k: computed[k] for k in ("today", "deadlines", "forum", "fee", "escalations", "evidence", "ladder")}

        if any(e["level"] == "refuse" for e in computed["escalations"]):
            system = prompts.REFUSE.format(language_name=lang_name + script_hint(lang))
        elif category == "other" or not computed["in_scope"]:
            system = prompts.OUT_OF_SCOPE.format(language_name=lang_name + script_hint(lang),
                                                 knowledge=self.kb.format_for_prompt(entries),
                                                 escalations="\n".join(f"- {e['reason']} {e['action']}"
                                                                         for e in computed["escalations"]) or "(none)")
        else:
            system = prompts.ADVISOR.format(language_name=lang_name, script_hint=script_hint(lang),
                                            max_words=380, knowledge=self.kb.format_for_prompt(entries),
                                            facts=json.dumps(facts, ensure_ascii=False, indent=1),
                                            case=json.dumps(self.case, ensure_ascii=False, indent=1))
        messages = self.history[-6:] + [{"role": "user", "content": user_text}]
        reply, glog = grounded_generate(self.llm, system, messages, self.kb, entries, purpose="advise")
        rendered, sources = guard.render_citations(reply, self.kb)

        self.history += [{"role": "user", "content": user_text}, {"role": "assistant", "content": guard.TAG_RE.sub("", reply)}]
        result = TurnResult(reply, rendered, sources, self.case, computed, [e.id for e in entries], glog)
        self.trace.append({"user": user_text, "case": self.case, "rules": computed, "kb_ids": result.kb_ids,
                           "reply_raw": reply, "guard": glog})
        return result


# A refusal is the most expensive mistake for a real user with a real claim, so the model's forgery flag
# needs a second, deterministic signal. Eval finding: a small model flagged "can I file a 420 case and
# give me judgments" as a forgery request and the person was refused. The advisor prompt still forbids
# forgery, so dropping an uncorroborated flag does not open a hole.
FORGERY_HINTS = ("fake", "forg", "backdat", "back date", "back-date", "fabricat", "false receipt", "false document",
                 "nakli", "jaali", "jali ", "farzi", "farji", "फर्जी", "नकली", "जाली", "बैकडेट", "झूठी रसीद")


def corroborate_flags(case: dict, convo_text: str) -> None:
    t = convo_text.lower()
    if "forgery_request" in case["red_flags"] and not any(h in t for h in FORGERY_HINTS):
        case["red_flags"].remove("forgery_request")
        case.setdefault("dropped_flags", []).append("forgery_request")


def normalise_case(case: dict[str, Any]) -> dict:
    """Make the LLM's JSON safe to use: fill missing keys, coerce types, clamp category."""
    case = dict(case or {})
    if case.get("category") not in CATEGORIES:
        case["category"] = "other"
    case.setdefault("language", "en")
    case.setdefault("language_name", "English")
    for k in ("timeline", "evidence_have", "steps_taken", "red_flags", "open_questions"):
        v = case.get(k)
        case[k] = v if isinstance(v, list) else ([] if v in (None, "") else [v])
    for k in ("amounts", "dates", "other_party"):
        if not isinstance(case.get(k), dict):
            case[k] = {}
    case["red_flags"] = [str(f).strip().lower() for f in case["red_flags"]]
    case["evidence_have"] = [str(x) for x in case["evidence_have"]]
    case["open_questions"] = case["open_questions"][:3]
    return case
