"""Nyaya Saathi - Streamlit app.  Run:  streamlit run app.py"""
from __future__ import annotations

import datetime as dt
import json
import os

import streamlit as st

# Streamlit Cloud: copy secrets into env so nyaya.config sees them
try:
    for k, v in st.secrets.items():
        if isinstance(v, str):
            os.environ.setdefault(k, v)
except Exception:
    pass

from nyaya import drafter, guard, rules, voice  # noqa: E402
from nyaya.assistant import LANG_OVERRIDES, Session  # noqa: E402
from nyaya.kb import load_kb  # noqa: E402
from nyaya.llm import LLM, LLMError  # noqa: E402
from nyaya.notice import explain, read_document  # noqa: E402
from nyaya.sparring import Sparring  # noqa: E402

st.set_page_config(page_title="Nyaya Saathi - free legal help", page_icon="⚖️", layout="wide")

LEVEL_STYLE = {"refuse": st.error, "emergency": st.error, "lawyer_now": st.warning,
               "lawyer_recommended": st.info, "legal_aid": st.info}
LEVEL_LABEL = {"refuse": "Cannot help with this", "emergency": "Emergency", "lawyer_now": "Talk to a lawyer now",
               "lawyer_recommended": "A lawyer is recommended", "legal_aid": "Where to get help"}
EXAMPLES = [
    "Mere landlord ne 40,000 ka deposit wapas nahi kiya, maine 15 September ko flat khali kiya tha. Ab woh phone nahi utha raha.",
    "I ordered a laptop on Flipkart for 52,000 in August, returned it as defective but the refund never came. Customer care keeps saying 'in process'.",
    "मैंने अक्टूबर में नौकरी छोड़ी, कंपनी ने दो महीने की सैलरी (60,000) अभी तक नहीं दी।",
]


# ------------------------------------------------------------------ state
def get_llm() -> LLM | None:
    if "llm" not in st.session_state:
        try:
            st.session_state.llm = LLM()
        except LLMError as e:
            st.session_state.llm_error = str(e)
            st.session_state.llm = None
    return st.session_state.llm


def new_case():
    for k in ("session", "chat", "spar", "last", "notice_result", "draft"):
        st.session_state.pop(k, None)


llm = get_llm()
kb = load_kb()

# ------------------------------------------------------------------ sidebar
with st.sidebar:
    st.title("⚖️ Nyaya Saathi")
    st.caption("Free help with everyday legal problems in India - in your language.")
    st.markdown("**I can help with**\n- 🏠 Deposit not returned by landlord\n- 🛒 Refunds, defective products, bad service\n"
                "- 💼 Salary / wages not paid\n- 📨 Understanding a notice you received")
    lang_choice = st.selectbox("Reply language", list(LANG_OVERRIDES), index=0,
                               help="'auto' replies in the language you write in")
    if st.button("🗂️ Start a new case", width="stretch"):
        new_case()
        st.rerun()
    st.divider()
    st.caption("**I am not a lawyer.** I explain your options using a checked list of Indian laws and tell you when you "
               "need a real lawyer. Free legal aid: **15100**. Emergency: **112**.")
    st.caption("🔒 Don't share Aadhaar, bank passwords or OTPs. Conversations are not stored after you close this tab.")
    if llm:
        st.caption(f"Model: `{llm.label}`")



def setup_notice():
    st.warning("**No language model is configured yet**, so the conversation features are off. "
               "The **🧪 Try to fool it** and **📚 What I know** tabs work without one.")
    st.code("cp .env.example .env   # then add ONE free key, e.g.\nGEMINI_API_KEY=...   (aistudio.google.com)\n"
            "GROQ_API_KEY=...     (console.groq.com - also turns on voice input)", language="bash")
    st.caption(st.session_state.get("llm_error", ""))


def show_escalations(escalations):
    for e in escalations:
        LEVEL_STYLE.get(e["level"], st.info)(f"**{LEVEL_LABEL.get(e['level'], 'Note')}:** {e['reason']} {e['action']}")


