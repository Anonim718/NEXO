# NEXO Development

## Windows 10

### Arduino

Use Arduino IDE with the Arduino-compatible board selected.

Open:

software/arduino/nexo_core.ino

The firmware expects a generic H-bridge motor driver with the pin mapping documented in `config.h`.

### Python bridge

Install Python 3.11+ and the bridge dependencies:

```text
python -m pip install -r software/bridge/requirements.txt
```

Run the interactive bridge from the repository root:

```text
python software/bridge/nexo_cli.py COM3
```

Replace `COM3` with the serial port assigned to the NEXO controller.

### Tests

```text
python -m pip install pytest
pytest software/bridge/tests
```

## Hardware safety

Keep the wheels lifted during initial motor tests. Start at low speed and keep a physical STOP path available.

The Arduino controller remains the final authority for physical safety.
