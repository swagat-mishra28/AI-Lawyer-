# notice-court-summons - Court summons (must say lawyer now)

## Input notice
```
IN THE COURT OF THE CIVIL JUDGE (JUNIOR DIVISION), LUCKNOW
Civil Suit No. 1123 of 2026
SUMMONS TO DEFENDANT
To: Shri Anil Verma, 22 Gomti Nagar, Lucknow
Whereas the plaintiff has instituted a suit against you for recovery of Rs. 3,40,000, you are hereby summoned to
appear in this Court in person or by a pleader duly instructed on 05.12.2026 at 10:30 AM to answer the claim,
and to file your written statement. Take notice that in default of your appearance the suit will be heard and
determined in your absence.
By order of the Court, Seal
```

## Extracted
```json
{
 "doc_type": "court_summons",
 "sender": "Court of the Civil Judge (Junior Division), Lucknow",
 "recipient": "Shri Anil Verma",
 "date_of_notice": null,
 "what_they_claim": "The plaintiff is seeking recovery of Rs. 3,40,000.",
 "what_they_demand": "Appear in court in person or by a pleader on 05.12.2026 at 10:30 AM and file a written statement.",
 "amount_demanded": 340000,
 "deadline_text": "05.12.2026 at 10:30 AM",
 "deadline_days": null,
 "consequences_threatened": [
  "the suit will be heard and determined in your absence"
 ],
 "laws_mentioned": [],
 "court_or_case_number": "Civil Suit No. 1123 of 2026",
 "hearing_date": "2026-12-05"
}
```

## Reply (unedited)
**क्या है यह?**  
यह एक **कोर्ट समन्स** (court summons) है, जो “Court of the Civil Judge (Junior Division), Lucknow” ने आपको भेजा है। यह अदालत का आधिकारिक दस्तावेज़ है, न कि केवल वकील का पत्र। [​K:court-summons]  

**वे क्या चाहते हैं?**  
- वादी ₹3,40,000 की वसूली का दावा कर रहा है।  
- आपको 05‑12‑2026 को सुबह 10:30 बजे कोर्ट में व्यक्तिगत रूप से या अपने वकील (pleader) के माध्यम से उपस्थित होना है और लिखित उत्तर (written statement) दाखिल करना है।  
- आज (21‑11‑2026) से इस तारीख़ तक **14 दिन** बचे हैं, इसलिए यह **तत्काल** (urgent) है। [​K:notice-legal-what]  

**यह कितना गंभीर है?**  
कोर्ट समन्स को अनदेखा करने पर अदालत आपकी अनुपस्थिति में ही मामला सुन‑सुन कर फैसला कर सकती है, और आपके खिलाफ अनुकूल निर्णय निकल सकता है। [​K:court-summons] इसलिए इसे हल्के में न लें, पर शांति से तैयार रहें।  

**अब क्या करें?** (क्रमांकित कदम)  
1. समन्स की एक प्रति सुरक्षित रखें; मूल दस्तावेज़ को नुकसान‑रहित जगह पर रखें।  
2. तुरंत एक वकील से संपर्क करें या 15100 पर फ्री लीगल एड के लिए कॉल करें। [​K:legal-aid]  
3. वकील को सभी दस्तावेज़ (समन्स, कोई भी पत्र‑व्यवहार) दिखाएँ।  
4. वकील के निर्देशानुसार लिखित उत्तर तैयार कर, निर्धारित तारीख़ से पहले (आदर्शतः 02‑12‑2026 तक) कोर्ट में दाखिल कराएँ।  
5. यदि आप स्वयं उत्तर भेजना चाहते हैं, तो रजिस्टर्ड पोस्ट/स्पीड पोस्ट के साथ रसीद रखें; ई‑मेल या व्हाट्सएप पर भी कॉपी भेजें। [​K:notice-how-to-send]  

**कब वकील लें?**  
- जब आपको कोर्ट की तारीख़ (05‑12‑2026) के भीतर उत्तर दाखिल करना हो।  
- यदि आप उत्तर की सामग्री या प्रक्रिया को लेकर अनिश्चित हैं।  
- यदि आपकी आय सीमा या सामाजिक वर्ग के कारण आप फ्री लीगल एड के पात्र हैं। [​K:legal-aid]  

समय पर कार्रवाई करके आप अपने अधिकारों की रक्षा कर सकते हैं। शुभकामनाएँ!

## Computed by code
```json
{
 "deadlines": [
  {
   "label": "Deadline stated in the notice",
   "date": "2026-12-05",
   "days_left": 14,
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
   "flag": "court_summons",
   "level": "lawyer_now",
   "reason": "You have a court summons or a court date.",
   "action": "Do not miss the date. Contact a lawyer or DLSA legal aid (15100) now."
  },
  {
   "flag": "deadline_close",
   "level": "lawyer_now",
   "reason": "Deadline stated in the notice: 2026-12-05 (14 days left).",
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
- PASS guard_clean