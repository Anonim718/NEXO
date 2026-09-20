#include "commands.h"

RobotCommand parseCommand(String input) {
  input.trim();
  input.toUpperCase();

  if (input == "STOP") return RobotCommand::Stop;
  if (input == "FORWARD" || input == "F") return RobotCommand::Forward;
  if (input == "BACK" || input == "BACKWARD" || input == "B") return RobotCommand::Back;
  if (input == "LEFT" || input == "L") return RobotCommand::Left;
  if (input == "RIGHT" || input == "R") return RobotCommand::Right;
  if (input == "STATUS" || input == "S") return RobotCommand::Status;

  return RobotCommand::Unknown;
}

const __FlashStringHelper* commandName(RobotCommand command) {
  switch (command) {
    case RobotCommand::Stop: return F("STOP");
    case RobotCommand::Forward: return F("FORWARD");
    case RobotCommand::Back: return F("BACK");
    case RobotCommand::Left: return F("LEFT");
    case RobotCommand::Right: return F("RIGHT");
    case RobotCommand::Status: return F("STATUS");
    default: return F("UNKNOWN");
  }
}
