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
 "sender": "Advocate A. Sharma on behalf of Mr. Suresh Gupta",
 "recipient": "Mr. Ramesh Kumar",
 "date_of_notice": "2026-11-10",
 "what_they_claim": "Mr. Ramesh Kumar issued a cheque for Rs. 1,50,000 for a friendly loan, which was returned unpaid due to insufficient funds.",
 "what_they_demand": "Pay the amount of Rs. 1,50,000 within 15 days of receipt of the notice.",
 "amount_demanded": 150000,
 "deadline_text": "within 15 days of receipt of this notice",
 "deadline_days": 15,
 "consequences_threatened": [
  "file a criminal complaint under Section 138 read with Section 142 of the Negotiable Instruments Act, 1881 against you, at your risk as to costs and consequences"
 ],
 "laws_mentioned": [
  "Section 138 of the Negotiable Instruments Act, 1881",
  "Section 138",
  "Section 142 of the Negotiable Instruments Act, 1881"
 ],
 "court_or_case_number": null,
 "hearing_date": null
}
```

## Reply (unedited)
**What this is**
Yeh ek legal notice hai jo Advocate A. Sharma ne Mr. Suresh Gupta ki taraf se bheja hai [K:notice-legal-what]. Yeh koi court order nahi hai, balki ek formal letter hai [K:notice-legal-what]. Isme kaha gaya hai ki Mr. Ramesh Kumar dwara diya gaya Rs. 1,50,000 ka cheque insufficient funds ki wajah se bounce ho gaya.

**What they want**
Unki demand hai ki aap cheque ka amount (Rs. 1,50,000) notice milne ke 15 din ke andar pay karein [K:nia-138]. Iski computed deadline **30 November 2026** hai.

**How serious is it**
Yeh ek serious matter hai [K:nia-138]. Notice mein mention kiya gaya hai ki agar aapne payment nahi kiya, toh woh Negotiable Instruments Act ke tahat criminal complaint file kar sakte hain [K:nia-138]. Lekin calm rahein—agar aap time par pay kar dete hain, toh mamla aam taur par khatam ho jata hai [K:nia-138].

**What to do now**
1. Check karein ki demand sahi hai ya nahi, aur panic na karein.
2. Agar aapko lagta hai ki payment karni chahiye, toh 30 November 2026 tak payment karne par vichar karein taaki matter settle ho sake [K:nia-138][K:nia-compound].
3. Aap chahein toh apna paksh rakhne ke liye ek short aur factual reply bhej sakte hain [K:notice-legal-what].

**Get a lawyer if**
Aapko ek lawyer se turant consult karna chahiye kyunki cheque-bounce notice ek criminal matter hota hai aur iska 15 din ka strict window hota hai [K:nia-138]. Agar aapki income kam hai ya aap eligible category mein aate hain (jaise women ya SC/ST), toh aap District Legal Services Authority (DLSA) se free legal aid bhi le sakte hain [K:legal-aid]. Helpline number 15100 par call kar sakte hain [K:legal-aid].

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