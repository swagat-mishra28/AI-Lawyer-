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
 "sender": "The Court of the Civil Judge (Junior Division), Lucknow",
 "recipient": "Shri Anil Verma",
 "date_of_notice": null,
 "what_they_claim": "The plaintiff has instituted a suit against you for the recovery of Rs. 3,40,000.",
 "what_they_demand": "Appear in this Court in person or by a pleader to answer the claim and file your written statement.",
 "amount_demanded": 340000,
 "deadline_text": "05.12.2026 at 10:30 AM",
 "deadline_days": null,
 "consequences_threatened": [
  "The suit will be heard and determined in your absence."
 ],
 "laws_mentioned": [],
 "court_or_case_number": "Civil Suit No. 1123 of 2026",
 "hearing_date": "2026-12-05"
}
```

## Reply (unedited)
नमस्ते! मैं 'न्याय साथी' हूँ। आपके लिए इस अदालती समंस की सरल जानकारी नीचे दी गई है:

**यह क्या है**
यह लखनऊ के सिविल जज (जूनियर डिवीज़न) की अदालत से भेजा गया एक औपचारिक अदालती समंस (Court Summons) है, कोई आम पत्र नहीं [K:court-summons]। 

**वे क्या चाहते हैं**
आप पर 3,40,000 रुपये की वसूली का मुकदमा दर्ज किया गया है। मांग है कि आप 05.12.2026 को सुबह 10:30 बजे अदालत में खुद या अपने वकील के जरिए पेश होकर अपना जवाब दें [K:court-summons]।

**यह कितना गंभीर है**
यह बहुत गंभीर है क्योंकि यह अदालत का आदेश है। इसे कभी भी नजरअंदाज न करें। यदि आप पेश नहीं होते हैं, तो अदालत आपकी अनुपस्थिति में आपके खिलाफ एकतरफा फैसला सुना सकती है [K:court-summons]। घबराएं नहीं, समय रहते सही कदम उठाएं।

**अब आपको क्या करना चाहिए**
1. निर्धारित तारीख (05.12.2026) से पहले अदालती कार्यवाही के लिए तैयारी करें [K:court-summons]।
2. तुरंत किसी वकील से संपर्क करें [K:court-summons]।
3. यदि आप वकील का खर्च उठाने में असमर्थ हैं, तो मुफ्त कानूनी सहायता (Free Legal Aid) के लिए NALSA हेल्पलाइन नंबर **15100** पर कॉल करें या अपने जिले के जिला कानूनी सेवा प्राधिकरण (DLSA) से मिलें [K:legal-aid]।

**वकील कब लें**
चूंकि यह अदालत का समंस है, आपको तारीख से पहले ही किसी वकील या मुफ्त कानूनी सहायता से तुरंत सलाह लेनी चाहिए [K:court-summons], [K:legal-aid]।

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