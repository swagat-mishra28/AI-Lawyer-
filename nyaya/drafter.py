"""Document drafting.

Design choice: the legal skeleton (headings, legal basis, demand, forum) is a fixed template
written from the verified knowledge base; the model only writes the FACTS paragraphs from the
case file, and the guard checks those too. Anything unknown becomes a visible [FILL: ...]
placeholder, so a draft can be incomplete but never invented.
"""
from __future__ import annotations

import datetime as dt
import io
import json
import re

from . import guard, prompts, rules
from .kb import load_kb
from .llm import LLM

DOCS = {
    "consumer": {"grievance_email": "Grievance email to the company",
                 "legal_notice": "Legal notice (demand for refund)",
                 "consumer_complaint": "Consumer complaint (District Commission) - draft"},
    "deposit": {"legal_notice": "Legal notice to landlord (deposit refund)"},
    "wages": {"legal_notice": "Legal notice to employer (unpaid salary)",
              "labour_complaint": "Complaint to Labour Department"},
}

BASIS_IDS = {
    "consumer": ["cpa-deficiency", "ecom-grievance", "cpa-reliefs"],
    "deposit": ["deposit-contract"],
    "wages": ["cw-timely-payment", "wages-contract"],
}


def available(category: str) -> dict:
    return DOCS.get(category, {})


def _money(x) -> str:
    v = rules.num(x)
    return f"Rs {v:,.0f}" if v else "Rs [FILL: amount]"


def _fill(v, label):
    return v if v else f"[FILL: {label}]"


