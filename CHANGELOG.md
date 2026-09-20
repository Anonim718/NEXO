# Changelog

## Unreleased

### Added
- MotorDriver abstraction for the Arduino H-bridge boundary.
- Structured controller response parsing.
- Brain intent-to-command tests.
- Deterministic controller simulator.
- End-to-end software integration tests.
- Hardware-independent battery and arm interfaces.
- Voice adapter boundary.

### Improved
- Computer bridge now exposes send_and_parse() while preserving the raw send_command() API.
- Repository documentation now reflects the layered integration architecture.

### Safety
- AI/brain and bridge layers remain allowlisted.
- Arduino remains the final physical safety authority.
- No physical battery or servo pin assumptions were added before hardware selection.
