# NEXO Brain Layer

The Brain is the deterministic safety boundary between language/AI intent and physical controller commands.

## Flow

`Voice / AI → Intent → Brain → Safety checks → Controller command`

The Brain does **not**:
- call an LLM;
- open a serial connection;
- drive motors directly;
- bypass Arduino safety.

## Current decisions

| Intent | Condition | Controller command |
|---|---|---|
| STOP | any | STOP |
| PING | any | PING |
| STATUS | any | STATUS |
| FORWARD | clear + battery OK | FORWARD |
| FORWARD | obstacle too close | STOP |
| FORWARD | battery at/below limit | STOP |
| BACK/LEFT/RIGHT | battery OK | requested command |
| Any motion | FAULT mode | STOP |

Default software limits:
- obstacle stop: 30 cm
- minimum battery: 10%

The Arduino remains the final physical safety authority. These software checks are an additional layer, not a replacement.

## Why this exists

Natural-language systems can produce ambiguous or incorrect commands. Keeping the final decision deterministic makes the robot easier to test, debug and constrain before any command reaches hardware.
