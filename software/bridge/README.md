# NEXO Brain Bridge

This directory will contain the computer-side bridge between NEXO's higher-level software and the Arduino controller.

## Planned responsibilities

1. Receive commands from the voice/AI layer.
2. Validate and normalize commands.
3. Send commands over USB serial.
4. Read controller responses.
5. Expose robot state to higher-level software.
6. Never bypass controller-side safety logic.

## Planned stack

The first bridge implementation will be intentionally small:

- Python
- USB serial
- line-based protocol
- explicit command allow-list

The bridge should remain hardware-agnostic. Hardware-specific safety belongs in the Arduino controller.

## Example flow

```text
Voice / AI
    |
    v
Brain Bridge
    |
    | USB Serial
    v
Arduino Controller
    |
    +--> Motor driver
    +--> Distance sensors
    +--> Future arm controller
```
