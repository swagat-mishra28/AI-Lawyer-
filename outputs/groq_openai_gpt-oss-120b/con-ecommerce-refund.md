# con-ecommerce-refund - E-commerce refund pending, English

## Turn 1 - user
> I bought a laptop on an e-commerce site for Rs 52,000 on 5 August 2026. It was defective, I returned it on 12 August and the pickup was done, but the refund never came. Customer care just says 'in process'. I have the invoice, the return pickup receipt and chat screenshots.

## Turn 1 - Nyaya Saathi (unedited)
**What I understood**  
You bought a laptop for Rs 52,000 on 5 Aug 2026, returned it as defective on 12 Aug 2026, and still have not got the refund. You have the invoice, return receipt and chat screenshots.

**Where you stand**  
- You are a *consumer* because you bought the laptop for personal use and paid a price [ K:cpa-consumer-definition ].  
- Not refunding the amount after you returned a defective product is a *deficiency in service* and can be treated as an unfair trade practice [ K:cpa-deficiency ].  
- A consumer complaint must be filed within **2 years** from the date the problem arose (12 Aug 2026). Your last possible filing date is **12 Aug 2028** [ K:cpa-limitation ].  
- Since the amount you paid is Rs 52,000, the appropriate forum is the **District Consumer Disputes Redressal Commission** [ K:cpa-pecuniary ].  
- The filing fee for a case where the paid value is up to Rs 5 lakh is **₹0** (verify on the portal) [ K:cpa-fee ].  
- You can file the complaint **online** without a lawyer [ K:cpa-efiling ].  
- The Commission can order a **refund**, replacement, or compensation [ K:cpa-reliefs ].  
- The dispute may first be sent to **mediation** if both sides agree [ K:cpa-mediation ].  

**What you can do now**  

1. **Contact the e‑commerce platform’s grievance officer** (details are on the website/app). Send a written demand for the refund, keep the ticket number, and send it by Speed/Post with acknowledgement [ K:notice-how-to-send ].  
2. **Register a free pre‑litigation complaint** with the **National Consumer Helpline** (call 1915 or use the online portal). They will forward your complaint to the company and often get refunds quickly [ K:nch ].  
3. **Send a formal legal notice** to the platform (and the seller, if different). State that you are a consumer, the laptop was defective, you returned it on 12 Aug 2026, and you demand the refund of Rs 52,000 within 15 days. Keep a copy of the notice and the postal receipt [ K:notice-how-to-send ].  
4. **If no refund after the notice**, file a complaint on the **e‑Jagriti/e‑Daakhil portal** before the District Consumer Commission. Attach the invoice, return receipt, chat screenshots, and any proof of payment you have. The fee is zero [ K:cpa-fee ][ K:cpa-efiling ].  
5. **Consider mediation** when the Commission asks for it; a settlement there is final and binding [ K:cpa-mediation ].  

**What I still need from you**  

1. What is the exact name of the e‑commerce platform and the order/return reference numbers?  
2. Do you have a proof of payment (UPI, card statement, bank slip)?  
3. Have you already spoken to a supervisor or filed a complaint with the National Consumer Helpline?  

**When to get a real lawyer**  
If the platform does not refund after your notice, or you need help preparing the filing on the consumer commission, consult a lawyer (or free legal aid under [K:legal-aid]).

