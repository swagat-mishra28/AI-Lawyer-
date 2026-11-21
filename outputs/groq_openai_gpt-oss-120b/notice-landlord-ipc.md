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
 "sender": "Advocate K. Menon (on behalf of Mr. Thomas Varghese)",
 "recipient": "Ms. Priya Nair, Flat 3B, Green Apartments, Kochi",
 "date_of_notice": "2026-11-16",
 "what_they_claim": "You vacated the flat on 30/09/2026 leaving it damaged, and repairs cost Rs. 25,000 which exceeds your deposit of Rs. 20,000.",
 "what_they_demand": "Pay Rs. 5,000 within 7 days",
 "amount_demanded": 5000,
 "deadline_text": "within 7 days",
 "deadline_days": 7,
 "consequences_threatened": [
  "initiate civil and criminal proceedings against you including under Section 406 IPC for criminal breach of trust"
 ],
 "laws_mentioned": [
  "Section 406 IPC"
 ],
 "court_or_case_number": null,
 "hearing_date": null
}
```

## Reply (unedited)
**What this is**  
The document is a **legal demand notice** sent by Advocate K. Menon on behalf of Mr. Thomas Varghese. A legal notice is a formal letter (usually from a lawyer) stating a claim and demanding payment by a deadline. It is **not a court order** and does not by itself make you liable — it is a step before any court case may start. [ K:notice-legal-what ]

**What they want**  
- They say you left the flat on 30 Sept 2026, caused damage costing **₹ 25,000**.  
- Your security deposit was **₹ 20,000**, so they claim a shortfall of **₹ 5,000**.  
- **Demand:** Pay **₹ 5,000** **within 7 days** of the notice date (16 Nov 2026).  
- **Deadline:** 25 Nov 2026 – you have **4 days left**. [ computed ]

**How serious is it**  
- The notice is only a **demand**; it does **not** yet mean a court case is filed.  
- The sender threatens to start **civil and criminal proceedings**, and the notice mentions **Section 406 IPC** (criminal breach of trust). [ K:ipc-bns ]  
- Ignoring the notice may lead to a lawsuit, which could increase costs and affect credit.

**What to do now** (numbered steps)

1. **Check the facts** – Look at the move‑out inspection report, photographs, repair bills, and your deposit receipt.  
2. **Gather evidence** – Save any emails, WhatsApp chats, or receipts that show the flat’s condition when you left.  
3. **Prepare a short reply** – State whether you agree or dispute the claim; do **not** admit anything you dispute.  
4. **Send your reply** by Speed Post/Registered Post with acknowledgement, and also email/WhatsApp a copy. Keep the receipt and tracking number. [ K:notice-how-to-send ]  
5. **Consider settlement** – If the amount is genuine, you may pay the ₹ 5,000 now to avoid escalation.  
6. **Record everything** – Keep copies of the notice, your reply, and all correspondence.

**Get a lawyer if**  

- You **disagree** with the damage amount or believe the claim is false.  
- The notice threatens **criminal proceedings** (Section 406 IPC).  
- You are unsure how to draft a proper reply or need advice on possible court action.  
- You need help negotiating a settlement or want to explore **free legal aid** (call 15100) or a **Lok Adalat** for an out‑of‑court settlement. [ K:legal-aid ][ K:lok-adalat ]

Act quickly—four days remain before the deadline. If you cannot resolve it yourself, consult a lawyer **before 25 Nov 2026**.

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

## Guard: first pass 1 violation(s), repaired=True, scrubbed=False, final=0
- unbacked_section: `Section 406` - Bharatiya Nyaya Sanhita, 2023 406 is not backed by a retrieved knowledge entry

## Automatic checks
- PASS mentions:7
- PASS mentions:not a court order
- PASS guard_clean