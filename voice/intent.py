"""Offline-friendly voice-to-intent boundary.

Speech recognition engines should produce text; this module maps only explicit
phrases to deterministic NEXO intents. It never executes commands itself.
"""
from software.brain.brain import Intent

_PHRASES = {
    "stop": Intent.STOP, "para": Intent.STOP, "parar": Intent.STOP,
    "forward": Intent.FORWARD, "go forward": Intent.FORWARD, "avança": Intent.FORWARD,
    "back": Intent.BACK, "go back": Intent.BACK, "recua": Intent.BACK,
    "left": Intent.LEFT, "turn left": Intent.LEFT, "vira à esquerda": Intent.LEFT,
    "right": Intent.RIGHT, "turn right": Intent.RIGHT, "vira à direita": Intent.RIGHT,
    "status": Intent.STATUS, "estado": Intent.STATUS,
    "ping": Intent.PING,
}

def text_to_intent(text: str) -> Intent | None:
    if not isinstance(text, str): return None
    return _PHRASES.get(" ".join(text.lower().strip().split()))
