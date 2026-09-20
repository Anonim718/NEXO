# NEXO Simulator

The simulator reproduces the controller command boundary without requiring Arduino hardware.

It is intended for deterministic integration tests of:

AI intent -> Brain -> Bridge/protocol -> Controller

The simulator deliberately models safety behaviour such as stopping forward motion when the configured obstacle distance is reached. It is not a physics simulator.
