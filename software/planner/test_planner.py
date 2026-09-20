from software.planner.planner import Action, Goal, NexoPlanner

def test_forward_goal_creates_bounded_step():
    step = NexoPlanner().plan(Goal.MOVE_FORWARD, 500)[0]
    assert step.action is Action.FORWARD
    assert step.duration_ms == 500

def test_duration_is_bounded():
    step = NexoPlanner().plan(Goal.MOVE_FORWARD, 5000)[0]
    assert step.duration_ms == 1000

def test_stop_is_immediate():
    step = NexoPlanner().plan(Goal.STOP)[0]
    assert step.action is Action.STOP
    assert step.duration_ms == 1

def test_turn_goal_maps_to_controller_action():
    step = NexoPlanner().plan(Goal.TURN_RIGHT, 250)[0]
    assert step.action is Action.RIGHT
