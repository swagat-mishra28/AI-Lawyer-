# con-builder-large - Builder delay, Rs 85 lakh (state commission, large amount)

## Turn 1 - user
> I paid 85 lakh rupees to a builder in Noida for a flat in 2021. Possession was promised in December 2023 but the project is still incomplete. What can I do?

## Turn 1 - Nyaya Saathi (unedited)
**What I understood**
You paid 85 lakh rupees to a builder in Noida in 2021 for a flat, but the builder missed the promised December 2023 possession date and the project is still incomplete.

**Where you stand**
- Because the value paid is above Rs 50 lakh up to Rs 2 crore, your case generally goes to the State Consumer Disputes Redressal Commission [K:cpa-pecuniary].
- The filing fee is generally around Rs 2,000, but you should verify this on the filing portal [K:cpa-fee].
- Delays in handing over a flat by a builder can be taken to the state RERA authority, and sometimes to a Consumer Commission [K:rera-note].
- Note that because the problem is still continuing, when the 2-year time limit [K:cpa-limitation] starts is not straightforward, so you should act without delay.

**What you can do now**
1. Write to the company's customer care or grievance officer and keep the ticket number.
2. Send a written demand or legal notice giving a clear deadline (usually 15 days) [K:notice-how-to-send].
3. For builder and flat delays, these cases usually involve large amounts and complex agreements, so you should talk to a lawyer [K:rera-note].

**What I still need from you**
- Do you have a builder-buyer agreement with the possession date mentioned?
- Have you sent any written complaints or legal notices to the builder yet?
- Are you seeking a refund of the amount paid or possession with compensation for delay?

**When to get a real lawyer**
Because the amount (Rs 8,500,000) is large and involves a builder delay, consult a lawyer before filing [K:rera-note]. *(Note: I do not quote judgments because AI often invents them, and a lawyer can find the right ones [K:no-case-law].)*

## Case file (intake)
```json
{
 "language": "en",
 "language_name": "English",
 "category": "consumer",
 "sub_type": "builder delayed possession",
 "summary": "The user paid 85 lakh rupees to a builder in Noida in 2021 for a flat. Possession was promised by December 2023, but the project is still incomplete.",
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
 "user_goal": "Get possession of the flat or take legal action regarding the delayed project.",
 "open_questions": [
  "Do you have a builder-buyer agreement with the possession date mentioned?",
  "Have you sent any written complaints or legal notices to the builder yet?",
  "Are you seeking a refund of the amount paid or possession with compensation for delay?"
 ]
}
```

## Computed by code
```json
{
 "deadlines": [],
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
   "flag": "limitation_unclear",
   "level": "lawyer_recommended",
   "reason": "The problem is still continuing, so when the 2-year time limit starts is not straightforward.",
   "action": "File without delay and ask a lawyer to confirm the time limit for your facts."
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