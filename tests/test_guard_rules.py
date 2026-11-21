"""Offline tests (no API key needed): the citation guard and the rules engine."""
import datetime as dt

from nyaya import guard, rules
from nyaya.kb import load_kb

KB = load_kb()
TODAY = dt.date(2026, 11, 21)


def g(text, cat="consumer", ctx=""):
    return guard.check(text, KB, KB.retrieve(cat, ctx))


# ------------------------------------------------------------------ guard: things that must pass
def test_backed_section_passes():
    assert g("You must file within 2 years under Section 69 of the Consumer Protection Act, 2019 [K:cpa-limitation].").ok


def test_backed_section_act_before():
    assert g("The Consumer Protection Act, 2019 (Section 35) lets you file online.").ok


def test_hindi_backed_section_passes():
    assert g("उपभोक्ता संरक्षण अधिनियम, 2019 की धारा 69 के तहत 2 साल में शिकायत करें [K:cpa-limitation]").ok


def test_year_not_read_as_section():
    assert g("The Consumer Protection (E-Commerce) Rules 2020 require a grievance officer.").ok


def test_order_id_not_cpc():
    assert g("Your order 40521 was not delivered.").ok


def test_known_act_name_without_section_ok():
    assert g("The Payment of Wages Act, 1936 has been replaced.", "wages").ok


def test_subsection_matches_base():
    assert g("You are a consumer under Section 2(7) of the Consumer Protection Act.").ok


# ------------------------------------------------------------------ guard: things that must be caught
def test_invented_section_caught():
    r = g("Under Section 12 of the Consumer Protection Act, 2019 you get double compensation.")
    assert not r.ok and r.violations[0].kind == "unbacked_section"


def test_unknown_act_caught():
    r = g("The Tenant Deposit Protection Act, 2017 says landlords must pay 18% interest.", "deposit")
    assert any(v.kind == "unknown_act" for v in r.violations)


def test_case_law_caught():
    r = g("In Lucknow Development Authority v. M.K. Gupta the court held this.")
    assert any(v.kind == "case_law" for v in r.violations)


def test_air_citation_caught():
    assert not g("See AIR 1994 SC 787.").ok


def test_ipc_420_caught_when_not_retrieved():
    # ipc-bns entry is only retrieved when the conversation mentions cheating/420 etc.
    assert not g("You can file a case under Section 420 IPC.", "deposit", ctx="landlord not returning deposit").ok


def test_ipc_420_allowed_when_retrieved():
    assert g("Old IPC Section 420 is now BNS Section 318 [K:ipc-bns].", "deposit", ctx="can I file 420 cheating case").ok


def test_bad_tag_caught():
    assert not g("Something [K:made-up-entry].").ok


def test_wrong_act_for_section_caught():
    # 138 exists in the KB, but for the NI Act, not the Contract Act
    r = g("Section 138 of the Indian Contract Act applies here.", "notice", ctx="cheque bounce")
    assert not r.ok


def test_scrub_removes_reference():
    text = "File under Section 99 of the Consumer Protection Act, 2019 now."
    r = g(text)
    out = guard.scrub(text, r)
    assert "99" not in out and guard.REMOVED in out


def test_quoted_refs_from_notice_allowed():
    r = guard.check("The notice mentions Section 406 of the IPC.", KB, KB.retrieve("notice"), quoted_refs=[("IPC1860", "406")])
    assert r.ok


def test_render_citations():
    out, src = guard.render_citations("A [K:cpa-limitation]. B [K:nch]. C [K:cpa-limitation].", KB)
    assert out.count("[1]") == 2 and len(src) == 2 and src[0]["id"] == "cpa-limitation"


# ------------------------------------------------------------------ KB integrity
def test_every_ref_points_to_registered_act():
    for e in KB.entries.values():
        for r in e.refs:
            assert r["act"] in KB.acts, e.id


def test_kb_ids_unique():
    ids = [e.id for t in KB.topics.values() for e in t.entries]
    assert len(ids) == len(set(ids))


# ------------------------------------------------------------------ rules engine
def test_consumer_forum_and_fee():
    assert "District" in rules.consumer_forum(30_000)["forum"]
    assert "State" in rules.consumer_forum(80 * rules.LAKH)["forum"]
    assert "National" in rules.consumer_forum(3 * rules.CRORE)["forum"]
    assert rules.consumer_fee(4 * rules.LAKH)["fee_inr"] == 0


