# con-builder-large - Builder delay, Rs 85 lakh (state commission, large amount)

## Turn 1 - user
> I paid 85 lakh rupees to a builder in Noida for a flat in 2021. Possession was promised in December 2023 but the project is still incomplete. What can I do?

## Turn 1 - Nyaya Saathi (unedited)
**What I understood**  
You paid ₹85 lakh for a flat in Noida in 2021. Possession was promised for December 2023, but the building is still not ready in November 2026.

**Where you stand**  
- You are a *consumer* because you bought a flat for personal use and paid a price [K:cpa-consumer-definition].  
- The builder’s failure to give you possession on time is a *deficiency in service* and may also be an *unfair trade practice* [K:cpa-deficiency].  
- Normally you could file a complaint before the State Consumer Disputes Redressal Commission (value ₹8.5 million) [K:cpa-pecuniary].  
- However, a consumer complaint must be filed within **2 years** of the cause of action (here, 1 Dec 2023) [K:cpa-limitation]. The last date was 1 Dec 2025, which has already passed [K:cpa-limitation].  
- Because the time‑limit is missed, only a **court** can excuse the delay, and you need a lawyer urgently [K:lawyer_now] (see escalation).  
- The Commission can order a refund, possession, compensation, or costs [K:cpa-reliefs].  

**What you can do now** (cheapest / fastest first)  

1. **Send a formal notice to the builder** – use Speed/Post or Registered Post, keep receipt and a copy of the email/WhatsApp. State that you demand possession within 15 days or a full refund, and that you will approach a court if not complied [K:notice-how-to-send].  
2. **Contact the builder’s grievance officer** (if the project is on an e‑commerce portal or the builder’s website) – they must acknowledge within 48 hours and try to resolve within 1 month [K:ecom-grievance].  
3. **Register a free pre‑litigation complaint with the National Consumer Helpline** (call 1915 or use the online portal). They forward the complaint to the builder and may help settle [K:nch].  
4. **Approach the Uttar Pradesh RERA authority** – delays in possession are also covered under the Real Estate (Regulation and Development) Act, 2016. You can file a complaint there; it may lead to compensation or specific performance [K:rera-note].  
5. **Seek free legal aid** – if you qualify (low income, etc.), call 15100 for a free lawyer from the Legal Services Authority [K:legal-aid].  
6. **If you decide to file a consumer case despite the time‑bar**, you must first obtain a court order excusing the delay, which a lawyer can apply for. The filing fee is generally around ₹2,000 for amounts above ₹5 lakh, but verify on the portal [K:cpa-fee]. You can file online (e‑Jagriti) without a lawyer, but given the large sum and time‑bar, a lawyer is strongly advised [K:cpa-efiling].  

**What I still need from you**  
1. Exact name of the builder/developer and the project.  
2. Dates and copies of each payment (bank statements, receipts).  
3. Any written communication (letters, emails, notices) you have received from the builder about the delay.  

**When to get a real lawyer**  
Because the consumer‑complaint deadline has passed and the claim is for ₹8.5 million, you should consult a lawyer **immediately** to seek a court order excusing the delay and to pursue a refund or specific performance.

## Case file (intake)
```json
{
 "language": "en",
 "language_name": "English",
 "category": "consumer",
 "sub_type": "delayed possession",
 "summary": "The user paid 85 lakh rupees to a builder in Noida in 2021 for a flat. Possession was promised for December 2023 but the project remains incomplete as of November 2026. The user seeks remedies to obtain possession or recover the payment.",
 "user_role": "buyer",
 "other_party": {
  "name": null,
  "type": "company"
 },
 "state": "Uttar Pradesh",
 "city": "Noida",
 "amounts": {
  "disputed": 8500000,
  "paid_value": 8500000,
  "monthly_rent": null,
  "monthly_salary": null
 },
 "dates": {
  "incident": "2023-12-01",
  "purchase": "2021-01-01",
  "complaint_to_company": null,
  "moved_out": null,
  "last_working_day": null,
  "wages_due_from": null,
  "notice_received": null,
  "notice_deadline": null,
  "bank_return_memo": null
 },
 "employment_ended": null,
 "timeline": [
  {
   "date": "2021-01-01",
   "event": "Paid 85 lakh rupees to the builder for a flat in Noida"
  },
  {
   "date": "2023-12-01",
   "event": "Possession of the flat was promised but the project remained incomplete"
  },
  {
   "date": "2026-11-21",
   "event": "Project still incomplete; user seeks legal remedy"
  }
 ],
 "evidence_have": [
  "payment receipts",
  "sale agreement",
  "bank transfer records"
 ],
 "steps_taken": [],
 "red_flags": [],
 "user_goal": "Obtain possession of the flat or recover the amount paid",
 "open_questions": [
  "What is the name of the builder/developer and the project?",
  "On what exact dates were the payments made and are there bank statements or receipts for each?",
  "Have you received any written communication or notice from the builder regarding delay or cancellation?"
 ]
}
```

## Computed by code
```json
{
 "deadlines": [
  {
   "label": "Last date to file a consumer complaint (2 years)",
   "date": "2025-12-01",
   "days_left": -355,
   "status": "passed",
   "kb": "cpa-limitation",
   "kind": "limitation",
   "basis": "2 years from 2023-12-01"
  }
 ],
 "forum": {
  "forum": "State Consumer Disputes Redressal Commission",
  "basis_value": 8500000.0,
  "kb": "cpa-pecuniary"
 },
 "fee": {
  "fee_inr": 2000,
  "kb": "cpa-fee",
  "note": "verify on the filing portal"
 },
 "escalations": [
  {
   "flag": "time_barred",
   "level": "lawyer_now",
   "reason": "The usual time limit (last date to file a consumer complaint (2 years)) passed on 2025-12-01.",
   "action": "Only a court can excuse the delay - see a lawyer or DLSA (15100) quickly."
  },
  {
   "flag": "large_amount",
   "level": "lawyer_recommended",
   "reason": "The amount (Rs 8,500,000) is large.",
   "action": "Consult a lawyer before filing; you can still use this plan to prepare."
  }
 ]
}
```

## Guard: first pass 0 violation(s), repaired=False, scrubbed=False, final=0

## Automatic checks
- PASS category
- PASS escalates:lawyer_recommended
- PASS forum
- PASS mentions:RERA
- PASS guard_clean