# con-builder-large - Builder delay, Rs 85 lakh (state commission, large amount)

## Turn 1 - user
> I paid 85 lakh rupees to a builder in Noida for a flat in 2021. Possession was promised in December 2023 but the project is still incomplete. What can I do?

## Turn 1 - Nyaya Saathi (unedited)
**Urgent Note:** The usual 2-year time limit to file a consumer complaint passed on 2025-12-01 [K:cpa-limitation]. Only a Commission can excuse this delay. Because the amount (Rs 8,500,000) is large, you should talk to a lawyer or the District Legal Services Authority (DLSA) by calling 15100 right away [K:legal-aid]. 

**What I understood**
You paid Rs 85 lakh to a builder in Noida in 2021 for a flat, but the project is still incomplete after the promised December 2023 possession date.

**Where you stand**
Not handing over possession on time is a deficiency in service [K:cpa-deficiency]. Since the amount paid is above Rs 50 lakh and up to Rs 2 crore, your case falls under the State Consumer Disputes Redressal Commission [K:cpa-pecuniary]. The filing fee is generally around Rs 2,000 (please verify on the portal) [K:cpa-fee]. Builder delay cases can also be taken to the state RERA authority, but these cases are complex and usually require a lawyer [K:rera-note].

**What you can do now**
1. Contact a lawyer or your local District Legal Services Authority (DLSA) at 15100 immediately to see how to handle the expired time limit [K:cpa-limitation, K:legal-aid].
2. Collect your builder-buyer agreement, payment receipts, bank statements, and any written communication with the builder.
3. Consult a lawyer or RERA expert before filing any formal case due to the large amount involved [K:rera-note].

**What I still need from you**
1. Do you have a builder-buyer agreement with a penalty clause for delayed possession?
2. Have you sent any formal written complaints or legal notices to the builder regarding this delay?

**When to get a real lawyer**
Right now, because your normal time limit has passed and the amount involved is large, you need a lawyer or free legal aid immediately [K:cpa-limitation, K:legal-aid].

## Case file (intake)
```json
{
 "language": "en",
 "language_name": "English",
 "category": "consumer",
 "sub_type": "builder delayed possession",
 "summary": "The user paid 85 lakh rupees to a builder in Noida in 2021 for a flat. Although possession was promised by December 2023, the project remains incomplete.",
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
   "date": "2021",
   "event": "Paid 85 lakh rupees to a builder in Noida for a flat."
  },
  {
   "date": "2023-12",
   "event": "Promised date of possession."
  }
 ],
 "evidence_have": [],
 "steps_taken": [],
 "red_flags": [],
 "user_goal": "Get resolution or refund for the delayed flat possession from the builder.",
 "open_questions": [
  "Do you have a builder-buyer agreement with a specified penalty clause for delayed possession?",
  "Have you sent any formal written complaints or legal notices to the builder regarding the delay?"
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