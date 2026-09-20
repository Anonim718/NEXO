# NEXO Serial Protocol

## Purpose

The USB serial link is the boundary between the NEXO brain and the low-level Arduino controller.

The controller is responsible for motors, sensors, timing and safety. A future computer/AI layer sends commands over serial, but it does not bypass the controller's safety checks.

## Connection

- USB serial
- Default baud rate: 115200
- One command per line
- Commands are ASCII text
- Every accepted command produces one response line

## Commands

| Command | Meaning | Response |
|---|---|---|
| STOP | Stop all motors immediately | `OK=STOP` |
| FORWARD | Drive forward | `OK=FORWARD` |
| BACK | Drive backward | `OK=BACK` |
| LEFT | Turn left | `OK=LEFT` |
| RIGHT | Turn right | `OK=RIGHT` |
| STATUS | Return controller state | `OK=STATUS STATE=... DIST_CM=...` |
| PING | Test that the controller is alive | `OK=PONG` |

Short aliases are supported by the firmware where documented.

## Safety behaviour

The controller may stop the motors even when a movement command was received.

Examples:

- An obstacle is detected during forward movement.
- The command timeout expires.
- An explicit STOP command is received.

Safety events are reported as a single line such as:

`SAFETY=OBSTACLE_STOP`

The brain should treat the controller as authoritative for physical safety.

## Timeout rule

Movement commands refresh the command timeout.

`STATUS` and `PING` do **not** refresh the movement timeout. This prevents repeated monitoring requests from accidentally keeping the robot moving indefinitely.

## Future protocol

The protocol is intentionally simple at this stage. Future versions can add:

- speed control
- arm/servo commands
- sensor telemetry
- battery state
- sequence IDs
- structured error codes

A future structured protocol may use explicit command and acknowledgement frames, but the current line-based format is deliberately easy to debug from a serial terminal.
