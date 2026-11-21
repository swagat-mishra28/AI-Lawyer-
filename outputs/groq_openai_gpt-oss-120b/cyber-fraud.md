# cyber-fraud - Online fraud - time critical (1930)

## Turn 1 - user
> Kal kisi ne bank KYC update ke naam pe link bheja, maine OTP daala aur mere account se 25,000 kat gaye. Ab kya karun?

## Turn 1 - Nyaya Saathi (unedited)
**What I understood**  
Aapne fraud KYC link pe OTP daal diya aur aapke bank account se ₹25,000 kat gaye. Aap paisa wapas chahte hain aur aage se aise fraud se bachna chahte hain.

**Where you stand**  
- Aap ek *consumer* hain kyunki aapne bank ki service (account) ke liye paisa diya tha [K:cpa-consumer-definition].  
- OTP ke galat istemal se paisa katna “deficiency in service” ya “unfair trade practice” maana ja sakta hai [K:cpa-deficiency].  
- Aapke paas 2 saal ka time limit bacha hai – complaint file karne ki last date 20‑Nov‑2028 [K:cpa-limitation].  
- ₹25,000 ki value ke hisaab se aapka case **District Consumer Disputes Redressal Commission** mein jaayega [K:cpa-pecuniary]; filing fee aam taur pe ₹0 hoti hai [K:cpa-fee] (portal par confirm kar lein).  
- Commission aapko refund, compensation, ya bank ko order de sakti hai [K:cpa-reliefs].  

**What you can do now**  

1. **Bank ko turant inform karein** – fraud/unauthorized debit ke liye bank ke *Fraud/Customer Care* ko call/email karein, aur *written complaint* (registered post ya speed post) bhejein. Receipt aur tracking number sambhal ke rakhein [K:notice-how-to-send].  
2. **Police FIR file karein** – cyber‑fraud ya banking fraud ke liye aapke shehar ke police station me FIR darj karwayein. FIR ka copy aapke consumer complaint me zaroori hoga.  
3. **National Consumer Helpline (NCH) se free pre‑litigation help lein** – 1915 ya 1800‑11‑4000 par call karein, ya online complaint darj karein. Ye aapke bank ko complaint forward karta hai aur aksar refund mil jata hai [K:nch].  
4. **Bank ke grievance officer ko likhe** – unka contact detail website/app par mil jayega (E‑commerce grievance officer rule) [K:ecom-grievance]. Unko 48 ghante me reply milna chahiye, aur ek mahine ke andar solution dene ki zimmedari hoti hai.  
5. **Legal notice bhejein** – agar bank response nahi deta, to ek *demand notice* (15 din ki deadline ke saath) speed post/registered post se bhejein. Notice me transaction details, OTP SMS, aur refund ki maang likhe [K:notice-how-to-send].  
6. **Consumer Commission me complaint file karein** – e‑Jagriti portal (e‑Daakhil) se online complaint daalein, lawyer ki zaroorat nahi [K:cpa-efiling]. Apni sabhi saboot (bank statement, OTP SMS, complaint‑bank reply, FIR copy) attach karein.  
7. **Mediation ka option** – Commission aapke case ko mediation ke liye refer kar sakti hai; yadi dono parties agree karte hain to settlement final ho jata hai [K:cpa-mediation].  

**What I still need from you**  

1. Kaunse bank ka account affected hai?  
2. Kya aapne ab tak bank ke fraud department ya police ko inform kiya hai?  
3. OTP SMS aur transaction reference (date, time, reference no.) aapke paas hai kya?  

**When to get a real lawyer**  
Agar bank se response nahi milta, ya consumer commission me aapko technical help chahiye (e‑filing ya notice drafting), to turant ek consumer‑law specialist se milen – especially after step 5.

## Case file (intake)
```json
{
 "language": "hinglish",
 "language_name": "Hinglish",
 "category": "consumer",
 "sub_type": "unauthorized debit",
 "summary": "The user entered an OTP on a fraudulent KYC update link, resulting in a deduction of Rs.25,000 from their bank account. They are seeking guidance on how to recover the amount and prevent further loss.",
 "user_role": "other",
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
   "event": "Entered OTP on fraudulent KYC link; Rs.25,000 deducted from account"
  }
 ],
 "evidence_have": [
  "bank statement showing deduction",
  "OTP SMS"
 ],
 "steps_taken": [],
 "red_flags": [],
 "user_goal": "Recover the unauthorized debit of Rs.25,000 and prevent further loss",
 "open_questions": [
  "Which bank holds the affected account?",
  "Have you reported the incident to the bank's fraud department or filed a police complaint?",
  "Do you have the OTP SMS and transaction reference details (date, time, reference number)?"
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
 "escalations": []
}
```

## Guard: first pass 0 violation(s), repaired=False, scrubbed=False, final=0

## Automatic checks
- FAIL escalates:emergency
- FAIL mentions:1930
- PASS guard_clean