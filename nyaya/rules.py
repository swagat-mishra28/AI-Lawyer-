"""Deterministic legal arithmetic: deadlines, forum, fees, escalation and evidence gaps.

None of this is left to the model. Dates and money are exactly where LLMs make silent,
confident mistakes, and they are fully specified by law, so plain code is both cheaper and
correct. The model receives these results as facts and only explains them.
"""
from __future__ import annotations

import datetime as dt
from typing import Any

from .kb import load_kb

LAKH = 100_000
CRORE = 10_000_000

# Assumption (documented in README): above this value a person should at least consult a
# lawyer before acting alone, even though self-representation is allowed.
LAWYER_AMOUNT_THRESHOLD = 10 * LAKH

RED_FLAG_RULES: dict[str, tuple[str, str, str]] = {
    # flag: (level, reason, action)
    "violence_or_threat": ("emergency", "You mentioned violence or a threat to your safety.",
                           "If you are in danger, call 112 now. Women: 181."),
    "self_harm": ("emergency", "You mentioned thoughts of harming yourself.",
                  "Please call Tele-MANAS 14416 (free, 24x7) or 112 right now. You are not alone."),
    "domestic_violence": ("emergency", "This involves domestic violence, which this assistant does not handle.",
                          "Call 181 (women's helpline) or 112; free legal aid: 15100."),
    "police_or_arrest": ("lawyer_now", "Police action or arrest is involved.",
                         "Speak to a criminal lawyer before meeting the police. Free legal aid: 15100."),
    "court_summons": ("lawyer_now", "You have a court summons or a court date.",
                      "Do not miss the date. Contact a lawyer or DLSA legal aid (15100) now."),
    "criminal_accusation_against_user": ("lawyer_now", "Someone is accusing you of a crime.",
                                         "Do not reply or sign anything before talking to a lawyer."),
    "cheque_bounce_against_user": ("lawyer_now", "A cheque-bounce notice against you is a criminal matter with a 15-day window.",
                                   "Pay within 15 days of receiving the notice, or consult a lawyer immediately."),
    "sexual_harassment": ("lawyer_now", "Sexual harassment at work needs specialised help.",
                          "Complain to the employer's Internal Committee; speak to a lawyer or call 15100."),
    "minor_involved": ("lawyer_recommended", "A child is involved.", "Get an adult guardian and a lawyer involved; child helpline 1098."),
    "government_party": ("lawyer_recommended", "The other side is a government body, which follows special procedures.",
                         "Consult a lawyer or DLSA (15100) before filing."),
    "cyber_fraud": ("emergency", "This sounds like online financial fraud, which is time-critical.",
                    "Call 1930 immediately and report at cybercrime.gov.in; also inform your bank."),
    "eviction_threat": ("lawyer_recommended", "You are being threatened with eviction.",
                        "Eviction needs due process; consult a lawyer if you are pressured to leave."),
    "forgery_request": ("refuse", "You asked for help creating a false or backdated document.",
                        "I can't help with that - it could be the crime of forgery. I can help with genuine documents."),
}


def _d(s: Any) -> dt.date | None:
    if not s or not isinstance(s, str):
        return None
    try:
        return dt.date.fromisoformat(s[:10])
    except ValueError:
        return None


def _add_years(d: dt.date, years: int) -> dt.date:
    try:
        return d.replace(year=d.year + years)
    except ValueError:  # 29 Feb
        return d.replace(year=d.year + years, day=28)


def _add_working_days(d: dt.date, n: int) -> dt.date:
    # Simplification (documented): only Sundays are skipped; public holidays vary by state.
    while n > 0:
        d += dt.timedelta(days=1)
        if d.weekday() != 6:
            n -= 1
    return d


def _seventh_of_next_month(d: dt.date) -> dt.date:
    y, m = (d.year + 1, 1) if d.month == 12 else (d.year, d.month + 1)
    return dt.date(y, m, 7)


def _deadline(label: str, date: dt.date, today: dt.date, kb_id: str, kind: str, basis: str) -> dict:
    left = (date - today).days
    if left < 0:
        status = "passed"
    elif left <= 30:
        status = "urgent"
    else:
        status = "ok"
    return {"label": label, "date": date.isoformat(), "days_left": left, "status": status,
            "kb": kb_id, "kind": kind, "basis": basis}


