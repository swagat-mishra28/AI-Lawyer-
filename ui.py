"""Look and feel for the Streamlit app: one stylesheet and small HTML helpers.

Kept separate from app.py so the app file reads as behaviour, not styling. Everything here is presentation only;
any text that comes from the model or the user is escaped before it goes into HTML.
"""
from __future__ import annotations

import html

import streamlit as st

GREEN, GREEN_DARK, INK, MUTED, PAPER, LINE = "#1f6f5c", "#155445", "#1d1d1b", "#6b6b66", "#fbfaf7", "#e6e2d8"

CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+Devanagari:wght@400;600&family=Noto+Sans+Tamil&family=Noto+Sans+Bengali&display=swap');
html, body, [class*="css"], .stMarkdown, .stChatMessage, button, input, textarea {{
  font-family: 'Inter', 'Noto Sans Devanagari', 'Noto Sans Tamil', 'Noto Sans Bengali', system-ui, sans-serif;
}}
#MainMenu, footer, [data-testid="stDecoration"] {{ visibility: hidden; height: 0; }}
.block-container {{ padding-top: 3.4rem; padding-bottom: 6rem; max-width: 1180px; }}

/* tabs as pills */
.stTabs [role="tablist"] {{ gap: .4rem; border-bottom: none; padding-bottom: .5rem; flex-wrap: wrap; }}
.stTabs button[role="tab"] {{ background: #efece4; border-radius: 999px; padding: .4rem 1rem !important; height: auto;
  border: 1px solid transparent; margin: 0; }}
