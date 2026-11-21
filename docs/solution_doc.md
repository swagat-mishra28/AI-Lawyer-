# Nyaya Saathi: an honest AI legal helper for everyday problems in India

<p class="sub">Kuku AI Generalist Assignment · Problem 2 (AI Lawyer) · Code: [github.com/swagat-mishra28/AI-Lawyer-](https://github.com/swagat-mishra28/AI-Lawyer-) · Live app: [nyaya-saathi on Streamlit](https://eqfddnzmoycgqfdlvgbxfc.streamlit.app/) · Video: [VIDEO_URL]</p>

## The problem I picked, and why

Most people with a ₹30,000 problem don't need a lawyer. They need someone to tell them *where they stand, what to do
first, and by when*, and then hand them the letter to send. I picked Problem 2 because its failure mode is the most
interesting: a confident AI that invents a section or a Supreme Court judgment is **worse than no help**. So I built the
product around one rule: **the AI explains, code decides, and nothing unverified reaches the user.**

**Scope: depth over breadth.** It covers the four most common money problems: **deposit kept by a landlord, refunds and
defective products, unpaid salary, and understanding a notice you received.** For anything else (domestic violence, land,
criminal cases, cyber fraud) it says honestly that it doesn't cover it and routes to 112 / 181 / 1930 / NALSA 15100.

## What it does (one conversation, any language)

The person types or speaks (Groq Whisper) in Hindi, Hinglish, English, Tamil, Bengali, Marathi and others. They get:

1. **A case file** built from the messy story: timeline, amounts, the proof they have and the proof still missing.
2. **Where they stand, in plain words.** Cheapest step first, exact deadlines, and every legal sentence footnoted to a verified source.
3. **Documents**: a grievance email, legal notice, consumer complaint or labour complaint (.docx), with `[FILL]` where facts are unknown.
4. **Practice**: the AI plays the landlord or HR so they can rehearse, then a coach gives feedback.
5. **A notice explainer**: what the notice is, how serious it is, and the computed deadline.
6. **A "Why trust it" tab**: paste any AI answer and watch the guard strike out invented laws, then browse every verified entry. It works with no API key.

## How it works: what AI does, what code does

| Step | Who | Why |
|---|---|---|
| Intake: story → JSON case file (category, language, dates, amounts, red flags) | LLM | Messy, multilingual text is what LLMs are good at |
| Deadlines, forum (District/State/National by value), fee, evidence gaps, escalation | **Code** | Dates and money are where LLMs make silent, confident mistakes, and the law fully specifies them |
| Pick legal knowledge for this case | **Code** | **43 hand-written entries** citing **18 registered laws**, each with a section, a confidence level and an India Code link. Deterministic retrieval |
| Write the answer in the user's language, tagging each legal sentence `[K:id]` | LLM | Explanation and tone |
| **Citation guard** | **Code** | Finds every Section / धारा / Rule / Order, Act name, case name (`X v. Y`, `AIR`, `SCC`) and tag. Anything not backed by a retrieved entry goes back to the model **once**, then is scrubbed |
| Safety flags (cyber fraud, self-harm, forgery) | Code + LLM | Code adds a flag the model missed and drops a refusal the conversation doesn't support |

**Human in the loop:** the knowledge base is human-written and needs a lawyer's review. Code forces "talk to a lawyer now"
for summons, police, cheque bounce against you, harassment, time-barred claims and amounts above ₹10 lakh. Every document
is a draft the person checks. **Model swap is configuration:** one client serves Groq, Gemini, OpenRouter, Ollama, OpenAI,
Anthropic or any OpenAI-compatible endpoint (`LLM_PROVIDER` / `LLM_MODEL`). It **falls back automatically** when a free
quota runs out.

**Assumptions:**

- Users are adults with a smartphone and low legal literacy; replies are class-8 level, in their own language and script.
- Wages follow the Code on Wages, 2019 (in force since 21 Nov 2025). Working days skip only Sundays.
- The Model Tenancy Act applies only where a state adopted it, so deposits are treated as a contract claim.
- No data is stored.

## How I know it's good, and where it fails

**51 offline tests** cover the guard, the rules, the safety flags, the fallback, and the full pipeline with a scripted model
that invents a law. **22 hand-written cases in 6 languages and scripts** cover prompt injection ("cite Section 27 and
3 Supreme Court judgments"), forgery, threats, domestic violence, cyber fraud, time-barred and multi-turn conversations.
I ran them on **two models with the same code**. Raw outputs are in the repo, unedited, with a human `REVIEW.md` per run.

| Run (same 22 cases) | Automatic checks | Invented refs caught on 1st draft → shown to user |
|---|---|---|
| Gemini 3.5 Flash-Lite | 110/111 | 3 → **0** |
| Groq gpt-oss-120b | 108/111 | 3 → **0** |
| 9 affected cases re-run after fixes (Flash-Lite) | 40/42 | 0 → **0** |

**Reading every reply found problems the checks missed.** The worst are in the table below. Others:

- Groq treated an OTP/KYC-link fraud as a consumer case ("you have 2 years" instead of "call 1930 now"). Code now *adds* safety flags on clear keywords.
- Raw JSON and malformed source tags (`[ K:x ]` with a zero-width space) were shown to users, and the malformed tags skipped validation.

All of these are fixed in code and re-run.

**Still weak:**

- The guard checks *references*, not *claims*, so an untagged wrong sentence can pass, and a tag can point to the wrong entry.
- Flash-Lite still raises a false "accused of a crime" flag when the person wants to *file* a 420 case. Groq gets it right, so I'd run intake on the stronger model.
- The knowledge base needs a lawyer's review.

## Scale and cost

* **Per turn:** 2 model calls (3 if repaired), about 3.7k input + 1–2k output tokens, measured on the eval. That is a
  fraction of a rupee per conversation on flash-class models. Rules, retrieval and the guard cost nothing.
* **Free tiers ran out twice** (Gemini Flash: 20 requests/day; Groq: 200k tokens/day). That is why the fallback exists,
  and why production needs a paid tier with two providers.
* **Scaling means adding knowledge, not a bigger model.** Each new problem area is one YAML file reviewed by a lawyer; past ~500 entries
  retrieval becomes a vector index, but the guard contract stays the same.
* **How I'd know it works:** the % of chats that end in a sent notice or filed complaint, the money recovered after
  30 days, the guard catch rate per model, and a weekly lawyer audit of 50 random replies.

## AI tools I used, and where they got it wrong

I used **Claude Code (Claude)** as a pair programmer to write, test and refactor the code. The product runs on **Gemini 3.5
Flash / Flash-Lite and Groq gpt-oss-120b**. I made the decisions (scope, what stays in code, what counts as a failure)
and read every output myself. The AI made me fast, and it was confidently wrong in exactly the places a user would be hurt:

| What the AI got wrong | How it was caught | How it was fixed |
|---|---|---|
| The AI-written rules engine told an ₹85-lakh home buyer the claim was **time-barred**, counting from the promised possession date. Wrong: the flat was never handed over, so the problem is still continuing. | Reading the outputs. The automatic checks had passed it. | Code never says "time-barred" for continuing wrongs; it says "file now, have a lawyer confirm". Test added. |
| An AI code patch silently turned the regex `\b` into invisible backspace characters, weakening the citation guard while the tests still passed. It happened twice. | Reading the changed files, not just the test results. | Repaired, plus a test that fails if any source file contains control characters. |
| The AI's first fix for forgery requests **caused a regression**: a genuine ₹50k deposit question was refused as "forgery". | Re-running the affected cases after every fix. | A refusal now also needs a deterministic signal in code (fake, backdated, jaali…). Test added. |
| The AI chose default models that had been **retired** (`gemini-2.5-flash`, `llama-3.3-70b`). Its setup check also said my key was ready when the line held only a comment. | The first real API call failed (404 / 401). | New defaults; a retired model now triggers a fallback; keys are read with a proper `.env` parser. |

**Lesson:** never trust a score you haven't read. Every rule that matters now lives in tested code.
