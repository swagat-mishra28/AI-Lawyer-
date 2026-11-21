# dep-hinglish - Deposit, Hinglish, painting excuse

## Turn 1 - user
> Bhai mera landlord 40000 ka security deposit wapas nahi de raha. Maine 15 sept ko flat khali kiya tha Bangalore mein, chaabi bhi de di thi. Ab bolta hai painting aur cleaning ka paisa katega, kitna katega bata bhi nahi raha. Rent agreement hai 11 mahine ka aur deposit UPI se diya tha.

## Turn 1 - Nyaya Saathi (unedited)
**What I understood**
Aapne Bangalore mein 15 September 2026 ko flat khali karke chaabi de di thi, aur landlord aapka 40,000 INR security deposit bina kisi proper bill ke painting aur cleaning ke naam par rok raha hai.

**Where you stand**
Aapke paas rent agreement aur UPI payment ka proof hai, jo ki bohot achha saboot hai [K:deposit-no-agreement]. Rent agreement ke mutabiq deposit refund hona chahiye, aur landlord bina kisi sahi bill ya reason ke paise nahi kaat sakta (yeh jankari aam taur par sahi maani jati hai) [K:deposit-contract, K:deposit-deductions]. Non-return of deposit ek civil (paison ka) dispute hai, iske liye police case karna sahi nahi hota [K:deposit-not-police]. Paisa wapas mangne ki aam taur par limit 3 saal hoti hai, aur aapke paas 2029-09-15 tak ka samay hai [K:deposit-limitation].

**What you can do now**
1. Landlord ko WhatsApp ya email par likh kar painting aur cleaning ke kharche ka bill aur itemised list mango [K:deposit-deductions]. Sabhi messages aur receipts sambhal kar rakhein [K:notice-how-to-send].
2. Ek formal legal notice bhejo jisme deposit jaldi wapas dene ki maang ho. Notice Speed Post ya Registered Post se bhejein aur receipt apne paas rakhein [K:notice-how-to-send].
3. Agar landlord nahi maanta, toh District Legal Services Authority (DLSA) mein muft (free) pre-litigation settlement ke liye Lok Adalat mein baat karein [K:lok-adalat]. Aap NALSA helpline 15100 par bhi call kar sakte hain [K:legal-aid].
4. Akhir mein, local civil court mein recovery suit file kiya ja sakta hai [K:deposit-civil-suit].

**What I still need from you**
1. Kya aapne jaane ke baad flat ki condition ke photos ya videos liye the?
2. Kya aapne landlord ko deposit ke liye koi written message ya notice bheja hai abhi tak?

**When to get a real lawyer**
Agar landlord legal notice ke baad bhi paise na de aur aapko civil court mein case file karna pade, toh ek wakil (lawyer) ya DLSA ki madad lein [K:deposit-civil-suit].

## Case file (intake)
```json
{
 "language": "hinglish",
 "language_name": "Hinglish",
 "category": "deposit",
 "sub_type": "security deposit withheld",
 "summary": "The user vacates a flat in Bangalore and returns the keys on 2026-09-15. The landlord is refusing to return the 40,000 INR security deposit, citing arbitrary painting and cleaning deductions without specifying an amount.",
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
   "event": "Vacated the flat and handed over the keys to the landlord."
  }
 ],
 "evidence_have": [
  "Rent agreement for 11 months",
  "UPI payment proof for the security deposit"
 ],
 "steps_taken": [],
 "red_flags": [],
 "user_goal": "Get back the 40,000 INR security deposit from the landlord",
 "open_questions": [
  "Have you sent any formal written notice or message demanding the deposit return?",
  "Did you take photos or videos of the flat's condition when you moved out?"
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

## Guard: first pass 1 violation(s), repaired=True, scrubbed=False, final=0
- bad_tag: `[K:ladder]` - no such knowledge entry

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

1. I was residing in the flat located in Bangalore, Karnataka, pursuant to a rent agreement for 11 months.

2. At the commencement of the tenancy, I paid a security deposit of 40,000 INR, the payment of which is supported by UPI payment proof.

3. I vacated the flat and formally handed over the keys to you on September 15, 2026.

4. Upon vacating, you have refused to return the security deposit of 40,000 INR, citing arbitrary painting and cleaning deductions without specifying any exact amount.

5. Despite my handing over the possession of the premises in proper condition, the aforesaid security deposit remains wrongfully withheld by you.

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
- **Other side:** Arrey, itni jaldi kya hai deposit ki? Flat ka halat dekho, pura paint aur deep cleaning karwana padega, uska kharcha toh katega hi na!
- **User:** If you don't return it in 15 days I will send a legal notice and go to Lok Adalat.
- **Other side:** Acha-acha, direct legal notice ki baat mat karo yaar, aapas mein hi sort out karte hain

### Coach feedback
Bhai, tumne negotiation mein yeh do cheezein achhi ki:
1. Amount (40,000) aur flat chhodne ki exact date clearly mention ki.
2. Lok Adalat aur legal action ki baat karke landlord ko serious kar diya [K:lok-adalat].

Yeh do cheezein improve karo:
1. Landlord ke vague "painting/cleaning" ke excuse par bill mango [K:deposit-deductions]. Aisa bolo: *"Aap mujhe painting aur cleaning ka itemised bill aur photos dijiye, kyunki rent agreement ke mutabiq normal wear and tear ke paise nahi kat sakte [K:deposit-contract]."*
2. Dhamki dene ki jagah unke vague claim ko proof par challenge karo. Aisa bolo: *"Agar aapke paas valid bills nahi hain, toh main yeh deduction nahi maan sakta."*

Strong closing line:
*"Sir, mujhe mera poora 40,000 Rs ka deposit agle 3 din yani Friday tak mere bank account mein chahiye, warna main DLSA jaakar Lok Adalat mein formal pre-litigation case file karunga [K:lok-adalat]."*

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