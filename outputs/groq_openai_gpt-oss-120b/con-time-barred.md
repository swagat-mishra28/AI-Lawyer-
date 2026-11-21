# con-time-barred - Consumer complaint after 2-year limit

## Turn 1 - user
> I bought a washing machine for 30,000 in March 2023 and it stopped working in April 2023. The company never fixed it. Can I file a consumer case now?

## Turn 1 - Nyaya Saathi (unedited)
**Urgent: Time‑limit issue – you need a lawyer now**  
The normal two‑year limit to file a consumer complaint ended on 1 April 2025. Because that date has passed, the complaint is **time‑barred** and only a court (or a skilled consumer lawyer) can try to get an excuse for the delay. See the limitation rule [K:cpa-limitation].

---

### What I understood
You bought a washing machine for ₹30,000 in March 2023. It stopped working in April 2023 and the company has not repaired or replaced it. You now want to know if you can start a consumer case.

### Where you stand
* You are a **consumer** – you bought a good for personal use. [K:cpa-consumer-definition]  
* The machine’s failure is a **defect in goods** and the company’s refusal to fix it is a **deficiency in service**. [K:cpa-deficiency]  
* The usual filing deadline (2 years from 1 April 2023) has already passed, so a regular consumer commission complaint is likely to be rejected unless a court allows the delay. [K:cpa-limitation]  
* If a court permits the late filing, you could ask the District Consumer Disputes Redressal Commission (value ₹30,000 → District level) for a refund, repair, or compensation. [K:cpa-pecuniary] [K:cpa-reliefs]  

### What you can do now  
1. **Contact a consumer lawyer immediately** – only a lawyer can apply to a court for condonation of delay. (see escalation “lawyer_now”).  
2. **Gather all evidence** – invoice, payment proof, any emails/chats with the company, photos of the faulty machine, warranty card. (Your list shows these are missing.)  
3. **Send a formal demand notice** to the company by Speed/Post or Registered Post, keep receipt and a copy of the notice. [K:notice-how-to-send]  
4. If the lawyer secures permission to file late, you can then **file the complaint online** on the e‑Jagriti portal (no lawyer required for filing, but you’ll still need the lawyer’s help for the delay issue). [K:cpa-efiling] [K:cpa-fee]  
5. While the lawyer works, you may also **call the National Consumer Helpline (1915)** for pre‑litigation help; they sometimes get companies to settle quickly. [K:nch]  

### What I still need from you  
1. What is the exact name of the company that sold the washing machine?  
2. Have you ever sent any complaint (email, call, ticket) to the company? If yes, what was their reply?  
3. In which state and city did you purchase the machine (for jurisdiction)?

### When to get a real lawyer  
Because the consumer‑complaint deadline has passed, you should **consult a consumer lawyer right away** (or contact the Legal Services Authority at 15100 for free aid if you qualify) [K:legal-aid].

## Case file (intake)
```json
{
 "language": "en",
 "language_name": "English",
 "category": "consumer",
 "sub_type": "defective product",
 "summary": "The user purchased a washing machine for ₹30,000 in March 2023, which stopped working in April 2023. The company has not repaired or replaced it. The user wants to know if they can file a consumer case now.",
 "user_role": "buyer",
 "other_party": {
  "name": null,
  "type": "company"
 },
 "state": null,
 "city": null,
 "amounts": {
  "disputed": 30000,
  "paid_value": 30000,
  "monthly_rent": null,
  "monthly_salary": null
 },
 "dates": {
  "incident": "2023-04-01",
  "purchase": "2023-03-01",
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
   "date": "2023-03-01",
   "event": "Purchased washing machine for ₹30,000"
  },
  {
   "date": "2023-04-01",
   "event": "Washing machine stopped working; company did not fix it"
  }
 ],
 "evidence_have": [],
 "steps_taken": [],
 "red_flags": [],
 "user_goal": "to file a consumer case to obtain a refund or repair for the defective washing machine",
 "open_questions": [
  "What is the name of the company that sold the washing machine?",
  "Did you lodge any complaint with the company or consumer forum earlier?",
  "In which state and city was the purchase made (for jurisdiction)?"
 ]
}
```

## Computed by code
```json
{
 "deadlines": [
  {
   "label": "Last date to file a consumer complaint (2 years)",
   "date": "2025-04-01",
   "days_left": -599,
   "status": "passed",
   "kb": "cpa-limitation",
   "kind": "limitation",
   "basis": "2 years from 2023-04-01"
  }
 ],
 "forum": {
  "forum": "District Consumer Disputes Redressal Commission",
  "basis_value": 30000.0,
  "kb": "cpa-pecuniary"
 },
 "fee": {
  "fee_inr": 0,
  "kb": "cpa-fee",
  "note": "verify on the filing portal"
 },
 "escalations": [
  {
   "flag": "time_barred",
   "level": "lawyer_now",
   "reason": "The usual time limit (last date to file a consumer complaint (2 years)) passed on 2025-04-01.",
   "action": "Only a court can excuse the delay - see a lawyer or DLSA (15100) quickly."
  }
 ]
}
```

## Guard: first pass 0 violation(s), repaired=False, scrubbed=False, final=0

## Automatic checks
- PASS category
- PASS escalates:lawyer_now
- PASS mentions:2 years
- PASS guard_clean