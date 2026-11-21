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
 "what_they_claim": "The plaintiff has instituted a suit against you for the recovery of Rs. 3,40,000.",
 "what_they_demand": "Appear in this Court in person or by a pleader duly instructed to answer the claim, and to file your written statement.",
 "amount_demanded": 340000,
 "deadline_text": "05.12.2026 at 10:30 AM",
 "deadline_days": null,
 "consequences_threatened": [
  "The suit will be heard and determined in your absence in default of your appearance."
 ],
 "laws_mentioned": [],
 "court_or_case_number": "Civil Suit No. 1123 of 2026",
 "hearing_date": "2026-12-05"
}
```

## Reply (unedited)
नमस्ते, मैं न्याय साथी हूँ। आपके द्वारा भेजे गए दस्तावेज़ को सरल भाषा में नीचे समझाया गया है:

**What this is (यह क्या है):**
यह लखनऊ के सिविल जज (जूनियर डिवीजन) की अदालत से भेजा गया एक आधिकारिक **कोर्ट समंस** है (कोई साधारण पत्र नहीं)। 

**What they want (वे क्या चाहते हैं):**
वादी (Plaintiff) ने आपके खिलाफ ₹3,40,000 की वसूली के लिए मामला दर्ज किया है। समंस की मांग है कि आप या आपका वकील अदालत में पेश हों, अपना लिखित जवाब (Written Statement) दाखिल करें और दावों का उत्तर दें [K:court-summons]। 
* **अंतिम तिथि (Deadline):** 05.12.2026 को सुबह 10:30 बजे।

**How serious is it (यह कितना गंभीर है):**
यह बहुत गंभीर मामला है क्योंकि यह सीधे अदालत से जुड़ा है। यदि आप इस समंस को नजरअंदाज करते हैं, तो अदालत आपकी अनुपस्थिति में ही मामले की सुनवाई करके फैसला सुना सकती है [K:court-summons]। इसे हल्के में न लें।

**What to do now (अब आपको क्या करना चाहिए):**
1. तारीख को बिल्कुल न भूलें—05.12.2026 से पहले अदालत में पेश होने की तैयारी करें [K:court-summons]।
2. तुरंत किसी वकील से संपर्क करें [K:court-summons]।
3. यदि आपको मुफ्त कानूनी सहायता चाहिए, तो आप राष्ट्रीय विधिक सेवा प्राधिकरण (NALSA) के हेल्पलाइन नंबर **15100** पर कॉल कर सकते हैं [K:legal-aid]।

**Get a lawyer if (वकील कब करें):**
चूंकि यह एक आधिकारिक **कोर्ट समंस** है, इसलिए आपको तुरंत एक वकील या मुफ्त कानूनी सेवा (Legal Aid) की मदद लेनी चाहिए [K:court-summons]।

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