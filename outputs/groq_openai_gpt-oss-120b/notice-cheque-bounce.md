# notice-cheque-bounce - Received a cheque-bounce notice (notice explainer)

## Input notice
```
LEGAL NOTICE UNDER SECTION 138 OF THE NEGOTIABLE INSTRUMENTS ACT, 1881
Date: 10.11.2026
To, Mr. Ramesh Kumar, H.No. 45, Sector 12, Faridabad, Haryana
Under instructions from my client Mr. Suresh Gupta, I serve you this notice. You issued cheque no. 004512
dated 01.10.2026 for Rs. 1,50,000 drawn on State Bank of India towards repayment of a friendly loan. The said
cheque was presented and returned unpaid with the remark "Funds Insufficient" vide return memo dated 28.10.2026.
You are hereby called upon to pay the said amount of Rs. 1,50,000 within 15 days of receipt of this notice,
failing which my client shall be constrained to file a criminal complaint under Section 138 read with Section 142
of the Negotiable Instruments Act, 1881 against you, at your risk as to costs and consequences.
Sd/- Advocate A. Sharma, District Courts, Faridabad
```

## Extracted
```json
{
 "doc_type": "cheque_bounce_notice",
 "sender": "Advocate A. Sharma, District Courts, Faridabad (on behalf of Mr. Suresh Gupta)",
 "recipient": "Mr. Ramesh Kumar, H.No. 45, Sector 12, Faridabad, Haryana",
 "date_of_notice": "2026-11-10",
 "what_they_claim": "You issued a cheque of Rs. 1,50,000 dated 01.10.2026 which was returned unpaid due to insufficient funds.",
 "what_they_demand": "Pay Rs. 1,50,000 within 15 days of receipt of this notice.",
 "amount_demanded": 150000,
 "deadline_text": "within 15 days of receipt of this notice",
 "deadline_days": 15,
 "consequences_threatened": [
  "file a criminal complaint under Section 138 read with Section 142 of the Negotiable Instruments Act, 1881 against you, at your risk as to costs and consequences"
 ],
 "laws_mentioned": [
  "Section 138 of the Negotiable Instruments Act, 1881",
  "Section 142 of the Negotiable Instruments Act, 1881"
 ],
 "court_or_case_number": null,
 "hearing_date": null
}
```

## Reply (unedited)
**What this is**  
Yeh ek *legal notice* hai – ek formal patra jo Advocate A. Sharma (Faridabad District Court) ne Mr. Suresh Gupta ke behalf mein aapko bheja hai. Notice ek court order nahi hota, lekin isme aapke khilaf ek claim aur demand likhi hoti hai. [K:notice-legal-what]

**What they want**  
- Aapne 01‑Oct‑2026 ko Rs. 1,50,000 ka cheque diya tha jo “insufficient funds” ki wajah se bounce hua.  
- Notice ke mutabik aapko **Rs. 1,50,000** “within 15 days of receipt of this notice” pay karna hai.  
- Notice ki date 10‑Nov‑2026 hai, isliye **last date 30‑Nov‑2026** (abhi 9 din bache hain). [K:nia-138]

**How serious is it**  
Section 138 (Negotiable Instruments Act) ke tahat cheque bounce ek criminal offence hai – 2 saal tak ki jail, ya cheque amount ka double fine, ya dono. Agar aap 15 din ke andar payment kar dete hain, to case aksar khatam ho jata hai. Lekin deadline miss karne par complain file ho sakti hai. Isliye yeh “urgent” aur “serious” hai, lekin aapke paas abhi bhi time hai ki aap payment ya settlement kar lein. [K:nia-138]

**What to do now**  
1. **Receipt date confirm karein** – notice aapko kab mila (usually Speed/Registered Post).  
2. **Cheque aur bank statement check karein** – fund shortage ka reason samjhein.  
3. **Payment arrange karein** – cash, demand draft ya NEFT se Rs. 1,50,000 bhejein.  
4. **Payment ka proof (bank receipt) turant copy banayein** aur usko Advocate ko ya unke client ko email/WhatsApp se bhejein.  
5. **Notice ka ek copy, postal receipt, aur payment proof safe rakhein** – future reference ke liye. [K:notice-how-to-send]  
6. Agar aap settlement (compounding) chahein, to opposite party se baat karke amount clear kar sakte hain; Section 147 ke tahat yeh possible hai. [K:nia-compound]

**Get a lawyer if**  
- Aapko lagta hai cheque galat tarike se bounce hua (funds available the).  
- Aap itni badi rashi ek baar mein pay nahi kar sakte.  
- Aap settlement ya compromise terms negotiate karna chahte hain.  
- Aapko legal advice chahiye ki criminal complaint se kaise bach sakte hain.  

Agar aapki annual income ya category eligible hai, to NALSA helpline **15100** ya apne District Legal Services Authority se free legal aid le sakte hain. [K:legal-aid]

## Computed by code
```json
{
 "deadlines": [
  {
   "label": "Last day to pay the cheque amount (15 days from receiving notice)",
   "date": "2026-11-30",
   "days_left": 9,
   "status": "urgent",
   "kb": "nia-138",
   "kind": "response",
   "basis": "15 days from 2026-11-15"
  },
  {
   "label": "Deadline stated in the notice",
   "date": "2026-11-30",
   "days_left": 9,
   "status": "urgent",
   "kb": "notice-legal-what",
   "kind": "response",
   "basis": "as written in the notice"
  }
 ],
 "forum": null,
 "fee": null,
 "escalations": [
  {
   "flag": "cheque_bounce_against_user",
   "level": "lawyer_now",
   "reason": "A cheque-bounce notice against you is a criminal matter with a 15-day window.",
   "action": "Pay within 15 days of receiving the notice, or consult a lawyer immediately."
  },
  {
   "flag": "deadline_close",
   "level": "lawyer_now",
   "reason": "Last day to pay the cheque amount (15 days from receiving notice): 2026-11-30 (9 days left).",
   "action": "Act now; get a lawyer's advice before the date."
  },
  {
   "flag": "deadline_close",
   "level": "lawyer_now",
   "reason": "Deadline stated in the notice: 2026-11-30 (9 days left).",
   "action": "Act now; get a lawyer's advice before the date."
  }
 ]
}
```

## Guard: first pass 0 violation(s), repaired=False, scrubbed=False, final=0

## Automatic checks
- PASS escalates:lawyer_now
- PASS deadline_computed
- PASS deadline_date
- PASS mentions:15
- PASS mentions:1,50,000
- PASS guard_clean