"""Citation guard: the code-level answer to "LLMs invent laws, sections and cases".

The model is told to cite only the knowledge entries it was given. Prompts are not enough,
so every model output passes through `check()`:

  1. Every "Section / Sec. / s. / u/s / धारा / Rule / Order / Article N" is located. The Act it
     belongs to is found from nearby text. The (Act, section) pair must be backed by a
     knowledge entry that was retrieved for this case (or quoted in the user's own document).
  2. Any "<Something> Act, <year>" that is not in the Act registry is flagged.
  3. Anything that looks like case law ("X v. Y", "AIR 2019 SC", "(2020) 3 SCC") is flagged -
     the assistant never cites judgments.
  4. Every [K:id] tag must point to a real knowledge entry.

The caller (advisor.py) asks the model to fix its answer once using the violation list; if
violations remain, `scrub()` removes them mechanically. Either way the user never sees an
unverified legal reference, and the trace records what was caught.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from .kb import Entry, KnowledgeBase

REMOVED = "[unverified legal reference removed]"

_NUM = r"(?!(?:19|20)\d\d\b)\d{1,4}[A-Z]?(?:\s*\(\s*[0-9a-zA-Z]{1,4}\s*\))*"  # never read a year as a section
REF_RE = re.compile(
    r"(?P<kw>\bsections?\b|\bsecs?\.|(?<![A-Za-z])s\.|\bu/s\.?|धारा|\brules?\b|\barticles?\b|अनुच्छेद|\bregulations?\b)"
    r"\s*(?P<nums>" + _NUM + r"(?:\s*(?:,|and|&|/|or|और)\s*" + _NUM + r")*)",
    re.IGNORECASE,
)
ORDER_RE = re.compile(r"\b[Oo]rder\s+(?P<num>[IVXL]{2,})\b")  # CPC Orders are Roman; avoids e-commerce order IDs
NUM_SPLIT = re.compile(_NUM)
ACT_NAME_RE = re.compile(
    r"\b([A-Z][\w()&'\-]*\s+(?:(?:[A-Z(][\w()&'\-]*|of|the|and|for|on|to|in)\s+){0,8}(?:Act|Code|Rules|Sanhita))"
    r"\s*,?\s*((?:18|19|20)\d{2})\b")
_PARTY = r"(?:the\s+)?[A-Z][\w.&']*(?:\s+(?:[A-Z][\w.&']*|of|and|&|for))*"
CASE_LAW_RES = [
    # "Lucknow Development Authority v. M.K. Gupta" - swallow the whole second party name
    re.compile(r"\b[A-Z][\w.&']+(?:\s+[A-Z][\w.&']+){0,5}\s+(?:v\.|vs\.?|versus)\s+" + _PARTY, re.UNICODE),
    re.compile(r"\bAIR\s+\d{4}(?:\s+[A-Z][A-Za-z]{1,10})?(?:\s+\d+)?"),       # AIR 1994 SC 787
    re.compile(r"\(\d{4}\)\s*\d+\s*SCC(?:\s+\d+)?"),                           # (2020) 3 SCC 45
    re.compile(r"\b\d{4}\s+SCC(?:\s+OnLine\s+[A-Z]+\s+\d+)?"),
    re.compile(r"\bSCC\s+OnLine(?:\s+[A-Z]+\s+\d+)?", re.IGNORECASE),
]
TAG_RE = re.compile(r"\[K:([a-z0-9\-]+)\]")
_TAIL_RE = re.compile(
    r"\s*(?:of\s+(?:the\s+)?[\w ()&'\-]{0,70}?(?:Act|Code|Rules|Sanhita)(?:,?\s*\d{4})?"
    r"|(?:IPC|BNS|BNSS|CPC|CrPC|Cr\.P\.C\.|NI\s+Act|CPA)\b(?:,?\s*\d{4})?)")


@dataclass
class Violation:
    kind: str  # unbacked_section | unknown_act | case_law | bad_tag
    text: str
    detail: str
    span: tuple[int, int]


@dataclass
class GuardReport:
    violations: list[Violation] = field(default_factory=list)
    refs_checked: int = 0

    @property
    def ok(self) -> bool:
        return not self.violations

    def as_feedback(self) -> str:
        return "\n".join(f"- {v.kind}: '{v.text}' ({v.detail})" for v in self.violations)

    def to_dict(self) -> dict:
        return {
            "refs_checked": self.refs_checked,
            "violations": [{"kind": v.kind, "text": v.text, "detail": v.detail} for v in self.violations],
        }


def _base(sec: str) -> str:
    return re.sub(r"\s+", "", sec).split("(")[0].upper()


def _norm(sec: str) -> str:
    return re.sub(r"\s+", "", sec).upper()


def _alias_index(kb: KnowledgeBase) -> list[tuple[str, str]]:
    pairs = []
    for key, act in kb.acts.items():
        for a in [act["name"], *act.get("aliases", [])]:
            pairs.append((a.lower(), key))
    pairs.sort(key=lambda p: -len(p[0]))  # longest alias first
    return pairs


def _nearest_act(text: str, start: int, end: int, aliases: list[tuple[str, str]]) -> str | None:
    lo, hi = max(0, start - 90), min(len(text), end + 110)
    window = text[lo:hi].lower()
    best, best_dist = None, 10**9
    rel_s, rel_e = start - lo, end - lo
    for alias, key in aliases:
        for m in re.finditer(r"(?<![a-z])" + re.escape(alias) + r"(?![a-z])", window):
            # prefer an act named right after the section ("Section 69 of the CPA") or just before it
            dist = m.start() - rel_e if m.start() >= rel_e else rel_s - m.end()
            if dist < best_dist:
                best, best_dist = key, dist
    return best


def allowed_refs(entries: list[Entry]) -> dict[str, set[str]]:
    allowed: dict[str, set[str]] = {}
    for e in entries:
        for r in e.refs:
            s = allowed.setdefault(r["act"], set())
            for k in ("section", "rule", "order"):
                if r.get(k):
                    s.add(_norm(str(r[k])))
                    s.add(_base(str(r[k])))
    return allowed


def check(text: str, kb: KnowledgeBase, entries: list[Entry],
          quoted_refs: list[tuple[str | None, str]] | None = None) -> GuardReport:
    """quoted_refs: (act_key or None, section) pairs that appear in the user's own document,
    which the assistant may repeat when explaining that document."""
    rep = GuardReport()
    aliases = _alias_index(kb)
    allowed = allowed_refs(entries)
    quoted = {(a, _base(s)) for a, s in (quoted_refs or [])}
    any_section = {s for secs in allowed.values() for s in secs}

    # 1. section / rule / article references
    for m in REF_RE.finditer(text):
        kw = m.group("kw").lower()
        nums = NUM_SPLIT.findall(m.group("nums"))
        act = _nearest_act(text, m.start(), m.end(), aliases)
        for n in nums:
            rep.refs_checked += 1
            nb, nn = _base(n), _norm(n)
            if kw.startswith(("article", "अनुच्छेद")) and act is None:
                act = "CONSTITUTION"
            if (act, nb) in quoted or (None, nb) in quoted:
                continue
            if act is None:
                if nb in any_section or nn in any_section:
                    continue
                rep.violations.append(Violation("unbacked_section", m.group(0), "section not in retrieved knowledge", m.span()))
            elif nn not in allowed.get(act, set()) and nb not in allowed.get(act, set()):
                name = kb.acts.get(act, {}).get("name", act)
                rep.violations.append(Violation("unbacked_section", m.group(0), f"{name} {n} is not backed by a retrieved knowledge entry", m.span()))
    for m in ORDER_RE.finditer(text):
        rep.refs_checked += 1
        if _norm(m.group("num")) not in allowed.get("CPC1908", set()):
            rep.violations.append(Violation("unbacked_section", m.group(0), "CPC order not in retrieved knowledge", m.span()))

    # 2. statute names not in the registry
    known = [a for a, _ in aliases]
    for m in ACT_NAME_RE.finditer(text):
        name = m.group(1).strip().lower()
        if not any(k in name or name.endswith(k) for k in known if len(k) > 3):
            rep.violations.append(Violation("unknown_act", m.group(0), "statute not in the verified registry", m.span()))

    # 3. case law
    for rx in CASE_LAW_RES:
        for m in rx.finditer(text):
            rep.violations.append(Violation("case_law", m.group(0), "judgments are never cited", m.span()))

    # 4. knowledge tags
    valid = set(kb.entries)
    for m in TAG_RE.finditer(text):
        if m.group(1) not in valid:
            rep.violations.append(Violation("bad_tag", m.group(0), "no such knowledge entry", m.span()))
    return rep


def scrub(text: str, report: GuardReport) -> str:
    """Mechanically remove whatever the guard flagged (used only if the model's own fix failed)."""
    merged: list[list[int]] = []
    for st, en in sorted({v.span for v in report.violations if v.kind != "bad_tag"}):
        if merged and st <= merged[-1][1] + 2:          # overlapping or adjacent ("X v. Y, AIR ...")
            merged[-1][1] = max(merged[-1][1], en)
        else:
            merged.append([st, en])
    for st, en in reversed(merged):
        # widen to swallow a trailing "of the X Act, 2019" or an abbreviation like "IPC"
        tail = _TAIL_RE.match(text[en:])
        if tail:
            en += tail.end()
        text = text[:st] + REMOVED + text[en:]
    for v in report.violations:
        if v.kind == "bad_tag":
            text = text.replace(v.text, "")
    return text


def render_citations(text: str, kb: KnowledgeBase) -> tuple[str, list[dict]]:
    """Turn [K:id] tags into numbered footnotes and return the source list for display."""
    order: list[str] = []
    entries = kb.entries

    def sub(m):
        kid = m.group(1)
        if kid not in entries:
            return ""
        if kid not in order:
            order.append(kid)
        return f"<sup>[{order.index(kid) + 1}]</sup>"

    out = TAG_RE.sub(sub, text)
    sources = []
    for i, kid in enumerate(order, 1):
        e = entries[kid]
        urls = [kb.acts[r["act"]].get("url") for r in e.refs if kb.acts.get(r["act"], {}).get("url")]
        sources.append({"n": i, "id": kid, "title": e.title, "law": e.cite_line(kb.acts),
                        "confidence": e.confidence, "url": urls[0] if urls else None})
    return out, sources


def highlight(text: str, report: GuardReport) -> str:
    """HTML with each flagged span struck through in red (used by the 'Try to fool it' demo)."""
    import html

    spans = sorted({v.span for v in report.violations if v.kind != "bad_tag"})
    merged: list[list[int]] = []
    for s, e in spans:
        if merged and s <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    out, pos = [], 0
    for s, e in merged:
        out.append(html.escape(text[pos:s]))
        out.append("<span style='background:#fde2e1;color:#a4161a;text-decoration:line-through'>"
                   f"{html.escape(text[s:e])}</span>")
        pos = e
    out.append(html.escape(text[pos:]))
    return "".join(out).replace("\n", "<br>")
