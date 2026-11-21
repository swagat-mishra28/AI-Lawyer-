# notice-landlord-ipc - Notice from landlord's lawyer citing IPC 406 (quoted law)

## Input notice
```
LEGAL NOTICE
Date: 16/11/2026
To: Ms. Priya Nair, Flat 3B, Green Apartments, Kochi
On behalf of my client Mr. Thomas Varghese, owner of the above flat, I state that you vacated the flat on
30/09/2026 leaving it damaged. Repairs cost Rs. 25,000 which exceeds your deposit of Rs. 20,000. You are called
upon to pay Rs. 5,000 within 7 days, failing which my client will initiate civil and criminal proceedings
against you including under Section 406 IPC for criminal breach of trust.
Advocate K. Menon
```

## Extracted
```json
{
 "doc_type": "legal_demand_notice",
 "sender": "Advocate K. Menon on behalf of Mr. Thomas Varghese",
 "recipient": "Ms. Priya Nair",
 "date_of_notice": "2026-11-16",
 "what_they_claim": "You vacated the flat on 30/09/2026 leaving it damaged, and the repair costs of Rs. 25,000 exceed your security deposit of Rs. 20,000.",
 "what_they_demand": "Pay the remaining amount of Rs. 5,000.",
 "amount_demanded": 5000,
 "deadline_text": "within 7 days",
 "deadline_days": 7,
 "consequences_threatened": [
  "Initiate civil and criminal proceedings against you including under Section 406 IPC for criminal breach of trust."
 ],
 "laws_mentioned": [
  "Section 406 IPC"
 ],
 "court_or_case_number": null,
 "hearing_date": null
}
```

## Reply (unedited)
Hello, I am Nyaya Saathi. Here is a simple explanation of your legal demand notice.

**What this is**
This document is a formal legal demand notice sent by Advocate K. Menon on behalf of Mr. Thomas Varghese [K:notice-legal-what]. It is **not** a court order or a court summons [K:notice-legal-what]. 

**What they want**
The sender claims you left a flat damaged when you vacated on 30/09/2026, and that repair costs of Rs. 25,000 exceed your Rs. 20,000 security deposit. They are demanding payment of the remaining Rs. 5,000. The notice states a deadline of **7 days** (by **November 25, 2026**). It also mentions potential civil and criminal proceedings, including under Section 406 IPC (note that the notice mentions this specific section).

**How serious is it**
Take a deep breath. A legal notice is a formal letter stating a claim, but it does not automatically make you liable [K:notice-legal-what]. However, because the deadline is close (4 days left), you should address it promptly. 

**What to do now**
1. **Gather your documents:** Collect your rental agreement, move-in/move-out photos, deposit receipts, and any chat or call records with the landlord.
2. **Do not panic or admit fault:** Never admit to things you dispute [K:notice-legal-what]. 
3. **Draft a reply:** While you are not legally forced to reply to most notices, sending a short, factual reply keeping a record of your side is often wise [K:notice-legal-what].

**Get a lawyer if**
* You want help drafting a factual reply denying unfair claims.
* The sender actually files a court case or sends a formal court summons.
* You need guidance on tenancy disputes. *(Note: If you qualify under Section 12 of the Legal Services Authorities Act, you may be eligible for free legal aid through the District Legal Services Authority (DLSA) or the NALSA helpline 15100 [K:legal-aid]).*

## Computed by code
```json
{
 "deadlines": [
  {
   "label": "Deadline stated in the notice",
   "date": "2026-11-25",
   "days_left": 4,
   "status": "urgent",
   "kb": "notice-legal-what",
   "kind": "response",
   "basis": "as written in the notice"
  }
 ],
 "forum": null,
 "fee": null,
 "escalations": [
  {
   "flag": "deadline_close",
   "level": "lawyer_now",
   "reason": "Deadline stated in the notice: 2026-11-25 (4 days left).",
   "action": "Act now; get a lawyer's advice before the date."
  }
 ]
}
```

## Guard: first pass 0 violation(s), repaired=False, scrubbed=False, final=0

## Automatic checks
- PASS mentions:7
- PASS mentions:not a court order
- PASS guard_clean