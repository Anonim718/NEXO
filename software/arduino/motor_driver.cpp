#include "motor_driver.h"

MotorDriver::MotorDriver(uint8_t leftPwm, uint8_t leftIn1, uint8_t leftIn2,
                         uint8_t rightPwm, uint8_t rightIn1, uint8_t rightIn2)
    : leftPwm_(leftPwm),
      leftIn1_(leftIn1),
      leftIn2_(leftIn2),
      rightPwm_(rightPwm),
      rightIn1_(rightIn1),
      rightIn2_(rightIn2) {}

void MotorDriver::begin() {
  pinMode(leftPwm_, OUTPUT);
  pinMode(leftIn1_, OUTPUT);
  pinMode(leftIn2_, OUTPUT);
  pinMode(rightPwm_, OUTPUT);
  pinMode(rightIn1_, OUTPUT);
  pinMode(rightIn2_, OUTPUT);
  stop();
}

int16_t MotorDriver::clampSpeed(int16_t speed) {
  return constrain(speed, -255, 255);
}

void MotorDriver::setMotor(uint8_t pwm, uint8_t in1, uint8_t in2,
                           int16_t speed) {
  speed = clampSpeed(speed);

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

void MotorDriver::stop() {
  setMotor(leftPwm_, leftIn1_, leftIn2_, 0);
  setMotor(rightPwm_, rightIn1_, rightIn2_, 0);
}

void MotorDriver::drive(int16_t leftSpeed, int16_t rightSpeed) {
  setMotor(leftPwm_, leftIn1_, leftIn2_, leftSpeed);
  setMotor(rightPwm_, rightIn1_, rightIn2_, rightSpeed);
}