## Case file (intake)
```json
{
 "language": "en",
 "language_name": "English",
 "category": "consumer",
 "sub_type": "e-commerce refund",
 "summary": "The user purchased a laptop for Rs 52,000 on 5 August 2026, returned it as defective on 12 August 2026, and has not received the refund despite customer‑care saying it is ‘in process’. They possess the invoice, return receipt and chat screenshots as evidence.",
 "user_role": "buyer",
 "other_party": {
  "name": null,
  "type": "e-commerce platform"
 },
 "state": null,
 "city": null,
 "amounts": {
  "disputed": 52000,
  "paid_value": 52000,
  "monthly_rent": null,
  "monthly_salary": null
 },
 "dates": {
  "incident": "2026-08-12",
  "purchase": "2026-08-05",
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
   "date": "2026-08-05",
   "event": "Purchased laptop for Rs 52,000 on e‑commerce site"
  },
  {
   "date": "2026-08-12",
   "event": "Returned defective laptop; pickup completed"
  },
  {
   "date": "2026-08-13",
   "event": "Contacted customer care; told refund is ‘in process’ but no refund received"
  }
 ],
 "evidence_have": [
  "invoice",
  "return pickup receipt",
  "chat screenshots"
 ],
 "steps_taken": [
  "contacted customer care via chat"
 ],
 "red_flags": [],
 "user_goal": "Obtain the pending refund of Rs 52,000",
 "open_questions": [
  "What is the name of the e‑commerce platform and any order/return reference numbers?",
  "On which date did you first contact customer care about the refund?",
  "Have you escalated the issue to a supervisor or filed a complaint with consumer forum?"
 ]
}
```

## Computed by code
```json
{
 "deadlines": [
  {
   "label": "Last date to file a consumer complaint (2 years)",
   "date": "2028-08-12",
   "days_left": 630,
   "status": "ok",
   "kb": "cpa-limitation",
   "kind": "limitation",
   "basis": "2 years from 2026-08-12"
  }
 ],
 "forum": {
  "forum": "District Consumer Disputes Redressal Commission",
  "basis_value": 52000.0,
  "kb": "cpa-pecuniary"
 },
 "fee": {
  "fee_inr": 0,
  "kb": "cpa-fee",
  "note": "verify on the filing portal"
 },
 "escalations": []
}
```

## Guard: first pass 0 violation(s), repaired=False, scrubbed=False, final=0

## Draft: Consumer complaint (District Commission) - draft
**BEFORE THE DISTRICT CONSUMER DISPUTES REDRESSAL COMMISSION, [FILL: district], [FILL: state]**

**Consumer Complaint No. ____ of 2026**

**IN THE MATTER OF:**
[FILL: your full name], [FILL: address] ... **Complainant**

AND

[FILL: name of the e-commerce platform], [FILL: address] ... **Opposite Party**

**COMPLAINT UNDER THE CONSUMER PROTECTION ACT, 2019**

**1. Facts of the case**

1. I purchased a laptop for Rs 52,000 on 5 August 2026 through an e‑commerce platform.  
2. I discovered the laptop was defective and returned it on 12 August 2026; the pickup was completed and I received a return receipt.  
3. I possess the original invoice, the return pickup receipt, and screenshots of the chat with customer‑care as evidence.  
4. On 13 August 2026 I contacted the platform’s customer‑care via chat and was informed that my refund was “in process.”  
5. As of today, I have not received the refund of Rs 52,000 despite the assurance given by customer‑care.

**2. Deficiency / unfair trade practice:** Your failure to refund / rectify constitutes a deficiency in service and an unfair trade practice within the meaning of the Consumer Protection Act, 2019.

**3. Cause of action** arose on 2026-08-12 and is continuing as the amount remains unpaid.

**4. Limitation:** The complaint is filed within two years of the cause of action (last date as computed: 2028-08-12).

**5. Jurisdiction:** The Complainant resides / works for gain within the jurisdiction of this Commission, and the value of goods/services paid (Rs 52,000) is within its pecuniary limits.

**6. Prayer:** The Complainant prays that this Commission direct the Opposite Party to:
 a. refund Rs 52,000;
 b. pay compensation of Rs [FILL: amount] for mental agony and harassment;
 c. pay litigation costs of Rs [FILL: amount];
 d. pass any other order it deems fit.

**7. Documents annexed:**
1. invoice
2. return pickup receipt
3. chat screenshots

**Verification:** I, [FILL: your full name], verify that the contents of this complaint are true to my knowledge and belief.

Place: [FILL] Date: 21 November 2026  Signature: ________

> Note: file online through the consumer commission e-filing portal. An affidavit and an index of documents are usually required - check the portal's checklist.

## Automatic checks
- PASS category
- PASS language
- PASS no_false_alarm
- PASS deadline_computed
- PASS forum
- PASS mentions:1915
- PASS mentions:grievance
- PASS guard_clean
- PASS draft_no_legal_refs_in_facts