"""Voice in and out, using only free options.

- Speech-to-text: Whisper via Groq's free API (or OpenAI). Whisper handles Hindi, Tamil, Bengali,
  Marathi, Telugu, etc. and code-mixed speech reasonably well.
- Text-to-speech: gTTS (free) so people who find reading hard can listen to the answer.
"""
from __future__ import annotations

import io
import re

from .config import stt_settings

GTTS_LANGS = {"en", "hi", "ta", "bn", "mr", "te", "kn", "gu", "ml", "pa", "ur"}


def stt_available() -> bool:
    return stt_settings() is not None


def transcribe(audio: bytes, filename: str = "speech.wav") -> str:
    s = stt_settings()
    if not s:
        raise RuntimeError("Voice input needs GROQ_API_KEY (free) or OPENAI_API_KEY for Whisper.")
    from openai import OpenAI

    client = OpenAI(api_key=s["api_key"], base_url=s["base_url"])
    r = client.audio.transcriptions.create(model=s["model"], file=(filename, audio))
    return r.text.strip()


def speak(markdown_text: str, lang: str = "en") -> bytes | None:
    from gtts import gTTS

    lang = "hi" if lang == "hinglish" else lang
    if lang not in GTTS_LANGS:
        lang = "en"
    plain = re.sub(r"<[^>]+>|\[K:[^\]]+\]|[*#>`_]", "", markdown_text)
    plain = re.sub(r"\s+", " ", plain).strip()[:3000]
    try:
        buf = io.BytesIO()
        gTTS(plain, lang=lang).write_to_fp(buf)
        return buf.getvalue()
    except Exception:  # network failure etc. - voice output is optional
        return None
