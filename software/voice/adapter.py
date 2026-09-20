"""Voice input boundary for NEXO.

Speech recognition engines belong behind this interface. This keeps the rest of
NEXO independent from a particular offline or online speech-to-text provider.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class VoiceIntent:
    text: str
    intent: str
    confidence: float | None = None


class VoiceAdapter:
    def transcribe(self, audio: bytes) -> VoiceIntent:
        raise NotImplementedError(
            "Connect an offline or online speech recognizer"
        )
