# wage-multiturn - Vague first message, details in second turn

## Turn 1 - user
> my company is not paying me

## Turn 1 - Nyaya Saathi (unedited)
I am not a lawyer. I am here to help you understand your options and guide you step by step.

**What I understood**
Your company has not paid your salary, and you want to recover your dues.

**Where you stand**
Your salary is both a contractual debt and a right. Generally, monthly wages must be paid before the 7th day of the next month [K:cw-timely-payment]. If you resigned or left, dues should generally be paid within two working days [K:cw-timely-payment]. You can generally file a claim with the state Labour Department within three years [K:cw-claims], or treat it as a breach of contract under the Indian Contract Act, 1872 - Section 73 [K:wages-contract]. 

**What you can do now**
1. Ask HR or your employer in writing (via email or WhatsApp) for your unpaid salary with the exact dates and amounts [K:wages-relieving, K:notice-how-to-send]. Keep a written trail [K:wages-relieving].
2. Send a formal written demand for payment.
3. File a claim or complaint with the state Labour Department (Labour Commissioner office) [K:cw-claims].
4. You can also approach the District Legal Services Authority (DLSA) at your district court for free legal aid or to settle through Lok Adalat [K:legal-aid, K:lok-adalat].

**What I still need from you**
1. For how many months is your salary unpaid?
2. What is your monthly salary amount?
3. Have you raised this issue with your HR or management yet?

**When to get a real lawyer**
Get a real lawyer if the company refuses to pay after your written requests, or if you are in a senior managerial role and need to file a civil suit for recovery.

## Turn 2 - user
> I work in a small IT company in Chennai, salary 35,000 per month. They have not paid for August, September and October 2026. I am still working there. I have offer letter and old payslips.

## Turn 2 - Nyaya Saathi (unedited)
I am not a lawyer. I am here to help you understand your options and guide you step by step.

**What I understood**
Your IT company in Chennai has not paid your monthly salary of ₹35,000 for August, September, and October 2026, and you are still working there with your offer letter and old payslips.

**Where you stand**
Monthly wages must generally be paid before the 7th day of the next month [K:cw-timely-payment]. For example, your August salary was due by 7 September 2026 [K:cw-timely-payment]. Your unpaid salary is also a contractual debt under the Indian Contract Act, 1872 - Section 73 [K:wages-contract]. You can generally file a claim for unpaid wages with the state Labour Department within three years from the date it arose [K:cw-claims].

**What you can do now**
1. Ask HR / employer in writing for the unpaid salary with dates and amount [K:wages-relieving, K:notice-how-to-send]. Keep every message, as a written trail is your strongest evidence [K:wages-relieving].
2. Send a legal notice demanding payment within a deadline (usually 15 days) using Speed Post or Registered Post [K:notice-how-to-send].
3. File a claim / complaint with the state Labour Department (Labour Commissioner / Inspector-cum-Facilitator office) [K:cw-claims].
4. If needed, approach the District Legal Services Authority (DLSA) at your district court for free legal aid if you qualify, or try to settle through Lok Adalat [K:legal-aid, K:lok-adalat].

**What I still need from you**
1. Do you have attendance records, timesheets, or work messages for the unpaid period?
2. Have you sent any messages or emails asking for your salary yet, and did they reply?

**When to get a real lawyer**
Get a real lawyer or visit the District Legal Services Authority if your employer refuses to clear your ₹1,05,000 dues after your written requests.

## Case file (intake)
```json
{
 "language": "en",
 "language_name": "English",
 "category": "wages",
 "sub_type": "unpaid salary",
 "summary": "The user works at a small IT company in Chennai with a monthly salary of 35,000, and has not been paid for August, September, and October 2026. They are still employed at the company and possess an offer letter and old payslips.",
 "user_role": "employee",
 "other_party": {
  "name": null,
  "type": "company"
 },
 "state": "Tamil Nadu",
 "city": "Chennai",
 "amounts": {
  "disputed": 105000,
  "paid_value": null,
  "monthly_rent": null,
  "monthly_salary": 35000
 },
 "dates": {
  "incident": null,
  "purchase": null,
  "complaint_to_company": null,
  "moved_out": null,
  "last_working_day": null,
  "wages_due_from": "2026-08-01",
  "notice_received": null,
  "notice_deadline": null,
  "bank_return_memo": null
 },
 "employment_ended": false,
 "timeline": [],
 "evidence_have": [
  "offer letter",
  "old payslips"
 ],
 "steps_taken": [],
 "red_flags": [],
 "user_goal": "Get their unpaid salary from the company",
 "open_questions": [
  "Have you raised this issue with your HR or management yet?"
 ]
}
```

## Computed by code
```json
{
 "deadlines": [
  {
   "label": "Salary for the first unpaid month was due",
   "date": "2026-09-07",
   "days_left": -75,
   "status": "passed",
   "kb": "cw-timely-payment",
   "kind": "statutory_due",
   "basis": "before the 7th of the month after August 2026"
  },
  {
   "label": "Last date to file a wage claim (generally 3 years)",
   "date": "2029-09-07",
   "days_left": 1021,
   "status": "ok",
   "kb": "cw-claims",
   "kind": "limitation",
   "basis": "3 years from 2026-09-07"
  }
 ],
 "forum": null,
 "fee": null,
 "escalations": []
}
```

## Guard: first pass 0 violation(s), repaired=False, scrubbed=False, final=0

## Automatic checks
- PASS category
- PASS deadline_computed
- PASS deadline_date
- PASS mentions:1,05,000
- PASS guard_clean