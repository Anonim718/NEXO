#pragma once

#include <Arduino.h>

enum class RobotCommand : uint8_t {
  Stop,
  Forward,
  Back,
  Left,
  Right,
  Status,
  Ping,
  Unknown
};

RobotCommand parseCommand(const char* input);
const __FlashStringHelper* commandName(RobotCommand command);
