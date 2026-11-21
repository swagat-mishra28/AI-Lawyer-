# Demo script: Nyaya Saathi

This has three parts:

- **Part A:** the 3-minute recorded video. Every scene says what to open, what to click and what to say.
- **Part B:** the longer live demo for the interview (about 10 minutes), including which code files to open.
- **Part C:** questions they will likely ask, with answers. Also, what to do if something breaks.

Spoken lines are in quotes. Say them in your own words; don't read them word for word.

---

## Before you record (10 minutes of setup)

1. Open the live app: https://eqfddnzmoycgqfdlvgbxfc.streamlit.app/
   It sleeps when idle and takes about 30 seconds to wake, so open it a few minutes early.
2. Click **🗂️ Start a new case** in the sidebar so the screen is clean.
3. Leave **Reply language** on `auto`.
4. Open a second browser tab with the GitHub repo: https://github.com/swagat-mishra28/AI-Lawyer-
5. Zoom the browser to 110%, close other tabs, and turn off notifications.
6. Do one practice click on an example card and wait for the answer. This warms up the model and shows you how long it
   takes (usually 20-40 seconds). Then click **Start a new case** again.
7. Recorder: Loom, OBS or the Windows Game Bar (Win + Alt + R). Record the browser window plus your microphone.

**Tip on waiting:** while the AI is thinking, keep talking. Explain what is happening behind the scenes; the lines below
are written for exactly those gaps.

---

## Part A: the 3-minute video

### Scene 1 (0:00-0:20): what it is and why
**Screen:** the app's home page (Talk tab, green banner, sidebar visible).
**Do:** nothing yet; move the mouse over the banner and the sidebar topics.

> "Hi, I'm Swagat. For Kuku's AI Generalist assignment I picked Problem 2, the AI lawyer. This is Nyaya Saathi. It
> helps ordinary people in India with four everyday money problems: a deposit the landlord won't return, a refund
> that never came, unpaid salary, and a legal notice they don't understand. They can type or speak in their own
> language. The one rule I built it around: the AI explains, code decides, and no invented law ever reaches the user."

### Scene 2 (0:20-0:55): a real problem, in Hinglish
**Screen:** Talk tab.
**Do:** click the card **🏠 Deposit not returned**. While it thinks, keep talking.

> "Here's a typical message, in Hinglish: the landlord kept a 40,000 rupee deposit and stopped answering the phone.
> Behind the scenes, two things happen. First, the AI turns this messy story into a structured case file. Then plain
> code, not the AI, works out the deadline, the right forum and the danger signs."

**When the answer appears:** scroll slowly through it.

> "It replies in the same Hinglish. First what it understood, then where they stand, then the steps, cheapest first:
> ask in writing, send a legal notice, try free Lok Adalat settlement, and only then court."

**Do:** point at a small number chip like `[1]`, then click the drawer **"… sources · every legal point is checked"**.

> "Every legal sentence has a source number. These come from a hand-checked list of Indian laws, each with a link to
> the official India Code. The AI isn't allowed to cite anything outside this list."

### Scene 3 (0:55-1:15): the case file
**Do:** click the **📁 My case** tab.

> "While we talked, it built a case file: the problem, the amount, the language. This deadline, 15 September 2029,
> three years from moving out, is calculated by code, because dates and money are exactly where AI models make
> confident mistakes. It also shows which proof they already have and what's missing, and the usual path."

### Scene 4 (1:15-1:35): the document
**Do:** click **📝 Documents**. Leave "Legal notice to landlord" selected, type a name (e.g. *Rahul Sharma*), and click
**✍️ Prepare draft**. Scroll to the draft.

> "It drafts the legal notice. The legal wording is a fixed template that I checked; the AI only writes the facts. And
> anything it doesn't know, like the landlord's address, becomes a FILL blank instead of a made-up detail. It
> downloads as a Word file."

### Scene 5 (1:35-1:50): practice
**Do:** click **🥊 Practice**. Type *"Please return my 40,000 deposit, I left the flat on 15 September"* and click
**💬 Say it**.

> "Most people give up because they're intimidated. So here they can rehearse. The AI plays a difficult landlord, and
> afterwards a coach gives feedback on what to say better."

(You don't need to wait for the reply. Move on if it's slow.)

