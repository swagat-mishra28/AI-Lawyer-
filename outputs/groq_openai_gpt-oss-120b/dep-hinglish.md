# dep-hinglish - Deposit, Hinglish, painting excuse

## Turn 1 - user
> Bhai mera landlord 40000 ka security deposit wapas nahi de raha. Maine 15 sept ko flat khali kiya tha Bangalore mein, chaabi bhi de di thi. Ab bolta hai painting aur cleaning ka paisa katega, kitna katega bata bhi nahi raha. Rent agreement hai 11 mahine ka aur deposit UPI se diya tha.

## Turn 1 - Nyaya Saathi (unedited)
**What I understood**  
Aapne 15 Sept 2026 ko Bangalore mein flat khali kiya, chaabi de di aur ₹40,000 ka security deposit UPI se diya. Landlord ab painting‑aur‑cleaning ke liye katne ka keh raha hai, lekin amount nahi bataya.

**Where you stand**  
- Rent agreement (chahe likha ho ya nahi) ek contract hai, aur usme likha ho toh deposit refundable hai jab tak agreement mein koi specific deduction ka clause na ho — agar landlord ne aisa clause nahi dala, to wo sirf actual damage ya unpaid rent ke liye hi kat sakta hai [K:deposit-contract].  
- Agar likhit clause nahi hai, to aapke paas UPI receipt, agreement aur keys handover ka proof strong evidence hai [K:deposit-no-agreement].  
- Deductions ko justify karne ke liye landlord ko itemised bill ya photos dikhane chahiye; “painting” ya “cleaning” bina amount ke kamzor claim hai [K:deposit-deductions] (generally).  
- Deposit wapas na milne ka case civil dispute hai, police ya consumer commission se nahi suljhega [K:deposit-not-police], [K:deposit-not-consumer].  
- Aapke paas 3 saal ka limitation period hai – suit file karne ki last date 15 Sept 2029 (ab 1029 din bache hain) [K:deposit-limitation].

**What you can do now**  

1. **Written demand** – WhatsApp/email se landlord ko likhit mein 15 din ka deadline dekar poora ₹40,000 wapas maange. Saath hi “itemised list of deductions with bills/photos” maange.  
   - Is notice ko Speed Post/Registered Post se bheje, receipt aur tracking save karein [K:notice-how-to-send].  

2. **Legal notice** – Agar 15 din mein response na mile, to ek lawyer ya free legal‑aid se formal legal notice bhejein (same 15‑day deadline).  

3. **Pre‑litigation settlement (Lok Adalat)** – District Legal Services Authority se free Lok Adalat ka option le sakte hain; yahan dono parties milke settlement karte hain, koi fee nahi [K:lok-adalat].  

4. **Civil suit for money recovery** – Agar settlement fail ho, to local civil court mein “money recovery suit” file karein (summary suit possible because a written agreement exists). Court fee aur process state‑wise alag hota hai, free legal‑aid se madad mil sakti hai [K:deposit-civil-suit] (generally).  

5. **Free legal aid** – Agar aapki annual income limit ke andar hain ya eligible categories mein aate hain, to NALSA (15100) ya apne district legal services authority se free lawyer le sakte hain [K:legal-aid].

**What I still need from you**  

1. Landlord ne koi likhit notice ya estimate of deductions bheja hai kya?  
2. Aapke paas move‑out ke din ki photos/videos ya landlord ko bheje gaye messages hain?  
3. Rent receipts ya proof ki aapne rent & bills time pe pay kiye the?

**When to get a real lawyer**  
Agar landlord 15 din ke andar koi itemised deduction nahi deta ya aapko legal notice bhejne mein madad chahiye, turant free legal‑aid ya private lawyer se sampark karein – especially before you file the court suit (deadline 15 Sept 2029).

## Case file (intake)
```json
{
 "language": "hinglish",
 "language_name": "Hinglish",
 "category": "deposit",
 "sub_type": "security deposit withheld",
 "summary": "The tenant vacated a rented flat in Bangalore on 15 September and handed over the keys. The landlord is refusing to return the ₹40,000 security deposit, claiming deductions for painting and cleaning without specifying amounts. The tenant seeks the full return of the deposit.",
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
   "event": "Vacated the flat and handed over the keys"
  },
  {
   "date": "2026-09-15",
   "event": "Landlord informed tenant that deductions will be made for painting and cleaning, amount not disclosed"
  },
  {
   "date": "unknown",
   "event": "Security deposit of ₹40,000 paid via UPI (receipt available)"
  }
 ],
 "evidence_have": [
  "rent agreement",
  "UPI transaction receipt for deposit",
  "keys handed over"
 ],
 "steps_taken": [],
 "red_flags": [],
 "user_goal": "Get the full security deposit of ₹40,000 returned",
 "open_questions": [
  "What year did you vacate the flat?",
  "Has the landlord provided any written notice or estimate of the deductions?",
  "Do you have any communication (messages/emails) with the landlord regarding the deposit?"
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

1. I entered into a rent agreement for a flat in Bangalore, Karnataka, as the tenant.  

2. I paid a security deposit of ₹40,000 by UPI (receipt available) on [FILL: date of deposit].  

3. I vacated the flat and handed over the keys to the landlord on 2026-09-15.  

4. On the same day, the landlord informed me that deductions would be made for painting and cleaning, but did not disclose any specific amount.  

5. I have not received the security deposit amount and am seeking its full return.

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
- **Other side:** Sir, flat ki painting aur deep cleaning ka kaafi kharcha hua hai, uska hisaab aapko dikhana padega. Thoda samay dijiye, main aapko details bhejta hoon.
- **User:** If you don't return it in 15 days I will send a legal notice and go to Lok Adalat.
- **Other side:** Sir, aapke notice aur Lok Adalat ki baat samajh aati hai, lekin pehle painting‑cleaning ka exact bill aur koi damage ka proof dekhna zaroori hai; tabhi hum final settlement kar sakte hain. कृपया ये दस्तावेज़ भेज दें, fir hum aage discuss karenge.

### Coach feedback
**Do cheezein aapne achhi ki:**  
1. Aapne seedha deposit ki amount (₹40,000) aur vacate date mention ki – yeh clarity banata hai.  
2. Aapne “legal notice” aur “Lok Adalat” ka zikr kiya, jo landlord ko serious sochne par majboor karta hai (see [K:lok-adalat]).

**Do cheezein improve kar sakte ho (better lines):**  
- *Original:* “If you don't return it in 15 days I will send a legal notice and go to Lok Adalat.”  
  *Better:* “Mujhe ₹40,000 ka full deposit 15 din (30 Sept tak) mein bank transfer se wapas chahiye, warna main Speed Post/Registered Post se legal notice bhejunga aur Lok Adalat me settlement ki request karunga.” [K:notice-how-to-send]  

- *Original:* “Sir, flat ki painting aur deep cleaning ka kaafi kharcha hua hai, uska hisaab aapko dikhana padega.”  
  *Better:* “Kripya painting‑cleaning ka itemised bill aur koi damage ka photo ya invoice bhejein, taki main deductions ko verify kar sakun.” [K:deposit-deductions]

**Strong closing line (amount, deadline, next step):**  
“Please ₹40,000 ka deposit 30 September tak bank transfer ya cash se wapas karein; agar is date tak nahi milta, to main 31 September ko registered notice bhej kar Lok Adalat me case file kar dunga.” [K:deposit-contract] [K:lok-adalat]

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