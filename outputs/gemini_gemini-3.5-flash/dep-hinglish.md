# dep-hinglish - Deposit, Hinglish, painting excuse

## Turn 1 - user
> Bhai mera landlord 40000 ka security deposit wapas nahi de raha. Maine 15 sept ko flat khali kiya tha Bangalore mein, chaabi bhi de di thi. Ab bolta hai painting aur cleaning ka paisa katega, kitna katega bata bhi nahi raha. Rent agreement hai 11 mahine ka aur deposit UPI se diya tha.

## Turn 1 - Nyaya Saathi (unedited)
Main AI assistant hoon, real lawyer nahi hoon. AAPKA case yahan samajhte hain:

**What I understood**
Aapne 15 September 2026 ko Bangalore mein flat khali karke keys de di thi. Landlord ₹40,000 deposit nahi lauta raha aur bina specific amount bataye painting/cleaning ka katne ki baat kar raha hai.

**Where you stand**
- Rent agreement ek contract hota hai. Agar aapne flat khali kar diya hai, toh landlord ko sirf allowed katoti (deductions) karke baaki paisa laotana hoga [K:deposit-contract].
- Painting ya cleaning ki vague katoti sahi nahi hoti; generally landlord ko bills ya proof dena chahiye [K:deposit-deductions].
- Non-return of deposit ek civil dispute hota hai, police ka maamla nahi [K:deposit-not-police].
- Paise recovery ke liye legal suit generally 3 saal ke andar file karna hota hai (15 September 2029 tak) [K:deposit-limitation].

**What you can do now**
1. **Written Request Bhejein:** Landlord ko WhatsApp/Email par message karein ki woh final refund de ya exact bills/itemised list de.
2. **Legal Notice Bhejein:** Agar woh response na de, toh Registered Post / Speed Post se ek legal notice bhejein [K:notice-how-to-send].
3. **Lok Adalat / Settlement:** District Legal Services Authority (DLSA) ke zariye bina kisi court fee ke Lok Adalat mein pre-litigation settlement try karein [K:lok-adalat].
4. **Civil Suit File Karein:** Baani na bane toh civil court mein recovery suit (summary suit) file kar sakte hain [K:deposit-civil-suit].
5. **Free Legal Aid:** Agar aap eligible hain (jaise low income, women, etc.), toh NALSA helpline 15100 par call karke free lawyer le sakte hain [K:legal-aid].

**What I still need from you**
1. Kya rent agreement mein khali karte waqt painting/cleaning charges katne ka koi clause likha hai?
2. Aapka monthly rent kitna tha?
3. Kya aapke paas keys handover karne aur flat ki photos/videos ki koi proof hai?

**When to get a real lawyer**
Agar legal notice bhejne ke baad bhi landlord refund na de, toh civil court mein recovery suit draft karwane ke liye lawyer se milein.

## Case file (intake)
```json
{
 "language": "hinglish",
 "language_name": "Hinglish",
 "category": "deposit",
 "sub_type": "security deposit refund",
 "summary": "The user's landlord in Bangalore is refusing to return a security deposit of ₹40,000 after the user moved out on September 15, 2026 and handed over the keys. The landlord claims deductions for painting and cleaning without specifying the amount.",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "state": "Karnataka",
 "city": "Bangalore",
 "amounts": {
  "disputed": 40000,
  "paid_value": null,
  "monthly_rent": null,
  "monthly_salary": null
 },
 "dates": {
  "incident": "2026-09-15",
  "purchase": null,
  "complaint_to_company": null,
  "moved_out": "2026-09-15",
  "last_working_day": null,
  "wages_due_from": null,
  "notice_received": null,
  "notice_deadline": null,
  "bank_return_memo": null
 },
 "employment_ended": null,
 "timeline": [
  {
   "date": "2026-09-15",
   "event": "User vacated the flat in Bangalore and handed over the keys."
  }
 ],
 "evidence_have": [
  "11-month rent agreement",
  "UPI payment proof of security deposit"
 ],
 "steps_taken": [
  "Vacated the flat and handed over keys"
 ],
 "red_flags": [],
 "user_goal": "Get full or fair refund of the ₹40,000 security deposit from the landlord",
 "open_questions": [
  "What is the landlord's name?",
  "Does the rent agreement mention painting or cleaning deduction clauses upon move-out?",
  "What was the monthly rent amount?"
 ]
}
```

