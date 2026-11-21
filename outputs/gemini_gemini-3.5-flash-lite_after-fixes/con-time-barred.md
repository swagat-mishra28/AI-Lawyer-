# con-time-barred - Consumer complaint after 2-year limit

## Turn 1 - user
> I bought a washing machine for 30,000 in March 2023 and it stopped working in April 2023. The company never fixed it. Can I file a consumer case now?

## Turn 1 - Nyaya Saathi (unedited)
**What I understood**
You bought a washing machine for Rs 30,000 in March 2023, but it broke down in April 2023 and the company never fixed it.

**Where you stand**
The usual time limit to file a consumer complaint is 2 years from the date the problem arose [K:cpa-limitation]. For your case, that deadline passed on April 1, 2025. Because the time limit has passed, you generally cannot file a standard case unless the District Consumer Disputes Redressal Commission agrees to excuse the delay for a very good reason. 

**What you can do now**
1. Talk to a lawyer or your local District Legal Services Authority (DLSA) by calling the NALSA helpline at 15100 to see if your delay can be excused [K:legal-aid].
2. You can still try calling the National Consumer Helpline at 1915 to see if they can help resolve the issue with the company informally [K:nch].

**What I still need from you**
1. Do you have the purchase invoice or bill?
2. Do you have any old emails, chat records, or service ticket numbers showing you complained to the company earlier?

**When to get a real lawyer**
You should speak to a lawyer immediately because your time limit to file a consumer case has already passed, and you will need legal help to ask the Commission for an extension.

## Case file (intake)
```json
{
 "language": "en",
 "language_name": "English",
 "category": "consumer",
 "sub_type": "defective product",
 "summary": "The user bought a washing machine for 30,000 in March 2023, which stopped working in April 2023. The company never fixed it, and the user wants to know if they can file a consumer case now.",
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
   "event": "Washing machine stopped working and the company never fixed it."
  }
 ],
 "evidence_have": [],
 "steps_taken": [],
 "red_flags": [],
 "user_goal": "File a consumer case to get a refund or resolution for the defective washing machine.",
 "open_questions": [
  "Do you have the purchase invoice or bill for the washing machine?",
  "Did you raise any written complaints or service tickets with the company?"
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
   "action": "Only the court or Commission can excuse the delay, and you must show a good reason - see a lawyer or DLSA (15100) quickly."
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