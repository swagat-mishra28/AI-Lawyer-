# con-bengali-flight - Flight cancelled, refund pending, Bengali

## Turn 1 - user
> আমার ১০ অক্টোবর ২০২৬-এর ফ্লাইট এয়ারলাইন বাতিল করেছে। টিকিটের দাম ১২,৫০০ টাকা, এখনও রিফান্ড পাইনি। কাস্টমার কেয়ার শুধু অপেক্ষা করতে বলছে।

## Turn 1 - Nyaya Saathi (unedited)
আমি আইনজীবী নই, তবে আপনার পরিস্থিতি বুঝে আপনাকে সাহায্য করার চেষ্টা করছি।

**আমি যা বুঝেছি** - আপনার ১০ অক্টোবরের ফ্লাইট বাতিল হওয়ার পর ১২,৫০০ টাকার রিফান্ড পাননি।

**আপনি যেখানে আছেন** - আপনি একজন ভোক্তা [কনজ্যুমার] [K:cpa-consumer-definition]। ফ্লাইট বাতিল হওয়ার পরও রিফান্ড না দেওয়া সেবার ক্ষেত্রে ত্রুটি বা ঘাটতি [ডিফিসিয়েন্সি ইন সার্ভিস] হিসেবে গণ্য হয় [K:cpa-deficiency]। আপনার টাকার পরিমাণ ১২,৫০০ টাকা হওয়ায় আপনি জেলা ভোক্তা কমিশন [District Consumer Disputes Redressal Commission]-এর কাছে যেতে পারেন [K:cpa-pecuniary]। এই মামলার জন্য আপনার হাতে ২০২৮ সালের ১০ অক্টোবর পর্যন্ত সময় আছে [K:cpa-limitation]। এই ক্ষেত্রে সাধারণত কোনো ফি লাগে না, তবে পোর্টাল থেকে তা যাচাই করে নেওয়া ভালো [K:cpa-fee]।

**আপনি এখন যা করতে পারেন**
১. প্রথমে ন্যাশনাল কনজ্যুমার হেল্পলাইন [National Consumer Helpline]-এ বিনামূল্যে অভিযোগ জানান (কল করুন ১৯১৫ বা ১৮০০-১১-৪০-০০ নম্বরে, অথবা ভিজিট করুন consumerhelpline.gov.in) [K:nch]।
২. আপনি নিজেই কোনো আইনজীবী ছাড়া জেলা ভোক্তা কমিশনের [District Consumer Commission] ই-জাগৃতি [e-Jagriti] পোর্টালে অনলাইনে অভিযোগ দায়ের করতে পারেন [K:cpa-efiling]।

**আমার যা জানা প্রয়োজন**
১. এয়ারলাইন্সের নাম কী?
২. আপনার কাছে কি টিকিটের কপি বা বুকিং কনফার্মেশন ইমেল আছে?

**কখন আসল আইনজীবী ধরবেন** - যদি কোম্পানি কোনোভাবেই রিফান্ড না দেয় এবং আপনি নিজে অনলাইনে কমিশন [Consumer Commission]-এ অভিযোগ করতে সমস্যা বোধ করেন, তখন একজন আইনজীবীর সাহায্য নিতে পারেন।

## Case file (intake)
```json
{
 "language": "bn",
 "language_name": "Bengali",
 "category": "consumer",
 "sub_type": "flight ticket refund",
 "summary": "The user's flight on October 10, 2026, was cancelled by the airline, and they have not received a refund of 12,500 rupees despite contacting customer care.",
 "user_role": "buyer",
 "other_party": {
  "name": null,
  "type": "company"
 },
 "state": null,
 "city": null,
 "amounts": {
  "disputed": 12500,
  "paid_value": 12500,
  "monthly_rent": null,
  "monthly_salary": null
 },
 "dates": {
  "incident": "2026-10-10",
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
   "date": "2026-10-10",
   "event": "Flight cancelled by the airline"
  }
 ],
 "evidence_have": [],
 "steps_taken": [
  "Contacted customer care"
 ],
 "red_flags": [],
 "user_goal": "Get refund of 12,500 rupees for the cancelled flight",
 "open_questions": [
  "What is the name of the airline?",
  "Do you have the flight ticket or booking confirmation email?",
  "Have you received any written communication from the airline regarding the cancellation or refund?"
 ]
}
```

## Computed by code
```json
{
 "deadlines": [
  {
   "label": "Last date to file a consumer complaint (2 years)",
   "date": "2028-10-10",
   "days_left": 689,
   "status": "ok",
   "kb": "cpa-limitation",
   "kind": "limitation",
   "basis": "2 years from 2026-10-10"
  }
 ],
 "forum": {
  "forum": "District Consumer Disputes Redressal Commission",
  "basis_value": 12500.0,
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