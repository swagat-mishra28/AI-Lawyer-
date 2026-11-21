"""Practice mode: the model plays the other side so the person can rehearse, then coaches them."""
from __future__ import annotations

from dataclasses import dataclass, field

from . import prompts
from .assistant import grounded_generate, script_hint
from .kb import load_kb
from .llm import LLM

PERSONAS = {
    "deposit": ("the landlord", "the flat needs painting, deep cleaning, 'you broke something', 'I will pay next month', 'the agreement was never registered'"),
    "consumer": ("a customer-care executive of the company", "'refund is under process', 'policy does not allow', 'raise a new ticket', 'seller's responsibility, not ours'"),
    "wages": ("the HR manager / employer", "'company has cash-flow issues', 'you did not serve notice period', 'full and final takes 90 days', 'you left without handover'"),
    "notice": ("the lawyer who sent the notice", "'pay now or face court', 'my client has all documents', 'no time extension'"),
}


@dataclass
class Sparring:
    llm: LLM
    case: dict
    transcript: list[dict] = field(default_factory=list)

    @property
    def role(self) -> str:
        return PERSONAS.get(self.case.get("category"), ("the other party", "delays and excuses"))[0]

    def _lang(self):
        return self.case.get("language_name", "English") + script_hint(self.case.get("language", "en"))

    def say(self, user_line: str) -> str:
        role, excuses = PERSONAS.get(self.case.get("category"), ("the other party", "delays and excuses"))
        system = prompts.OPPONENT.format(role=role, summary=self.case.get("summary", ""), excuses=excuses,
                                         language_name=self._lang())
        # from the model's point of view the person is the "user" and it is the opponent
        self.transcript.append({"role": "user", "content": user_line})
        reply = self.llm.chat(system, self.transcript[-12:], purpose="spar", temperature=0.7, max_tokens=400)
        self.transcript.append({"role": "assistant", "content": reply})
        return reply

    def coach(self) -> tuple[str, dict]:
        kb = load_kb()
        entries = kb.retrieve(self.case.get("category", "other"))
        convo = "\n".join(f"{'YOU' if m['role'] == 'user' else self.role.upper()}: {m['content']}" for m in self.transcript)
        system = prompts.COACH.format(role=self.role, language_name=self._lang(),
                                      knowledge=kb.format_for_prompt(entries), transcript=convo)
        return grounded_generate(self.llm, system, [{"role": "user", "content": "Give me feedback."}], kb, entries,
                                 purpose="coach", max_tokens=1500)
