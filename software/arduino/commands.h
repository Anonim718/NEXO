#pragma once

#include <Arduino.h>

enum class RobotCommand : uint8_t {
  Stop,
  Forward,
  Back,
  Left,
  Right,
  Status,
  Unknown
};

RobotCommand parseCommand(String input);
const __FlashStringHelper* commandName(RobotCommand command);
