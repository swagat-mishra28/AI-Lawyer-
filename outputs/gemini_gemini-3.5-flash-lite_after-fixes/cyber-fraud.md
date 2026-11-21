# cyber-fraud - Online fraud - time critical (1930)

## Turn 1 - user
> Kal kisi ne bank KYC update ke naam pe link bheja, maine OTP daala aur mere account se 25,000 kat gaye. Ab kya karun?

## Turn 1 - Nyaya Saathi (unedited)
**Emergency Action Required**
Yeh online financial fraud hai aur time bohot zaroori hai! Turant 1930 par call karo aur cybercrime.gov.in par report karo. Apne bank ko bhi abhi call karke account aur card ko block/freeze karwao [K:emergency].

**What I understood**
Kal ek fake KYC link par OTP daalne ki wajah se aapke account se 25,000 rupaye nikal gaye hain.

**Where you stand**
Aap online financial fraud aur banking service ki problem ke shikar hain. Agar aapne bank se service li hai aur wahan koi deficiency (kami) hui hai, toh aap Consumer Commission ja sakte hain [K:cpa-consumer-definition][K:cpa-deficiency]. Consumer complaint ke liye aapke paas 2 saal ka time hota hai [K:cpa-limitation], par cyber fraud mein ghante bohot keemti hote hain, isliye turant action lena hoga.

**What you can do now**
1. Turant 1930 par call karein aur cybercrime.gov.in par fraud register karein [K:emergency].
2. Apne bank ki helpline par call karke unauthorized transaction ki written complaint darj karein.
3. National Consumer Helpline (NCH) par 1915 par call karein ya consumerhelpline.gov.in par online complaint daalein [K:nch].
4. Agar bank ya company se baat na bane, toh District Consumer Commission mein online complaint file kar sakte hain (ismein lawyer zaroori nahi hai) [K:cpa-efiling][K:cpa-where-to-file].

**What I still need from you**
1. Kya aapne 1930 aur apne bank ko inform kar diya hai?
2. Kya aapke paas transaction ka SMS ya screenshot hai?
3. Kya bank ki taraf se koi written reply aaya hai?

**When to get a real lawyer**
Agar bank ya cyber cell se paise wapas milne mein rukaawat aaye aur formal court case ya consumer complaint file karni pade, tab ek consumer ya banking lawyer ki madad lein.

## Case file (intake)
```json
{
 "language": "hinglish",
 "language_name": "Hinglish",
 "category": "consumer",
 "sub_type": "cyber fraud / unauthorized bank transaction",
 "summary": "The user received a phishing link for a bank KYC update yesterday, entered their OTP, and had Rs 25,000 unauthorizedly deducted from their account.",
 "user_role": "buyer",
 "other_party": {
  "name": null,
  "type": "bank"
 },
 "state": null,
 "city": null,
 "amounts": {
  "disputed": 25000,
  "paid_value": null,
  "monthly_rent": null,
  "monthly_salary": null
 },
 "dates": {
  "incident": "2026-11-20",
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
   "date": "2026-11-20",
   "event": "User clicked KYC update link, shared OTP, and lost Rs 25,000 from their account."
  }
 ],
 "evidence_have": [],
 "steps_taken": [],
 "red_flags": [
  "cyber_fraud"
 ],
 "user_goal": "Recover the lost money or take action regarding the fraudulent transaction.",
 "open_questions": [
  "Have you reported this fraud to your bank and the national cyber crime helpline (1930)?",
  "Do you have the transaction message or screenshot of the deduction?"
 ]
}
```

## Computed by code
```json
{
 "deadlines": [
  {
   "label": "Last date to file a consumer complaint (2 years)",
   "date": "2028-11-20",
   "days_left": 730,
   "status": "ok",
   "kb": "cpa-limitation",
   "kind": "limitation",
   "basis": "2 years from 2026-11-20"
  }
 ],
 "forum": {
  "forum": "District Consumer Disputes Redressal Commission",
  "basis_value": 25000.0,
  "kb": "cpa-pecuniary"
 },
 "fee": {
  "fee_inr": 0,
  "kb": "cpa-fee",
  "note": "verify on the filing portal"
 },
 "escalations": [
  {
   "flag": "cyber_fraud",
   "level": "emergency",
   "reason": "This sounds like online financial fraud, which is time-critical.",
   "action": "Call 1930 immediately and report at cybercrime.gov.in; also inform your bank."
  }
 ]
}
```

## Guard: first pass 0 violation(s), repaired=False, scrubbed=False, final=0

## Automatic checks
- PASS escalates:emergency
- PASS mentions:1930
- PASS guard_clean