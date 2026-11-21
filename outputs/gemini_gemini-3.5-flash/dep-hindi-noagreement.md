# dep-hindi-noagreement - Deposit, Hindi (Devanagari), no written agreement

## Turn 1 - user
> मैं दिल्ली में किराए पर रहता था। मकान मालिक को 2 महीने का किराया 30,000 रुपये डिपॉज़िट दिया था, UPI से। कोई लिखित एग्रीमेंट नहीं बना। 1 अक्टूबर 2026 को कमरा खाली किया, अब वो पैसे नहीं दे रहे और कहते हैं कोई सबूत नहीं है।

## Turn 1 - Nyaya Saathi (unedited)
मैं वकील नहीं हूँ, लेकिन मैं आपको समझा सकता हूँ कि कानून के अनुसार आपकी स्थिति क्या है और आप क्या कर सकते हैं।

**मैं क्या समझा**
आप दिल्ली में किराए पर रहते थे और 1 अक्टूबर 2026 को आपने कमरा खाली कर दिया। आपने 30,000 रुपये का डिपॉज़िट UPI से दिया था, लेकिन कोई लिखित एग्रीमेंट (written agreement) नहीं बना था और मकान मालिक अब पैसे देने से मना कर रहा है।

**आपकी कानूनी स्थिति**
* लिखित एग्रीमेंट न होने पर भी, बैंक ट्रांसफर या UPI पेमेंट का सबूत और लेन-देन के मैसेज अदालत में मजबूत सबूत माने जाते हैं [K:deposit-no-agreement]।
* डिपॉज़िट वापस न मिलना दीवानी (civil) मामला होता है; पुलिस सामान्यतः पैसे वापस नहीं कराती [K:deposit-not-police]। यह सामान्यतः उपभोक्ता आयोग (Consumer Commission) का मामला भी नहीं होता [K:deposit-not-consumer]।
* सामान्य तौर पर, पैसे की वसूली के लिए केस दर्ज करने की समय-सीमा रकम देय होने (कमरा खाली करने) से 3 साल होती है [K:deposit-limitation]।

**अब आप क्या कर सकते हैं**
1. **सबूत जमा करें:** UPI पेमेंट की रसीद/स्टेटमेंट और कमरा खाली करने व डिपॉज़िट मांगने वाले मैसेज संभाल कर रखें [K:deposit-no-agreement]।
2. **लिखित संदेश भेजें:** मकान मालिक को मैसेज या ईमेल भेजकर पैसे वापस मांगे।
3. **लीगल नोटिस (Legal Notice) भेजें:** यदि वह न माने, तो स्पीड पोस्ट (Speed Post) या रजिस्टर्ड पोस्ट से लीगल नोटिस भेजें और उसकी रसीद संभाल कर रखें [K:notice-how-to-send]।
4. **लोक अदालत (Lok Adalat):** बिना किसी फीस के समझौते के लिए आप जिला कानूनी सेवा प्राधिकरण (DLSA) के जरिए लोक अदालत का सहारा ले सकते हैं [K:lok-adalat]।
5. **दीवानी मुकदमा (Civil Suit):** यदि बात न बने, तो आप स्थानीय दीवानी अदालत (civil court) में रिकवरी का केस दर्ज कर सकते हैं [K:deposit-civil-suit]। मुफ़्त कानूनी सहायता के लिए NALSA हेल्पलाइन 15100 पर संपर्क करें [K:legal-aid]।

**मुझे आपसे क्या जानकारी चाहिए**
1. क्या आपके पास मकान मालिक के साथ किराए या डिपॉज़िट के संबंध में हुई चैट या मैसेज मौजूद हैं?
2. क्या आपके पास मकान मालिक का पूरा नाम और उनका सही पता उपलब्ध है?

**असली वकील की सलाह कब लें**
यदि लीगल नोटिस भेजने और बात करने के बाद भी मकान मालिक पैसे लौटाने से मना करे, तो अदालत में केस दर्ज करने के लिए किसी वकील से संपर्क करें।

## Case file (intake)
```json
{
 "language": "hi",
 "language_name": "Hindi",
 "category": "deposit",
 "sub_type": "security deposit return",
 "summary": "The user lived in rented accommodation in Delhi and paid a security deposit of Rs 30,000 via UPI without a written agreement. He vacated the room on October 1, 2026, but the landlord is refusing to return the deposit claiming there is no proof.",
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
  "monthly_rent": 15000,
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
   "event": "Vacated the rented room; landlord refused to return the security deposit"
  }
 ],
 "evidence_have": [
  "UPI payment transaction record"
 ],
 "steps_taken": [
  "Requested refund from landlord directly"
 ],
 "red_flags": [],
 "user_goal": "Get the Rs 30,000 security deposit refunded from the landlord.",
 "open_questions": [
  "Do you have WhatsApp chats or messages discussing the rent and deposit with the landlord?",
  "What reason is the landlord giving for withholding the deposit besides the lack of an agreement?",
  "Do you know the landlord's full name and address?"
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