# wage-hindi-resigned - Salary unpaid after resignation, Hindi

## Turn 1 - user
> मैंने 31 अक्टूबर 2026 को नौकरी से इस्तीफा दिया। कंपनी ने सितंबर और अक्टूबर की सैलरी नहीं दी, कुल 60,000 रुपये। HR बोलता है फुल एंड फाइनल में 90 दिन लगेंगे। मेरे पास ऑफर लेटर और सैलरी स्लिप हैं। मैं जयपुर में काम करता था।

## Turn 1 - Nyaya Saathi (unedited)
**मैंने जो समझा**
आपने 31 अक्टूबर 2026 को इस्तीफा दिया, लेकिन कंपनी ने सितंबर और अक्टूबर के 60,000 रुपये रोक लिए हैं। HR का कहना है कि फुल एंड फाइनल (Full and Final) में 90 दिन लगेंगे।

**आपकी स्थिति**
नियम के अनुसार (जो आमतौर पर लागू होते हैं), नौकरी छोड़ने पर बकाया मजदूरी दो काम के दिनों (working days) के भीतर मिल जानी चाहिए [K:cw-timely-payment]। आपके मामले में यह समय 3 नवंबर 2026 को निकल चुका है [K:cw-timely-payment]। आप इसके लिए राज्य के श्रम विभाग (Labour Department) में तीन साल के भीतर दावा (claim) कर सकते हैं [K:cw-claims]। ध्यान दें कि मजदूरी कानूनों से जुड़े नियम और प्रक्रिया राज्य के हिसाब से अलग हो सकती है, इसलिए स्थानीय श्रम विभाग से पुष्टि करना सबसे सही रहेगा [K:cw-in-force]।

**आप आगे क्या कर सकते हैं**
1. HR या कंपनी को लिखित में (ईमेल या मैसेज द्वारा) तुरंत बकाया सैलरी की मांग भेजें और उसकी रसीद या कॉपी संभाल कर रखें [K:wages-relieving, K:notice-how-to-send]।
2. यदि कंपनी बात न सुने, तो आप राज्य के श्रम विभाग (Labour Department) के पास वेतन का दावा (claim) दर्ज करा सकते हैं [K:cw-claims]।
3. आप चाहें तो ज़िला विधिक सेवा प्राधिकरण (DLSA) से मुफ्त कानूनी सहायता या लोक अदालत (Lok Adalat) के माध्यम से बिना किसी फीस के समझौता कराने की कोशिश कर सकते हैं [K:legal-aid, K:lok-adalat]।

**मुझे आपसे अभी क्या चाहिए**
1. क्या आपके नियुक्ति पत्र (appointment letter) में फुल एंड फाइनल सेटलमेंट के लिए 90 दिन की बात लिखी है?
2. क्या आपने सैलरी मांगने के लिए HR को कोई ईमेल या लिखित संदेश भेजा है?

**असली वकील कब करें**
यदि कंपनी लिखित नोटिस या श्रम विभाग के बुलावे पर भी पैसे न दे, तब आप श्रम मामलों के किसी वकील [K:no-case-law] की मदद ले सकते हैं।

## Case file (intake)
```json
{
 "language": "hi",
 "language_name": "Hindi",
 "category": "wages",
 "sub_type": "final settlement withheld",
 "summary": "The user resigned from their job on October 31, 2026, but the company has not paid their salary for September and October, totaling 60,000 rupees. The HR claims that the full and final settlement will take 90 days. The user has an offer letter and salary slips, and they worked in Jaipur.",
 "user_role": "employee",
 "other_party": {
  "name": null,
  "type": "company"
 },
 "state": "Rajasthan",
 "city": "Jaipur",
 "amounts": {
  "disputed": 60000,
  "paid_value": null,
  "monthly_rent": null,
  "monthly_salary": null
 },
 "dates": {
  "incident": "2026-10-31",
  "purchase": null,
  "complaint_to_company": null,
  "moved_out": null,
  "last_working_day": "2026-10-31",
  "wages_due_from": "2026-09-01",
  "notice_received": null,
  "notice_deadline": null,
  "bank_return_memo": null
 },
 "employment_ended": true,
 "timeline": [
  {
   "date": "2026-10-31",
   "event": "Resigned from the job"
  }
 ],
 "evidence_have": [
  "Offer letter",
  "Salary slips"
 ],
 "steps_taken": [
  "Spoken to HR regarding the pending salary"
 ],
 "red_flags": [],
 "user_goal": "Get the unpaid salary for September and October without waiting for 90 days",
 "open_questions": [
  "Does your appointment letter or employment contract mention any specific timeline like 90 days for full and final settlement?",
  "Have you sent a written email or message to HR demanding your pending salary?"
 ]
}
```

## Computed by code
```json
{
 "deadlines": [
  {
   "label": "Final wages were due (2 working days after leaving)",
   "date": "2026-11-03",
   "days_left": -18,
   "status": "passed",
   "kb": "cw-timely-payment",
   "kind": "statutory_due",
   "basis": "2 working days after 2026-10-31"
  },
  {
   "label": "Last date to file a wage claim (generally 3 years)",
   "date": "2029-11-03",
   "days_left": 1078,
   "status": "ok",
   "kb": "cw-claims",
   "kind": "limitation",
   "basis": "3 years from 2026-11-03"
  }
 ],
 "forum": null,
 "fee": null,
 "escalations": []
}
```

## Guard: first pass 0 violation(s), repaired=False, scrubbed=False, final=0

## Draft: Complaint to Labour Department
**To,**
The Labour Commissioner / Inspector-cum-Facilitator,
[FILL: district and state] Labour Department

**Subject: Complaint for non-payment of wages of Rs 60,000 by [FILL: name of the company]**

Respected Sir/Madam,

1. I was employed and worked for the company located in Jaipur, Rajasthan.
2. I formally resigned from my job, and my last working day was October 31, 2026.
3. The company has withheld and failed to pay my salary for the months of September and October 2026, amounting to a total of 60,000 rupees.
4. When I followed up regarding my pending dues, the human resources department claimed that the full and final settlement would take 90 days.
5. In support of my employment and earnings, I possess my offer letter and salary slips, and I have previously spoken to HR regarding the pending salary.

Wages due to an employee who has resigned or been removed are payable within two working days, and monthly wages before the seventh day of the following month, under the Code on Wages, 2019. These deadlines have long passed.

I request you to direct the employer to pay my pending wages of Rs 60,000 along with compensation as per law, and to
take any other action you consider appropriate. Copies of my documents are attached.

**Documents attached:**
1. Offer letter
2. Salary slips

Yours faithfully,
[FILL: your full name]
[FILL: address, phone]
Date: 21 November 2026

## Automatic checks
- PASS category
- PASS language
- PASS deadline_computed
- PASS deadline_date
- PASS mentions:2
- PASS mentions:श्रम
- PASS guard_clean
- PASS draft_no_legal_refs_in_facts