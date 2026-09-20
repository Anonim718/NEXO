# NEXO Computer Bridge

The bridge is the controlled boundary between computer-side software and the Arduino controller.

## Responsibilities

- Connect to the NEXO serial controller.
- Accept only the controller command allowlist.
- Send ASCII commands at 115200 baud.
- Return raw responses for compatibility.
- Parse responses through the structured protocol API.

## API

send_command(command) returns the raw controller response string.

send_and_parse(command) returns a ControllerResponse with category, value and fields.

The bridge contains no AI logic and does not bypass Arduino safety.

## Testing

The bridge tests use mocked serial connections. Integration tests use the deterministic simulated controller, so the software stack can be tested without physical hardware.
