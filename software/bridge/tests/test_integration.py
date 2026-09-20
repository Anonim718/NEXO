from ai.brain import Intent, decide
from software.bridge.protocol import parse_response
from software.sim.controller import SimulatedController


def test_brain_to_simulated_controller_end_to_end():
    controller = SimulatedController(distance_cm=100)

    decision = decide(Intent.FORWARD)
    assert decision.command == "FORWARD"

    raw_response = controller.command(decision.command)
    response = parse_response(raw_response)

    assert response.category == "OK"
    assert response.value == "FORWARD"
    assert controller.state == "FORWARD"


def test_brain_never_emits_command_for_unknown_intent():
    decision = decide(Intent.UNKNOWN)
    assert decision.command is None
