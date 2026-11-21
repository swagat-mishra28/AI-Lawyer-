"""End-to-end pipeline test with a scripted fake model (no API key needed).

Proves the guard loop works as designed: the model's first answer invents a section and a
judgment, the pipeline sends it back once, and whatever survives is scrubbed - so the person
never sees an unverified legal reference.
"""
import datetime as dt
import json

from nyaya import guard
from nyaya.assistant import Session
from nyaya.kb import load_kb

INTAKE = {
    "language": "hinglish", "language_name": "Hinglish", "category": "deposit", "sub_type": "deposit withheld",
    "summary": "Tenant moved out on 15 Sept 2026; landlord keeps Rs 40,000 deposit.", "user_role": "tenant",
    "other_party": {"name": None, "type": "landlord"}, "state": "Karnataka", "city": "Bengaluru",
    "amounts": {"disputed": "40,000", "paid_value": None, "monthly_rent": None, "monthly_salary": None},
    "dates": {"moved_out": "2026-09-15"}, "employment_ended": None, "timeline": [],
    "evidence_have": ["rent agreement", "UPI payment of deposit"], "steps_taken": [], "red_flags": [],
    "user_goal": "get deposit back", "open_questions": [],
}
BAD = ("Aapka deposit milna chahiye [K:deposit-contract]. Section 27 of the Rent Act, 2001 ke hisaab se 18% byaaj milega. "
       "Sharma v. Gupta case mein court ne yahi kaha.")
STILL_BAD = "Aapka deposit milna chahiye [K:deposit-contract]. Sharma v. Gupta case mein court ne yahi kaha."


class FakeLLM:
    label = "fake:scripted"

    def __init__(self, replies):
        self.replies, self.calls = list(replies), []

    def json(self, system, messages, purpose="json", **kw):
        self.calls.append(purpose)
        return json.loads(json.dumps(INTAKE))

    def chat(self, system, messages, purpose="chat", **kw):
        self.calls.append(purpose)
        assert "[K:deposit-contract]" in system          # only verified knowledge is offered
        return self.replies.pop(0)


def run(replies):
    llm = FakeLLM(replies)
    s = Session(llm=llm, today=dt.date(2026, 11, 21))
    return llm, s.turn("landlord 40k deposit nahi de raha, 15 sept ko flat chhoda")


def test_repair_fixes_hallucination():
    llm, r = run([BAD, "Aapka deposit milna chahiye [K:deposit-contract]. Pehle likhit mein maangiye."])
    assert llm.calls == ["intake", "advise", "advise:repair"]
    assert r.guard_log["repaired"] and not r.guard_log["scrubbed"] and r.guard_log["final_violations"] == 0
    kinds = {v["kind"] for v in r.guard_log["first_pass"]["violations"]}
    assert {"unknown_act", "case_law"} <= kinds


def test_scrub_when_repair_fails():
    llm, r = run([BAD, STILL_BAD])
    assert r.guard_log["scrubbed"] and r.guard_log["final_violations"] == 0
    assert "Sharma" not in r.reply_markdown and guard.REMOVED in r.reply_markdown


def test_rules_use_code_not_model():
    _, r = run(["Theek hai [K:deposit-contract]."])
    assert r.rules["deadlines"][0]["date"] == "2029-09-15"          # 3 years from move-out, computed in code
    assert r.sources and r.sources[0]["id"] == "deposit-contract"
    assert not any(e["level"] in ("emergency", "lawyer_now") for e in r.rules["escalations"])


def test_kb_has_no_dangling_triggers():
    kb = load_kb()
    for e in kb.entries.values():
        assert e.plain.strip() and e.title


def test_uncorroborated_forgery_flag_is_dropped():
    from nyaya.assistant import corroborate_flags
    case = {"red_flags": ["forgery_request"]}
    corroborate_flags(case, "Kya main landlord pe 420 ka case kar sakta hoon? Supreme Court ke judgments batao")
    assert case["red_flags"] == [] and case["dropped_flags"] == ["forgery_request"]
    case = {"red_flags": ["forgery_request"]}
    corroborate_flags(case, "Make me backdated rent receipts with a landlord signature")
    assert case["red_flags"] == ["forgery_request"]
