# dep-hindi-noagreement - Deposit, Hindi (Devanagari), no written agreement

## Turn 1 - user
> मैं दिल्ली में किराए पर रहता था। मकान मालिक को 2 महीने का किराया 30,000 रुपये डिपॉज़िट दिया था, UPI से। कोई लिखित एग्रीमेंट नहीं बना। 1 अक्टूबर 2026 को कमरा खाली किया, अब वो पैसे नहीं दे रहे और कहते हैं कोई सबूत नहीं है।

## Turn 1 - Nyaya Saathi (unedited)
**मैं क्या समझा**  
आपने 30,000 ₹ सुरक्षा जमा UPI से दिया, कोई लिखित किराया‑एग्रीमेंट नहीं है, 1 अक्टूबर 2026 को कमरा खाली किया और अब मकान मालिक वह पैसा वापस नहीं कर रहा है।

**आपकी स्थिति**  
- जमा (deposit) एक किराया‑एग्रीमेंट (contract) का हिस्सा है, इसलिए मकान मालिक को वापस करना चाहिए, सिवाय उन कटौतियों के जो एग्रीमेंट में लिखी हों [K:deposit-contract]।  
- लिखित एग्रीमेंट न होने पर भी UPI रसीद और आपके और मकान मालिक के बीच के संदेश जमा के प्रमाण के रूप में काम करेंगे [K:deposit-no-agreement]।  
- यदि मकान मालिक कोई कटौती बताता है, तो उसे बिल या फोटो के साथ विस्तृत सूची देनी होगी [K:deposit-deductions] (आम तौर पर)।  
- यह मामला आमतौर पर सिविल (civil) विवाद है, पुलिस मदद नहीं करेगी [K:deposit-not-police]।  
- उपभोक्ता आयोग (Consumer Commission) में यह केस नहीं जाता, पहले नोटिस‑और‑समझौता, फिर लोक अदालत (Lok Adalat) या सिविल कोर्ट [K:deposit-not-consumer]।  
- 3 साल की सीमा (limitation) के भीतर आप मुकदमा दायर कर सकते हैं; आपका अंतिम दिन 1 अक्टूबर 2029 है [K:deposit-limitation]।  

**अब आप क्या कर सकते हैं**  

1. **लिखित माँग भेजें**  
   - WhatsApp/ई‑मेल में लिखें कि जमा वापस चाहिए, साथ में UPI रसीद संलग्न करें।  
   - “कृपया 15 दिन के भीतर जमा और कटौतियों की विस्तृत सूची भेजें” लिखें।  
   - इसे Speed Post/Registered Post से भी भेजें, रसीद रखें [K:notice-how-to-send]।  

2. **यदि जवाब नहीं मिले तो कानूनी नोटिस**  
   - वकील (या निःशुल्क कानूनी सहायता [K:legal-aid]) से 15 दिन की डेडलाइन वाला औपचारिक नोटिस तैयार करवा कर भेजें।  

3. **लोक अदालत (Lok Adalat) में निपटारा**  
   - जिला कानूनी सहायता कार्यालय (DLSA) से संपर्क करके प्री‑लिटिगेशन लोक अदालत में केस दाखिल करें – कोई फीस नहीं [K:lok-adalat]।  

4. **सिविल कोर्ट में पैसा वसूली का मुकदमा**  
   - यदि ऊपर के कदम काम न करें, तो स्थानीय सिविल कोर्ट में “money recovery suit” दायर करें [K:deposit-civil-suit]।  
   - लिखित एग्रीमेंट न होने पर “summary suit” प्रक्रिया तेज़ हो सकती है।  

5. **सभी दस्तावेज़ इकट्ठा रखें**  
   - UPI रसीद, मकान मालिक के साथ सभी संदेश, कमरे की खाली करने की फोटो/वीडियो, किराया‑रसीदें, हाथ‑हाथ नोट (यदि कोई) [K:deposit-no-agreement]।  

**मुझसे अभी कौन‑सी जानकारी चाहिए**  

1. मकान मालिक का पूरा नाम और संपर्क (फ़ोन/ई‑मेल) क्या है?  
2. क्या आपके पास मकान मालिक को भेजे‑भेजे संदेश (WhatsApp/ई‑मेल) हैं, जहाँ जमा की बात हुई?  
3. क्या आपके पास UPI ट्रांज़ैक्शन की स्क्रीनशॉट या बैंक स्टेटमेंट है?  

**कब वकील से मिलें**  
यदि नोटिस के बाद भी जवाब नहीं मिलता या आप लोक अदालत में समझौता नहीं कर पाते, तो तुरंत वकील से मिलें – आपके पास अभी 3 साल की सीमा बची है [K:deposit-limitation]।

## Case file (intake)
```json
{
 "language": "hi",
 "language_name": "Hindi",
 "category": "deposit",
 "sub_type": "security deposit withheld",
 "summary": "The user was a tenant in Delhi who paid a ₹30,000 security deposit via UPI without a written agreement. They vacated the premises on 2026-10-01, and the landlord is now refusing to return the deposit, claiming no proof exists.",
 "user_role": "tenant",
 "other_party": {
  "name": null,
  "type": "landlord"
 },
 "state": "Delhi",
 "city": "Delhi",
 "amounts": {
  "disputed": 30000,
  "paid_value": null,
  "monthly_rent": null,
  "monthly_salary": null
 },
 "dates": {
  "incident": "2026-10-01",
  "purchase": null,
  "complaint_to_company": null,
  "moved_out": "2026-10-01",
  "last_working_day": null,
  "wages_due_from": null,
  "notice_received": null,
  "notice_deadline": null,
  "bank_return_memo": null
 },
 "employment_ended": null,
 "timeline": [
  {
   "date": "2026-10-01",
   "event": "Vacated the rented room"
  }
 ],
 "evidence_have": [
  "UPI transaction receipt"
 ],
 "steps_taken": [],
 "red_flags": [],
 "user_goal": "To get the ₹30,000 security deposit back from the landlord",
 "open_questions": [
  "What is the landlord's name and contact details?",
  "Do you have any written communication (messages, emails) with the landlord regarding the deposit?",
  "Do you have a screenshot or statement showing the UPI payment of ₹30,000?"
 ]
}
```

## Computed by code
```json
{
 "deadlines": [
  {
   "label": "Last date to file a money-recovery suit (generally 3 years)",
   "date": "2029-10-01",
   "days_left": 1045,
   "status": "ok",
   "kb": "deposit-limitation",
   "kind": "limitation",
   "basis": "3 years from move-out 2026-10-01"
  }
 ],
 "forum": null,
 "fee": null,
 "escalations": []
}
```

## Guard: first pass 0 violation(s), repaired=False, scrubbed=False, final=0

## Automatic checks
- PASS category
- PASS language
- PASS deadline_computed
- PASS mentions:UPI
- PASS guard_clean