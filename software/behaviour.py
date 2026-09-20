"""Deterministic personality/behaviour policy, separate from safety."""
from dataclasses import dataclass

@dataclass(frozen=True)
class BehaviourPolicy:
    acknowledgement: str = "OK"
    safe_stop_message: str = "Movement stopped for safety."
    fault_message: str = "System fault: movement locked."
    def response_for(self, command: str, reason: str) -> str:
        if command == "STOP" and reason in {"obstacle_detected","battery_low","fault_lockout"}:
            return self.safe_stop_message
        return self.acknowledgement