## Computed by code
```json
{
 "deadlines": [
  {
   "label": "Last date to file a money-recovery suit (generally 3 years)",
   "date": "2029-09-15",
   "days_left": 1029,
   "status": "ok",
   "kb": "deposit-limitation",
   "kind": "limitation",
   "basis": "3 years from move-out 2026-09-15"
  }
 ],
 "forum": null,
 "fee": null,
 "escalations": []
}
```

## Guard: first pass 0 violation(s), repaired=False, scrubbed=False, final=0

## Draft: Legal notice to landlord (deposit refund)
**LEGAL NOTICE**

**Date:** 21 November 2026
**Sent by:** Speed Post / Registered Post A.D. and email

**From:** [FILL: your full name], [FILL: your address]
**To:** [FILL: name of the landlord], [FILL: their address]

**Subject: Notice for refund of the security deposit of Rs 40,000**

Sir/Madam,

I, the undersigned, state as follows:

**Facts**

1. I entered into an 11-month rent agreement with you for the residential property situated at [FILL: Property Address] in Bangalore, Karnataka, and paid a security deposit amount of ₹40,000 via UPI.

2. On September 15, 2026, I vacated the subject premises and duly handed over the keys of the property to you.

3. Following my move-out, you refused to return my security deposit of ₹40,000, citing deductions for painting and cleaning of the premises.

4. You have claimed these deductions for painting and cleaning without specifying or detailing the exact deduction amounts.

5. As of date, the total security deposit amount of ₹40,000 remains unpaid and withheld by you.

**Legal basis**

1. The security deposit was paid as a refundable sum under the rent agreement. Its retention after I vacated is a breach of contract, for which I am entitled to recover the amount with compensation under the Indian Contract Act, 1872.

**Demand**

I hereby call upon you to pay Rs 40,000 within **15 days** of receiving this notice, by bank transfer to the account
I will share on request, and to confirm in writing.

If you fail to do so, I shall be constrained to initiate proceedings for recovery before the competent civil court / Lok Adalat, claiming the amount along with interest, compensation
and costs, entirely at your risk as to costs and consequences.

A copy of this notice is retained for further action.

[FILL: your full name]
[FILL: signature]

## Practice mode
- **User:** Sir, please return my 40,000 deposit. I left the flat on 15 September in good condition.
- **Other side:** Arrey bhai, direct 40,000 kaise wapas kar du? Flat me painting aur deep
- **User:** If you don't return it in 15 days I will send a legal notice and go to Lok Adalat.
- **Other side:** Arrey bhai, chote se matter ke liye legal notice aur Lok Adalat ki kya zaroorat hai? Painter ne abhi tak final bill nahi diya hai, painting aur cleaning me bohot

### Coach feedback
**Aapne kya accha kiya:**
1. Move-out date aur exact amount (₹40,000) pehle hi clear mention kiya.
2. Calm and firm tone rakha aur Lok Adalat [K:lok-adalat] ka option use kiya.

**Kahan improve kar sakte hain:**
1. **Vague deductions ko challenge karein:** Landlord bina bill ke painting deduction ki baat kar raha hai. Unse receipts mangein [K:deposit-deductions].
   * *Better line:* "Sir, deductions generally justify karne padte hain [K:deposit-deductions]. Aap painter ke bills aur photos bhej dijiye, tab tak baaki balance refund kar dijiye."
2. **Rent contract cite karein:** Direct threat se pehle agreement ka refrence dein [K:deposit-contract].
   * *Better line:* "Contract ke according deposit refundable hai [K:deposit-contract]. Normal wear & tear ka paisa katna allow nahi hota."

**Strong Closing Line:**
"Sir, aap ₹40,000 deposit (ya valid bills kaat kar balance) 25 September tak mere bank account me transfer kar dijiye, nahi toh mujhe dispute resolution ke liye Lok Adalat [K:lok-adalat] jana padega."

## Automatic checks
- PASS category
- PASS language
- PASS no_false_alarm
- PASS deadline_computed
- PASS deadline_date
- PASS mentions:notice
- PASS mentions:itemised
- PASS guard_clean
- PASS draft_no_legal_refs_in_facts