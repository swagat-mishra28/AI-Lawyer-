# wage-construction-worker - Daily-wage construction worker, Hinglish, voice-like text

## Turn 1 - user
> sir main bihar se hu mumbai me construction site pe kaam karta tha thekedar ne 12 din ka paisa nahi diya 600 rupay roj ke hisab se. ab phone bhi nahi utha raha. koi kagaz nahi hai bas hajiri register me naam hai

## Turn 1 - Nyaya Saathi (unedited)
**What I understood**  
Aap Bihar se hain, Mumbai me construction site pe kaam karte the. Thekedar ne aapko 12 din ka ₹600 per day ka wage (₹7,200) nahi diya aur phone bhi nahi utha raha. Aapke paas sirf attendance register hai.

---

**Where you stand**  
- Daily wages ka payment Code on Wages, 2019 ke tahat aata hai. Ye law abhi lagu hai (generally) aur aapke employer ko har mahine ki wages agle mahine ke 7th din tak deni hoti hain. Agar aap resign ya dismiss ho gaye ho, to wages 2 working days ke andar deni hoti hain. [K:cw-timely-payment]  
- Sirf wahi deductions allowed hain jo law me likhe hain (tax, advance recovery, etc.). Agar aapke paise bina reason ke kat rahe hain, to aap challenge kar sakte hain. [K:cw-deductions]  
- Aapke paas attendance register ek strong evidence hai ki aap site pe kaam kar rahe the. [K:wages-relieving] (practical guidance)  
- Unpaid ya late wages ke liye aap labour department ke authority (State Labour Commissioner/Inspector‑cum‑Facilitator) ke paas claim file kar sakte hain, aur claim ko file karne ki limitation 3 saal hai. [K:cw-claims]  
- Agar aap eligible hain (income low, SC/ST, etc.) to NALSA se free legal aid mil sakti hai. [K:legal-aid]  
- Lok Adalat me aap bina fee ke settlement kar sakte hain; ye pre‑litigation stage me hi hota hai. [K:lok-adalat]  
- Notice bhejne ke liye Speed/Registered Post ka use karein, receipt aur tracking rakhein. [K:notice-how-to-send]

---

**What you can do now**  

1. **Written demand to the contractor** – HR ya thekedar ko ek simple letter likhe (Speed/Registered Post) jisme:  
   - Kaam ki dates, daily rate ₹600, total ₹7,200, aur “payment within 7 days” maange.  
   - Receipt/track copy sambhal ke rakhe. [K:notice-how-to-send]  

2. **Legal notice** – Agar 7 din me response nahi milta, to 15 din ka deadline ke saath ek legal notice bheje (aap khud likh sakte hain, ya free legal aid se madad le).  

3. **Labour department me claim file karein** – Nearest Maharashtra Labour Commissioner office ya Inspector‑cum‑Facilitator ke paas Section 45 ke tahat claim file karein. Form me attendance register ki copy lagaye. Fee aam tor pe nominal hoti hai (₹0‑₹200). [K:cw-claims]  

4. **Lok Adalat ka option** – Labour department ya District Legal Services Authority se pooche ki aapke case ko Lok Adalat me settle karne ka chance hai ya nahi. Ye free hai aur settlement court decree jaisa hota hai. [K:lok-adalat]  

5. **Free legal aid** – Agar aapki annual income limit ke andar hain, to NALSA 15100 par call karein ya apne district court ke DLSA office me jaake free lawyer le sakte hain. [K:legal-aid]  

6. **Future evidence** – Co‑workers se likhit statement (ya WhatsApp screenshot) lein ki aapne kaam kiya aur wage due tha.  

---

**What I still need from you**  

1. Un 12 din ki exact dates (kab se kab tak kaam kiya)?  
2. Koi likhit contract/appointment letter ya email hai?  
3. Koi gawah (co‑workers) jo aapki attendance aur unpaid wage confirm kar sakte hain?

---

**When to get a real lawyer**  
Agar contractor notice ke baad bhi nahi deta, ya labour department ka order aapke against aata hai, to turant free legal aid ya private lawyer se milkar civil suit (Indian Contract Act) ke liye aage badhein.

## Case file (intake)
```json
{
 "language": "hinglish",
 "language_name": "Hinglish",
 "category": "wages",
 "sub_type": "daily wages unpaid",
 "summary": "The user, a construction worker from Bihar working in Mumbai, says the contractor has not paid his wages for 12 days at Rs.600 per day and is not answering calls. He has only an attendance register as proof.",
 "user_role": "worker",
 "other_party": {
  "name": null,
  "type": "individual"
 },
 "state": "Maharashtra",
 "city": "Mumbai",
 "amounts": {
  "disputed": 7200,
  "paid_value": null,
  "monthly_rent": null,
  "monthly_salary": null
 },
 "dates": {
  "incident": null,
  "purchase": null,
  "complaint_to_company": null,
  "moved_out": null,
  "last_working_day": null,
  "wages_due_from": null,
  "notice_received": null,
  "notice_deadline": null,
  "bank_return_memo": null
 },
 "employment_ended": false,
 "timeline": [
  {
   "date": "approximate",
   "event": "Started working at construction site (date unknown)"
  },
  {
   "date": "approximate",
   "event": "Contractor failed to pay wages for 12 days (date unknown)"
  },
  {
   "date": "approximate",
   "event": "User tried calling contractor, no response (date unknown)"
  }
 ],
 "evidence_have": [
  "attendance register showing name"
 ],
 "steps_taken": [
  "tried calling contractor, no response"
 ],
 "red_flags": [],
 "user_goal": "to receive the unpaid wages of Rs.7200",
 "open_questions": [
  "What were the exact dates of the 12 days for which wages were not paid?",
  "Do you have any written agreement or contract with the contractor?",
  "Are there any witnesses (e.g., co‑workers) who can confirm your attendance and the unpaid wages?"
 ]
}
```

## Computed by code
```json
{
 "deadlines": [],
 "forum": null,
 "fee": null,
 "escalations": []
}
```

## Guard: first pass 0 violation(s), repaired=False, scrubbed=False, final=0

## Automatic checks
- PASS category
- PASS language
- PASS mentions:7,200
- PASS mentions:15100
- PASS guard_clean