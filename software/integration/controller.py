"""Deterministic Brain -> Planner -> Bridge controller orchestration."""
from software.brain.brain import Intent, NexoBrain
from software.planner.planner import Goal, NexoPlanner

_INTENT_TO_GOAL = {
    Intent.FORWARD: Goal.MOVE_FORWARD,
    Intent.BACK: Goal.MOVE_BACK,
    Intent.LEFT: Goal.TURN_LEFT,
    Intent.RIGHT: Goal.TURN_RIGHT,
    Intent.STOP: Goal.STOP,
}

class NexoController:
    def __init__(self, brain=None, planner=None, bridge=None):
        self.brain = brain or NexoBrain()
        self.planner = planner or NexoPlanner()
        self.bridge = bridge

    def prepare(self, intent: Intent, duration_ms: int = 500):
        decision = self.brain.apply(intent)
        if decision.command in {"STOP", "PING", "STATUS"}:
            return decision, []
        goal = _INTENT_TO_GOAL[intent]
        return decision, self.planner.plan(goal, duration_ms)

    def execute(self, intent: Intent, duration_ms: int = 500):
        decision, steps = self.prepare(intent, duration_ms)
        if self.bridge is None:
            return decision, steps, []
        responses = []
        for step in steps:
            responses.append(self.bridge.send_command(step.action.value))
        return decision, steps, responses