def show_sources(sources):
    if not sources:
        return
    with st.expander(f"📚 Sources used ({len(sources)}) - checked list of laws"):
        for s in sources:
            conf = "" if s["confidence"] == "high" else " · ⚠️ verify (medium confidence)"
            link = f" · [read the law]({s['url']})" if s.get("url") else ""
            st.markdown(f"**[{s['n']}] {s['title']}** - {s['law']}{conf}{link}")


def handle(user_text: str):
    st.session_state.chat.append({"role": "user", "content": user_text})
    with st.spinner("Understanding your problem and checking the law..."):
        try:
            res = sess.turn(user_text)
        except LLMError as e:
            st.session_state.chat.append({"role": "assistant", "content": f"⚠️ The AI model is unavailable right now ({e}). Please try again in a minute."})
            return
    st.session_state.last = res
    st.session_state.chat.append({"role": "assistant", "content": res.reply_rendered, "sources": res.sources,
                                  "escalations": res.rules["escalations"], "lang": res.case.get("language", "en")})


tab_talk, tab_case, tab_docs, tab_spar, tab_notice, tab_fool, tab_kb, tab_trust = st.tabs(
    ["💬 Talk", "📁 My case", "📝 Documents", "🥊 Practice", "📨 Understand a notice", "🧪 Try to fool it",
     "📚 What I know", "🔍 How it was checked"])

FOOL_EXAMPLES = {
    "Invented section + fake judgment (consumer)": ("consumer", "",
        "Under Section 12 of the Consumer Protection Act, 2019 the company must pay you double the price as penalty. "
        "In Lucknow Development Authority v. M.K. Gupta, AIR 1994 SC 787, the Supreme Court held this. "
        "You must file within 2 years [K:cpa-limitation], which Section 69 of the Consumer Protection Act allows."),
    "Made-up Act (deposit)": ("deposit", "",
        "As per the Tenant Deposit Protection Act, 2017 your landlord must return the deposit within 30 days with 18% "
        "interest. The deposit is owed under your agreement, Section 73 of the Indian Contract Act [K:deposit-contract]."),
    "Repealed IPC, not asked about (deposit)": ("deposit", "",
        "File an FIR under Section 420 IPC - the police will recover your deposit in a week."),
    "Hindi: wrong section number (wages)": ("wages", "",
        "वेतन संहिता की धारा 17 के अनुसार नौकरी छोड़ने के दो कार्य दिवस में वेतन देना होता है [K:cw-timely-payment]। "
        "वेतन संहिता की धारा 99 के तहत कंपनी को दोगुना जुर्माना देना होगा।"),
    "Clean, grounded answer (should pass)": ("consumer", "",
        "You can file a complaint within 2 years of the problem [K:cpa-limitation]. Since you paid Rs 52,000, the "
        "District Commission is the right place [K:cpa-pecuniary], and you can file online without a lawyer [K:cpa-efiling]."),
}
GUARD_CATS = ["consumer", "deposit", "wages", "notice"]

