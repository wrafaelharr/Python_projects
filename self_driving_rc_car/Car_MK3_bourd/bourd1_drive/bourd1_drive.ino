#include <Wire.h>
#include <VL53L0X.h>
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <Servo.h>

VL53L0X sensor;
RF24 radio(9, 10); // CE, CSN

#define forward 3
#define backward 2
#define r 2
#define l 4

const byte addresses [][6] = {"00001", "00002"}; 
int sensor2_pin = 6;
int servo_ang_pin = 5;
int dist;
int dist2;
int comb_dist;
int up = 0;
int down = 0;
int left = 0;
int right = 0;
int comb = 0;
int x;
int y;
int angle;
int comb_ang;
int count;


void setup() {
  Serial.begin(9600);
  Wire.begin();

  //initalize sensor
  sensor.init();
  sensor.setTimeout(500);
  sensor.startContinuous();

  radio.begin();                            //Starting the radio communication
  radio.openWritingPipe(addresses[1]);      //Setting the address at which we will send the data
  radio.openReadingPipe(1, addresses[0]);   //Setting the address at which we will receive the data
  radio.setPALevel(RF24_PA_MIN);              

  //control pins
  pinMode(forward, OUTPUT);
  pinMode(backward, OUTPUT);
  pinMode(l, OUTPUT);
  pinMode(r, OUTPUT);

  //declare pinmodes
  pinMode(sensor2_pin, INPUT);
  pinMode(servo_ang_pin, INPUT);
}

void loop() {
  //read bourd 2
  int var = pulseIn(sensor2_pin, HIGH, 4200);
  if (var == 0 && digitalRead(sensor2_pin) == 1) {
      var = 2100;
  }
  
  int angle = pulseIn(servo_ang_pin, HIGH, 4200);
  if (angle == 0 && digitalRead(servo_ang_pin) == 1) {
      angle = 2100;
  }

  angle = map(angle, 0, 1970, 0, 180);

  //inturpret bourd 1 data
  dist = map(sensor.readRangeContinuousMillimeters(), 0, 1290, 0, 250);
  if (dist > 250){
    dist = 250;
  }

  //interpret bourd 2 data
  dist2 = map(var, 0, 990, 0, 250);

  //condense
  comb_dist = 10000 + map(dist2, 0, 250, 0, 99)*100 + map(dist, 0, 250, 0, 99);
  comb_ang = 1000 + angle;

  //radio
  radio.stopListening();                             //This sets the module as transmitter
  if (count > 0){
    comb = comb_dist;
    count = 0;
  }
  else{
    comb = comb_ang;
    count = 1;
  }
  radio.write(&comb, sizeof(comb));        //Sending the data

  //driving controll
  
  //print
  Serial.println(1000);
  Serial.println(dist2);
}
