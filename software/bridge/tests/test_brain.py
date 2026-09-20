from ai.brain import BrainDecision, Intent, decide


def test_known_intent_is_allowlisted():
    decision = decide(Intent.FORWARD)
    assert decision == BrainDecision(
        Intent.FORWARD,
        "FORWARD",
        "Mapped to allowlisted controller command",
    )


def test_unknown_intent_cannot_reach_hardware():
    decision = decide(Intent.UNKNOWN)
    assert decision.intent is Intent.UNKNOWN
    assert decision.command is None


def test_all_controller_intents_map_to_commands():
    for intent in Intent:
        decision = decide(intent)
        if intent is Intent.UNKNOWN:
            assert decision.command is None
        else:
            assert decision.command == intent.value