# ------------------------------------------------------------------ offline: guard playground
with tab_fool:
    st.markdown("### Can you make it cite a law that isn't real?")
    st.caption("Language models confidently invent sections, Acts and Supreme Court cases. Every answer this assistant "
               "writes passes through a **citation guard - plain code, no AI**. Pick an example or paste any AI-written "
               "answer and see what gets blocked. Works without an API key.")
    pick = st.selectbox("Example", list(FOOL_EXAMPLES))
    cat0, ctx0, txt0 = FOOL_EXAMPLES[pick]
    c1, c2 = st.columns([1, 3])
    gcat = c1.selectbox("Case type (decides which verified laws are allowed)", GUARD_CATS,
                        index=GUARD_CATS.index(cat0), key=f"gcat_{pick}")
    gctx = c1.text_input("What the person said (trigger words can unlock extra entries, e.g. '420' unlocks IPC->BNS)",
                         ctx0, key=f"gctx_{pick}")
    gtext = c2.text_area("AI answer to check", txt0, height=170, key=f"gtext_{pick}")
    g_entries = kb.retrieve(gcat, gctx)
    rep = guard.check(gtext, kb, g_entries)
    m1, m2, m3 = st.columns(3)
    m1.metric("Section references checked", rep.refs_checked)
    m2.metric("Unverified - blocked", len(rep.violations))
    m3.metric("Verified entries allowed for this case", len(g_entries))
    if rep.ok:
        st.success("Every legal reference is backed by a verified knowledge entry - this answer would be shown as-is.")
    else:
        st.markdown("**What the guard flagged**")
        st.markdown(f"<div style='line-height:1.7'>{guard.highlight(gtext, rep)}</div>", unsafe_allow_html=True)
        for v in rep.violations:
            st.markdown(f"- `{v.kind}` **{v.text}** - {v.detail}")
        st.markdown("**What the person would see.** In the app the model is first sent this list and asked to rewrite; "
                    "this mechanical scrub is only the last resort.")
    shown, srcs = guard.render_citations(gtext if rep.ok else guard.scrub(gtext, rep), kb)
    st.markdown(f"<div style='border-left:3px solid #1f6f5c;padding:.5rem 1rem;background:#f0eee8'>{shown}</div>",
                unsafe_allow_html=True)
    for s_ in srcs:
        st.caption(f"[{s_['n']}] {s_['title']} - {s_['law']}")

# ------------------------------------------------------------------ offline: knowledge browser
with tab_kb:
    st.markdown("### Everything this assistant is allowed to say about the law")
    st.caption(f"{len(kb.entries)} hand-written entries across {len(kb.topics)} topics, citing {len(kb.acts)} registered "
               "laws. The AI only sees the entries for your case; any other law it writes is blocked.")
    for topic in kb.topics.values():
        with st.expander(f"**{topic.title}** · {len(topic.entries)} entries"):
            if topic.covers:
                st.markdown(f"**Covers:** {topic.covers}")
            if topic.not_covered:
                st.markdown(f"**Does not cover:** {topic.not_covered}")
            for e in topic.entries:
                badge = "🟢 high confidence" if e.confidence == "high" else "🟡 medium - verify"
                st.markdown(f"**{e.title}** · `{e.id}` · {badge}  \n_{e.cite_line(kb.acts)}_  \n{e.plain.strip()}")
    st.markdown("#### Registered laws (the only statutes it may name)")
    st.dataframe([{"Law": a["name"], "Status": a.get("status", "").replace("_", " "), "Note": a.get("note", ""),
                   "Link": a.get("url", "")} for a in kb.acts.values()],
                 column_config={"Link": st.column_config.LinkColumn()}, hide_index=True, width="stretch")

# ------------------------------------------------------------------ transparency (works with or without a model)
with tab_trust:
    st.markdown("""**How every answer is checked**
1. Your story is turned into a structured case file (AI).
2. Deadlines, forum, fees and danger signs are calculated by **code**, not AI.
3. Only entries from a **hand-checked list of Indian laws** are given to the AI.
4. A **citation guard** scans the answer: any Act, section or court case not in that list is sent back to be fixed, and removed if it is still there.""")
    res = st.session_state.get("last")
    if res:
        g = res.guard_log
        c1, c2, c3 = st.columns(3)
        c1.metric("Legal references checked", g["first_pass"]["refs_checked"])
        c2.metric("Caught on first draft", len(g["first_pass"]["violations"]))
        c3.metric("Unverified refs shown to you", g["final_violations"])
        if g["first_pass"]["violations"]:
            st.json(g["first_pass"]["violations"])
        st.caption("Knowledge entries given to the AI: " + ", ".join(res.kb_ids))
    if llm:
        st.caption("Model usage this session:")
        st.json(llm.usage_summary())

# ------------------------------------------------------------------ everything below needs a model
if not llm:
    for t in (tab_talk, tab_case, tab_docs, tab_spar, tab_notice):
        with t:
            setup_notice()
    st.stop()

if "session" not in st.session_state:
    st.session_state.session = Session(llm=llm)
    st.session_state.chat = []  # [{"role","content","sources","escalations"}]
sess: Session = st.session_state.session
sess.language_override = lang_choice


