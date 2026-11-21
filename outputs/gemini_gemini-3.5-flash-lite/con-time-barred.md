# con-time-barred - Consumer complaint after 2-year limit

## Turn 1 - user
> I bought a washing machine for 30,000 in March 2023 and it stopped working in April 2023. The company never fixed it. Can I file a consumer case now?

## Turn 1 - Nyaya Saathi (unedited)
**What I need to tell you first (Important):**
The usual time limit (last date to file a consumer complaint (2 years)) passed on 2025-04-01 [K:cpa-limitation]. Only a court can excuse the delay - see a lawyer or DLSA (15100) quickly.

**What I understood**
You bought a washing machine for Rs 30,000 in March 2023, it broke down in April 2023, and the company did not repair it.

**Where you stand**
You are a "consumer" under the Consumer Protection Act, 2019 - Section 2(7) [K:cpa-consumer-definition], because you bought the machine for your own use. The company's failure to repair or refund is a "deficiency in service" [K:cpa-deficiency]. 

However, a consumer complaint must be filed within 2 years from the date the problem arose [K:cpa-limitation]. Since the issue started in April 2023, that 2-year deadline has already passed [K:cpa-limitation]. Late complaints are accepted only if the Commission is satisfied there was sufficient cause for the delay [K:cpa-limitation]. 

Your case would normally go to the District Consumer Disputes Redressal Commission [K:cpa-pecuniary]. The filing fee is generally Rs 0 for amounts up to Rs 5 lakh, but you should verify this on the portal [K:cpa-fee].

**What you can do now**
1. Call the National Consumer Helpline at 1915 or visit consumerhelpline.gov.in to see if they can still help resolve it informally [K:nch].
2. Contact the District Legal Services Authority (DLSA) or call the NALSA helpline at 15100 to ask about free legal aid [K:legal-aid], as they can help explain if your delay can be excused.
3. If you want to approach the District Consumer Commission, you can file online through the e-Jagriti portal without a lawyer [K:cpa-efiling], but you will need to ask the Commission to excuse the delay in filing.

**What I still need from you**
- Do you have the purchase invoice and warranty card?
- Did you raise any written complaints or service requests with the company?
- What is the name of the company or brand of the washing machine?

**When to get a real lawyer**
Get a real lawyer or visit the District Legal Services Authority immediately because your 2-year time limit to file a consumer case has already passed [K:cpa-limitation], and you need help asking the Commission to excuse the delay.

## Case file (intake)
```json
{
 "language": "en",
 "language_name": "English",
 "category": "consumer",
 "sub_type": "defective product",
 "summary": "The user purchased a washing machine for 30,000 in March 2023, which stopped working in April 2023. The company failed to repair it, and the user wants to know if they can file a consumer case now.",
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
   "event": "Bought a washing machine for 30,000."
  },
  {
   "date": "2023-04-01",
   "event": "Washing machine stopped working and company never fixed it."
  }
 ],
 "evidence_have": [],
 "steps_taken": [],
 "red_flags": [],
 "user_goal": "File a consumer case to get a resolution or refund for the defective washing machine.",
 "open_questions": [
  "Do you have the purchase invoice and warranty card?",
  "Did you raise any written complaints or service requests with the company?",
  "What is the name of the company or brand of the washing machine?"
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