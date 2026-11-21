"""Runtime configuration. Everything model-related is driven by environment variables so
the model can be swapped without touching code:

    LLM_PROVIDER = gemini | groq | openrouter | ollama | openai | anthropic | custom
    LLM_MODEL    = model id for that provider (optional - each provider has a default)
    LLM_API_KEY  = key (optional if the provider-specific variable below is set)
    LLM_BASE_URL = only for `custom` (any OpenAI-compatible endpoint, e.g. vLLM, LM Studio)

Streamlit Cloud users can put the same keys in st.secrets; app.py copies them into env.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
except Exception:  # dotenv is optional
    pass

ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = ROOT / "knowledge"
PROMPTS_DIR = Path(__file__).resolve().parent / "prompts"

# Provider presets. All except `anthropic` speak the OpenAI chat-completions protocol.
PRESETS: dict[str, dict] = {
    "gemini": {
        "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/",
        "key_env": "GEMINI_API_KEY",
        "default_model": "gemini-3.5-flash",
        "extra": {"reasoning_effort": "low"},
        "free_tier": True,
    },
    "groq": {
        "base_url": "https://api.groq.com/openai/v1",
        "key_env": "GROQ_API_KEY",
        "default_model": "openai/gpt-oss-120b",
        "extra": {},
        "free_tier": True,
    },
    "openrouter": {
        "base_url": "https://openrouter.ai/api/v1",
        "key_env": "OPENROUTER_API_KEY",
        "default_model": "meta-llama/llama-3.3-70b-instruct:free",
        "extra": {},
        "free_tier": True,
    },
    "ollama": {
        "base_url": "http://localhost:11434/v1",
        "key_env": "OLLAMA_API_KEY",
        "default_model": "qwen2.5:7b",
        "extra": {},
        "free_tier": True,
    },
    "openai": {
        "base_url": None,
        "key_env": "OPENAI_API_KEY",
        "default_model": "gpt-4o-mini",
        "extra": {},
        "free_tier": False,
    },
    "anthropic": {
        "base_url": None,
        "key_env": "ANTHROPIC_API_KEY",
        "default_model": "claude-opus-5-5",
        "extra": {},
        "free_tier": False,
    },
    "custom": {
        "base_url": None,
        "key_env": "LLM_API_KEY",
        "default_model": "",
        "extra": {},
        "free_tier": False,
    },
}


@dataclass
class LLMSettings:
    provider: str
    model: str
    api_key: str | None
    base_url: str | None
    extra: dict = field(default_factory=dict)

    @property
    def label(self) -> str:
        return f"{self.provider}:{self.model}"


def auto_provider() -> str:
    """Pick a provider: explicit LLM_PROVIDER wins, else the first one whose key is present."""
    explicit = os.getenv("LLM_PROVIDER")
    if explicit:
        return explicit.strip().lower()
    # Groq first: its free tier (~200k tokens/day) outlasts Gemini Flash's 20 requests/day by far.
    for name in ("groq", "gemini", "anthropic", "openai", "openrouter"):
        if os.getenv(PRESETS[name]["key_env"]):
            return name
    return "gemini"


def provider_for_model(model: str | None) -> str | None:
    """Infer the provider from an unambiguous model name, so `--model gemini-3.5-flash-lite` alone just works."""
    m = (model or os.getenv("LLM_MODEL") or "").lower()
    if not m or os.getenv("LLM_PROVIDER"):
        return None
    if m.startswith("gemini"):
        return "gemini"
    if m.startswith("claude"):
        return "anthropic"
    if m.startswith(("openai/gpt-oss", "qwen/", "meta-llama/llama-4", "whisper")):
        return "groq"
    return None


def llm_settings(provider: str | None = None, model: str | None = None) -> LLMSettings:
    provider = (provider or provider_for_model(model) or auto_provider()).lower()
    if provider not in PRESETS:
        raise ValueError(f"Unknown LLM_PROVIDER '{provider}'. Choose one of {list(PRESETS)}")
    p = PRESETS[provider]
    model = model or os.getenv("LLM_MODEL") or p["default_model"]
    api_key = os.getenv("LLM_API_KEY") or os.getenv(p["key_env"])
    if provider == "ollama":
        api_key = api_key or "ollama"
    base_url = os.getenv("LLM_BASE_URL") or p["base_url"]
    return LLMSettings(provider=provider, model=model, api_key=api_key, base_url=base_url, extra=dict(p["extra"]))


def fallback_settings(primary: LLMSettings) -> list[LLMSettings]:
    """Providers to try if the primary runs out of quota.

    LLM_FALLBACK="groq:openai/gpt-oss-20b,gemini:gemini-3.5-flash-lite" sets the chain explicitly; otherwise every
    other provider whose key is present is used with its default model, plus the cheap Gemini model.
    """
    chain: list[tuple[str, str | None]] = []
    explicit = os.getenv("LLM_FALLBACK", "").strip()
    if explicit:
        for item in explicit.split(","):
            prov, _, model = item.strip().partition(":")
            chain.append((prov.strip().lower(), model.strip() or None))
    else:
        for name in ("groq", "gemini", "anthropic", "openai", "openrouter"):
            if os.getenv(PRESETS[name]["key_env"]):
                chain.append((name, None))
        if os.getenv("GEMINI_API_KEY"):
            chain.append(("gemini", "gemini-3.5-flash-lite"))
    out, seen = [], {primary.label}
    for prov, model in chain:
        if prov not in PRESETS:
            continue
        p = PRESETS[prov]
        s = LLMSettings(prov, model or p["default_model"], os.getenv(p["key_env"]), p["base_url"], dict(p["extra"]))
        if s.api_key and s.label not in seen:
            seen.add(s.label)
            out.append(s)
    return out


# Speech-to-text: Groq's free Whisper endpoint if a Groq key exists, else OpenAI Whisper.
def stt_settings() -> dict | None:
    if os.getenv("GROQ_API_KEY"):
        return {"base_url": PRESETS["groq"]["base_url"], "api_key": os.getenv("GROQ_API_KEY"), "model": "whisper-large-v3-turbo"}
    if os.getenv("OPENAI_API_KEY"):
        return {"base_url": None, "api_key": os.getenv("OPENAI_API_KEY"), "model": "whisper-1"}
    return None
