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

**49 offline tests** cover the guard (invented sections, fake Acts, case citations, Hindi धारा, malformed tags), the
rules engine, the safety flags, provider fallback, and the full pipeline with a scripted model that invents a law. They
check that the repair-then-scrub loop leaves zero unverified references.

**22 hand-written cases in 6 languages and scripts**, including prompt injection ("cite Section 27 and 3 Supreme Court
judgments"), forgery, threats, domestic violence, cyber fraud, time-barred and multi-turn cases. I ran them on **two
models with the same code**. All raw outputs are in the repo, unedited, with a human `REVIEW.md` per run.

| Run (same 22 cases) | Automatic checks | Invented refs caught on 1st draft → shown to user |
|---|---|---|
| Gemini 3.5 Flash-Lite | 110/111 | 3 → **0** |
| Groq gpt-oss-120b | 108/111 | 3 → **0** |
| 9 affected cases re-run after fixes (Flash-Lite) | 40/42 | 0 → **0** |

**Reading every reply found problems the checks missed, and I fixed them in code, not with prompts.**

- **The worst was mine: my rules code told an ₹85-lakh home buyer the claim was time-barred.** A flat still not handed over is a continuing problem, so the code now says "time limit unclear, file now, have a lawyer confirm".
- **Groq missed a cyber fraud** (OTP + KYC link) and said "you have 2 years" instead of "call 1930 now". Code now *adds* safety flags on clear keywords, because a false banner is cheap and a miss is not.
- **My first forgery fix caused a regression:** a real ₹50k deposit question was refused as "forgery". A refusal now also needs a deterministic signal in code.
- **Others:** raw JSON shown to users, malformed source tags (`[ K:x ]` with a zero-width space) that skipped validation, and duplicate warnings.

**Still weak:**

- The guard checks *references*, not *claims*, so an untagged wrong sentence can pass.
- A tag can point to the wrong entry.
- Flash-Lite's intake still raises a false "accused of a crime" flag on the 420 case. Groq gets it right, so I would run intake (one short call) on the stronger model.
- The knowledge base was written by a non-lawyer and needs a lawyer's review.

## Scale and cost

* **Per turn:** 2 model calls (3 if repaired), about 3.7k input + 1–2k output tokens, measured on the eval (Flash-Lite:
  84k in / 22k out for 22 cases). That is a fraction of a rupee per conversation on flash-class models. Rules, retrieval
  and the guard are free.
* **Free tiers ran out twice:** Gemini Flash allows 20 requests a day (exhausted at case 6), and Groq allows 200k tokens a day
  (one full run). The client now **falls back automatically** (Groq → Gemini Flash → Flash-Lite), verified live in the
  app. Evals pin one model. Production needs a paid tier, and I would keep two providers anyway.
* **Scaling the knowledge, not the model, is the real work.** Each new problem area is one YAML file reviewed by a lawyer.
  Past ~500 entries, retrieval becomes a vector index, but the guard contract (cite only what was retrieved) stays.
* **How I'd know it works with real users:**
    - % of conversations that end in a sent notice or a filed complaint;
    - money recovered, self-reported, 30 days later;
    - guard catch rate per model;
    - a weekly lawyer audit of 50 random replies.

## AI tools I used, and where they got it wrong

[EDIT IN YOUR OWN WORDS: I used Claude Code (Claude) to write and refactor most of the code, and Gemini 3.5 Flash /
Flash-Lite and Groq gpt-oss-120b as the product's models. Where it went wrong: the AI-written rules engine declared the
builder case time-barred, and an AI-generated patch silently turned the regex `\b` into backspace characters, which
disabled word boundaries in the guard until I spotted it. That is why every fix now ships with a test.]