### Scene 6 (1:50-2:30): the most important part, "try to fool it"
**Do:** click **🛡️ Why trust it**, then the sub-tab **🧪 Try to fool it**. The first example is already selected.

> "The brief warned that AI invents laws and court cases. So here's an answer with a fake section and a fake Supreme
> Court judgment. On the left, the citation guard has struck them out in red. The guard is plain code, no AI. It
> checks every section, Act and case name against the verified list. On the right is what the user would actually see.
> In the real app, the model is first asked to fix its own answer; this mechanical removal is only the last resort."

**Do:** click the option **"Hindi: wrong section number"**.

> "It works in Hindi too. Section 17 of the Code on Wages is real and verified, so it passes. Section 99 is invented,
> so it's blocked."

### Scene 7 (2:30-2:50): knowing its limits
**Do:** click **📨 Understand a notice**, then **📄 Try: Cheque-bounce notice**, then **📖 Explain this notice**.
While it loads:

> "Being honest about limits matters as much as being helpful. Here someone received a cheque-bounce notice. That's a
> criminal matter with a 15-day window. So the app leads with 'talk to a lawyer now', calculates the exact last date,
> and explains the notice in plain Hindi."

(If the answer is slow, say the line and move to the last scene; the red/amber warning card is enough.)

### Scene 8 (2:50-3:00): proof it was tested
**Do:** switch to the GitHub tab and open the **outputs** folder (its README shows the table).

> "I tested it on 22 hand-written cases in six languages, on two different AI models, including attempts to make it
> invent judgments. The guard caught every invented reference, and none reached a user. Reading every answer myself
> found real bugs, and the raw outputs and my notes on where it fails are all here. Thank you!"

---

## Part B: the live interview demo (about 10 minutes)

They may ask you to run it on a **new input**. Run the same flow as the video, but go deeper at three points and open
code files. Have VS Code open on the project folder.

### B1. Start the same way (2 min)
Do Scenes 1-3 from the video. If they give you their own problem, type it into the Talk box instead of clicking a card.
After the answer, ask them: "Shall I show you how that answer was checked?"

### B2. Show how the answer was checked (1 min)
**Do:** **🛡️ Why trust it → 🔍 This answer's check**.

> "This shows the check for the answer we just got: how many legal references it found, how many were caught on the
> first draft, and how many reached the user, which should always be zero. It also lists exactly which knowledge
> entries the AI was allowed to use."

### B3. Open the code: the pipeline (2 min)
Open these files in VS Code, in this order:

1. **`nyaya/assistant.py`**, the docstring at the top.
   > "One user turn is five steps: intake by the AI into JSON, then rules in code, then retrieval of verified entries
   > in code, then the AI writes the answer, then the guard in code. That's two AI calls per turn, three if the guard
   > asks for a repair."
2. **`knowledge/deposit.yaml`**: scroll to one entry.
   > "This is the knowledge base: plain YAML that a lawyer can review, no code. Each entry has the plain-language rule,
   > the exact Act and section, a confidence level and a link. Adding a new problem area means adding one file like
   > this."
3. **`nyaya/rules.py`**: the `compute` function.
   > "Deadlines, forum, fees and escalation are all here, in code. For example, wages after resigning are due within
   > two working days, skipping Sundays, and a consumer complaint has a two-year limit."
4. **`nyaya/guard.py`**: the docstring at the top.
   > "The guard finds every section, धारा, Act name and case citation, checks each one against the entries that were
   > retrieved for this case, sends violations back to the model once, and scrubs whatever is left."

### B4. Swap the model live (1 min)
This shows that the model is easy to swap. In a terminal in the project folder:

```bash
python cli.py ask "My employer has not paid my salary for October, I still work there, 30000 per month" --provider groq
python cli.py ask "My employer has not paid my salary for October, I still work there, 30000 per month" --provider gemini --model gemini-3.5-flash-lite
```

> "Same code, different model: it's one setting. If they connect a stronger model through their API, it's
> `LLM_PROVIDER` and `LLM_MODEL` in the environment, or an OpenAI-compatible endpoint. The app also falls back
> automatically if a provider runs out of quota."

### B5. Run a test case live (optional, 1 min)
```bash
pytest -q                                             # 51 offline tests, no API key, about 2 seconds
python -m evals.run_evals --only con-builder-large    # one eval case end to end
```

> "The tests need no API key. They test the guard, the rules, the safety flags and the whole pipeline with a scripted
> fake model that deliberately invents a law."

