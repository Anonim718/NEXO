from software.sim.controller import SimulatedController


def test_simulator_movement_and_status():
    controller = SimulatedController(distance_cm=100, battery_percent=87)
    assert controller.command("FORWARD") == "OK=FORWARD"
    assert controller.command("STATUS") == "OK=STATUS STATE=FORWARD DIST_CM=100 BATTERY=87"
    assert controller.history == ["FORWARD", "STATUS"]


def test_simulator_enforces_obstacle_stop():
    controller = SimulatedController(distance_cm=15)
    assert controller.command("FORWARD") == "SAFETY=OBSTACLE_STOP DIST_CM=15"
    assert controller.state == "STOP"