.stTabs button[role="tab"]:hover {{ background: #e6f1ed; border-color: #cfe3db; }}
.stTabs button[role="tab"][aria-selected="true"] {{ background: {GREEN}; border-color: {GREEN}; }}
.stTabs button[role="tab"][aria-selected="true"] p {{ color: white !important; font-weight: 600; }}
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] {{ display: none; }}

/* hero */
.ns-hero {{ background: linear-gradient(135deg, {GREEN} 0%, #2b8a72 55%, #3c9c83 100%); color: white;
  border-radius: 18px; padding: 1.6rem 1.8rem 1.4rem; margin-bottom: 1.1rem; position: relative; overflow: hidden; }}
.ns-hero:after {{ content: "⚖"; position: absolute; right: 1.4rem; top: -.6rem; font-size: 8.5rem; opacity: .10; }}
.ns-hero h1 {{ color: white; font-size: 1.85rem; margin: 0 0 .25rem; font-weight: 700; line-height: 1.2; }}
.ns-hero p {{ color: #e8f3ef; margin: 0 0 .9rem; font-size: 1.02rem; }}
.ns-badges {{ display: flex; gap: .5rem; flex-wrap: wrap; }}
.ns-badge {{ background: rgba(255,255,255,.16); border: 1px solid rgba(255,255,255,.28); border-radius: 999px;
  padding: .28rem .75rem; font-size: .85rem; color: white; }}

/* example cards = buttons */
.st-key-examples div[data-testid="stButton"] button {{ text-align: left; }}
.st-key-examples div[data-testid="stButton"] button {{ background: white; border: 1px solid {LINE}; border-radius: 14px;
  padding: .85rem 1rem; min-height: 8.4rem; height: 100%; align-items: flex-start; justify-content: flex-start; white-space: normal;
  box-shadow: 0 1px 2px rgba(0,0,0,.03); transition: all .15s ease; }}
.st-key-examples div[data-testid="stButton"] button:hover {{ border-color: {GREEN}; box-shadow: 0 4px 14px rgba(31,111,92,.12);
  transform: translateY(-1px); }}
.st-key-examples div[data-testid="stButton"] button p {{ font-size: .9rem; line-height: 1.4; text-align: left; }}
.st-key-examples div[data-testid="stButton"] button * {{ white-space: normal !important; overflow: visible !important;
  text-overflow: clip !important; }}
.st-key-examples div[data-testid="stButton"] button > div {{ width: 100%; }}
.st-key-examples div[data-testid="stButton"] button p strong {{ display: block; font-size: .98rem; margin-bottom: .25rem; color: #1d1d1b; }}
.st-key-examples div[data-testid="stButton"] button p {{ color: #6b6b66; }}
header[data-testid="stHeader"] {{ background: transparent; }}

/* generic card */
.ns-card {{ background: white; border: 1px solid {LINE}; border-radius: 14px; padding: .9rem 1.1rem; margin-bottom: .7rem; }}
.ns-kpi {{ background: white; border: 1px solid {LINE}; border-radius: 14px; padding: .8rem 1rem; height: 100%; }}
.ns-kpi .lbl {{ color: {MUTED}; font-size: .78rem; text-transform: uppercase; letter-spacing: .04em; }}
.ns-kpi .val {{ font-size: 1.35rem; font-weight: 700; color: {INK}; margin-top: .15rem; }}
.ns-section {{ font-weight: 700; font-size: 1.02rem; margin: 1.1rem 0 .5rem; color: {INK}; }}
.ns-muted {{ color: {MUTED}; font-size: .88rem; }}

/* alerts */
.ns-alert {{ border-radius: 12px; padding: .75rem 1rem; margin: .2rem 0 .7rem; border: 1px solid; display: flex; gap: .7rem; }}
.ns-alert .ic {{ font-size: 1.25rem; line-height: 1.3; }}
.ns-alert b {{ display: block; margin-bottom: .1rem; }}
.ns-red {{ background: #fdecea; border-color: #f5c2bd; color: #7a1c13; }}
.ns-amber {{ background: #fff4e0; border-color: #f3d39b; color: #6b4300; }}
.ns-blue {{ background: #eaf2fb; border-color: #c4d9f0; color: #1d3f66; }}

/* deadlines */
.ns-dl {{ display: flex; align-items: center; gap: .9rem; background: white; border: 1px solid {LINE};
  border-radius: 14px; padding: .7rem 1rem; margin-bottom: .55rem; }}
.ns-dl .count {{ min-width: 4.6rem; text-align: center; border-radius: 10px; padding: .35rem .4rem; font-weight: 700; line-height: 1.1; }}
.ns-dl .count small {{ display: block; font-weight: 500; font-size: .7rem; }}
.ns-ok {{ background: #e3f3ec; color: {GREEN_DARK}; }} .ns-urgent {{ background: #fff0d6; color: #8a5300; }}
.ns-passed {{ background: #fde2df; color: #8f1d12; }}

/* proof + steps */
.ns-check {{ padding: .28rem 0; }}
.ns-bar {{ height: 8px; background: #ece9e1; border-radius: 99px; overflow: hidden; margin: .2rem 0 .6rem; }}
.ns-bar > div {{ height: 100%; background: {GREEN}; border-radius: 99px; }}
.ns-step {{ display: flex; gap: .7rem; align-items: flex-start; margin-bottom: .5rem; }}
.ns-step .n {{ background: {GREEN}; color: white; border-radius: 50%; width: 1.6rem; height: 1.6rem; flex: none;
  display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: .85rem; }}

/* sources and citation chips */
.stChatMessage sup, .ns-answer sup {{ background: #e3f3ec; color: {GREEN_DARK}; border-radius: 6px; padding: 0 .3rem;
  font-size: .7rem; font-weight: 600; margin-left: 1px; }}
.ns-src {{ display: flex; gap: .6rem; padding: .45rem 0; border-bottom: 1px dashed {LINE}; }}
.ns-src:last-child {{ border-bottom: none; }}
.ns-src .num {{ background: {GREEN}; color: white; border-radius: 6px; padding: 0 .4rem; height: 1.3rem; font-size: .75rem;
  font-weight: 700; flex: none; margin-top: .1rem; }}
.ns-pill {{ display: inline-block; border-radius: 999px; padding: .05rem .55rem; font-size: .72rem; font-weight: 600; margin-left: .3rem; }}
.ns-pill.high {{ background: #e3f3ec; color: {GREEN_DARK}; }} .ns-pill.medium {{ background: #fff0d6; color: #8a5300; }}

/* chat */
.stChatMessage {{ background: white; border: 1px solid {LINE}; border-radius: 16px; padding: .9rem 1rem; }}
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {{ background: #eef6f3; border-color: #d3e7df; }}

/* sidebar */
section[data-testid="stSidebar"] {{ background: #f4f2ec; border-right: 1px solid {LINE}; }}
.ns-brand {{ display: flex; align-items: center; gap: .6rem; margin-bottom: .2rem; }}
.ns-brand .logo {{ background: {GREEN}; color: white; width: 2.4rem; height: 2.4rem; border-radius: 12px;
  display: flex; align-items: center; justify-content: center; font-size: 1.3rem; }}
.ns-brand .name {{ font-weight: 700; font-size: 1.25rem; line-height: 1.1; }}
.ns-brand .sub {{ color: {MUTED}; font-size: .78rem; }}
.ns-topics {{ display: flex; flex-wrap: wrap; gap: .35rem; margin: .6rem 0 .9rem; }}
.ns-topic {{ background: white; border: 1px solid {LINE}; border-radius: 999px; padding: .2rem .6rem; font-size: .8rem; }}
.ns-help {{ display: grid; grid-template-columns: 1fr 1fr; gap: .4rem; margin: .4rem 0 .8rem; }}
.ns-help div {{ background: white; border: 1px solid {LINE}; border-radius: 10px; padding: .4rem .55rem; font-size: .74rem; color: {MUTED}; }}
.ns-help b {{ display: block; color: {INK}; font-size: 1rem; }}
.ns-status {{ display: inline-flex; align-items: center; gap: .35rem; font-size: .75rem; color: {MUTED}; }}
.ns-dot {{ width: .5rem; height: .5rem; border-radius: 50%; background: #2fb37b; display: inline-block; }}

/* guard demo */
.ns-answer {{ background: white; border: 1px solid {LINE}; border-left: 4px solid {GREEN}; border-radius: 12px;
  padding: .8rem 1rem; line-height: 1.65; }}
.ns-flagged {{ background: white; border: 1px solid #f5c2bd; border-left: 4px solid #c0392b; border-radius: 12px;
  padding: .8rem 1rem; line-height: 1.75; }}
</style>
"""

LEVELS = {
    "refuse": ("ns-red", "⛔", "I can't help with this"),
    "emergency": ("ns-red", "🚨", "Emergency"),
    "lawyer_now": ("ns-amber", "⚠️", "Talk to a lawyer now"),
    "lawyer_recommended": ("ns-blue", "👩‍⚖️", "A lawyer is recommended"),
    "legal_aid": ("ns-blue", "🤝", "Where to get help"),
}


def e(x) -> str:
    return html.escape(str(x if x is not None else ""))


def inject():
    st.markdown(CSS, unsafe_allow_html=True)


def sidebar_brand():
    st.markdown("""
<div class="ns-brand"><div class="logo">⚖️</div>
  <div><div class="name">Nyaya Saathi</div><div class="sub">न्याय साथी · your legal companion</div></div></div>
<div class="ns-muted" style="margin-top:.4rem">Free help with everyday legal problems in India, in your language.</div>
<div class="ns-topics"><span class="ns-topic">🏠 Deposit</span><span class="ns-topic">🛒 Refunds</span>
<span class="ns-topic">💼 Unpaid salary</span><span class="ns-topic">📨 Notices</span></div>""", unsafe_allow_html=True)


def sidebar_help(model_label: str | None, backups: int, switches: list[str]):
    st.markdown("""
<div class="ns-section" style="margin-top:.2rem">Helplines</div>
<div class="ns-help">
  <div><b>112</b>Emergency</div><div><b>15100</b>Free legal aid</div>
  <div><b>1930</b>Cyber fraud</div><div><b>1915</b>Consumer helpline</div>
</div>
<div class="ns-muted">⚖️ <b>I am not a lawyer.</b> I explain your options using a checked list of Indian laws and tell you
when you need a real one.</div>
<div class="ns-muted" style="margin-top:.5rem">🔒 Never share Aadhaar, OTPs or passwords. Nothing is stored after you close
this tab.</div>""", unsafe_allow_html=True)
    if model_label:
        extra = f" · {backups} backup" + ("s" if backups != 1 else "") if backups else ""
        st.markdown(f'<div class="ns-status" style="margin-top:.8rem"><span class="ns-dot"></span>{e(model_label)}{e(extra)}</div>',
                    unsafe_allow_html=True)
        if switches:
            st.caption("↪️ Switched after a quota limit: " + "; ".join(s.split(" (")[0] for s in switches))


def hero():
    st.markdown("""
<div class="ns-hero">
  <h1>Tell me what happened. I'll tell you where you stand.</h1>
  <p>Type or speak in Hindi, English, Hinglish, Tamil, Bengali, Marathi… I'll explain your rights, your deadline and your
  next step, and draft the letter for you.</p>
  <div class="ns-badges">
    <span class="ns-badge">✅ Only verified Indian laws, never invented</span>
    <span class="ns-badge">⏰ Deadlines calculated by code</span>
    <span class="ns-badge">🆓 Free · tells you when you need a lawyer</span>
  </div>
</div>""", unsafe_allow_html=True)


def alerts(escalations: list[dict], levels: tuple[str, ...] | None = None):
    for x in escalations:
        if levels and x["level"] not in levels:
            continue
        cls, icon, title = LEVELS.get(x["level"], ("ns-blue", "ℹ️", "Note"))
        st.markdown(f'<div class="ns-alert {cls}"><div class="ic">{icon}</div><div><b>{e(title)}</b>'
                    f'{e(x["reason"])} {e(x["action"])}</div></div>', unsafe_allow_html=True)


def sources(srcs: list[dict]):
    if not srcs:
        return
    with st.expander(f"📚 {len(srcs)} source{'s' if len(srcs) != 1 else ''} · every legal point is checked"):
        rows = []
        for s in srcs:
            conf = "high" if s["confidence"] == "high" else "medium"
            pill = '<span class="ns-pill high">verified</span>' if conf == "high" else \
                '<span class="ns-pill medium">general · verify</span>'
            link = f' · <a href="{e(s["url"])}" target="_blank">read the law ↗</a>' if s.get("url") else ""
            rows.append(f'<div class="ns-src"><span class="num">{s["n"]}</span><div><b>{e(s["title"])}</b>{pill}'
                        f'<div class="ns-muted">{e(s["law"])}{link}</div></div></div>')
        st.markdown("".join(rows), unsafe_allow_html=True)


def kpis(items: list[tuple[str, str]]):
    cols = st.columns(len(items))
    for c, (label, value) in zip(cols, items):
        c.markdown(f'<div class="ns-kpi"><div class="lbl">{e(label)}</div><div class="val">{e(value)}</div></div>',
                   unsafe_allow_html=True)


def deadline(d: dict):
    cls = {"ok": "ns-ok", "urgent": "ns-urgent", "passed": "ns-passed"}[d["status"]]
    left = d["days_left"]
    big = f"{left}<small>days left</small>" if left >= 0 else f"{-left}<small>days ago</small>"
    st.markdown(f'<div class="ns-dl"><div class="count {cls}">{big}</div><div><b>{e(d["label"])}</b>'
                f'<div class="ns-muted">{e(d["date"])} · {e(d["basis"])}</div></div></div>', unsafe_allow_html=True)


def proof(have: list[str], missing: list[str]):
    total = len(have) + len(missing)
    pct = int(100 * len(have) / total) if total else 0
    rows = [f'<div class="ns-muted">{len(have)} of {total} usual documents</div>',
            f'<div class="ns-bar"><div style="width:{pct}%"></div></div>']
    rows += [f'<div class="ns-check">✅ {e(h)}</div>' for h in have]
    rows += [f'<div class="ns-check" style="color:#8a8a83">⬜ {e(m)}</div>' for m in missing]
    st.markdown("".join(rows), unsafe_allow_html=True)


def steps(items: list[str]):
    st.markdown("".join(f'<div class="ns-step"><div class="n">{i}</div><div>{e(s)}</div></div>'
                        for i, s in enumerate(items, 1)), unsafe_allow_html=True)


def section(title: str):
    st.markdown(f'<div class="ns-section">{e(title)}</div>', unsafe_allow_html=True)
