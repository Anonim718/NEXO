#include <Arduino.h>
#include "commands.h"

// Motor driver pins. Update after final hardware selection.
constexpr uint8_t LEFT_PWM  = 5;
constexpr uint8_t LEFT_IN1  = 7;
constexpr uint8_t LEFT_IN2  = 8;
constexpr uint8_t RIGHT_PWM = 6;
constexpr uint8_t RIGHT_IN1 = 9;
constexpr uint8_t RIGHT_IN2 = 10;

// Ultrasonic sensor.
constexpr uint8_t TRIG_PIN = 12;
constexpr uint8_t ECHO_PIN = 11;

constexpr uint16_t OBSTACLE_STOP_CM = 20;
constexpr uint8_t DEFAULT_SPEED = 150;
constexpr unsigned long COMMAND_TIMEOUT_MS = 3000;

unsigned long lastCommandAt = 0;
RobotCommand activeCommand = RobotCommand::Stop;

void setMotor(uint8_t pwm, uint8_t in1, uint8_t in2, int16_t speed) {
  speed = constrain(speed, -255, 255);

  if (speed > 0) {
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    analogWrite(pwm, speed);
  } else if (speed < 0) {
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    analogWrite(pwm, -speed);
  } else {
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
    analogWrite(pwm, 0);
  }
}

void stopMotors() {
  setMotor(LEFT_PWM, LEFT_IN1, LEFT_IN2, 0);
  setMotor(RIGHT_PWM, RIGHT_IN1, RIGHT_IN2, 0);
}

void drive(int16_t leftSpeed, int16_t rightSpeed) {
  setMotor(LEFT_PWM, LEFT_IN1, LEFT_IN2, leftSpeed);
  setMotor(RIGHT_PWM, RIGHT_IN1, RIGHT_IN2, rightSpeed);
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

bool obstacleDetected(long& distanceCm) {
  distanceCm = readDistanceCm();
  return distanceCm > 0 && distanceCm <= OBSTACLE_STOP_CM;
}

void executeCommand(RobotCommand command) {
  activeCommand = command;
  lastCommandAt = millis();

  switch (command) {
    case RobotCommand::Stop:
      stopMotors();
      break;
    case RobotCommand::Forward:
      if (!obstacleDetected(lastDistanceCm)) drive(DEFAULT_SPEED, DEFAULT_SPEED);
      else stopMotors();
      break;
    case RobotCommand::Back:
      drive(-DEFAULT_SPEED, -DEFAULT_SPEED);
      break;
    case RobotCommand::Left:
      drive(-DEFAULT_SPEED, DEFAULT_SPEED);
      break;
    case RobotCommand::Right:
      drive(DEFAULT_SPEED, -DEFAULT_SPEED);
      break;
    case RobotCommand::Status:
      Serial.print(F("STATE="));
      Serial.print(commandName(activeCommand));
      Serial.print(F(" DIST_CM="));
      Serial.println(lastDistanceCm);
      break;
    default:
      Serial.println(F("ERR=UNKNOWN_COMMAND"));
      break;
  }
}

void setup() {
  pinMode(LEFT_PWM, OUTPUT);
  pinMode(LEFT_IN1, OUTPUT);
  pinMode(LEFT_IN2, OUTPUT);
  pinMode(RIGHT_PWM, OUTPUT);
  pinMode(RIGHT_IN1, OUTPUT);
  pinMode(RIGHT_IN2, OUTPUT);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  Serial.begin(115200);
  stopMotors();
  lastCommandAt = millis();

  Serial.println(F("NEXO CORE ONLINE"));
  Serial.println(F("Commands: STOP FORWARD BACK LEFT RIGHT STATUS"));
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    RobotCommand command = parseCommand(input);

    if (command != RobotCommand::Unknown) {
      executeCommand(command);
      Serial.print(F("OK="));
      Serial.println(commandName(command));
    } else {
      Serial.println(F("ERR=UNKNOWN_COMMAND"));
    }
  }

  long distanceCm = readDistanceCm();

  if (activeCommand == RobotCommand::Forward &&
      distanceCm > 0 &&
      distanceCm <= OBSTACLE_STOP_CM) {
    stopMotors();
    activeCommand = RobotCommand::Stop;
    Serial.println(F("SAFETY=OBSTACLE_STOP"));
  }

  if (activeCommand != RobotCommand::Stop &&
      millis() - lastCommandAt >= COMMAND_TIMEOUT_MS) {
    stopMotors();
    activeCommand = RobotCommand::Stop;
    Serial.println(F("SAFETY=COMMAND_TIMEOUT"));
  }

  lastDistanceCm = distanceCm;
  delay(30);
}

long lastDistanceCm = -1;
