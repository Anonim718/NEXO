# NEXO Command Specification

| Command | Effect |
|---|---|
| STOP | Stop motors immediately |
| FORWARD | Move forward unless obstacle safety blocks it |
| BACK | Move backward |
| LEFT | Turn left |
| RIGHT | Turn right |
| STATUS | Report state and latest distance |
| PING | Return communication acknowledgement |

Commands are ASCII, one per line, terminated by LF, at 115200 baud.

Response categories: OK= for successful operations, SAFETY= for controller-enforced safety actions, ERR= for rejected or invalid commands.

The controller remains authoritative for physical safety.
