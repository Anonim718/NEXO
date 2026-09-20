#include "commands.h"

namespace {
constexpr size_t INPUT_BUFFER_SIZE = 32;
char inputBuffer[INPUT_BUFFER_SIZE];
size_t inputLength = 0;

void normalize(char* text) {
  size_t start = 0;
  while (text[start] == ' ' || text[start] == '\t' || text[start] == '\r') {
    ++start;
  }

  if (start > 0) {
    size_t i = 0;
    while (text[start + i] != '\0') {
      text[i] = text[start + i];
      ++i;
    }
    text[i] = '\0';
  }

  size_t length = 0;
  while (text[length] != '\0') ++length;

  while (length > 0 &&
         (text[length - 1] == ' ' || text[length - 1] == '\t' ||
          text[length - 1] == '\r')) {
    text[--length] = '\0';
  }

  for (size_t i = 0; i < length; ++i) {
    if (text[i] >= 'a' && text[i] <= 'z') {
      text[i] = static_cast<char>(text[i] - 'a' + 'A');
    }
  }
}

bool equals(const char* a, const char* b) {
  size_t i = 0;
  while (a[i] != '\0' || b[i] != '\0') {
    if (a[i] != b[i]) return false;
    ++i;
  }
  return true;
}
}  // namespace

RobotCommand parseCommand(const char* input) {
  if (input == nullptr) return RobotCommand::Unknown;

  char normalized[INPUT_BUFFER_SIZE];
  size_t i = 0;
  while (i < INPUT_BUFFER_SIZE - 1 && input[i] != '\0') {
    normalized[i] = input[i];
    ++i;
  }
  normalized[i] = '\0';

  normalize(normalized);

  if (equals(normalized, "STOP")) return RobotCommand::Stop;
  if (equals(normalized, "FORWARD") || equals(normalized, "F")) {
    return RobotCommand::Forward;
  }
  if (equals(normalized, "BACK") || equals(normalized, "BACKWARD") ||
      equals(normalized, "B")) {
    return RobotCommand::Back;
  }
  if (equals(normalized, "LEFT") || equals(normalized, "L")) {
    return RobotCommand::Left;
  }
  if (equals(normalized, "RIGHT") || equals(normalized, "R")) {
    return RobotCommand::Right;
  }
  if (equals(normalized, "STATUS") || equals(normalized, "S")) {
    return RobotCommand::Status;
  }
  if (equals(normalized, "PING")) return RobotCommand::Ping;

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
    case RobotCommand::Ping: return F("PING");
    default: return F("UNKNOWN");
  }
}
