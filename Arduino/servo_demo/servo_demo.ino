
#include <Servo.h>

int servoPin = 3;         //remember to choose a PWM capable pin  
Servo servo1;


void setup() {
  pinMode(servoPin,OUTPUT);
  servo1.attach(servoPin);
}

void loop() {
  //waves servo back and forth
  servo1.write(90);
  delay(500);             //servos need some time delay to move to position
  servo1.write(0);
  delay(500);
}
