import unittest

from software.brain.brain import Intent, NexoBrain, RobotMode


class BrainSafetyTests(unittest.TestCase):
    def test_forward_when_clear(self):
        brain = NexoBrain()
        brain.state.distance_cm = 100
        self.assertEqual(brain.apply(Intent.FORWARD).command, "FORWARD")
        self.assertEqual(brain.state.mode, RobotMode.MOVING)

    def test_forward_stops_for_obstacle(self):
        brain = NexoBrain()
        brain.state.distance_cm = 20
        decision = brain.apply(Intent.FORWARD)
        self.assertEqual(decision.command, "STOP")
        self.assertEqual(decision.reason, "obstacle_detected")

    def test_low_battery_blocks_motion(self):
        brain = NexoBrain()
        brain.state.battery_percent = 5
        decision = brain.apply(Intent.FORWARD)
        self.assertEqual(decision.command, "STOP")
        self.assertEqual(decision.reason, "battery_low")

    def test_fault_lockout(self):
        brain = NexoBrain()
        brain.set_fault("test_fault")
        self.assertEqual(brain.apply(Intent.RIGHT).command, "STOP")
        self.assertEqual(brain.state.mode, RobotMode.FAULT)

    def test_explicit_stop_always_wins(self):
        brain = NexoBrain()
        brain.state.distance_cm = 1
        self.assertEqual(brain.apply(Intent.STOP).command, "STOP")


if __name__ == "__main__":
    unittest.main()
