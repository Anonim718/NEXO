# NEXO Brain Architecture

The brain is deliberately separated from the physical controller.

## Layers

### 1. Input
Voice, keyboard, app or another interface produces an intent.

Example:

`"NEXO, move forward"`

### 2. Intent layer
Natural language is converted into a small set of safe robot intents:

`FORWARD`

### 3. Bridge
The computer-side bridge validates the intent against an allow-list and sends it over USB serial.

### 4. Controller
The Arduino executes the command only within its hardware and safety rules.

### 5. Hardware
Motors and sensors perform the physical action.

## Principle

AI should decide **what the user means**, not directly manipulate GPIO pins.

The controller decides whether a physical action is safe.

## Future

The brain can later add:

- speech recognition
- text-to-speech
- conversational AI
- memory/state
- task planning
- autonomous behaviours
- arm planning

All of those features should eventually converge on explicit, testable robot intents.
