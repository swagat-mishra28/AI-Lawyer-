"""Curated legal knowledge base (knowledge/*.yaml).

Retrieval is deliberately simple and deterministic: the case category selects a topic file,
plus `general` entries that are marked `always` or whose trigger words appear in the
conversation. With ~50 hand-written entries, rules beat embeddings: they are predictable,
debuggable, and never pull in an irrelevant law. (At scale - see README - this becomes a
vector index over a reviewed corpus, but the guard contract stays the same.)
"""
from __future__ import annotations

from dataclasses import dataclass, field
from functools import lru_cache

import yaml

from .config import KNOWLEDGE_DIR

TOPICS = ("consumer", "deposit", "wages", "notice")


@dataclass
class Entry:
    id: str
    topic: str
    title: str
    plain: str
    refs: list[dict] = field(default_factory=list)
    confidence: str = "high"
    triggers: list[str] = field(default_factory=list)
    always: bool = False
    notice_basis: str | None = None

    def cite_line(self, acts: dict) -> str:
        parts = []
        for r in self.refs:
            act = acts.get(r["act"], {}).get("name", r["act"])
            loc = ""
            if r.get("section"):
                loc = f" - Section {r['section']}"
            elif r.get("rule"):
                loc = f" - Rule {r['rule']}"
            elif r.get("order"):
                loc = f" - Order {r['order']}"
            parts.append(act + loc)
        return "; ".join(dict.fromkeys(parts)) or "practical guidance (no statute cited)"


@dataclass
class Topic:
    topic: str
    title: str
    covers: str = ""
    not_covered: str = ""
    checklist: list[dict] = field(default_factory=list)
    ladder: list[str] = field(default_factory=list)
    entries: list[Entry] = field(default_factory=list)


@dataclass
class KnowledgeBase:
    acts: dict
    topics: dict[str, Topic]

    @property
    def entries(self) -> dict[str, Entry]:
        return {e.id: e for t in self.topics.values() for e in t.entries}

    def retrieve(self, category: str, text: str = "") -> list[Entry]:
        """Entries for one case: the topic's entries + general/cross-topic entries triggered by words."""
        text_l = (text or "").lower()
        out: list[Entry] = []
        if category in self.topics:
            for e in self.topics[category].entries:
                if not e.triggers or _hit(e.triggers, text_l):
                    out.append(e)
        for t in self.topics.values():
            if t.topic == category:
                continue
            for e in t.entries:
                if e.always or (e.triggers and _hit(e.triggers, text_l)):
                    out.append(e)
        seen, uniq = set(), []
        for e in out:
            if e.id not in seen:
                seen.add(e.id)
                uniq.append(e)
        return uniq

    def format_for_prompt(self, entries: list[Entry]) -> str:
        lines = []
        for e in entries:
            conf = "" if e.confidence == "high" else f" (confidence: {e.confidence} - say 'generally' and suggest verifying)"
            lines.append(f"[K:{e.id}] {e.title}{conf}\n  Law: {e.cite_line(self.acts)}\n  {e.plain.strip()}")
        return "\n".join(lines)


def _hit(triggers: list[str], text_l: str) -> bool:
    return any(str(t).lower() in text_l for t in triggers)


@lru_cache(maxsize=1)
def load_kb() -> KnowledgeBase:
    acts = yaml.safe_load((KNOWLEDGE_DIR / "acts.yaml").read_text(encoding="utf-8"))
    topics: dict[str, Topic] = {}
    for name in (*TOPICS, "general"):
        raw = yaml.safe_load((KNOWLEDGE_DIR / f"{name}.yaml").read_text(encoding="utf-8"))
        entries = [Entry(topic=name, **{k: v for k, v in e.items()}) for e in raw.get("entries", [])]
        for e in entries:
            for r in e.refs:
                if r["act"] not in acts:
                    raise ValueError(f"KB entry {e.id} cites unknown act key {r['act']}")
        topics[name] = Topic(
            topic=name,
            title=raw.get("title", name),
            covers=raw.get("covers", ""),
            not_covered=raw.get("not_covered", ""),
            checklist=raw.get("checklist", []),
            ladder=raw.get("ladder", []),
            entries=entries,
        )
    return KnowledgeBase(acts=acts, topics=topics)
