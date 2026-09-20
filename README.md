# NEXO 🤖

**NEXO** is an autonomous hybrid AI robot project built around a layered architecture:

**Voice / AI → Brain → Bridge → Arduino Controller → Hardware**

The goal is a physical robot that can understand natural-language commands, operate autonomously, interact with its environment and eventually manipulate objects with an arm.

## Current status

### 🟢 Foundation
- Repository structure
- Hardware and software documentation
- Development roadmap
- Layered safety architecture
- Python CI and automated tests

### 🟢 Controller prototype
- Forward / reverse movement
- Left / right turning
- Ultrasonic obstacle detection
- Automatic obstacle stop
- Command timeout safety stop
- Serial command interface at 115200 baud
- Centralized hardware configuration
- Isolated MotorDriver abstraction

### 🟢 Software integration foundations
- Allowlisted computer-to-Arduino bridge
- Structured controller response parsing
- Brain intent-to-command boundary
- Deterministic simulated controller
- Integration tests without physical hardware
- Hardware-independent battery interface
- Hardware-independent arm interface
- Voice adapter boundary

### 🟡 In progress
- CI verification across supported Python versions
- Full bridge ↔ brain integration
- Physical battery implementation after hardware selection
- Physical servo/arm implementation after hardware selection
- Offline voice engine integration

### 🔴 Future
- Online AI integration
- Persistent robot state and memory
- Personality / behaviour layer
- Autonomous navigation
- Object detection and interaction
- Full hardware integration

## Serial commands

STOP
FORWARD
BACK
LEFT
RIGHT
STATUS
PING

See docs/serial-protocol.md and docs/command-spec.md.

## Repository structure

NEXO/
├── ai/                  # AI and behaviour layer
├── docs/                # Architecture, protocol, testing and integration
├── hardware/            # Wiring and component documentation
├── software/
│   ├── arduino/         # Low-level robot controller and MotorDriver
│   ├── bridge/          # Computer ↔ Arduino bridge and tests
│   ├── hardware/        # Hardware-independent subsystem interfaces
│   └── sim/             # Deterministic controller simulator
├── voice/               # Voice subsystem documentation
└── roadmap.md           # Project roadmap

## Safety architecture

The AI layer does **not** directly control motors or other physical hardware.

All physical commands pass through the brain allowlist, bridge allowlist and Arduino controller. The controller remains the final physical safety authority.

Examples include:
- obstacle detection
- command timeout
- explicit STOP
- future battery and actuator limits

## Hardware note

The current Arduino firmware is a **generic H-bridge prototype**. Its pin configuration should not be treated as an Adafruit Motor Shield configuration.

The MotorDriver class isolates the motor boundary so the final driver can be changed without changing the brain protocol. The exact physical driver must be selected before implementing driver-specific code.

## Development principle

Build NEXO in layers, test each layer independently, then integrate them.

No magic. No giant spaghetti sketch. No robot possessed by a 14-line bug.
