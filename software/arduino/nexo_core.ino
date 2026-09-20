#include <Arduino.h>
#include "config.h"
#include "commands.h"

unsigned long lastCommandAt = 0;
unsigned long lastSensorAt = 0;

RobotCommand activeCommand = RobotCommand::Stop;
long lastDistanceCm = -1;

MotorDriver motorDriver(
    LEFT_PWM, LEFT_IN1, LEFT_IN2,
    RIGHT_PWM, RIGHT_IN1, RIGHT_IN2);

void stopMotors() {
  motorDriver.stop();
}

void drive(int16_t leftSpeed, int16_t rightSpeed) {
  motorDriver.drive(leftSpeed, rightSpeed);
}

long readDistanceCm() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  const unsigned long duration = pulseIn(ECHO_PIN, HIGH, 25000UL);
  if (duration == 0) return -1;

  return static_cast<long>(duration / 58UL);
}

bool obstacleDetected(long distanceCm) {
  return distanceCm > 0 && distanceCm <= OBSTACLE_STOP_CM;
}

void reportStatus() {
  Serial.print(F("OK=STATUS STATE="));
  Serial.print(commandName(activeCommand));
  Serial.print(F(" DIST_CM="));
  Serial.println(lastDistanceCm);
}

void executeCommand(RobotCommand command) {
  switch (command) {
    case RobotCommand::Stop:
      activeCommand = RobotCommand::Stop;
      stopMotors();
      lastCommandAt = millis();
      Serial.println(F("OK=STOP"));
      break;

    case RobotCommand::Forward:
      if (obstacleDetected(lastDistanceCm)) {
        stopMotors();
        activeCommand = RobotCommand::Stop;
        lastCommandAt = millis();
        Serial.println(F("SAFETY=OBSTACLE_STOP"));
      } else {
        activeCommand = RobotCommand::Forward;
        drive(DEFAULT_SPEED, DEFAULT_SPEED);
        lastCommandAt = millis();
        Serial.println(F("OK=FORWARD"));
      }
      break;

    case RobotCommand::Back:
      activeCommand = RobotCommand::Back;
      drive(-DEFAULT_SPEED, -DEFAULT_SPEED);
      lastCommandAt = millis();
      Serial.println(F("OK=BACK"));
      break;

    case RobotCommand::Left:
      activeCommand = RobotCommand::Left;
      drive(-DEFAULT_SPEED, DEFAULT_SPEED);
      lastCommandAt = millis();
      Serial.println(F("OK=LEFT"));
      break;

    case RobotCommand::Right:
      activeCommand = RobotCommand::Right;
      drive(DEFAULT_SPEED, -DEFAULT_SPEED);
      lastCommandAt = millis();
      Serial.println(F("OK=RIGHT"));
      break;

    case RobotCommand::Status:
      reportStatus();
      break;

    case RobotCommand::Ping:
      Serial.println(F("OK=PONG"));
      break;

    default:
      Serial.println(F("ERR=UNKNOWN_COMMAND"));
      break;
  }
}

void readSerialLine() {
  while (Serial.available() > 0) {
    const char incoming = static_cast<char>(Serial.read());

    if (incoming == '\r') continue;

    if (incoming == '\n') {
      inputBuffer[inputLength] = '\0';
      executeCommand(parseCommand(inputBuffer));
      inputLength = 0;
      continue;
    }

    if (inputLength < INPUT_BUFFER_SIZE - 1) {
      inputBuffer[inputLength++] = incoming;
    } else {
      inputLength = 0;
      Serial.println(F("ERR=COMMAND_TOO_LONG"));
    }
  }
}

void setup() {
  motorDriver.begin();

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  Serial.begin(115200);
  stopMotors();

  const unsigned long now = millis();
  lastCommandAt = now;
  lastSensorAt = now;

  Serial.println(F("NEXO CORE ONLINE"));
  Serial.println(F("Commands: STOP FORWARD BACK LEFT RIGHT STATUS PING"));
}

void loop() {
  const unsigned long now = millis();

  readSerialLine();

  if (now - lastSensorAt >= SENSOR_INTERVAL_MS) {
    lastSensorAt = now;
    lastDistanceCm = readDistanceCm();

    if (activeCommand == RobotCommand::Forward &&
        obstacleDetected(lastDistanceCm)) {
      stopMotors();
      activeCommand = RobotCommand::Stop;
      Serial.println(F("SAFETY=OBSTACLE_STOP"));
    }
  }

  if (activeCommand != RobotCommand::Stop &&
      now - lastCommandAt >= COMMAND_TIMEOUT_MS) {
    stopMotors();
    activeCommand = RobotCommand::Stop;
    Serial.println(F("SAFETY=COMMAND_TIMEOUT"));
  }
}
