"""Nyaya Saathi - Streamlit app.  Run:  streamlit run app.py"""
from __future__ import annotations

import datetime as dt
import json
import os
from pathlib import Path

import streamlit as st

# Streamlit Cloud: copy secrets into env so nyaya.config sees them
try:
    for k, v in st.secrets.items():
        if isinstance(v, str):
            os.environ.setdefault(k, v)
except Exception:
    pass

import ui  # noqa: E402
from nyaya import drafter, guard, rules, voice  # noqa: E402
from nyaya.assistant import LANG_OVERRIDES, Session  # noqa: E402
from nyaya.kb import load_kb  # noqa: E402
from nyaya.llm import LLM, LLMError  # noqa: E402
from nyaya.notice import explain, read_document  # noqa: E402
from nyaya.sparring import Sparring  # noqa: E402

st.set_page_config(page_title="Nyaya Saathi · free legal help", page_icon="⚖️", layout="wide")
ui.inject()

ROOT = Path(__file__).resolve().parent
EXAMPLES = [
    ("🏠", "Deposit not returned",
     "Mere landlord ne 40,000 ka deposit wapas nahi kiya, maine 15 September ko flat khali kiya tha. Ab woh phone nahi utha raha."),
    ("🛒", "Refund never came",
     "I ordered a laptop on Flipkart for 52,000 in August, returned it as defective but the refund never came. Customer care keeps saying 'in process'."),
    ("💼", "Salary not paid",
     "मैंने अक्टूबर में नौकरी छोड़ी, कंपनी ने दो महीने की सैलरी (60,000) अभी तक नहीं दी।"),
    ("🧾", "Defective phone",
     "நான் ஜூன் மாதம் 18,000 ரூபாய்க்கு மொபைல் வாங்கினேன். ஒரு மாதத்தில் திரை வேலை செய்யவில்லை, வாரண்டியில் சரி செய்ய மறுக்கிறார்கள்."),
]
SAMPLE_NOTICES = {"Cheque-bounce notice": "samples/cheque_notice.txt", "Court summons": "samples/court_summons.txt"}


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
    for k in ("session", "chat", "spar", "last", "notice_result", "draft", "notice_text"):
        st.session_state.pop(k, None)


llm = get_llm()
kb = load_kb()

# ------------------------------------------------------------------ sidebar
with st.sidebar:
    ui.sidebar_brand()
    lang_choice = st.selectbox("Reply language", list(LANG_OVERRIDES), index=0,
                               help="'auto' replies in the language you write in")
    if st.button("🗂️ Start a new case", width="stretch"):
        new_case()
        st.rerun()
    ui.sidebar_help(llm.label if llm else None, len(llm.fallbacks) if llm else 0, llm.switches if llm else [])


def setup_notice():
    st.markdown('<div class="ns-alert ns-amber"><div class="ic">🔑</div><div><b>No language model is configured yet</b>'
                'Conversation features are off. The <b>🛡️ Why trust it</b> tab works without one.</div></div>',
                unsafe_allow_html=True)
    st.code("cp .env.example .env   # then paste a free key:\nGROQ_API_KEY=gsk_...    (console.groq.com - also voice)\n"
            "GEMINI_API_KEY=...      (aistudio.google.com)", language="bash")
    st.caption(st.session_state.get("llm_error", ""))


def handle(user_text: str):
    st.session_state.chat.append({"role": "user", "content": user_text})
    with st.spinner("Understanding your problem and checking the law…"):
        try:
            res = sess.turn(user_text)
        except LLMError as e:
            st.session_state.chat.append({"role": "assistant", "content": f"⚠️ The AI model is unavailable right now ({e}). "
                                                                          "Please try again in a minute."})
            return
    st.session_state.last = res
    st.session_state.chat.append({"role": "assistant", "content": res.reply_rendered, "sources": res.sources,
                                  "escalations": res.rules["escalations"], "lang": res.case.get("language", "en")})


tab_talk, tab_case, tab_docs, tab_spar, tab_notice, tab_trust = st.tabs(
    ["💬 Talk", "📁 My case", "📝 Documents", "🥊 Practice", "📨 Understand a notice", "🛡️ Why trust it"])

