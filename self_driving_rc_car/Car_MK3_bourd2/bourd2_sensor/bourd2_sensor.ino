#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <Servo.h>
#include <Wire.h>
#include <VL53L0X.h>

#define sensor2_pin 6
#define servo_ang_pin 3
#define SERVO_PIN 9
#define stoper1 A0
#define stoper2 A1

VL53L0X sensor;

Servo Servo1; //create a servo object

//variables
int dist;
int x;
long reset_time = 0;
long timer = 0;
int first_timer;
int last_timer;
int angle = 0;
int check = 0;
int moves = 0;
int compare = 1000;
boolean r_clock;
boolean c_clock;

void setup() {
  Serial.begin(9600);

  Wire.begin();

  sensor.init();
  sensor.setTimeout(500);
  sensor.startContinuous();

  //declare pins
  pinMode(sensor2_pin, OUTPUT);
  pinMode(servo_ang_pin, OUTPUT);
  pinMode(stoper1, INPUT);
  pinMode(stoper2, INPUT);

  //attach servo
  Servo1.attach(SERVO_PIN);
}

void loop() {
  
  if ((analogRead(stoper1) > compare or analogRead(stoper2) > compare) and (millis()-reset_time > 500)){
    if (moves < 90){
      moves = 180;
      timer = millis();
      last_timer = millis()-reset_time + first_timer;
      
      r_clock = true;
      c_clock = false;
    }
    else{
      moves = 0;
      first_timer = millis()-timer;
      
      r_clock = false;
      c_clock = true;
    }
    reset_time = millis();
  }

  if (r_clock){
    angle = map(millis()-timer, 0,  first_timer, 0,255);
    
  }
  
  else if (c_clock){
    angle = map(millis()-timer, first_timer,  last_timer, 255, 0);  
  }
  
  if (angle > 255){
      angle = 255;
  }
  else if (angle < 0){
    angle = 0;
  }
  
  Servo1.write(moves);
  
  //Servo1.write(90);
  Serial.println(angle);

  //read distance
  dist = sensor.readRangeContinuousMillimeters();

  //convert to pwm value
  if (dist < 1290){
    dist = map(dist, 0, 1290, 0, 250);
  }
  else{
    dist = 250;
  }
  
  //Serial.println(angle);
  analogWrite(sensor2_pin, dist);
  analogWrite(servo_ang_pin, angle);
}
