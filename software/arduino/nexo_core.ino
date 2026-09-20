/*
 * NEXO Core Firmware
 * Initial foundation for movement, safety and sensors.
 *
 * Hardware assumptions are intentionally kept configurable.
 */

#include <Arduino.h>

// Motor pins: change these to match the final motor driver wiring.
constexpr uint8_t LEFT_PWM  = 5;
constexpr uint8_t LEFT_IN1  = 7;
constexpr uint8_t LEFT_IN2  = 8;
constexpr uint8_t RIGHT_PWM = 6;
constexpr uint8_t RIGHT_IN1 = 9;
constexpr uint8_t RIGHT_IN2 = 10;

// Ultrasonic sensor
constexpr uint8_t TRIG_PIN = 12;
constexpr uint8_t ECHO_PIN = 11;

// Safety
constexpr uint16_t OBSTACLE_STOP_CM = 20;
constexpr uint8_t DEFAULT_SPEED = 150;

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

bool obstacleDetected() {
  const long distance = readDistanceCm();
  return distance > 0 && distance <= OBSTACLE_STOP_CM;
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

  Serial.println(F("NEXO core online."));
}

void loop() {
  // Safety layer gets priority over movement commands.
  if (obstacleDetected()) {
    stopMotors();
    Serial.println(F("SAFETY: obstacle detected."));
    delay(50);
    return;
  }

  // Temporary autonomous test:
  // forward -> stop -> reverse -> stop.
  drive(DEFAULT_SPEED, DEFAULT_SPEED);
  delay(1000);

  stopMotors();
  delay(500);

  drive(-DEFAULT_SPEED, -DEFAULT_SPEED);
  delay(500);

  stopMotors();
  delay(1000);
}