def test_consumer_limitation():
    r = rules.compute({"category": "consumer", "dates": {"incident": "2025-03-10"}, "amounts": {"paid_value": 25000}}, TODAY)
    d = r["deadlines"][0]
    assert d["date"] == "2027-03-10" and d["status"] == "ok"


def test_time_barred_escalates():
    r = rules.compute({"category": "consumer", "dates": {"incident": "2022-01-05"}}, TODAY)
    assert r["deadlines"][0]["status"] == "passed"
    assert any(e["flag"] == "time_barred" and e["level"] == "lawyer_now" for e in r["escalations"])


def test_wages_two_working_days_skips_sunday():
    # 2026-10-31 is a Saturday -> Mon 2 Nov (Sun skipped) and Tue 3 Nov
    r = rules.compute({"category": "wages", "employment_ended": True, "dates": {"last_working_day": "2026-10-31"}}, TODAY)
    assert r["deadlines"][0]["date"] == "2026-11-03"


def test_wages_monthly_due_7th():
    r = rules.compute({"category": "wages", "dates": {"wages_due_from": "2026-09-01"}}, TODAY)
    assert r["deadlines"][0]["date"] == "2026-10-07"


def test_cheque_bounce_recipient_15_days_and_escalation():
    case = {"category": "notice", "sub_type": "cheque bounce", "user_role": "drawer",
            "dates": {"notice_received": "2026-11-15"}}
    r = rules.compute(case, TODAY)
    assert r["deadlines"][0]["date"] == "2026-11-30" and r["deadlines"][0]["days_left"] == 9
    assert r["escalations"][0]["level"] == "lawyer_now"


def test_red_flag_emergency_first():
    r = rules.compute({"category": "deposit", "red_flags": ["violence_or_threat"], "amounts": {"disputed": 2_000_000}}, TODAY)
    assert r["escalations"][0]["level"] == "emergency"
    assert any(e["flag"] == "large_amount" for e in r["escalations"])


def test_out_of_scope():
    r = rules.compute({"category": "other"}, TODAY)
    assert not r["in_scope"] and r["escalations"][0]["flag"] == "out_of_scope"


def test_evidence_checklist():
    r = rules.compute({"category": "deposit", "evidence_have": ["rent agreement", "UPI screenshot of deposit"]}, TODAY)
    assert any("agreement" in h.lower() for h in r["evidence"]["have"])
    assert any("handed over keys" in m for m in r["evidence"]["missing"])


# ------------------------------------------------------------------ robustness to messy model JSON
def test_num_parses_indian_formats():
    assert rules.num("40,000") == 40000
    assert rules.num("₹1,50,000") == 150000
    assert rules.num("Rs. 2.5 lakh") == 250000
    assert rules.num("1 crore") == 10_000_000
    assert rules.num(None) is None and rules.num("unknown") is None and rules.num(True) is None


def test_null_user_role_does_not_crash():
    case = {"category": "notice", "sub_type": "cheque bounce", "user_role": None,
            "dates": {"notice_received": "2026-11-15", "bank_return_memo": "2026-11-01"}}
    rules.compute(case, TODAY)  # used to raise AttributeError on None.lower()


def test_string_amount_triggers_large_amount_escalation():
    r = rules.compute({"category": "consumer", "amounts": {"disputed": "85 lakh"}}, TODAY)
    assert any(e["flag"] == "large_amount" for e in r["escalations"])
    assert "State" in r["forum"]["forum"]


def test_highlight_marks_violation():
    text = "Under Section 12 of the Consumer Protection Act you get double."
    html_out = guard.highlight(text, g(text))
    assert "line-through" in html_out and "Section 12" in html_out


def test_scrub_removes_whole_case_citation():
    text = "In Lucknow Development Authority v. M.K. Gupta, AIR 1994 SC 787, the court agreed."
    out = guard.scrub(text, g(text))
    assert "Gupta" not in out and "787" not in out and "AIR" not in out


def test_scrub_swallows_act_abbreviation():
    text = "File an FIR under Section 420 IPC now."
    out = guard.scrub(text, g(text, "deposit"))
    assert "IPC" not in out and "420" not in out


def test_case_law_does_not_flag_plain_prose():
    assert g("You vs. the company is a common situation; keep your invoice.").ok
