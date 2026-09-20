from software.brain.brain import Intent
from software.integration.controller import NexoController

class FakeBridge:
    def __init__(self): self.commands=[]
    def send_command(self, command):
        self.commands.append(command); return "OK="+command

def test_prepare_keeps_safety_before_planning():
    controller=NexoController()
    controller.brain.state.distance_cm=20
    decision, steps=controller.prepare(Intent.FORWARD)
    assert decision.command=="STOP"
    assert steps==[]

def test_execute_sends_planned_command_to_bridge():
    bridge=FakeBridge(); controller=NexoController(bridge=bridge)
    decision, steps, responses=controller.execute(Intent.LEFT, 250)
    assert decision.command=="LEFT"
    assert [s.action.value for s in steps]==["LEFT"]
    assert bridge.commands==["LEFT"]
    assert responses==["OK=LEFT"]
