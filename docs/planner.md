# NEXO Planner

The Planner is the layer between high-level goals and controller actions.

VOICE / AI -> INTENT -> BRAIN / SAFETY -> PLANNER -> BRIDGE -> ARDUINO

## Responsibilities

The Planner:
- converts a validated goal into a short deterministic action sequence;
- bounds action duration to prevent runaway commands;
- remains hardware-independent;
- never opens serial connections or controls motors directly.

## Safety boundary

The Planner is not a replacement for the Brain or Arduino safety logic. A planned movement still has to pass through the Brain before being sent to the controller, and the Arduino remains the final physical safety authority.

The initial implementation supports STOP, MOVE_FORWARD, MOVE_BACK, TURN_LEFT, and TURN_RIGHT, with a maximum individual action duration of 1000 ms.
