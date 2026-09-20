# NEXO Firmware

## Current prototype

The first firmware lives in `software/arduino/nexo_core.ino`.

It currently provides:

- Configurable left/right motor control
- Forward and reverse movement
- Ultrasonic distance reading
- Automatic obstacle stop
- Serial diagnostics at 115200 baud
- A temporary movement test sequence

## Important

The pin mapping is a starting point, not a final wiring specification. Update the constants in the sketch after the actual motor driver and sensor wiring are selected.

The safety layer intentionally runs before movement logic. Future voice and AI commands should call a higher-level command interface rather than directly driving motor pins.

## Next firmware milestones

1. Replace the temporary movement test with a command parser.
2. Add explicit STOP, FORWARD, BACK, LEFT, and RIGHT commands.
3. Add non-blocking timing with millis().
4. Add battery monitoring.
5. Add servo/arm control.
6. Add a clean hardware abstraction layer.
