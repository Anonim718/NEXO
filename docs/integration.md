# NEXO Integration

## Runtime path

User input enters through voice or another interface, becomes an intent, passes through the brain allowlist, then crosses the serial bridge to the Arduino controller.

Input -> Voice/Interface -> Intent -> Brain -> Bridge -> Controller -> Hardware

### Safety boundaries

- The AI/brain layer produces only allowlisted controller commands.
- The bridge rejects commands outside its allowlist.
- The Arduino remains the final physical safety authority.
- Unknown commands never cause movement.
- The controller can stop movement on obstacle detection or command timeout.

## Test path

The simulated controller allows the software path to be exercised without motors, batteries, servos or an Arduino connected.

Intent -> Brain -> command -> SimulatedController -> ControllerResponse

## Hardware interfaces

Battery and arm APIs are deliberately hardware-independent. No ADC pin, servo pin, voltage divider or motor driver model should be committed until the physical components are selected.
