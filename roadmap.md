# NEXO Roadmap

## Phase 1 — Foundation
- [x] Create the GitHub repository
- [x] Define the project structure
- [x] Document the robot architecture
- [ ] Finalise the physical hardware prototype

## Phase 2 — Movement
- [x] Motor control prototype
- [x] Basic obstacle detection
- [x] Command timeout safety
- [x] Stable serial manual control
- [x] Motor-driver abstraction
- [ ] Hardware-specific motor driver implementation
- [ ] Autonomous navigation prototype
- [x] Deterministic Planner layer

## Phase 3 — Voice
- [x] Voice adapter boundary
- [ ] Offline wake word / basic commands
- [ ] Speech recognition engine
- [ ] Text-to-speech
- [ ] Online voice fallback

## Phase 4 — Intelligence
- [x] AI intent boundary
- [x] Allowlisted command mapping
- [x] Shared state model
- [x] Software safety orchestration
- [x] Deterministic Brain decision layer
- [x] Memory/state persistence
- [ ] Personality and behaviour rules
- [x] Safe tool/device orchestration
- [ ] Online AI integration

## Phase 5 — Physical Interaction
- [x] Hardware-independent arm interface
- [ ] Final arm mechanism
- [ ] Servo driver implementation
- [ ] Object detection
- [ ] Basic object interaction

## Phase 6 — Integration
- [x] Deterministic controller simulator
- [x] Software integration tests
- [x] CI verification across supported Python versions
- [ ] Connect physical hardware, voice and AI
- [ ] Battery monitoring on final hardware
- [x] Diagnostics and telemetry
- [ ] Autonomous behaviour
- [ ] Full-system test
- [ ] Polished demo

## Current engineering sequence

`VOICE/AI → INTENT → BRAIN/SAFETY → PLANNER → BRIDGE → ARDUINO → HARDWARE`

The Brain layer is now deterministic and hardware-independent. The next software milestone is a planner that can turn validated high-level goals into short, safe controller actions without bypassing the Brain or Arduino safety layer.

## Engineering rule

Build each layer independently, test it, then integrate it. The Arduino controller remains the final physical safety authority.
