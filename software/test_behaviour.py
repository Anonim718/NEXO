from software.behaviour import BehaviourPolicy

def test_safety_response_is_deterministic():
    assert "safety" in BehaviourPolicy().response_for("STOP","obstacle_detected").lower()
