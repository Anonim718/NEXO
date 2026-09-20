"""Safe software-side command orchestration for NEXO.

This layer is intentionally conservative: it validates brain decisions against
the shared software state before the serial bridge is allowed to act.

The Arduino remains the final physical safety authority.
"""

from __future__ import annotations

from ai.brain import BrainDecision, Intent
from software.core.safety import forward_allowed
from software.core.state import RobotSnapshot


def authorize(decision: BrainDecision, snapshot: RobotSnapshot) -> BrainDecision:
    """Return a safe decision or an explicit STOP decision.

    Unknown/unmapped intents are never promoted into controller commands.
    Forward is additionally blocked when the current software snapshot says it
    is unsafe. The controller must still repeat these checks independently.
    """
    if decision.command is None or decision.intent is Intent.UNKNOWN:
        return BrainDecision(
            Intent.UNKNOWN,
            None,
            "Blocked: no safe controller command",
        )

    if decision.intent is Intent.FORWARD and not forward_allowed(snapshot):
        return BrainDecision(
            Intent.STOP,
            "STOP",
            "Blocked FORWARD by software safety state",
        )

    return decision
