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
Yeh ek legal notice hai jo Advocate A. Sharma ne Mr. Suresh Gupta ki taraf se bheja hai [K:notice-legal-what]. Yeh ek formal letter hai, koi court ka order nahi hai [K:notice-legal-what].

**What they want**
Inka kehna hai ki aapne Rs. 1,50,000 ka cheque diya tha jo insufficient funds ki wajah se bounce ho gaya. Woh chahte hain ki aap notice milne ke 15 din ke andar, yaani **30 November 2026** tak, yeh poora amount pay kar dein [K:nia-138].

**How serious is it**
Yeh bohot serious maamla hai [K:nia-138]. Notice mein Negotiable Instruments Act ke Section 138 aur 142 ka zikr hai [K:nia-138]. Agar aap 15 din mein payment nahi karte, toh woh aapke khilaf criminal complaint file kar sakte hain, jismein jail ya fine ya dono ho sakte hain [K:nia-138].

**What to do now**
1. Is notice ko bilkul ignore mat kariye aur calm rahiye [K:nia-138].
2. Agar aapko lagta hai ki payment banti hai, toh deadline (30 November 2026) se pehle pay kar dein kyunki is waqt pay karne se matter aasaani se khatam ho jata hai [K:nia-138].
3. Agar aapko free salah chahiye, toh aap District Legal Services Authority (DLSA) ya NALSA helpline **15100** par call kar sakte hain [K:legal-aid].

**Get a lawyer if**
Aapko samajh nahi aa raha ki aage kya step lein, ya aapko lag raha hai ki maamla galat hai aur aapko dispute karna hai, toh turant ek lawyer se salah lein [K:nia-138].

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