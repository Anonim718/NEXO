# NEXO Arduino Controller

This directory contains the low-level firmware that sits between NEXO's brain and the physical hardware.

## Responsibilities

- Motor control
- Distance sensing
- Physical safety checks
- Command timeout
- Serial communication
- Future actuator limits

## Files

- `nexo_core.ino` — main controller loop
- `config.h` — hardware and timing configuration
- `commands.h/.cpp` — command parsing and command names

## Current commands

| Command | Action |
|---|---|
| STOP | Stop both motors |
| FORWARD | Drive forward |
| BACK | Drive backward |
| LEFT | Turn left |
| RIGHT | Turn right |
| STATUS | Report state and distance |

## Safety

The controller can stop movement independently of the computer or AI layer.

Current automatic stops:

- obstacle detected while moving forward
- command timeout
- explicit STOP

## Hardware warning

The current motor code uses a **generic H-bridge pin interface**.

It is **not an Adafruit Motor Shield driver**. If the final build uses an Adafruit Motor Shield, its specific library/API should be implemented as a separate motor-controller layer rather than changing the brain protocol.

Test with the wheels lifted before allowing the robot to move on the floor.