# ------------------------------------------------------------------ trust (works with or without a model)
FOOL_EXAMPLES = {
    "Invented section + fake Supreme Court case": ("consumer",
        "Under Section 12 of the Consumer Protection Act, 2019 the company must pay you double the price as penalty. "
        "In Lucknow Development Authority v. M.K. Gupta, AIR 1994 SC 787, the Supreme Court held this. "
        "You must file within 2 years [K:cpa-limitation], which Section 69 of the Consumer Protection Act allows."),
    "A law that doesn't exist": ("deposit",
        "As per the Tenant Deposit Protection Act, 2017 your landlord must return the deposit within 30 days with 18% "
        "interest. The deposit is owed under your agreement, Section 73 of the Indian Contract Act [K:deposit-contract]."),
    "Repealed IPC section": ("deposit",
        "File an FIR under Section 420 IPC - the police will recover your deposit in a week."),
    "Hindi: wrong section number": ("wages",
        "वेतन संहिता की धारा 17 के अनुसार नौकरी छोड़ने के दो कार्य दिवस में वेतन देना होता है [K:cw-timely-payment]। "
        "वेतन संहिता की धारा 99 के तहत कंपनी को दोगुना जुर्माना देना होगा।"),
    "A clean, grounded answer": ("consumer",
        "You can file a complaint within 2 years of the problem [K:cpa-limitation]. Since you paid Rs 52,000, the "
        "District Commission is the right place [K:cpa-pecuniary], and you can file online without a lawyer [K:cpa-efiling]."),
}
GUARD_CATS = ["consumer", "deposit", "wages", "notice"]

with tab_trust:
    st.markdown("### Why you can trust what it says")
    st.markdown('<div class="ns-muted">AI models confidently invent laws, sections and court cases. Here the AI only '
                '<b>explains</b>; plain code checks every legal reference before you see it.</div>', unsafe_allow_html=True)
    ui.section("How every answer is made")
    ui.steps(["Your story becomes a structured case file (AI).",
              "Deadlines, the right forum, fees and danger signs are calculated by code, not AI.",
              "Only entries from a hand-checked list of Indian laws are given to the AI.",
              "A citation guard scans the answer. Any Act, section or court case not in that list is sent back to be fixed, "
              "and removed if it is still there."])
    t_fool, t_kb, t_this = st.tabs(["🧪 Try to fool it", "📚 What I know", "🔍 This answer's check"])

    with t_fool:
        st.markdown("**Can you make it cite a law that isn't real?** Pick an example, or paste any AI-written answer. "
                    "This runs the real guard, which is plain code with no AI, so it works without an API key.")
        pick = st.radio("Example", list(FOOL_EXAMPLES), horizontal=True, label_visibility="collapsed")
        cat0, txt0 = FOOL_EXAMPLES[pick]
        c1, c2 = st.columns([1, 3])
        gcat = c1.selectbox("Case type", GUARD_CATS, index=GUARD_CATS.index(cat0), key=f"gcat_{pick}",
                            help="Decides which verified laws are allowed for this case")
        gctx = c1.text_input("What the person said", "", key=f"gctx_{pick}",
                             help="Trigger words unlock extra entries, e.g. '420' unlocks the IPC→BNS entry")
        gtext = c2.text_area("AI answer to check", txt0, height=150, key=f"gtext_{pick}")
        g_entries = kb.retrieve(gcat, gctx)
        rep = guard.check(guard.normalize_tags(gtext), kb, g_entries)
        ui.kpis([("References checked", str(rep.refs_checked)), ("Blocked as unverified", str(len(rep.violations))),
                 ("Verified entries allowed", str(len(g_entries)))])
        left, right = st.columns(2)
        with left:
            ui.section("What the AI wrote")
            if rep.ok:
                st.markdown(f'<div class="ns-answer">{ui.e(gtext)}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="ns-flagged">{guard.highlight(gtext, rep)}</div>', unsafe_allow_html=True)
                for v in rep.violations:
                    st.markdown(f'<div class="ns-muted">✗ <b>{ui.e(v.text)}</b>: {ui.e(v.detail)}</div>', unsafe_allow_html=True)
        with right:
            ui.section("What you would see")
            shown, srcs = guard.render_citations(gtext if rep.ok else guard.scrub(gtext, rep), kb)
            st.markdown(f'<div class="ns-answer">{shown}</div>', unsafe_allow_html=True)
            if rep.ok:
                st.success("Every legal reference is backed by a verified entry, so it is shown as is.")
            else:
                st.caption("In the app, the model is first asked to rewrite without these references; this mechanical "
                           "scrub is only the last resort.")
            for s_ in srcs:
                st.caption(f"[{s_['n']}] {s_['title']} - {s_['law']}")

    with t_kb:
        st.markdown(f"**{len(kb.entries)} hand-written entries** across {len(kb.topics)} topics, citing "
                    f"**{len(kb.acts)} registered laws**. The AI only sees the entries for your case, and any other law "
                    "it writes is blocked.")
        for topic in kb.topics.values():
            with st.expander(f"**{topic.title}** · {len(topic.entries)} entries"):
                if topic.covers:
                    st.markdown(f"**Covers:** {topic.covers}")
                if topic.not_covered:
                    st.markdown(f"**Does not cover:** {topic.not_covered}")
                for en in topic.entries:
                    pill = '<span class="ns-pill high">high confidence</span>' if en.confidence == "high" else \
                        '<span class="ns-pill medium">medium · verify</span>'
                    st.markdown(f'<div class="ns-card"><b>{ui.e(en.title)}</b>{pill}<div class="ns-muted">'
                                f'{ui.e(en.cite_line(kb.acts))}</div><div style="margin-top:.3rem">{ui.e(en.plain.strip())}'
                                f'</div></div>', unsafe_allow_html=True)
        ui.section("Registered laws: the only statutes it may name")
        st.dataframe([{"Law": a["name"], "Status": a.get("status", "").replace("_", " "), "Note": a.get("note", ""),
                       "Link": a.get("url", "")} for a in kb.acts.values()],
                     column_config={"Link": st.column_config.LinkColumn()}, hide_index=True, width="stretch")

    with t_this:
        res = st.session_state.get("last")
        if not res:
            st.info("Ask something in the Talk tab, and this shows how that answer was checked.")
        else:
            g = res.guard_log
            ui.kpis([("Legal references checked", str(g["first_pass"]["refs_checked"])),
                     ("Caught on first draft", str(len(g["first_pass"]["violations"]))),
                     ("Unverified refs shown to you", str(g["final_violations"]))])
            if g["first_pass"]["violations"]:
                st.json(g["first_pass"]["violations"])
            st.caption("Knowledge entries given to the AI: " + ", ".join(res.kb_ids))
        if llm:
            with st.expander("Model usage this session"):
                st.json(llm.usage_summary())

