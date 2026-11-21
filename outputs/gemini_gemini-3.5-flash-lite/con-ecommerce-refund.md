# con-ecommerce-refund - E-commerce refund pending, English

## Turn 1 - user
> I bought a laptop on an e-commerce site for Rs 52,000 on 5 August 2026. It was defective, I returned it on 12 August and the pickup was done, but the refund never came. Customer care just says 'in process'. I have the invoice, the return pickup receipt and chat screenshots.

## Turn 1 - Nyaya Saathi (unedited)
**What I understood**
You bought a laptop for Rs 52,000 that arrived defective, returned it on 12 August 2026, but the e-commerce company is holding your refund and only saying it is "in process".

**Where you stand**
You are a "consumer" because you bought goods for your own use [K:cpa-consumer-definition]. Failing to refund your money for a returned item is a "deficiency in service" [K:cpa-deficiency]. 

You have plenty of time: your last date to file a consumer complaint is **12 August 2028** (you have 630 days left) [K:cpa-limitation]. Your case goes to the **District Consumer Disputes Redressal Commission** [K:cpa-pecuniary]. The filing fee is generally Rs 0 for this amount, but you should verify this on the portal [K:cpa-fee].

**What you can do now**
1. Check the e-commerce website for their grievance officer's details and send them a formal written complaint; they are required to address it quickly [K:ecom-grievance].
2. Register a free complaint with the **National Consumer Helpline** by calling 1915 or visiting consumerhelpline.gov.in [K:nch]. Many refund issues get solved here without going to court.
3. If they still do not refund, you can file a case online through the e-Jagriti portal before the District Consumer Commission [K:cpa-efiling, K:cpa-pecuniary]. You can do this yourself without paying for a lawyer [K:cpa-efiling].

**What I still need from you**
1. What is the name of the e-commerce platform?
2. Do you have proof of payment, such as a bank or UPI statement?

**When to get a real lawyer**
You can handle this yourself online without a lawyer [K:cpa-efiling], but you can consult one if the company refuses to cooperate and the case gets complicated at the Consumer Commission.

## Case file (intake)
```json
{
 "language": "en",
 "language_name": "English",
 "category": "consumer",
 "sub_type": "e-commerce refund",
 "summary": "The user purchased a laptop for Rs 52,000 on August 5, 2026, which arrived defective. They returned it on August 12, 2026, but have not received their refund despite customer care stating it is 'in process'.",
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
   "event": "Purchased laptop on e-commerce site for Rs 52,000"
  },
  {
   "date": "2026-08-12",
   "event": "Returned defective laptop and pickup was completed"
  }
 ],
 "evidence_have": [
  "invoice",
  "return pickup receipt",
  "chat screenshots"
 ],
 "steps_taken": [
  "contacted customer care"
 ],
 "red_flags": [],
 "user_goal": "Get the refund of Rs 52,000 for the returned defective laptop",
 "open_questions": [
  "What is the name of the e-commerce platform?",
  "Have you sent a formal written complaint or legal notice to the company yet?"
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

1. On August 5, 2026, I purchased a laptop on the [FILL: name of e-commerce platform] e-commerce site for the total amount of Rs 52,000, and I possess the invoice for the same.

2. Upon delivery, I discovered that the laptop was defective. 

3. Consequently, I initiated a return, and the pickup of the defective laptop was successfully completed on August 12, 2026, for which I hold the return pickup receipt.

4. Following the return, I contacted customer care regarding my refund and hold chat screenshots documenting these communications.

5. Despite customer care stating that my refund of Rs 52,000 is "in process," I have not yet received the credited amount.

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