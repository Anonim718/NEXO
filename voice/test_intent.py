from software.brain.brain import Intent
from intent import text_to_intent

def test_portuguese_stop(): assert text_to_intent("  PARAR ") is Intent.STOP
def test_motion_phrase(): assert text_to_intent("turn left") is Intent.LEFT
def test_unknown_phrase_is_not_executed(): assert text_to_intent("do something dangerous") is None
