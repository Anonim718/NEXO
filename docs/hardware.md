# NEXO Hardware

## Initial target

The first prototype should prioritise reliability and modularity rather than maximum complexity.

### Main components

- Arduino-compatible microcontroller
- Motor driver
- DC gear motors
- Wheels and chassis
- Servo motors for the arm
- Distance / obstacle sensors
- Microphone
- Speaker
- Battery and regulated power
- Status LEDs or display

## Design principles

- Keep high-current motor power separate from logic power where appropriate.
- Add common ground between modules that communicate electrically.
- Use connectors that make components easy to replace.
- Document every pin assignment before wiring the final prototype.
- Add physical and software safety limits to moving parts.
