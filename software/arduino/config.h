#pragma once

#include <Arduino.h>

// Starting configuration for the generic H-bridge prototype.
// Keep hardware-specific pin choices here rather than scattering them
// through the firmware.

constexpr uint8_t LEFT_PWM = 5;
constexpr uint8_t LEFT_IN1 = 7;
constexpr uint8_t LEFT_IN2 = 8;

constexpr uint8_t RIGHT_PWM = 6;
constexpr uint8_t RIGHT_IN1 = 9;
constexpr uint8_t RIGHT_IN2 = 10;

constexpr uint8_t TRIG_PIN = 12;
constexpr uint8_t ECHO_PIN = 11;

constexpr uint16_t OBSTACLE_STOP_CM = 20;
constexpr uint8_t DEFAULT_SPEED = 150;

constexpr unsigned long COMMAND_TIMEOUT_MS = 3000;
constexpr unsigned long SENSOR_INTERVAL_MS = 100;