# ------------------------------------------------------------------ everything below needs a model
if not llm:
    for t in (tab_talk, tab_case, tab_docs, tab_spar, tab_notice):
        with t:
            setup_notice()
    st.stop()

if "session" not in st.session_state:
    st.session_state.session = Session(llm=llm)
    st.session_state.chat = []
sess: Session = st.session_state.session
sess.language_override = lang_choice

# ------------------------------------------------------------------ talk
with tab_talk:
    if not st.session_state.chat:
        ui.hero()
        st.markdown('<div class="ns-muted" style="margin-bottom:.4rem">Not sure how to start? Tap an example:</div>',
                    unsafe_allow_html=True)
        with st.container(key="examples"):
            cols = st.columns(len(EXAMPLES))
            for c, (icon, title, text) in zip(cols, EXAMPLES):
                short = text if len(text) <= 72 else text[:70].rstrip() + "…"
                if c.button(f"**{icon} {title}** {short}", width="stretch", key=f"ex_{title}"):
                    handle(text)
                    st.rerun()
    for i, m in enumerate(st.session_state.chat):
        with st.chat_message(m["role"], avatar="🧑" if m["role"] == "user" else "⚖️"):
            if m.get("escalations"):
                ui.alerts(m["escalations"], ("refuse", "emergency", "lawyer_now"))
            st.markdown(m["content"], unsafe_allow_html=True)
            if m["role"] == "assistant":
                ui.sources(m.get("sources"))
                if st.button("🔊 Listen", key=f"tts{i}"):
                    audio = voice.speak(m["content"], m.get("lang", "en"))
                    if audio:
                        st.audio(audio, format="audio/mp3")
                    else:
                        st.caption("Voice playback unavailable right now.")
    if st.session_state.chat and st.session_state.get("last"):
        st.markdown('<div class="ns-muted">📁 Your <b>case file</b>, 📝 <b>documents</b> and 🥊 <b>practice</b> are ready '
                    'in the tabs above. Keep talking to add details.</div>', unsafe_allow_html=True)

    if voice.stt_available():
        audio_in = st.audio_input("🎙️ Or speak, in any Indian language")
        if audio_in is not None and st.session_state.get("last_audio") != audio_in.file_id:
            st.session_state.last_audio = audio_in.file_id
            with st.spinner("Listening…"):
                try:
                    text = voice.transcribe(audio_in.getvalue(), "speech.wav")
                except Exception as e:  # noqa: BLE001
                    st.error(f"Could not transcribe: {e}")
                    text = ""
            if text:
                handle(text)
                st.rerun()
    if prompt := st.chat_input("Describe your problem in your own words…"):
        handle(prompt)
        st.rerun()

