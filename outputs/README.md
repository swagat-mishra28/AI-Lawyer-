# Raw outputs

Every file here was written by `python -m evals.run_evals` and is **unedited**. Each case has:
- `<case>.md`: a readable transcript (user turns, assistant replies, the case file, the deadlines and escalations computed by code, the guard log, any draft or practice session, and the automatic checks);
- `<case>.json`: the full trace, including every model call with its latency and token counts.

`summary.md` / `summary.csv` hold the per-run scorecard. `REVIEW.md` is my human review of where it fails.
The `eval_run*.log` files are the console logs.

| Folder | What it is |
|---|---|
| `gemini_gemini-3.5-flash-lite/` | **Full run, 22 cases**, before fixes. 110/111 checks. [REVIEW](gemini_gemini-3.5-flash-lite/REVIEW.md) |
| `groq_openai_gpt-oss-120b/` | **Full run, 22 cases**, same code. 108/111 checks. [REVIEW](groq_openai_gpt-oss-120b/REVIEW.md) |
| `gemini_gemini-3.5-flash-lite_after-fixes/` | The 9 cases whose problems I fixed (from both models' reviews), re-run: 40/42. [REVIEW](gemini_gemini-3.5-flash-lite_after-fixes/REVIEW.md) |
| `gemini_gemini-3.5-flash/` | **Partial**: the first 5 cases passed 34/34, then the free tier's 20 requests/day ran out (the 429 errors are kept as evidence). No summary, because the run was stopped. |

A Groq re-run of its failures after the fixes was blocked by Groq's free-tier limit (200k tokens/day). To redo it:
`python -m evals.run_evals --provider groq --only cyber-fraud adv-forgery con-builder-large --out outputs/groq_after-fixes`.

All runs pin today's date to 2026-11-21, so the deadlines are reproducible.
