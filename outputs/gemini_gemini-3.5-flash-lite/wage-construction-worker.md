# wage-construction-worker - Daily-wage construction worker, Hinglish, voice-like text

## Turn 1 - user
> sir main bihar se hu mumbai me construction site pe kaam karta tha thekedar ne 12 din ka paisa nahi diya 600 rupay roj ke hisab se. ab phone bhi nahi utha raha. koi kagaz nahi hai bas hajiri register me naam hai

## Turn 1 - Nyaya Saathi (unedited)
**What I understood**
Aapne Mumbai me construction site pe 12 din kaam kiya (₹600 roz ke hisab se, total ₹7,200), lekin contractor ne paisa nahi diya aur phone nahi utha raha. Aapke paas attendance register me naam hona sabse bada saboot hai. Main koi lawyer nahi hu, par aapko bata sakta hu ki aage kya karna hai.

**Where you stand**
* Contractor ka kaam hai ki agar aapne kaam kiya hai toh aapko samay par wages (salary) milni chahiye [K:cw-timely-payment]. Generally, agar job chhod di ya hataye gaye, toh wages jaldi milni chahiye (Code on Wages, 2019 ke tahat state Labour Department me claim file kiya ja sakta hai 3 saal ke andar) [K:cw-claims].
* Kyunki aap construction worker hain, aapko state Labour Department aur free legal aid ki madad mil sakti hai.

**What you can do now**
1. **Attendance Register ka proof:** Site par jahan aapka naam hajiri register (attendance register) me hai, uska photo ya video lene ki koshish karein agar mil sake.
2. **State Labour Department me jaein:** Apne local state Labour Department office (Labour Commissioner / Inspector-cum-Facilitator office) me jaakar apna claim file karein [K:cw-claims]. Aap yahan apne 12 din ke wages (₹7,200) ke liye shikayat kar sakte hain.
3. **Free Legal Aid lo:** Agar aapko koi madad chahiye, toh aap District Legal Services Authority (DLSA) ya NALSA helpline (15100) par call kar sakte hain. Industrial workmen aur kam income wale logon ko free lawyer milta hai [K:legal-aid].

**What I still need from you**
1. Contractor ka naam ya phone number kya hai?
2. Aapka aakhri din (last working day) kab tha construction site par?

**When to get a real lawyer**
Agar Labour Department me baat aage na bade ya contractor bada fraud kare, toh aapko DLSA ke zariye ya ek personal lawyer ki madad leni chahiye.

## Case file (intake)
```json
{
 "language": "hinglish",
 "language_name": "Hinglish",
 "category": "wages",
 "sub_type": "unpaid daily wages",
 "summary": "A construction worker from Bihar who worked in Mumbai states that his contractor has not paid his wages for 12 days at the rate of 600 rupees per day and is now ignoring his calls. The user has no physical documents except for his name being in the attendance register.",
 "user_role": "worker",
 "other_party": {
  "name": null,
  "type": "individual"
 },
 "state": "Maharashtra",
 "city": "Mumbai",
 "amounts": {
  "disputed": 7200,
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
 "employment_ended": true,
 "timeline": [],
 "evidence_have": [
  "attendance register entry"
 ],
 "steps_taken": [
  "called the contractor, but he is not picking up the phone"
 ],
 "red_flags": [],
 "user_goal": "Get the unpaid wages of 12 days from the contractor",
 "open_questions": [
  "What is the contractor's name or phone number?",
  "When was your last working day on the construction site?"
 ]
}
```

## Computed by code
```json
{
 "deadlines": [],
 "forum": null,
 "fee": null,
 "escalations": []
}
```

## Guard: first pass 0 violation(s), repaired=False, scrubbed=False, final=0

## Automatic checks
- PASS category
- PASS language
- PASS mentions:7,200
- PASS mentions:15100
- PASS guard_clean