# ------------------------------------------------------------------ case file
with tab_case:
    res = st.session_state.get("last")
    if not res:
        st.info("Your case file builds itself as you talk. Start in the 💬 Talk tab.")
    else:
        c, r = res.case, res.rules
        st.markdown(f"### {ui.e((c.get('sub_type') or c.get('category') or 'Your case').capitalize())}")
        if c.get("summary"):
            st.markdown(f'<div class="ns-muted" style="margin-bottom:.7rem">{ui.e(c["summary"])}</div>', unsafe_allow_html=True)
        amt = rules.num((c.get("amounts") or {}).get("disputed"))
        forum = (r.get("forum") or {}).get("forum", "").replace(" Disputes Redressal", "") or             {"deposit": "Lok Adalat / civil court", "wages": "Labour Department", "notice": "Depends on the notice"}.get(
                c.get("category"), "-")
        ui.kpis([("Problem", (c.get("category") or "-").title()), ("Amount", f"₹{amt:,.0f}" if amt else "unknown"),
                 ("Where to file", forum), ("Language", c.get("language_name") or "-")])
        st.write("")
        ui.alerts(r["escalations"])
        ui.section("⏰ Deadlines (calculated by code, not AI)")
        if r["deadlines"]:
            for dl in r["deadlines"]:
                ui.deadline(dl)
        else:
            st.caption("Tell me the key dates (when it happened, when you moved out, your last working day) to calculate deadlines.")
        if r.get("fee") and r["fee"].get("fee_inr") is not None:
            st.caption(f"Filing fee: ₹{r['fee']['fee_inr']} ({r['fee']['note']})")
        col1, col2 = st.columns(2)
        with col1:
            ui.section("📜 What happened")
            if c.get("timeline"):
                for t in c["timeline"]:
                    st.markdown(f"- **{t.get('date') or '?'}** · {t.get('event')}")
            else:
                st.caption("No dated events yet.")
        with col2:
            if r.get("evidence"):
                ui.section("🧾 Your proof")
                ui.proof(r["evidence"]["have"], r["evidence"]["missing"])
        if r.get("ladder"):
            ui.section("🪜 Usual path, cheapest first")
            ui.steps(r["ladder"])
        if c.get("open_questions"):
            ui.section("❓ I still need to know")
            for q in c["open_questions"]:
                st.markdown(f"- {q}")
        st.download_button("⬇️ Download case file (JSON)", json.dumps({"case": c, "computed": r}, ensure_ascii=False, indent=2),
                           "case_file.json", "application/json")

