# con-ecommerce-refund - E-commerce refund pending, English

## Turn 1 - user
> I bought a laptop on an e-commerce site for Rs 52,000 on 5 August 2026. It was defective, I returned it on 12 August and the pickup was done, but the refund never came. Customer care just says 'in process'. I have the invoice, the return pickup receipt and chat screenshots.

## Turn 1 - Nyaya Saathi (unedited)
**What I understood**  
You bought a defective laptop for Rs 52,000 on 5 August 2026, returned it on 12 August 2026, but have not received your refund despite contacting customer support.

**Where you stand**  
*   I am "Nyaya Saathi", a legal-help assistant, not a lawyer.
*   You bought this item for personal use, so you are a consumer under the law [K:cpa-consumer-definition]. 
*   Taking the item back and withholding your refund is a deficiency in service [K:cpa-deficiency]. 
*   Your case falls under the District Consumer Disputes Redressal Commission [K:cpa-pecuniary]. You can file it in the district where you live [K:cpa-where-to-file].
*   Generally, there is no court fee for claims where the paid amount is up to Rs 5 lakh [K:cpa-fee].
*   Your deadline to file a consumer complaint is 12 August 2028 [K:cpa-limitation].

**What you can do now**  
1. **Contact Grievance Officer**: Send an email to the platform’s Grievance Officer with your invoice and pickup receipt; generally, they must respond within 48 hours and resolve it within one month [K:ecom-grievance].
2. **Call National Consumer Helpline**: File a free complaint by calling 1915 or online at consumerhelpline.gov.in [K:nch].
3. **Send Written Notice**: Send a final demand notice by Speed Post and email giving them 15 days to return your money, and keep the tracking receipt [K:notice-how-to-send].
4. **File Consumer Complaint**: File a complaint online through the e-Jagriti portal; generally, you can argue your own case without hiring a lawyer [K:cpa-efiling].

**What I still need from you**  
1. What is the name of the e-commerce website?  
2. Which city and state do you live in?  
3. Do you have a bank statement or UPI receipt showing the Rs 52,000 payment?

**When to get a real lawyer**  
Get a real lawyer if the e-commerce site ignores your written notice and you need help preparing your papers for the Consumer Commission.

## Case file (intake)
```json
{
 "language": "en",
 "language_name": "English",
 "category": "consumer",
 "sub_type": "e-commerce refund",
 "summary": "The user purchased a defective laptop for Rs 52,000 from an e-commerce site on August 5, 2026. The product was picked up for return on August 12, 2026, but the refund has not been processed yet despite contacting customer care.",
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
   "event": "Laptop purchased for Rs 52,000"
  },
  {
   "date": "2026-08-12",
   "event": "Defective laptop returned and picked up"
  }
 ],
 "evidence_have": [
  "Invoice",
  "Return pickup receipt",
  "Chat screenshots"
 ],
 "steps_taken": [
  "Contacted customer care"
 ],
 "red_flags": [],
 "user_goal": "Get a full refund of Rs 52,000 for the returned laptop.",
 "open_questions": [
  "What is the name of the e-commerce platform?",
  "Which state and city do you reside in?"
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

1. On August 5, 2026, I purchased a laptop for an amount of Rs 52,000 from the e-commerce platform [FILL: Name of e-commerce platform] while residing in [FILL: City, State].

2. Upon receiving the laptop, I found the product to be defective and initiated a return request with the e-commerce platform.

3. Pursuant to my return request, the defective laptop was successfully picked up by the e-commerce platform on August 12, 2026.

4. Following the pickup, I contacted customer care to request my refund, but the amount of Rs 52,000 has not been refunded to me to date.

5. I have retained all relevant records of this transaction, including the invoice, return pickup receipt, and chat screenshots with customer care.

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
1. Invoice
2. Return pickup receipt
3. Chat screenshots

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