# ------------------------------------------------------------------ talk
with tab_talk:
    if not st.session_state.chat:
        st.markdown("### Tell me what happened, in your own words and language.")
        st.caption("Type or speak. Hindi, English, Hinglish, Tamil, Bengali, Marathi... all fine. Examples:")
        cols = st.columns(3)
        for c, ex in zip(cols, EXAMPLES):
            if c.button(ex[:70] + "...", width="stretch"):
                handle(ex)
                st.rerun()
    for i, m in enumerate(st.session_state.chat):
        with st.chat_message(m["role"], avatar="🧑" if m["role"] == "user" else "⚖️"):
            if m.get("escalations"):
                show_escalations([e for e in m["escalations"] if e["level"] in ("refuse", "emergency", "lawyer_now")])
            st.markdown(m["content"], unsafe_allow_html=True)
            if m["role"] == "assistant":
                show_sources(m.get("sources"))
                if st.button("🔊 Listen", key=f"tts{i}"):
                    audio = voice.speak(m["content"], m.get("lang", "en"))
                    if audio:
                        st.audio(audio, format="audio/mp3")
                    else:
                        st.caption("Voice playback unavailable right now.")

    if voice.stt_available():
        audio_in = st.audio_input("🎙️ Or speak (any Indian language)")
        if audio_in is not None and st.session_state.get("last_audio") != audio_in.file_id:
            st.session_state.last_audio = audio_in.file_id
            with st.spinner("Listening..."):
                try:
                    text = voice.transcribe(audio_in.getvalue(), "speech.wav")
                except Exception as e:  # noqa: BLE001
                    st.error(f"Could not transcribe: {e}")
                    text = ""
            if text:
                handle(text)
                st.rerun()
    else:
        st.caption("🎙️ Voice input turns on when GROQ_API_KEY (free) is set.")
    if prompt := st.chat_input("Describe your problem..."):
        handle(prompt)
        st.rerun()

# ------------------------------------------------------------------ case file
with tab_case:
    res = st.session_state.get("last")
    if not res:
        st.info("Your case file builds itself as you talk.")
    else:
        c, r = res.case, res.rules
        st.subheader(f"Case: {c.get('sub_type') or c.get('category')}")
        st.write(c.get("summary", ""))
        a, b, d = st.columns(3)
        a.metric("Problem type", c.get("category", "-").title())
        amt = (c.get("amounts") or {}).get("disputed")
        b.metric("Amount involved", f"₹{rules.num(amt):,.0f}" if rules.num(amt) else "unknown")
        d.metric("Language", c.get("language_name", "-"))
        show_escalations(r["escalations"])
        st.markdown("#### ⏰ Deadlines (calculated by code, not AI)")
        if r["deadlines"]:
            for dl in r["deadlines"]:
                icon = {"passed": "🔴", "urgent": "🟠", "ok": "🟢"}[dl["status"]]
                st.markdown(f"{icon} **{dl['label']}**: {dl['date']} ({dl['days_left']} days left) - _{dl['basis']}_")
        else:
            st.caption("Tell me the key dates (when it happened / when you moved out / last working day) to calculate deadlines.")
        if r.get("forum"):
            st.markdown(f"**Where to file:** {r['forum']['forum']}" +
                        (f" · **Fee:** ₹{r['fee']['fee_inr']}" if r.get("fee") and r["fee"]["fee_inr"] is not None else ""))
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 📜 What happened")
            for t in c.get("timeline", []):
                st.markdown(f"- **{t.get('date') or '?'}** - {t.get('event')}")
        with col2:
            if r.get("evidence"):
                st.markdown("#### 🧾 Your proof")
                for h in r["evidence"]["have"]:
                    st.markdown(f"✅ {h}")
                for m in r["evidence"]["missing"]:
                    st.markdown(f"⬜ {m}")
        if r.get("ladder"):
            st.markdown("#### 🪜 Usual path (cheapest first)")
            for i, step in enumerate(r["ladder"], 1):
                st.markdown(f"{i}. {step}")
        if c.get("open_questions"):
            st.markdown("#### ❓ Still needed")
            for q in c["open_questions"]:
                st.markdown(f"- {q}")
        st.download_button("⬇️ Download case file (JSON)", json.dumps({"case": c, "computed": r}, ensure_ascii=False, indent=2),
                           "case_file.json", "application/json")

