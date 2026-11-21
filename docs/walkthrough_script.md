# 3-minute walkthrough script

Record with Loom or OBS at 1080p, browser zoomed to 110%. Before recording, open the app, click **Start a new case**
and close other tabs. Speak naturally; the timings are a guide.

| Time | Screen | Say |
|---|---|---|
| 0:00-0:15 | App home, sidebar visible | "This is Nyaya Saathi, a legal helper for four everyday problems in India: a deposit the landlord keeps, a refund that never came, unpaid salary, and a notice you don't understand. You can type or speak in your own language." |
| 0:15-0:50 | **Talk** tab: click the Hinglish deposit example | "Here's a Hinglish message: the landlord has kept Rs 40,000. It answers in Hinglish, cheapest step first, and every legal sentence has a numbered source." Open **Sources used**: "These come from a hand-checked list of laws, each linked to India Code." |
| 0:50-1:15 | **My case** tab | "Behind the scenes, the story became a case file: timeline, amount, proof they have and proof still missing. The deadline is calculated by code, not by the AI, because dates and money are where models make confident mistakes." |
| 1:15-1:35 | **Documents** tab: Legal notice, click Prepare | "It drafts the legal notice. The legal text is a fixed template. The AI writes only the facts, and anything it doesn't know becomes a [FILL] placeholder instead of an invented detail. Download as Word." |
| 1:35-1:55 | **Practice** tab: send one line | "People give up because they're intimidated, so here they can rehearse. It plays a difficult landlord, then coaches them." |
| 1:55-2:30 | **Try to fool it** tab: example 1, then example 4 (Hindi) | "The brief says AI invents laws. Here's an answer with a fake section, a fake Supreme Court case and a made-up Act. The citation guard is plain code. It blocks every legal reference that isn't backed by a verified entry, in English or Hindi. In the real flow, the model is first asked to fix its answer. This scrub is only the last resort." |
| 2:30-2:50 | Paste the cheque-bounce sample into **Understand a notice** | "When it shouldn't handle something alone, it says so. A cheque-bounce notice against you is criminal and has a 15-day window, so it leads with 'talk to a lawyer now' and gives the exact date." |
| 2:50-3:00 | `outputs/.../summary.md` in the editor | "I ran 22 test cases in six languages, including attempts to make it invent judgments. The raw outputs and my review of where it fails are in the repo. Thanks!" |

**Backup plan:** if the free-tier model is slow during recording, run `python cli.py ask "..."` in a terminal
before recording and show the output.
