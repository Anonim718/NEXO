# NEXO State Machine

Movement is an explicit controller state.

## Prototype states

- STOP
- FORWARD
- BACK
- LEFT
- RIGHT

STATUS reports the current state. PING checks communication without changing movement.

## Safety transitions

- Active movement -> STOP when command timeout expires.
- FORWARD -> STOP when the ultrasonic sensor detects an obstacle at or below the configured threshold.
- Explicit STOP -> STOP immediately.
- Unknown commands never start movement.

Higher-level AI may request an intent, but only the controller can commit a physical state change.

Future states: ARM_IDLE, ARM_MOVING, NAVIGATING, LOW_BATTERY, FAULT.
