# NEXO Serial Protocol

## Purpose

The USB serial link is the boundary between the NEXO brain and the low-level Arduino controller.

The controller is responsible for motors, sensors, timing and safety. A future computer/AI layer sends commands over serial, but it does not bypass the controller's safety checks.

## Connection

- USB serial
- Default baud rate: 115200
- One command per line
- Commands are ASCII text
- Replies are ASCII text

## Commands

| Command | Meaning |
|---|---|
| STOP | Stop all motors immediately |
| FORWARD | Drive forward |
| BACK | Drive backward |
| LEFT | Turn left |
| RIGHT | Turn right |
| STATUS | Return controller state |
| PING | Test that the controller is alive |

Short aliases are supported by the firmware where documented.

## Safety behaviour

The controller may stop the motors even when a movement command was received.

Examples:

- An obstacle is detected during forward movement.
- The command timeout expires.
- An explicit STOP command is received.

The brain should treat the controller as authoritative for physical safety.

## Future protocol

The protocol is intentionally simple at this stage. Future versions can add:

- speed control
- arm/servo commands
- sensor telemetry
- battery state
- sequence IDs
- acknowledgements
- structured responses

A future structured protocol may use lines such as `CMD FORWARD` and `ACK FORWARD`, but the current firmware keeps compatibility with simple human-readable commands.