# ------------------------------------------------------------------ documents
with tab_docs:
    res = st.session_state.get("last")
    docs = drafter.available(res.case.get("category")) if res else {}
    if not res:
        st.info("Describe your problem in the 💬 Talk tab first; I'll prepare documents from your case file.")
    elif not docs:
        st.info("I don't draft documents for this kind of problem. A reply to a notice you received is best prepared with a lawyer.")
    else:
        st.markdown("### Prepare a document")
        st.markdown('<div class="ns-muted">The legal wording is a fixed, checked template. The AI writes only your facts, '
                    'and anything it doesn\'t know becomes a <b>[FILL: …]</b> blank instead of a guess.</div>',
                    unsafe_allow_html=True)
        c1, c2 = st.columns([2, 2])
        dtype = c1.selectbox("Document", list(docs), format_func=lambda k: docs[k])
        name = c2.text_input("Your full name (as it should appear)", "")
        if st.button("✍️ Prepare draft", type="primary"):
            with st.spinner("Drafting…"):
                st.session_state.draft = drafter.draft(llm, res.case, dtype, sender_name=name)
        dr = st.session_state.get("draft")
        if dr:
            st.markdown(f'<div class="ns-alert ns-amber"><div class="ic">✍️</div><div>{ui.e(dr["disclaimer"])}</div></div>',
                        unsafe_allow_html=True)
            if dr["placeholders"]:
                st.caption("Fill these before sending: " + ", ".join(dr["placeholders"]))
            with st.container(border=True):
                st.markdown(dr["markdown"])
            c1, c2 = st.columns(2)
            c1.download_button("⬇️ Word (.docx)", drafter.to_docx(dr["markdown"]), f"{dr['doc_type']}.docx",
                               "application/vnd.openxmlformats-officedocument.wordprocessingml.document", width="stretch")
            c2.download_button("⬇️ Text (.md)", dr["markdown"], f"{dr['doc_type']}.md", width="stretch")

# ------------------------------------------------------------------ practice
with tab_spar:
    res = st.session_state.get("last")
    if not res or res.case.get("category") == "other":
        st.info("Describe your problem first; then you can practise talking to the other side.")
    else:
        if "spar" not in st.session_state:
            st.session_state.spar = Sparring(llm, res.case)
        sp: Sparring = st.session_state.spar
        st.markdown(f"### Practise with {sp.role}")
        st.markdown('<div class="ns-muted">I\'ll play them, realistically difficult. Stay calm, be specific (amount, date, '
                    'proof) and name your next step. Ask for feedback when you\'re done.</div>', unsafe_allow_html=True)
        for m in sp.transcript:
            with st.chat_message("user" if m["role"] == "user" else "assistant", avatar="🧑" if m["role"] == "user" else "🎭"):
                st.markdown(m["content"])
        line = st.text_input("What do you say?", key=f"spar_in_{len(sp.transcript)}",
                             placeholder="e.g. Sir, please return my 40,000 deposit. I left the flat on 15 September.")
        c1, c2, _ = st.columns([1, 1, 3])
        if c1.button("💬 Say it", disabled=not line, type="primary", width="stretch"):
            with st.spinner("…"):
                sp.say(line)
            st.rerun()
        if c2.button("🎯 Get feedback", disabled=len(sp.transcript) < 2, width="stretch"):
            with st.spinner("Coaching…"):
                text, _ = sp.coach()
            with st.container(border=True):
                rendered, _src = guard.render_citations(text, kb)
                st.markdown(rendered, unsafe_allow_html=True)

# ------------------------------------------------------------------ notice
with tab_notice:
    st.markdown("### Got a notice? I'll explain it in plain words.")
    st.markdown('<div class="ns-muted">Paste or upload it. I\'ll tell you what it is, how serious it is, and your exact '
                'deadline, and whether you need a lawyer now.</div>', unsafe_allow_html=True)
    sc = st.columns(len(SAMPLE_NOTICES) + 2)
    for col, (label, path) in zip(sc, SAMPLE_NOTICES.items()):
        if col.button(f"📄 Try: {label}", width="stretch"):
            st.session_state.notice_text = (ROOT / path).read_text(encoding="utf-8")
    up = st.file_uploader("Upload (.txt, or a .pdf with selectable text)", type=["txt", "pdf"])
    txt = st.text_area("…or paste the notice text", value=st.session_state.get("notice_text", ""), height=200)
    c1, c2 = st.columns(2)
    received = c1.date_input("When did you receive it?", dt.date.today())
    nlang = c2.selectbox("Explain in", [k for k in LANG_OVERRIDES if k != "auto"], index=1)
    if st.button("📖 Explain this notice", type="primary", disabled=not (txt or up)):
        doc = read_document(up.getvalue(), up.name) if up else txt
        with st.spinner("Reading the notice…"):
            st.session_state.notice_result = explain(llm, doc, LANG_OVERRIDES[nlang], received_on=received)
    nr = st.session_state.get("notice_result")
    if nr:
        ui.alerts(nr["rules"]["escalations"])
        for dl in nr["rules"]["deadlines"]:
            ui.deadline(dl)
        with st.container(border=True):
            st.markdown(nr["reply_rendered"], unsafe_allow_html=True)
        ui.sources(nr["sources"])
