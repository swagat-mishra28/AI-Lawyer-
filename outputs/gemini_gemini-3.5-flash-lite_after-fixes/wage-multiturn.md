# wage-multiturn - Vague first message, details in second turn

## Turn 1 - user
> my company is not paying me

## Turn 1 - Nyaya Saathi (unedited)
*I am not a lawyer. I am Nyaya Saathi, here to help you understand your options.*

**What I understood**
Your company has not paid your salary, and you want to get your money.

**Where you stand**
Generally, monthly wages must be paid before the 7th day of the next month [K:cw-timely-payment]. If you resigned or left, your due wages must generally be paid within two working days [K:cw-timely-payment]. Unpaid salary is also treated as a debt under your employment contract, which you can recover [K:wages-contract]. You generally have up to three years to file a claim for unpaid wages [K:cw-claims].

**What you can do now**
1. Ask your employer or HR in writing (via email or message) for your unpaid salary, stating the exact amount and dates [K:wages-relieving][K:notice-how-to-send]. Keep a written trail of all your messages [K:wages-relieving].
2. Send a formal written demand notice to the company for the payment.
3. File a claim with the authority appointed under the state Labour Department [K:cw-claims].
4. If you qualify (such as for industrial workmen or low annual income), you can contact the District Legal Services Authority (DLSA) at your district court or call the NALSA helpline 15100 for free legal aid [K:legal-aid].

**What I still need from you**
1. How many months of salary are pending?
2. Are you still working there or has your employment ended?
3. Do you have your appointment letter or any emails/messages showing your salary?

**When to get a real lawyer**
Consult a lawyer if the company refuses to pay after your written requests, or if you are in a senior managerial role where civil court recovery is needed.

## Turn 2 - user
> I work in a small IT company in Chennai, salary 35,000 per month. They have not paid for August, September and October 2026. I am still working there. I have offer letter and old payslips.

## Turn 2 - Nyaya Saathi (unedited)
*I am not a lawyer. I am Nyaya Saathi, here to help you understand your options.*

**What I understood**
You work at an IT company in Chennai with a monthly salary of ₹35,000. Your salary for August, September, and October 2026 has not been paid, and you are still working there.

**Where you stand**
* Monthly wages must generally be paid before the 7th day of the next month [K:cw-timely-payment]. For example, your August salary was due by 7 September 2026 [K:cw-timely-payment].
* Your appointment letter is a contract, and unpaid salary is a debt your employer owes you [K:wages-contract]. 
* You generally have up to three years from the date the wage was due to file a claim [K:cw-claims].
* The rules come under the Code on Wages, 2019 [K:cw-in-force], but your local state Labour Department office can confirm the exact procedure in Tamil Nadu [K:cw-in-force].

**What you can do now**
1. Ask HR or your employer in writing (via email or message) for your unpaid salary, and keep a written trail of all your messages [K:wages-relieving][K:notice-how-to-send].
2. File a claim for unpaid wages before the authority appointed under the state Labour Department [K:cw-claims].
3. Visit the District Legal Services Authority (DLSA) at your district court or call the NALSA helpline 15100 if you want to check if you qualify for a free lawyer [K:legal-aid].
4. You can also ask about settling the matter without a court case through a Lok Adalat at the DLSA, which is free [K:lok-adalat].

**What I still need from you**
1. Have you raised a written complaint or sent an email to HR or management regarding the pending salary?
2. Do you have attendance records, timesheets, or work emails/messages for August, September, and October?

**When to get a real lawyer**
Consult a lawyer or consider a civil suit if the company refuses to pay, or if you hold a senior managerial role that requires formal legal recovery [K:wages-contract].

## Case file (intake)
```json
{
 "language": "en",
 "language_name": "English",
 "category": "wages",
 "sub_type": "unpaid salary",
 "summary": "The user works at a small IT company in Chennai with a monthly salary of 35,000 rupees and states that their salary has not been paid for August, September, and October 2026. The user is still employed there and possesses an offer letter and old payslips.",
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
 "timeline": [
  {
   "date": "2026-11-21",
   "event": "User stated that their company is not paying them."
  },
  {
   "date": "2026-11-21",
   "event": "User provided details: works in Chennai IT company, monthly salary 35000, unpaid for August, September, and October 2026, still working."
  }
 ],
 "evidence_have": [
  "offer letter",
  "old payslips"
 ],
 "steps_taken": [],
 "red_flags": [],
 "user_goal": "Get their unpaid salary from the company",
 "open_questions": [
  "Have you raised a written complaint or sent an email to HR or management regarding the pending salary?"
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
- FAIL mentions:1,05,000
- PASS guard_clean