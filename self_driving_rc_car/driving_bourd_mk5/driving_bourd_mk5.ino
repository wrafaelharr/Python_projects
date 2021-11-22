#include <Wire.h>
#include <VL53L0X.h>

VL53L0X sensor;

#define sens_bourd 3
#define f 6
#define b 5
#define l 7
#define r 8

int right_sensor;
int left_sensor;
int forward;
int backward;
int left;
int right;
int reverse_distance = 70;
int uturn_direction;
long uturn_timer = 0;

void setup() {
  Serial.begin(9600);
  Wire.begin();

  //initalize sensor
  sensor.init();
  sensor.setTimeout(500);
  sensor.startContinuous();
  
  //initalize pins
  pinMode(sens_bourd, INPUT);
  pinMode(f, OUTPUT);
  pinMode(b, OUTPUT);
  pinMode(l, OUTPUT);
  pinMode(r, OUTPUT);
}

void loop() {
  //get right sensor
  int right_sensor = pulseIn(sens_bourd, HIGH, 4200);
  if (right_sensor == 0 && digitalRead(sens_bourd) == 1) {
      right_sensor = 2100;
  }
  right_sensor = map(right_sensor, 0, 2100, 0, 255);
  
  //get left sensor
  left_sensor = map(sensor.readRangeContinuousMillimeters(), 0, 1300, 0, 255);
  if (left_sensor > 250){
    left_sensor = 255;
  }

  //logic
  //left and right
  if ((left_sensor-right_sensor) > 20){
    left = true;
    right = false;
  }
  else if ((left_sensor-right_sensor) < -10){
    left = false;
    right = true;
  }
  else{
    left = false;
    right = false;
  }
  
  //forward backward
  if ((left_sensor+right_sensor)/2 > 250){
    forward = 250;
    backward = 0;
  } 
  else if ((left_sensor+right_sensor)/2 > reverse_distance){
    forward = 220;
    backward = 0;
  }
  
  else{
    uturn_timer = millis();
    if ((left_sensor-right_sensor) > 5){
       uturn_direction = 0;
    }
    else {
       uturn_direction == 1;
    }
  }

  if (millis()-uturn_timer < 900){
    forward = 0;
    backward = 250;

    if (uturn_direction = 0){
      left = false;
      right = true;
    }
    else{
      left = true;
      right = false;
    }
  }
  
  //control motors
  analogWrite(f, forward);
  analogWrite(b, backward);
  digitalWrite(l, left);
  digitalWrite(r, right);

  Serial.println(right_sensor);
}