def num(x: Any) -> float | None:
    """Coerce model output to rupees: 40000, "40,000", "Rs 40,000", "₹1,50,000", "2.5 lakh", "1 crore"."""
    if x is None or isinstance(x, bool):
        return None
    if isinstance(x, (int, float)):
        return float(x)
    s = str(x).lower().replace(",", "").replace("₹", "").replace("rs.", "").replace("rs", "").replace("inr", "").strip()
    mult = 1
    for word, m in (("crore", CRORE), ("cr", CRORE), ("lakh", LAKH), ("lac", LAKH), ("k", 1000)):
        if s.endswith(word):
            s, mult = s[: -len(word)].strip(), m
            break
    try:
        return float(s) * mult if s else None
    except ValueError:
        return None


# ---------------------------------------------------------------------------- consumer
def consumer_forum(paid: float | None) -> dict | None:
    if paid is None:
        return None
    if paid <= 50 * LAKH:
        level = "District Consumer Disputes Redressal Commission"
    elif paid <= 2 * CRORE:
        level = "State Consumer Disputes Redressal Commission"
    else:
        level = "National Consumer Disputes Redressal Commission"
    return {"forum": level, "basis_value": paid, "kb": "cpa-pecuniary"}


def consumer_fee(paid: float | None) -> dict | None:
    # Fee slabs per the 2020 Consumer Commission Procedure Regulations (confidence: medium).
    if paid is None:
        return None
    slabs = [(5 * LAKH, 0), (10 * LAKH, 200), (20 * LAKH, 400), (50 * LAKH, 1000), (1 * CRORE, 2000),
             (2 * CRORE, 2500)]
    for limit, fee in slabs:
        if paid <= limit:
            return {"fee_inr": fee, "kb": "cpa-fee", "note": "verify on the filing portal"}
    return {"fee_inr": None, "kb": "cpa-fee", "note": "State/National Commission fee - check the portal"}


