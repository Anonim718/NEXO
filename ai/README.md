# NEXO AI

The AI layer is responsible for understanding higher-level commands and turning them into safe, structured actions.

## Planned responsibilities

- Natural-language command interpretation
- Task planning
- Context and state
- Personality
- Tool selection
- Hardware command generation

The AI should never directly control hardware without passing through the robot's control and safety layers.


## Architecture rule

The brain produces validated intent; the bridge transports commands; the Arduino controller owns physical safety.
