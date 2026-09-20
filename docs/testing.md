# NEXO Testing Strategy

NEXO should be tested in layers instead of debugging the entire robot at once. Humanity has suffered enough from "just plug everything in and see what happens."

## 1. Firmware tests

Before connecting motors:

- Confirm the board boots.
- Confirm `NEXO CORE ONLINE` appears at 115200 baud.
- Send `STATUS`.
- Send `PING` once implemented.
- Confirm invalid commands do not move the robot.

## 2. Sensor tests

With motors disconnected:

- Check distance readings at known distances.
- Confirm an obstacle below the configured threshold causes a forward stop.
- Confirm sensor failure does not produce an unsafe movement command.

## 3. Motor tests

Raise the robot so its wheels cannot touch the floor.

- Test STOP.
- Test FORWARD.
- Test BACK.
- Test LEFT.
- Test RIGHT.

Only after the direction logic is confirmed should the wheels touch the ground.

## 4. Bridge tests

Test the computer-to-Arduino connection without autonomous movement first.

The bridge should verify:

- serial connection
- command formatting
- responses
- timeout handling
- rejection of unsupported commands

## 5. Integration tests

Use controlled, low-speed tests in an open area.

Record:

- command sent
- controller response
- distance readings
- stop reason
- unexpected behaviour

## 6. Regression rule

A firmware change is not finished until the previously working safety behaviours still work.

## Hardware note

The current firmware uses a generic H-bridge pin model. It is **not automatically compatible with an Adafruit Motor Shield**. The shield-specific driver should be isolated behind the motor-controller layer once the exact shield revision is confirmed.
