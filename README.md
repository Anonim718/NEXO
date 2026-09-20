# NEXO 🤖

**NEXO** is an autonomous hybrid AI robot project built around a layered architecture:

**Voice / AI → Brain Bridge → Arduino Controller → Hardware**

The goal is a physical robot that can understand natural-language commands, operate autonomously, interact with its environment and eventually manipulate objects with an arm.

## Current status

### 🟢 Foundation
- Repository structure
- Hardware and software documentation
- Development roadmap
- Testing strategy

### 🟢 Arduino controller prototype
- Forward / reverse movement
- Left / right turning
- Ultrasonic obstacle detection
- Automatic obstacle stop
- Command timeout safety stop
- Serial command interface at 115200 baud
- Centralized hardware configuration

### 🟡 In progress
- Computer-side brain bridge
- Structured serial protocol
- Hardware abstraction
- Arm / servo subsystem
- Offline voice control

### 🔴 Future
- Online AI integration
- Persistent robot state
- Personality / behaviour layer
- Autonomous navigation
- Object detection and interaction
- Full system integration

## Serial commands

STOP
FORWARD
BACK
LEFT
RIGHT
STATUS

See docs/serial-protocol.md for the protocol design.

## Repository structure

NEXO/
├── ai/                  # AI and behaviour layer
├── docs/                # Architecture, hardware, protocol and testing
├── hardware/            # Wiring and component documentation
├── software/
│   ├── arduino/         # Low-level robot controller
│   └── bridge/          # Planned computer ↔ Arduino bridge
├── voice/               # Hybrid voice subsystem
└── roadmap.md           # Project roadmap

## Safety architecture

The AI layer does **not** directly control motors or other physical hardware.

All physical commands pass through the controller, where safety checks can stop the robot independently of the AI.

Examples include:
- obstacle detection
- command timeout
- explicit STOP
- future battery and actuator limits

## Hardware note

The current Arduino firmware is a **generic H-bridge prototype**. Its pin configuration should not be treated as an Adafruit Motor Shield configuration.

The final motor driver will be isolated behind a hardware abstraction layer once the exact hardware is selected.

## Development principle

Build NEXO in layers, test each layer independently, then integrate them.

No magic. No giant spaghetti sketch. No robot possessed by a 14-line bug.