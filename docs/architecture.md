# NEXO Architecture

NEXO is planned as a modular autonomous robot combining mobility, sensors, voice, AI and physical interaction.

## Core layers

1. **Hardware layer**
   - Motors and motor driver
   - Servos
   - Sensors
   - Power system
   - Microcontroller

2. **Control layer**
   - Movement commands
   - Sensor processing
   - Safety limits
   - Robot state

3. **Voice layer**
   - Offline commands
   - Speech recognition
   - Text-to-speech
   - Online fallback

4. **AI layer**
   - Natural-language understanding
   - Task planning
   - Memory/state
   - Tool and device control

5. **Behaviour layer**
   - Personality
   - Responses
   - Autonomous routines

The design should remain modular so individual components can be replaced without rebuilding the entire system.
