"""One small interface over many model providers.

Every other module calls `LLM.chat()` or `LLM.json()` and never imports a provider SDK, so
swapping the model is a config change (see config.py). Each call is recorded in `self.calls`
(latency, token usage) so we can estimate cost per conversation.
"""
from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass, field

from .config import LLMSettings, llm_settings


class LLMError(RuntimeError):
    pass


@dataclass
class CallRecord:
    purpose: str
    model: str
    seconds: float
    input_tokens: int | None = None
    output_tokens: int | None = None
    error: str | None = None


@dataclass
class LLM:
    settings: LLMSettings = field(default_factory=llm_settings)
    calls: list[CallRecord] = field(default_factory=list)

    def __post_init__(self):
        s = self.settings
        if not s.api_key:
            raise LLMError(
                f"No API key for provider '{s.provider}'. Set it in .env (see .env.example), e.g. "
                f"GEMINI_API_KEY=... (free at aistudio.google.com) or GROQ_API_KEY=... (free at console.groq.com)."
            )
        if s.provider == "anthropic":
            import anthropic

            self._client = anthropic.Anthropic(api_key=s.api_key, max_retries=4)
        else:
            from openai import OpenAI

            self._client = OpenAI(api_key=s.api_key, base_url=s.base_url, max_retries=4, timeout=120)

    @property
    def label(self) -> str:
        return self.settings.label

    # ------------------------------------------------------------------ public API
    def chat(self, system: str, messages: list[dict], *, purpose: str = "chat", json_mode: bool = False,
             temperature: float = 0.2, max_tokens: int = 4096) -> str:
        """messages: [{"role": "user"|"assistant", "content": str}, ...]"""
        last_err: Exception | None = None
        for attempt in range(4):  # extra patience for free-tier rate limits
            t0 = time.time()
            try:
                if self.settings.provider == "anthropic":
                    text, usage = self._anthropic(system, messages, max_tokens)
                else:
                    text, usage = self._openai_compat(system, messages, json_mode, temperature, max_tokens)
                self.calls.append(CallRecord(purpose, self.label, round(time.time() - t0, 2), *usage))
                return text
            except Exception as e:  # noqa: BLE001 - we classify below
                last_err = e
                self.calls.append(CallRecord(purpose, self.label, round(time.time() - t0, 2), error=str(e)[:300]))
                msg = str(e).lower()
                if "429" in msg or "rate" in msg or "quota" in msg or "resource_exhausted" in msg or "503" in msg or "overloaded" in msg:
                    time.sleep(15 * (attempt + 1))
                    continue
                raise LLMError(f"{self.label} failed: {e}") from e
        raise LLMError(f"{self.label} failed after retries: {last_err}")

    def json(self, system: str, messages: list[dict], *, purpose: str = "json", max_tokens: int = 4096) -> dict:
        """Ask for a JSON object; tolerate code fences / chatter; one repair retry."""
        text = self.chat(system, messages, purpose=purpose, json_mode=True, temperature=0.0, max_tokens=max_tokens)
        try:
            return parse_json(text)
        except ValueError:
            repair = messages + [
                {"role": "assistant", "content": text},
                {"role": "user", "content": "That was not valid JSON. Reply again with ONLY the JSON object, nothing else."},
            ]
            return parse_json(self.chat(system, repair, purpose=purpose + ":repair", json_mode=True, temperature=0.0,
                                        max_tokens=max_tokens))

    # ------------------------------------------------------------------ providers
    def _openai_compat(self, system, messages, json_mode, temperature, max_tokens):
        kwargs = dict(
            model=self.settings.model,
            messages=[{"role": "system", "content": system}] + messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        if json_mode:
            kwargs["response_format"] = {"type": "json_object"}
        extra = dict(self.settings.extra)
        try:
            resp = self._client.chat.completions.create(**kwargs, **extra)
        except Exception as e:  # some endpoints reject optional params - retry without them
            if "429" in str(e) or "rate" in str(e).lower():
                raise
            kwargs.pop("response_format", None)
            resp = self._client.chat.completions.create(**kwargs)
        text = resp.choices[0].message.content or ""
        u = getattr(resp, "usage", None)
        return text, (getattr(u, "prompt_tokens", None), getattr(u, "completion_tokens", None))

    def _anthropic(self, system, messages, max_tokens):
        # Claude 5-family models: no temperature, adaptive thinking is on by default,
        # effort controls depth. Low effort is enough for this structured, grounded task.
        kwargs = dict(model=self.settings.model, max_tokens=max(max_tokens, 8000), system=system, messages=messages)
        try:
            resp = self._client.messages.create(**kwargs, output_config={"effort": "low"})
        except TypeError:
            resp = self._client.messages.create(**kwargs, extra_body={"output_config": {"effort": "low"}})
        if resp.stop_reason == "refusal":
            raise LLMError("Model declined this request (refusal stop reason).")
        text = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
        return text, (resp.usage.input_tokens, resp.usage.output_tokens)

    # ------------------------------------------------------------------ cost helpers
    def usage_summary(self) -> dict:
        ok = [c for c in self.calls if not c.error]
        return {
            "model": self.label,
            "calls": len(ok),
            "failed_attempts": len(self.calls) - len(ok),
            "input_tokens": sum(c.input_tokens or 0 for c in ok),
            "output_tokens": sum(c.output_tokens or 0 for c in ok),
            "seconds": round(sum(c.seconds for c in ok), 1),
        }


_FENCE = re.compile(r"^```(?:json)?\s*|\s*```$", re.MULTILINE)


def parse_json(text: str) -> dict:
    t = _FENCE.sub("", text.strip())
    try:
        return json.loads(t)
    except json.JSONDecodeError:
        start, end = t.find("{"), t.rfind("}")
        if start != -1 and end > start:
            try:
                return json.loads(t[start:end + 1])
            except json.JSONDecodeError:
                pass
    raise ValueError(f"Could not parse JSON from model output: {text[:200]}")