# ---------------------------------------------------------------------------- main
def compute(case: dict, today: dt.date | None = None) -> dict:
    today = today or dt.date.today()
    kb = load_kb()
    cat = case.get("category") or "other"
    dates = case.get("dates") or {}
    amounts = case.get("amounts") or {}
    disputed = num(amounts.get("disputed"))
    paid = num(amounts.get("paid_value")) or disputed
    out: dict[str, Any] = {"today": today.isoformat(), "category": cat, "deadlines": [], "escalations": [],
                           "forum": None, "fee": None, "evidence": None, "ladder": [], "in_scope": cat in kb.topics}

    # ---- deadlines
    if cat == "consumer":
        base = _d(dates.get("incident")) or _d(dates.get("complaint_to_company")) or _d(dates.get("purchase"))
        if base:
            out["deadlines"].append(_deadline("Last date to file a consumer complaint (2 years)", _add_years(base, 2), today,
                                              "cpa-limitation", "limitation", f"2 years from {base.isoformat()}"))
        out["forum"] = consumer_forum(paid)
        out["fee"] = consumer_fee(paid)
    elif cat == "deposit":
        base = _d(dates.get("moved_out"))
        if base:
            out["deadlines"].append(_deadline("Last date to file a money-recovery suit (generally 3 years)", _add_years(base, 3),
                                              today, "deposit-limitation", "limitation", f"3 years from move-out {base.isoformat()}"))
    elif cat == "wages":
        lwd = _d(dates.get("last_working_day"))
        unpaid_from = _d(dates.get("wages_due_from"))
        due = None
        if lwd and case.get("employment_ended"):
            due = _add_working_days(lwd, 2)
            out["deadlines"].append(_deadline("Final wages were due (2 working days after leaving)", due, today, "cw-timely-payment",
                                              "statutory_due", f"2 working days after {lwd.isoformat()}"))
        elif unpaid_from:
            due = _seventh_of_next_month(unpaid_from)
            out["deadlines"].append(_deadline("Salary for the first unpaid month was due", due, today, "cw-timely-payment",
                                              "statutory_due", f"before the 7th of the month after {unpaid_from:%B %Y}"))
        if due:
            out["deadlines"].append(_deadline("Last date to file a wage claim (generally 3 years)", _add_years(due, 3), today,
                                              "cw-claims", "limitation", f"3 years from {due.isoformat()}"))
    elif cat == "notice":
        rec = _d(dates.get("notice_received"))
        sub = (case.get("sub_type") or "").lower()
        if rec and "cheque" in sub and (case.get("user_role") or "").lower() in ("drawer", "accused", "notice recipient", "recipient"):
            out["deadlines"].append(_deadline("Last day to pay the cheque amount (15 days from receiving notice)",
                                              rec + dt.timedelta(days=15), today, "nia-138", "response", f"15 days from {rec.isoformat()}"))
        memo = _d(dates.get("bank_return_memo"))
        if memo and "cheque" in sub and (case.get("user_role") or "").lower() in ("payee", "complainant"):
            out["deadlines"].append(_deadline("Last day to send the cheque-bounce demand notice (30 days)",
                                              memo + dt.timedelta(days=30), today, "nia-138", "response", f"30 days from {memo.isoformat()}"))
        nd = _d(dates.get("notice_deadline"))
        if nd:
            out["deadlines"].append(_deadline("Deadline stated in the notice", nd, today, "notice-legal-what", "response",
                                              "as written in the notice"))

    # ---- escalation
    flags = set(case.get("red_flags") or [])
    if cat == "notice" and "cheque" in (case.get("sub_type") or "").lower() and \
            (case.get("user_role") or "").lower() in ("drawer", "accused", "notice recipient", "recipient"):
        flags.add("cheque_bounce_against_user")
    for f in flags:
        if f in RED_FLAG_RULES:
            level, reason, action = RED_FLAG_RULES[f]
            out["escalations"].append({"flag": f, "level": level, "reason": reason, "action": action})
    if (disputed or 0) >= LAWYER_AMOUNT_THRESHOLD:
        out["escalations"].append({"flag": "large_amount", "level": "lawyer_recommended",
                                   "reason": f"The amount (Rs {disputed:,.0f}) is large.",
                                   "action": "Consult a lawyer before filing; you can still use this plan to prepare."})
    for d in out["deadlines"]:
        if d["kind"] == "limitation" and d["status"] == "passed":
            out["escalations"].append({"flag": "time_barred", "level": "lawyer_now",
                                       "reason": f"The usual time limit ({d['label'].lower()}) passed on {d['date']}.",
                                       "action": "Only a court can excuse the delay - see a lawyer or DLSA (15100) quickly."})
        elif d["kind"] == "response" and d["status"] in ("urgent", "passed"):
            out["escalations"].append({"flag": "deadline_close", "level": "lawyer_now",
                                       "reason": f"{d['label']}: {d['date']} ({d['days_left']} days left).",
                                       "action": "Act now; get a lawyer's advice before the date."})
    if not out["in_scope"]:
        out["escalations"].append({"flag": "out_of_scope", "level": "legal_aid",
                                   "reason": "This problem is outside what this assistant covers (deposits, consumer refunds, unpaid wages, notices).",
                                   "action": "Call NALSA legal aid 15100 or visit your District Legal Services Authority."})
    order = {"refuse": 0, "emergency": 1, "lawyer_now": 2, "lawyer_recommended": 3, "legal_aid": 4}
    out["escalations"].sort(key=lambda e: order.get(e["level"], 9))

    # ---- evidence checklist and next-step ladder
    if cat in kb.topics:
        topic = kb.topics[cat]
        have_text = " ".join(case.get("evidence_have") or []).lower()
        have, missing = [], []
        for item in topic.checklist:
            (have if any(k.lower() in have_text for k in item["keywords"]) else missing).append(item["item"])
        out["evidence"] = {"have": have, "missing": missing}
        out["ladder"] = topic.ladder
    return out


def needs_human(rules: dict) -> bool:
    return any(e["level"] in ("emergency", "lawyer_now", "refuse") for e in rules["escalations"])