# ------------------------------------------------------------------ documents
with tab_docs:
    res = st.session_state.get("last")
    docs = drafter.available(res.case.get("category")) if res else {}
    if not res:
        st.info("Describe your problem in the Talk tab first; I'll prepare documents from your case file.")
    elif not docs:
        st.info("I don't draft documents for this kind of problem - for notices you received, a reply is best prepared with a lawyer.")
    else:
        dtype = st.selectbox("Document", list(docs), format_func=lambda k: docs[k])
        name = st.text_input("Your full name (as it should appear)", "")
        if st.button("✍️ Prepare draft", type="primary"):
            with st.spinner("Drafting..."):
                st.session_state.draft = drafter.draft(llm, res.case, dtype, sender_name=name)
        dr = st.session_state.get("draft")
        if dr:
            st.warning(dr["disclaimer"])
            if dr["placeholders"]:
                st.caption("Fill these before sending: " + ", ".join(dr["placeholders"]))
            st.markdown(dr["markdown"])
            c1, c2 = st.columns(2)
            c1.download_button("⬇️ Word (.docx)", drafter.to_docx(dr["markdown"]), f"{dr['doc_type']}.docx",
                               "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            c2.download_button("⬇️ Text (.md)", dr["markdown"], f"{dr['doc_type']}.md")

# ------------------------------------------------------------------ practice
with tab_spar:
    res = st.session_state.get("last")
    if not res or res.case.get("category") == "other":
        st.info("Describe your problem first; then you can practise talking to the other side.")
    else:
        if "spar" not in st.session_state:
            st.session_state.spar = Sparring(llm, res.case)
        sp: Sparring = st.session_state.spar
        st.markdown(f"Practise asking **{sp.role}** for what you're owed. I'll play them - realistically difficult. "
                    "When done, ask for feedback.")
        for m in sp.transcript:
            with st.chat_message("user" if m["role"] == "user" else "assistant", avatar="🧑" if m["role"] == "user" else "🎭"):
                st.markdown(m["content"])
        line = st.text_input("What do you say?", key=f"spar_in_{len(sp.transcript)}")
        c1, c2 = st.columns(2)
        if c1.button("Say it", disabled=not line):
            with st.spinner("..."):
                sp.say(line)
            st.rerun()
        if c2.button("🎯 Get feedback", disabled=len(sp.transcript) < 2):
            with st.spinner("Coaching..."):
                text, _ = sp.coach()
            st.markdown(text.replace("[K:", "[source: "), unsafe_allow_html=True)

# ------------------------------------------------------------------ notice
with tab_notice:
    st.markdown("### Got a notice? Paste it or upload it - I'll explain it in plain words.")
    up = st.file_uploader("Upload (.txt or .pdf with selectable text)", type=["txt", "pdf"])
    txt = st.text_area("...or paste the notice text", height=200)
    c1, c2 = st.columns(2)
    received = c1.date_input("When did you receive it?", dt.date.today())
    nlang = c2.selectbox("Explain in", [k for k in LANG_OVERRIDES if k != "auto"], index=1)
    if st.button("📖 Explain this notice", type="primary", disabled=not (txt or up)):
        doc = read_document(up.getvalue(), up.name) if up else txt
        with st.spinner("Reading the notice..."):
            st.session_state.notice_result = explain(llm, doc, LANG_OVERRIDES[nlang], received_on=received)
    nr = st.session_state.get("notice_result")
    if nr:
        show_escalations(nr["rules"]["escalations"])
        for dl in nr["rules"]["deadlines"]:
            st.markdown(f"⏰ **{dl['label']}**: {dl['date']} ({dl['days_left']} days left)")
        st.markdown(nr["reply_rendered"], unsafe_allow_html=True)
        show_sources(nr["sources"])
