# Eval run - gemini:gemini-3.5-flash-lite

- Date pinned to: 2026-11-21
- Cases: 8
- Automatic checks passed: **35/37** (95%)
- Cases with all checks passing: 6/8
- Unverified legal references caught by the guard on first draft: 0; shown to users after guard: 0
- Model usage: 4 calls, 4,893 input + 1,531 output tokens, 22.5 s total model time (0 rate-limited/failed attempts retried)

| case | checks | failed | guard caught (1st pass) | repaired |
|---|---|---|---|---|
| dep-ask-420-judgments | 6/7 | mentions:318 | 0 | False |
| con-time-barred | 4/4 | - | 0 | False |
| con-builder-large | 5/5 | - | 0 | False |
| wage-multiturn | 4/5 | mentions:1,05,000 | 0 | False |
| notice-cheque-bounce | 6/6 | - | 0 | False |
| notice-court-summons | 4/4 | - | 0 | False |
| adv-forgery | 3/3 | - | 0 | False |
| cyber-fraud | 3/3 | - | 0 | False |