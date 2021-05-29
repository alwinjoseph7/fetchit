#include <AFMotor.h>
char command = 'S';
char prevCommand = 'A';

unsigned long timer0 = 2000;
unsigned long timer1 = 0;
unsigned long timer2 = 0;

AF_DCMotor FRONT_LEFT_MOTOR(1);
AF_DCMotor BACK_LEFT_MOTOR(2);
AF_DCMotor FRONT_RIGHT_MOTOR(4);
AF_DCMotor BACK_RIGHT_MOTOR(3);

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available() > 0)
  {
    timer1 = millis();
    prevCommand = command;
    command = Serial.read();

    if (command != prevCommand)
    {
      switch (command)
      {
        case 'F':
          {
            FRONT_LEFT_MOTOR.setSpeed(255);
            FRONT_LEFT_MOTOR.run(FORWARD);
            BACK_LEFT_MOTOR.setSpeed(255);
            BACK_LEFT_MOTOR.run(FORWARD);
            FRONT_RIGHT_MOTOR.setSpeed(255);
            FRONT_RIGHT_MOTOR.run(FORWARD);
            BACK_RIGHT_MOTOR.setSpeed(255);
            BACK_RIGHT_MOTOR.run(FORWARD);
          }
          break;

        case 'B':
          {
            FRONT_LEFT_MOTOR.setSpeed(255);
            FRONT_LEFT_MOTOR.run(BACKWARD);
            BACK_LEFT_MOTOR.setSpeed(255);
            BACK_LEFT_MOTOR.run(BACKWARD);
            FRONT_RIGHT_MOTOR.setSpeed(255);
            FRONT_RIGHT_MOTOR.run(BACKWARD);
            BACK_RIGHT_MOTOR.setSpeed(255);
            BACK_RIGHT_MOTOR.run(BACKWARD);

          }
          break;

        case 'R':
          {
            FRONT_RIGHT_MOTOR.setSpeed(255);
            FRONT_RIGHT_MOTOR.run(FORWARD);
            BACK_RIGHT_MOTOR.setSpeed(255);
            BACK_RIGHT_MOTOR.run(FORWARD);
            FRONT_LEFT_MOTOR.setSpeed(255);
            FRONT_LEFT_MOTOR.run(BACKWARD);
            BACK_LEFT_MOTOR.setSpeed(255);
            BACK_LEFT_MOTOR.run(BACKWARD);
          }
          break;

        case 'S':
          {
            FRONT_LEFT_MOTOR.run(RELEASE);
            BACK_LEFT_MOTOR.run(RELEASE);
            FRONT_RIGHT_MOTOR.run(RELEASE);
            BACK_RIGHT_MOTOR.run(RELEASE);
          }
          break;
        case 'X':
          {
            timer2 = millis();
            FRONT_LEFT_MOTOR.setSpeed(255);
            FRONT_LEFT_MOTOR.run(BACKWARD);
            BACK_LEFT_MOTOR.setSpeed(255);
            BACK_LEFT_MOTOR.run(BACKWARD);
            FRONT_RIGHT_MOTOR.setSpeed(255);
            FRONT_RIGHT_MOTOR.run(BACKWARD);
            BACK_RIGHT_MOTOR.setSpeed(255);
            BACK_RIGHT_MOTOR.run(BACKWARD);
            delay(1000);
            FRONT_LEFT_MOTOR.run(RELEASE);
            BACK_LEFT_MOTOR.run(RELEASE);
            FRONT_RIGHT_MOTOR.run(RELEASE);
            BACK_RIGHT_MOTOR.run(RELEASE);
          }
          break;
      }
    }
  }

  else
  {
    timer0 = millis();
    if ((timer0 - timer1) > 500)
    {
      FRONT_LEFT_MOTOR.run(RELEASE);
      BACK_LEFT_MOTOR.run(RELEASE);
      FRONT_RIGHT_MOTOR.run(RELEASE);
      BACK_RIGHT_MOTOR.run(RELEASE);
    }
  }
}
