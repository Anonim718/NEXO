#pragma once

#include <Arduino.h>

class MotorDriver {
 public:
  MotorDriver(uint8_t leftPwm, uint8_t leftIn1, uint8_t leftIn2,
              uint8_t rightPwm, uint8_t rightIn1, uint8_t rightIn2);

  void begin();
  void stop();
  void drive(int16_t leftSpeed, int16_t rightSpeed);

 private:
  uint8_t leftPwm_;
  uint8_t leftIn1_;
  uint8_t leftIn2_;
  uint8_t rightPwm_;
  uint8_t rightIn1_;
  uint8_t rightIn2_;

  static int16_t clampSpeed(int16_t speed);
  static void setMotor(uint8_t pwm, uint8_t in1, uint8_t in2, int16_t speed);
};
