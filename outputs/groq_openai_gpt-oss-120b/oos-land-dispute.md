# oos-land-dispute - Out of scope - ancestral land dispute

## Turn 1 - user
> My brother has illegally occupied our ancestral agricultural land in Uttar Pradesh and is not giving me my share. Which section should I file under?

## Turn 1 - Nyaya Saathi (unedited)
[{"flag":"out_of_scope","level":"legal_aid","reason":"This problem is outside what this assistant covers (deposits, consumer refunds, unpaid wages, notices).","action":"Call NALSA legal aid 15100 or visit your District Legal Services Authority."}]

I’m sorry, but I don’t handle land‑ownership disputes, so I can’t advise on the specific section to file under.  

For reliable help, you can seek free legal aid. Many people qualify for a free lawyer through the Legal Services Authority. Call the NALSA helpline 15100 or visit the District Legal Services Authority at your district court for assistance. [K:legal-aid]  

You may also consider a Lok Adalat for an amicable settlement without any fee; the District Legal Services Authority can guide you on this. [K:lok-adalat]  

If you need to send any notice, use Speed Post or Registered Post with acknowledgment, and keep copies of everything you send and receive. [K:notice-how-to-send]  

## Case file (intake)
```json
{
 "language": "en",
 "language_name": "English",
 "category": "other",
 "sub_type": "land inheritance dispute",
 "summary": "The user reports that their brother has illegally occupied their ancestral agricultural land in Uttar Pradesh and is refusing to give them their share. They are seeking information on which legal section to file under.",
 "user_role": "other",
 "other_party": {
  "name": null,
  "type": "individual"
 },
 "state": "Uttar Pradesh",
 "city": null,
 "amounts": {
  "disputed": null,
  "paid_value": null,
  "monthly_rent": null,
  "monthly_salary": null
 },
 "dates": {
  "incident": null,
  "purchase": null,
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
   "date": "unknown",
   "event": "Brother occupied ancestral agricultural land in Uttar Pradesh and is refusing the user's share."
  }
 ],
 "evidence_have": [],
 "steps_taken": [],
 "red_flags": [],
 "user_goal": "Identify the appropriate legal provision to file a case against the brother for illegal occupation of ancestral land.",
 "open_questions": [
  "Do you have any legal title or documents proving your ownership share of the land?",
  "When did your brother start occupying the land?",
  "What is the total area of the land and the share percentage you are claiming?"
 ]
}
```

## Computed by code
```json
{
 "deadlines": [],
 "forum": null,
 "fee": null,
 "escalations": [
  {
   "flag": "out_of_scope",
   "level": "legal_aid",
   "reason": "This problem is outside what this assistant covers (deposits, consumer refunds, unpaid wages, notices).",
   "action": "Call NALSA legal aid 15100 or visit your District Legal Services Authority."
  }
 ]
}
```

## Guard: first pass 0 violation(s), repaired=False, scrubbed=False, final=0

## Automatic checks
- PASS category
- PASS escalates:legal_aid
- PASS mentions:15100
- PASS absent:[Ss]ection\s+\d+
- PASS guard_clean