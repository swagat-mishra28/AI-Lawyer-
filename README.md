# ⚖️ Nyaya Saathi: an AI legal-help assistant for everyday problems in India

**Kuku AI Generalist Assignment, Problem 2 (Build an AI Lawyer)**

Nyaya Saathi helps an ordinary person with four common problems: a **landlord keeping the security deposit**, a **refund that never came or a defective product**, **unpaid salary or wages**, and **a notice they don't understand**. The person can type or speak in their own language (Hindi, Hinglish, English, Tamil, Bengali, Marathi and others). It then:

1. **Builds the case**: turns a messy story into a timeline, amounts, the proof they have and the proof still missing.
2. **Explains where they stand**: plain language, cheapest option first, with exact deadlines.
3. **Prepares documents**: a grievance email, a legal notice, a consumer complaint or a labour complaint, as .docx.
4. **Helps them argue**: role-plays the landlord, HR or customer care so they can practise, then coaches them.
5. **Explains notices**: paste or upload a notice to learn what it is, how serious it is and what the deadline is.
6. **Knows its limits**: it refers to a lawyer, legal aid (15100) or an emergency line (112) when it should, and refuses forgery.

> **No API key? You can still try it.** The **🧪 Try to fool it** tab runs the citation guard on any AI-style answer you paste (invented sections, fake judgments, made-up Acts, in English or Hindi), and **📚 What I know** lists every law the assistant is allowed to state.

> **It is not a lawyer and never claims to be.** It only states law that appears in a hand-checked knowledge base, and a code-level citation guard removes anything else.

---

## Why you can trust what it says (anti-hallucination design)

LLMs confidently invent sections ("Section 27 of the Consumer Protection Act"), Acts and Supreme Court judgments. The system has **four layers** so that an invented reference never reaches the user:

| Layer | What | AI or code |
|---|---|---|
| 1. Curated knowledge | ~45 hand-written entries in `knowledge/*.yaml`. Each has a plain-language statement, the exact Act and section, a confidence level, and a link to indiacode.nic.in. Repealed laws are handled explicitly (IPC → BNS from 1 July 2024). | Human-written |
| 2. Retrieval | Only the entries for this case's category, plus triggered general ones, go into the prompt. | Code (deterministic) |
| 3. Grounded prompt | Every legal sentence must carry a `[K:id]` tag. The model may not name any law not in the entries, never cites judgments, and says "I don't know" otherwise. | AI |
| 4. **Citation guard** (`nyaya/guard.py`) | Regex and alias matching find every Section, धारा, Rule, Order, Article, Act name, case name (`X v. Y`, `AIR 1994 SC`, `SCC`) and `[K:id]` tag. Each (Act, section) pair must be backed by a retrieved entry. Violations go back to the model **once** to fix; anything left is **scrubbed mechanically**. Each answer's trace records what was caught. | **Code** |

The same idea applies to numbers. **Deadlines, forum, filing fee, evidence gaps and escalation are computed in code** (`nyaya/rules.py`), not by the model. Examples: 2-year consumer limitation, District, State or National Commission by value paid, wages due within 2 working days of leaving, 15 days to pay after a cheque-bounce notice. The model receives them as facts and only explains them.

## Architecture

```
user text / voice ──► Whisper STT (Groq free) ──┐
                                                 ▼
             ┌──────────── 1. INTAKE (LLM → JSON case file: category, language, dates, amounts, proof, red flags)
             │             2. RULES  (code: deadlines, forum, fee, escalation, missing evidence)
  Session ───┤             3. RETRIEVE (code: verified KB entries for this category)
             │             4. ADVISE (LLM, grounded, replies in the user's language & script)
             └──────────── 5. GUARD  (code: check → model repair → scrub) ──► answer + numbered sources
                                                                             └─► gTTS voice reply
   Documents: fixed legal template + LLM-written facts only ([FILL: …] for unknowns) → .docx
   Practice:  LLM plays the other side → coach feedback (guarded)
   Notice:    LLM extracts → code computes deadline/severity → grounded explanation (laws quoted in the notice are allowed, labelled)
```

Each turn makes **2 model calls**, or 3 if the guard requests a repair.

## Run it

```bash
python -m venv .venv && .venv/Scripts/activate      # Windows (use bin/activate on mac/linux)
pip install -r requirements.txt
cp .env.example .env        # add a free key: GROQ_API_KEY (also voice) and/or GEMINI_API_KEY
streamlit run app.py        # web app
python cli.py chat          # terminal chat
python cli.py ask "Landlord kept my 40k deposit, I moved out on 15 Sept" --draft legal_notice
python cli.py notice samples/cheque_notice.txt --lang Hindi
pytest -q                   # 49 offline tests: guard, rules, safety flags, fallback, pipeline (no key needed)
python -m evals.run_evals   # full eval: 22 cases → outputs/<model>/  (--resume after a quota stop)
```

