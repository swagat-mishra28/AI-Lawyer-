# con-marathi-courier - Courier lost parcel, Marathi

## Turn 1 - user
> मी 3 ऑक्टोबर 2026 रोजी कुरिअरने 8,000 रुपयांचे पार्सल पाठवले, ते हरवले. कंपनी भरपाई द्यायला नकार देते. माझ्याकडे पावती आहे.

## Turn 1 - Nyaya Saathi (unedited)
**मी काय समजलो**
तुम्ही ३ ऑक्टोबर २०२६ रोजी ८,००० रुपयांचे पार्सल कुरिअरने पाठवले होते, पण ते हरवले. कुरिअर कंपनी आता भरपाई द्यायला नकार देत आहे आणि तुमच्याकडे कुरिअरची पावती आहे.

**तुम्ही कुठे आहात**
तुम्ही एक ग्राहक (Consumer) आहात कारण तुम्ही पैसे देऊन सेवा घेतली आहे [K:cpa-consumer-definition]. कुरिअर सेवा नीट न देणे ही सेवेतील त्रुटी (Deficiency in service) आहे [K:cpa-deficiency]. 
या समस्येसाठी तुम्ही जिल्हा ग्राहक विवाद निवारण आयोग (District Consumer Disputes Redressal Commission) मध्ये तक्रार दाखल करू शकता [K:cpa-where-to-file]. 
तक्रार दाखल करण्याची अंतिम मुदत २ वर्षे आहे (३ ऑक्टोबर २०२८ पर्यंत) [K:cpa-limitation]. भरपाईची रक्कम ८,००० रुपये असल्यामुळे, यासाठी साधारणपणे कोणतेही शुल्क (Fee) नाही, तरीही पोर्टलवर पडताळणी करा [K:cpa-fee].

**तुम्ही आता काय करू शकता**
१. राष्ट्रीय ग्राहक हेल्पलाइन (National Consumer Helpline) वर 1915 किंवा 1800-11-4000 वर कॉल करून किंवा consumerhelpline.gov.in वर मोफत तक्रार नोंदवा [K:nch].
२. कुरिअर कंपनीला लेखी तक्रार किंवा ई-मेल पाठवून भरपाईची मागणी करा.
३. तुम्ही जिल्हा ग्राहक आयोगाकडे (District Consumer Commission) स्वतः ऑनलाईन (e-Jagriti पोर्टलवर) तक्रार दाखल करू शकता, त्यासाठी वकिलाची सक्ती नाही [K:cpa-efiling].

**मला तुमच्याकडून अजून काय हवे आहे**
- कुरिअर कंपनीचे नाव काय आहे?
- तुम्ही कंपनीकडे कोणतीही लेखी तक्रार केली आहे का?

**खरं वकील कधी गाठावे**
जर कुरिअर कंपनीने समजूत काढण्यास स्पष्ट नकार दिला आणि तुम्हाला कायदेशीर कागदपत्रे समजून घेण्यात अडचण येत असेल, तर तुम्ही जिल्हा कायदेशीर सेवा प्राधिकरणाशी (DLSA) संपर्क साधून मोफत कायदेशीर मदत (Free legal aid) घेऊ शकता [K:legal-aid].

## Case file (intake)
```json
{
 "language": "mr",
 "language_name": "Marathi",
 "category": "consumer",
 "sub_type": "courier service loss",
 "summary": "The user sent a parcel worth 8,000 rupees via courier on October 3, 2026, which got lost. The courier company is refusing to pay compensation, and the user has the receipt.",
 "user_role": "buyer",
 "other_party": {
  "name": null,
  "type": "company"
 },
 "state": null,
 "city": null,
 "amounts": {
  "disputed": 8000,
  "paid_value": null,
  "monthly_rent": null,
  "monthly_salary": null
 },
 "dates": {
  "incident": "2026-10-03",
  "purchase": null,
  "complaint_to_company": null,
  "moved_out": null,
  "last_working_day": null,
  "wages_due_from": null,
  "notice_received": null,
  "notice_deadline": null,
  "bank_return_memo": null
 },
 "employment_ended": null,
 "timeline": [
  {
   "date": "2026-10-03",
   "event": "Sent parcel worth 8,000 rupees via courier, which got lost."
  }
 ],
 "evidence_have": [
  "Courier receipt"
 ],
 "steps_taken": [],
 "red_flags": [],
 "user_goal": "Get compensation of 8,000 rupees from the courier company for the lost parcel.",
 "open_questions": [
  "What is the name of the courier company?",
  "Have you filed a formal written complaint or legal notice to the courier company?"
 ]
}
```

## Computed by code
```json
{
 "deadlines": [
  {
   "label": "Last date to file a consumer complaint (2 years)",
   "date": "2028-10-03",
   "days_left": 682,
   "status": "ok",
   "kb": "cpa-limitation",
   "kind": "limitation",
   "basis": "2 years from 2026-10-03"
  }
 ],
 "forum": {
  "forum": "District Consumer Disputes Redressal Commission",
  "basis_value": 8000.0,
  "kb": "cpa-pecuniary"
 },
 "fee": {
  "fee_inr": 0,
  "kb": "cpa-fee",
  "note": "verify on the filing portal"
 },
 "escalations": []
}
```

## Guard: first pass 0 violation(s), repaired=False, scrubbed=False, final=0

## Automatic checks
- PASS category
- PASS language
- PASS deadline_computed
- PASS guard_clean