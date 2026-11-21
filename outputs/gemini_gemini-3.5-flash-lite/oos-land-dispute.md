# oos-land-dispute - Out of scope - ancestral land dispute

## Turn 1 - user
> My brother has illegally occupied our ancestral agricultural land in Uttar Pradesh and is not giving me my share. Which section should I file under?

## Turn 1 - Nyaya Saathi (unedited)
I am sorry, but property and land disputes are outside what I cover, and I cannot guess about the law or suggest sections. 

For real help, you can approach Free legal aid [K:legal-aid]. Under the Legal Services Authorities Act, many people are entitled to a free lawyer from the Legal Services Authority: women and children, members of Scheduled Castes/Tribes, persons with disabilities, industrial workmen, victims of disaster or trafficking, people in custody, and people whose annual income is below the limit set by their state [K:legal-aid]. Call the NALSA helpline 15100 or visit the District Legal Services Authority (DLSA) at your district court [K:legal-aid]. 

You may also explore Lok Adalat (settlement, free), which settles disputes by agreement, including before any case is filed [K:lok-adalat]. There is no fee, and a settlement there is final and binding like a court decree; ask the District Legal Services Authority about this [K:lok-adalat].

[{"flag": "out_of_scope", "level": "legal_aid", "reason": "This problem is outside what this assistant covers (deposits, consumer refunds, unpaid wages, notices).", "action": "Call NALSA legal aid 15100 or visit your District Legal Services Authority."}]

## Case file (intake)
```json
{
 "language": "en",
 "language_name": "English",
 "category": "other",
 "sub_type": "ancestral land dispute",
 "summary": "The user states that their brother has illegally occupied their ancestral agricultural land in Uttar Pradesh and is denying them their rightful share. The user is asking for legal advice on which section to file under.",
 "user_role": "other",
 "other_party": {
  "name": "Brother",
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
 "timeline": [],
 "evidence_have": [],
 "steps_taken": [],
 "red_flags": [],
 "user_goal": "Find out which section to file under to get their share of ancestral agricultural land",
 "open_questions": [
  "Is there a formal partition or will regarding the ancestral land?",
  "Have you approached the local revenue authorities or police regarding the occupation?"
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