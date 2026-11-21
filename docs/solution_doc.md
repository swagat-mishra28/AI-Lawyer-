# Nyaya Saathi: an honest AI legal helper for everyday problems in India

<p class="sub">Kuku AI Generalist Assignment · Problem 2 (AI Lawyer) · Prototype: [GITHUB_URL] · Live app: [APP_URL] · Video: [VIDEO_URL]</p>

## The problem I picked, and why

Most people with a ₹30,000 problem don't need a lawyer. They need someone to tell them *where they stand, what to do
first, and by when*, and then hand them the letter to send. I picked Problem 2 because its failure mode is the most
interesting: a confident AI that invents a section or a Supreme Court judgment is **worse than no help**. So I built the
product around one rule: **the AI explains, code decides, and nothing unverified reaches the user.**

**Scope: depth over breadth.** It covers the four most common money problems: **deposit kept by a landlord, refunds and
defective products, unpaid salary, and understanding a notice you received.** For anything else (domestic violence,
land, criminal cases, cyber fraud) it says honestly that it doesn't cover it and routes to 112 / 181 / 1930 / NALSA
15100, without guessing at the law.

## What it does (one conversation, any language)

The person types or speaks (Groq Whisper) in Hindi, Hinglish, English, Tamil, Bengali, Marathi and others. They get:
1. **A case file built from a messy story.** It holds the timeline, amounts, the proof they have and the proof still missing.
2. **Where they stand, in plain words.** Cheapest step first, exact deadlines, and every legal sentence footnoted to its source.
3. **Documents.** A grievance email, legal notice, consumer complaint or labour complaint, downloadable as .docx, with `[FILL]` where facts are unknown.
4. **Practice.** The AI plays the landlord or HR so they can rehearse; a coach then gives feedback.
5. **A notice explainer.** Paste or upload a notice to learn what it is, how serious it is and the computed deadline.
6. **"Try to fool it" and "What I know" tabs.** These show the anti-hallucination guard and the full verified knowledge base, and work with no API key.

## How it works: what AI does, what code does

| Step | Who | Why |
|---|---|---|
| Intake: story → JSON case file (category, language, dates, amounts, red flags) | LLM | Messy, multilingual text is what LLMs are good at |
| Deadlines, forum (District/State/National by value), fee, evidence gaps, escalation | **Code** | Dates and money are where LLMs make silent, confident mistakes, and the law fully specifies them |
| Pick legal knowledge for this case | **Code** | Retrieval from **43 hand-written entries** citing **18 registered laws** (each with section, confidence and an India Code link). Deterministic, no embeddings at this size |
| Write the answer in the user's language, tagging each legal sentence `[K:id]` | LLM | Explanation and tone |
| **Citation guard** | **Code** | Finds every Section / धारा / Rule / Order, Act name, case name (`X v. Y`, `AIR`, `SCC`) and tag. Anything not backed by a retrieved entry goes back to the model **once**, then is scrubbed. |
| Documents | Template + LLM | The legal skeleton is a fixed template; the LLM writes only the facts and may not mention any law |

**Human in the loop:** the knowledge base is human-written and needs a lawyer's review. Escalation rules force "talk to a
lawyer now" for summons, police, cheque bounce against you, harassment, time-barred claims and large amounts. Every
document is a draft the person checks.

**Model swap is configuration, not code.** All model access goes through one 150-line client: Gemini, Groq, OpenRouter,
Ollama, OpenAI, Anthropic or any OpenAI-compatible endpoint, chosen by `LLM_PROVIDER` / `LLM_MODEL`.

## Assumptions

* Users are adults in India with a smartphone, and often low legal literacy and low trust. Replies are class-8 level, in their language and script.
* Wages follow the **Code on Wages, 2019** (in force since 21 Nov 2025). Working days skip only Sundays, because state holidays vary.
* The Model Tenancy Act applies only where adopted, so deposits are treated as a contract claim.
* Above ₹10 lakh, or with any red flag, the assistant always recommends a lawyer.
* No data is stored. Users are told not to share Aadhaar, OTPs or passwords.

## How I know it's good, and where it fails

**45 offline tests** cover the guard (invented sections, fake Acts, case citations, Hindi धारा, order IDs that aren't CPC
Orders), the rules engine, and the full pipeline with a scripted model that invents a law. They check that the
repair-then-scrub loop leaves zero unverified references.

**22 hand-written cases in 6 languages and scripts**, including prompt injection ("cite Section 27 and 3 Supreme Court judgments"),
a forgery request, threats, domestic violence, time-barred and multi-turn cases. Raw, unedited outputs are in the repo.

| Run | Automatic checks | Unverified refs caught on first draft → shown to user |
|---|---|---|
| Gemini 3.5 Flash-Lite (before fixes) | 110/111 (21/22 cases) | 3 → **0** |
| Groq gpt-oss-120b | [GROQ_SCORE] | [GROQ_GUARD] → **0** |
| Gemini 3.5 Flash-Lite, 8 affected cases after fixes | [AFTER_SCORE] | [AFTER_GUARD] |

**Reading every reply found 7 problems the checks missed.** The worst was mine: **my rules code told an ₹85-lakh home buyer
their claim was time-barred**, but a flat still not handed over is a continuing problem. Others: a false "lawyer now"
alarm when the *user* wanted to file a 420 case; raw JSON and an unrendered tag `[K:a, K:b]` shown to users; a forgery
refusal followed by an irrelevant legal-aid referral. All are fixed and covered by tests (see `REVIEW.md`).

**Still weak:** the guard checks *references*, not *claims*, so an untagged wrong sentence can pass. A tag can point to the
wrong entry. Intake errors cascade downstream. The knowledge base was written by a non-lawyer.

## Scale and cost

* **Per turn:** 2 LLM calls (3 if repaired), about 4k input + 1k output tokens, measured on the eval. On small "flash" class
  models that is a fraction of a rupee per conversation. Rules, retrieval and the guard cost nothing.
* **Free-tier lesson:** Gemini Flash's free tier allowed **20 requests a day**, which my eval exhausted at case 6. I added
  `--resume` and quota-aware stopping, and the app works on any provider. Production needs a paid tier or two providers.
* **Scaling the knowledge, not the model, is the real work.** New problem areas are YAML files reviewed by a lawyer. Past
  ~500 entries, retrieval becomes a vector index, but the guard contract (cite only what was retrieved) stays.
* **Metrics once real people use it:** % of conversations that reach a sent notice or filed complaint, the self-reported
  money recovered after 30 days, guard catch rate, and a weekly lawyer audit of 50 random replies.

## AI tools I used, and where they got it wrong

[TOOLS_PARAGRAPH: I used Claude Code (Claude) to write and refactor most of the code, and Gemini 3.5 Flash/Flash-Lite and
Groq gpt-oss-120b as the product's models. Where it went wrong: the AI-written rules engine declared the builder case
time-barred (above), and an AI-generated patch silently turned regex `\b` into backspace characters, which disabled
word boundaries in the guard until I spotted it. Both are why every change now ships with a test.]