**Swapping the model needs no code change.** Set `LLM_PROVIDER` / `LLM_MODEL` to Gemini, Groq, OpenRouter, Ollama (local), OpenAI, Anthropic, or any OpenAI-compatible endpoint (`custom` + `LLM_BASE_URL`). All model access goes through `nyaya/llm.py`.

**It survives free-tier limits.** With both keys set, the default is Groq `openai/gpt-oss-120b`. If a provider hits a *daily* quota or a retired model, the client switches to the next one automatically (Groq → Gemini 3.5 Flash → Flash-Lite; set `LLM_FALLBACK` to change the order), and the sidebar shows the switch. Evals pin one model and never fall back.

**Deploy (free):** push to GitHub → share.streamlit.io → New app → `app.py` → add `GROQ_API_KEY` and `GEMINI_API_KEY` under *Secrets* (TOML: `GROQ_API_KEY = "gsk_..."`).

## What it covers and what it doesn't

| Covered in depth | Pointers only, then a lawyer | Not covered (honest referral) |
|---|---|---|
| Deposit not returned (residential) | Builder delays (RERA), POSH, cheque bounce *against* you, court summons, police notices | Divorce, domestic violence, criminal cases, land/property, family, tax, government service matters |
| Consumer refunds, defects, deficient service, e-commerce | Eviction threats | |
| Unpaid salary/wages, final settlement | | |
| Explaining a notice received | | |

## How we know it's good

* `pytest`: 49 deterministic tests. They cover the guard (invented sections, fake Acts, case names, Hindi धारा, order IDs that are not CPC Orders, years that are not sections) the rules (limitation, Sunday-skipping working days, forum and fee slabs, cheque-bounce windows, amounts like "2.5 lakh"), and the whole turn pipeline with a scripted fake model whose first answer invents a section and a judgment. The tests check that the repair-then-scrub loop leaves zero unverified references.
* `evals/cases.yaml`: 22 hand-written cases in 6 languages and scripts, including adversarial ones (prompt injection asking for fake sections and judgments, backdated rent receipts, "file 420 against landlord"), safety cases (threats, domestic violence, cyber fraud), out-of-scope cases, multi-turn intake, drafting, notice explanation and practice mode.
* **Results:** Gemini 3.5 Flash-Lite **110/111** automatic checks, Groq gpt-oss-120b **108/111**. Across both runs the guard caught 6 unverified references on first drafts and **0 reached users**. Reading every reply found problems the checks missed, including a legal error in my own rules code (a builder-delay case called time-barred) and a missed cyber-fraud emergency. All are fixed in code, covered by tests and re-run: see [outputs/README.md](outputs/README.md).
* `outputs/<model>/`: **unedited** outputs for each case (`.md` readable, `.json` full trace including the guard's first-pass catches), with `summary.md` and a human `REVIEW.md` covering where it fails.

## Repo map

```
app.py               Streamlit UI (Talk · My case · Documents · Practice · Notice · Try to fool it · What I know · How it was checked)
cli.py               terminal interface
nyaya/config.py      provider presets, env-driven model choice
nyaya/llm.py         provider-agnostic LLM client (OpenAI-compatible + Anthropic), retries, usage log
nyaya/assistant.py   the turn pipeline (intake → rules → retrieve → advise → guard)
nyaya/rules.py       deterministic deadlines / forum / fee / escalation / evidence gaps
nyaya/guard.py       citation guard + footnote rendering
nyaya/kb.py          knowledge loader and retrieval
nyaya/drafter.py     document templates + .docx export
nyaya/sparring.py    practice-mode opponent and coach
nyaya/notice.py      notice extraction and explanation
nyaya/voice.py       Whisper STT, gTTS speech
nyaya/prompts.py     every prompt in one file
knowledge/           acts.yaml (allowed statutes) + consumer / deposit / wages / notice / general
evals/               cases.yaml + run_evals.py
outputs/             raw outputs of eval runs
docs/                solution doc (PDF)
```

**Knowledge-base caveat:** the entries were compiled from public sources (India Code, Department of Consumer Affairs, NALSA) by a non-lawyer and are marked high or medium confidence. Before any real launch they need review by a practising lawyer, and a re-check whenever the law changes (for example, Labour Code state rules).
