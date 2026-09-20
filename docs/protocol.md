# NEXO Serial Protocol

Allowed controller commands: STOP, FORWARD, BACK, LEFT, RIGHT, STATUS, PING.

The protocol layer normalizes commands, rejects unknown values, and formats
accepted commands with a newline terminator. It does not open serial
connections and does not decide whether movement is safe. Brain and Arduino
remain the safety boundaries.