### B6. The honest part: where it fails (2 min)
Open **`outputs/gemini_gemini-3.5-flash-lite/REVIEW.md`** on GitHub and scroll to the "What I changed" table.

> "The automatic checks said 110 out of 111. But I read every answer, and found problems the checks missed. The worst
> was in my own rules code: it told someone who paid 85 lakh for a delayed flat that their claim was time-barred.
> That's wrong, because the flat was never handed over, so the problem is continuing. If a real person read that, they
> might give up a valid claim. I fixed it in code with a test, not with a prompt."

Then open **`outputs/groq_openai_gpt-oss-120b/REVIEW.md`**:

> "The bigger Groq model was better at nuance, but it missed an OTP fraud and said 'you have two years' instead of 'call
> 1930 now'. So safety flags are now added by code on clear keywords. Neither model is safe enough alone; that's
> why the decisions that matter are in code."

---

## Part C: likely questions, with answers

**Why Problem 2?**
"Its failure mode is the most interesting. A confident AI that invents a section or a judgment is worse than no help.
That forced a design question I liked: what should the AI do, and what must code do?"

**How exactly do you stop hallucinated laws?**
"Four layers. A human-written knowledge base. Code picks only the entries for this case. The prompt says every legal
sentence must carry a tag from those entries. And then the guard, which is code, checks every section, Act and case
name. If something isn't backed, the model gets one chance to fix it, and anything left is removed. Across 44 model
runs the guard caught 6 invented references, and 0 reached users."

**What can the guard NOT catch?**
"It checks references, not claims. If the model writes 'the company must pay you double' without citing any section,
the guard can't verify that sentence. Also, a tag can point to the wrong entry. The next step would be a cheap second
model asking 'does this entry support this sentence?'"

**Why not RAG with embeddings?**
"With 43 entries, rules beat embeddings: they're predictable, debuggable and never pull in an irrelevant law. Past a
few hundred entries I'd move to a vector index, but the guard contract stays the same: cite only what was retrieved."

**What does it cost?**
"About 4,000 input and 1,000-2,000 output tokens per turn, measured on the eval. On flash-class models that's a fraction
of a rupee per conversation. Rules, retrieval and the guard cost nothing."

**How would it scale to millions of users?**
"The expensive part isn't the model, it's knowledge. Each new problem area is a YAML file reviewed by a lawyer. For
traffic: a paid tier on two providers with automatic fallback, which I already built because the free tiers ran out
twice during testing."

**Where is the human in the loop?**
"Three places. A lawyer reviews the knowledge base. Code forces 'talk to a lawyer now' for court summons, police,
cheque bounce, harassment, time-barred claims and large amounts. And every document is a draft the person checks, with
FILL blanks for anything unknown."

**How would you know it works with real users?**
"The share of conversations that end in a sent notice or a filed complaint; money recovered, asked 30 days later;
the guard catch rate per model; and a weekly lawyer audit of 50 random answers."

**Which AI tools did you use, and where did they go wrong?**
"Claude Code for writing and refactoring code, and Gemini and Groq inside the product. It went wrong in exactly the
risky places: the time-barred rule, a patch that silently put invisible characters into the guard's regex, a fix that
caused a genuine user to be refused as 'forgery', and default models that had been retired. I caught each by reading
outputs and files, not by trusting scores."

**What would you build next?**
"First, a claim-support check so every tagged sentence is verified against its entry. Second, run intake on the stronger
model, since that's where the small model makes its mistakes. Third, a lawyer review of the knowledge base and more
problem areas."

---

## If something breaks during the demo

| Problem | What to do and say |
|---|---|
| The app is asleep | Click "Yes, get this app back up" and talk over the wait: "It's on a free host, so it sleeps when idle." |
| An answer is slow (40 s+) | Keep talking. Use the "behind the scenes" lines. Free tiers are slow at busy times. |
| An error says the model is unavailable | "That's the free tier's daily limit." Go to **🛡️ Why trust it**, which works without any model, then show `outputs/` on GitHub. |
| The sidebar says "Switched model after a quota limit" | Point at it: "That's the automatic fallback working. Groq ran out, so it moved to Gemini." |
| Nothing works at all | Run it locally: `streamlit run app.py`, or `python cli.py ask "…"` in the terminal. |
