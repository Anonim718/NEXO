# NEXO 🤖

**NEXO** is an autonomous hybrid AI robot project designed around a modular, safety-first architecture:

**Voice / AI → Intent → Brain / Safety → Planner → Bridge → Arduino → Hardware**

The goal is a physical robot that can understand natural-language commands, operate autonomously, interact with its environment and eventually manipulate objects with an arm.

## 🚀 Current status

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
- Deterministic controller simulator

### 🟢 Brain / safety layer
- Natural-language/AI intent boundary
- Allowlisted controller commands
- Shared robot state
- Deterministic safety decisions
- Obstacle-aware movement validation
- Battery-aware movement validation
- Fault lockout
- Explicit STOP priority
- Unit tests without physical hardware

### 🟢 Software integration foundations
- Computer-to-Arduino bridge
- Structured controller response parsing
- Hardware-independent battery interface
- Hardware-independent arm interface
- Voice adapter boundary
- Integration tests without physical hardware

### 🟡 In progress
- Planner layer
- Full bridge ↔ brain integration
- Offline voice engine integration
- Physical battery implementation after hardware selection
- Physical servo/arm implementation after hardware selection

### 🔴 Future
- Autonomous navigation
- Online AI integration
- Persistent robot state and memory
- Personality / behaviour layer
- Object detection and interaction
- Diagnostics and telemetry
- Full hardware integration
- Full-system testing
- Polished public demo

## 🧠 Architecture

```
Voice / AI
    ↓
Intent
    ↓
Brain / Safety
    ↓
Planner
    ↓
Computer Bridge
    ↓
Arduino Controller
    ↓
Motors / Sensors / Servos
```

The AI layer does **not** directly control physical hardware.

Every physical command passes through deterministic software checks and the Arduino controller. The Arduino remains the final physical safety authority.

## ⚙️ Serial commands

The current controller supports:

```
STOP
FORWARD
BACK
LEFT
RIGHT
STATUS
PING
```

Serial communication currently uses **115200 baud**.

See:
- `docs/brain.md`
- `docs/serial-protocol.md`
- `docs/command-spec.md`

## 📁 Repository structure

```
NEXO/
├── ai/                  # AI and behaviour layer
├── docs/                # Architecture, protocol, testing and integration
├── hardware/            # Wiring and component documentation
├── software/
│   ├── arduino/         # Low-level robot controller and MotorDriver
│   ├── brain/           # Deterministic intent, state and safety layer
│   ├── bridge/          # Computer ↔ Arduino bridge and tests
│   ├── hardware/        # Hardware-independent subsystem interfaces
│   └── sim/             # Deterministic controller simulator
├── voice/               # Voice subsystem documentation
└── roadmap.md           # Project roadmap
```

## 🛡️ Safety architecture

NEXO is intentionally layered.

The Brain can reject unsafe software-level requests, while the Arduino controller independently enforces physical safety rules such as:

- obstacle detection
- command timeout
- explicit STOP
- future battery and actuator limits

This means an AI mistake should not become a direct motor command.

## 🔧 Hardware note

The current Arduino firmware is a **generic H-bridge prototype**.

Its pin configuration should not be treated as an Adafruit Motor Shield configuration. The MotorDriver abstraction isolates the motor boundary so the final driver can be changed without rewriting the Brain or command protocol.

The exact physical driver must be selected before implementing driver-specific code.

## 🧪 Development philosophy

NEXO is built in layers:

1. Design the interface.
2. Implement the smallest deterministic component.
3. Test it without hardware.
4. Integrate the next layer.
5. Only then connect physical hardware.

**No magic. No giant spaghetti sketch. No robot possessed by a 14-line bug.**

---

### 📌 Project status

NEXO is currently a **software-first robotics prototype**. The architecture and safety boundaries are being built before final hardware integration, so the physical robot can be developed on top of a tested foundation rather than becoming an expensive debugging experiment.