def draft(llm: LLM, case: dict, doc_type: str, today: dt.date | None = None, sender_name: str = "") -> dict:
    today = today or dt.date.today()
    kb = load_kb()
    cat = case.get("category")
    if doc_type not in DOCS.get(cat, {}):
        raise ValueError(f"No '{doc_type}' template for category '{cat}'")
    title = DOCS[cat][doc_type]
    n = 3 if doc_type == "grievance_email" else 5
    facts_prompt = prompts.DRAFT_FACTS.format(doc_title=title, n=n, case=json.dumps(case, ensure_ascii=False, indent=1))
    facts = llm.chat("You draft precise, factual legal letters. You never invent facts.",
                     [{"role": "user", "content": facts_prompt}], purpose="draft_facts", max_tokens=1500)
    rep = guard.check(facts, kb, [])            # facts must contain NO legal references at all
    if not rep.ok:
        facts = guard.scrub(facts, rep)

    entries = kb.entries
    basis = [entries[i].notice_basis.strip() for i in BASIS_IDS.get(cat, []) if entries[i].notice_basis]
    party = case.get("other_party") or {}
    other = _fill(party.get("name"), f"name of the {party.get('type') or 'other party'}")
    me = sender_name or "[FILL: your full name]"
    amt = _money((case.get("amounts") or {}).get("disputed"))
    date = today.strftime("%d %B %Y")
    rcomp = rules.compute(case, today)

    if doc_type == "grievance_email":
        body = f"""**To:** Grievance Officer / Customer Care, {other}
**Subject:** Unresolved complaint - request for refund of {amt} [FILL: order / ticket number]

Dear Grievance Officer,

{facts}

I request you to refund {amt} to my original payment method within 7 days of this email and confirm in writing.
Please treat this as a formal grievance. If it is not resolved, I will register a complaint with the National
Consumer Helpline and approach the Consumer Commission, without further notice.

Regards,
{me}
[FILL: phone] | [FILL: registered email]
Date: {date}"""

    elif doc_type == "legal_notice":
        reason = {"consumer": "refund and compensation for deficient goods/services",
                  "deposit": "refund of the security deposit",
                  "wages": "payment of unpaid salary / wages"}[cat]
        forum = {"consumer": "file a complaint before the appropriate Consumer Disputes Redressal Commission",
                 "deposit": "initiate proceedings for recovery before the competent civil court / Lok Adalat",
                 "wages": "file a claim before the Labour authority and pursue all other remedies"}[cat]
        basis_txt = "\n\n".join(f"{i}. {b}" for i, b in enumerate(basis, 1))
        body = f"""**LEGAL NOTICE**

**Date:** {date}
**Sent by:** Speed Post / Registered Post A.D. and email

**From:** {me}, [FILL: your address]
**To:** {other}, [FILL: their address]

**Subject: Notice for {reason} of {amt}**

Sir/Madam,

I, the undersigned, state as follows:

**Facts**

{facts}

**Legal basis**

{basis_txt}

**Demand**

I hereby call upon you to pay {amt} within **15 days** of receiving this notice, by bank transfer to the account
I will share on request, and to confirm in writing.

If you fail to do so, I shall be constrained to {forum}, claiming the amount along with interest, compensation
and costs, entirely at your risk as to costs and consequences.

A copy of this notice is retained for further action.

{me}
[FILL: signature]"""

    elif doc_type == "consumer_complaint":
        forum = (rcomp.get("forum") or {}).get("forum", "District Consumer Disputes Redressal Commission")
        lim = next((d for d in rcomp["deadlines"] if d["kind"] == "limitation"), None)
        docs = "\n".join(f"{i}. {e}" for i, e in enumerate(case.get("evidence_have") or ["[FILL: list of documents]"], 1))
        body = f"""**BEFORE THE {forum.upper()}, [FILL: district], [FILL: state]**

**Consumer Complaint No. ____ of {today.year}**

**IN THE MATTER OF:**
{me}, [FILL: address] ... **Complainant**

AND

{other}, [FILL: address] ... **Opposite Party**

**COMPLAINT UNDER THE CONSUMER PROTECTION ACT, 2019**

**1. Facts of the case**

{facts}

**2. Deficiency / unfair trade practice:** {basis[0] if basis else ''}

**3. Cause of action** arose on {_fill((case.get('dates') or {}).get('incident'), 'date problem arose')} and is continuing as the amount remains unpaid.

**4. Limitation:** The complaint is filed within two years of the cause of action{f" (last date as computed: {lim['date']})" if lim else ""}.

**5. Jurisdiction:** The Complainant resides / works for gain within the jurisdiction of this Commission, and the value of goods/services paid ({_money((case.get('amounts') or {}).get('paid_value') or (case.get('amounts') or {}).get('disputed'))}) is within its pecuniary limits.

**6. Prayer:** The Complainant prays that this Commission direct the Opposite Party to:
 a. refund {amt};
 b. pay compensation of Rs [FILL: amount] for mental agony and harassment;
 c. pay litigation costs of Rs [FILL: amount];
 d. pass any other order it deems fit.

**7. Documents annexed:**
{docs}

**Verification:** I, {me}, verify that the contents of this complaint are true to my knowledge and belief.

Place: [FILL] Date: {date}  Signature: ________

> Note: file online through the consumer commission e-filing portal. An affidavit and an index of documents are usually required - check the portal's checklist."""

    elif doc_type == "labour_complaint":
        body = f"""**To,**
The Labour Commissioner / Inspector-cum-Facilitator,
[FILL: district and state] Labour Department

**Subject: Complaint for non-payment of wages of {amt} by {other}**

Respected Sir/Madam,

{facts}

{basis[0] if basis else ''}

I request you to direct the employer to pay my pending wages of {amt} along with compensation as per law, and to
take any other action you consider appropriate. Copies of my documents are attached.

**Documents attached:**
{chr(10).join(f"{i}. {e}" for i, e in enumerate(case.get('evidence_have') or ['[FILL: documents]'], 1))}

Yours faithfully,
{me}
[FILL: address, phone]
Date: {date}"""
    else:  # pragma: no cover
        raise ValueError(doc_type)

    placeholders = sorted(set(re.findall(r"\[FILL:[^\]]*\]", body)))
    return {"doc_type": doc_type, "title": title, "markdown": body, "placeholders": placeholders,
            "facts_guard": rep.to_dict(),
            "disclaimer": "Draft prepared by an AI assistant from your answers. Check every fact, fill every [FILL] "
                          "and, if the amount is large or the other side has a lawyer, have it reviewed."}


def to_docx(markdown: str) -> bytes:
    from docx import Document
    from docx.shared import Pt

    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(12)
    for line in markdown.splitlines():
        p = doc.add_paragraph()
        parts = re.split(r"(\*\*[^*]+\*\*)", line.lstrip("> "))
        for part in parts:
            if part.startswith("**") and part.endswith("**"):
                p.add_run(part[2:-2]).bold = True
            elif part:
                p.add_run(part)
    buf = io.BytesIO()
    doc.save(buf)
    return buf.getvalue()
