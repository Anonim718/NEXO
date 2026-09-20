# NEXO State Model

NEXO now has a shared software state model for higher-level logic and simulation.

## States

- STOP
- FORWARD
- BACK
- LEFT
- RIGHT
- LOW_BATTERY
- FAULT

The Arduino remains authoritative for physical state. The Python model is a planning and testing representation, not a replacement for firmware safety.

## Safety

Forward movement is denied when:
- an obstacle is at or below the configured threshold;
- battery level is at or below 10%;
- the software snapshot is already LOW_BATTERY or FAULT.

Physical battery thresholds and actuator limits must still be implemented in firmware once the final hardware is selected.
