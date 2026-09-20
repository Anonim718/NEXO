# NEXO State and Telemetry

NEXO separates live telemetry from optional persistent state.

- Telemetry is timestamped and hardware-independent.
- JSON persistence is for non-critical state and future memory metadata.
- Safety-critical state never depends on a saved JSON file.
- Persistence failure must not prevent the system from entering a safe state.
