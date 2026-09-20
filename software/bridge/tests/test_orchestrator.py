from ai.brain import Intent, decide
from software.core.orchestrator import authorize
from software.core.state import RobotSnapshot, RobotState


def test_forward_is_allowed_with_clear_path():
    decision = authorize(
        decide(Intent.FORWARD),
        RobotSnapshot(RobotState.STOP, distance_cm=100, battery_percent=80),
    )

    assert decision.intent is Intent.FORWARD
    assert decision.command == "FORWARD"


def test_forward_is_blocked_by_obstacle():
    decision = authorize(
        decide(Intent.FORWARD),
        RobotSnapshot(RobotState.STOP, distance_cm=15, battery_percent=80),
    )

    assert decision.intent is Intent.STOP
    assert decision.command == "STOP"


def test_forward_is_blocked_by_low_battery():
    decision = authorize(
        decide(Intent.FORWARD),
        RobotSnapshot(RobotState.STOP, distance_cm=100, battery_percent=10),
    )

    assert decision.intent is Intent.STOP
    assert decision.command == "STOP"


def test_unknown_intent_cannot_reach_controller():
    decision = authorize(
        decide(Intent.UNKNOWN),
        RobotSnapshot(RobotState.STOP, distance_cm=100),
    )

    assert decision.intent is Intent.UNKNOWN
    assert decision.command is None


def test_fault_blocks_forward():
    decision = authorize(
        decide(Intent.FORWARD),
        RobotSnapshot(RobotState.FAULT, distance_cm=100),
    )

    assert decision.intent is Intent.STOP
    assert decision.command == "STOP"
