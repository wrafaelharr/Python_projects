#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <Servo.h>

#define SERVO_PIN 3
#define forward 6
#define backward 5
#define r 2
#define l 4

Servo Servo1; //create a servo object
RF24 radio(9, 10); // CE, CSN

const byte address[6] = "00001";
boolean button_state = 0;
int xaxis = 0;
int yaxis = 0;
int up = 0;
int down = 0;
int left = 0;
int right = 0;
int comb = 0;
int num_times = 0;
int x;
int y;
int servoAngle = 0;
int count = 0;
long reset_time = 0;

void setup() {
  pinMode(6, OUTPUT);
  
  Serial.begin(9600);
  
  radio.begin();
  radio.openReadingPipe(0, address);   //Setting the address at which we will receive the data
  radio.setPALevel(RF24_PA_MIN);       //You can set this as minimum or maximum depending on the distance between the transmitter and receiver.
  radio.startListening();              //This sets the module as receiver

  //control pins
  pinMode(forward, OUTPUT);
  pinMode(backward, OUTPUT);
  pinMode(l, OUTPUT);
  pinMode(r, OUTPUT);

  Servo1.attach(SERVO_PIN);  //attach the pin to the object so that we can send the signal to it
}

void loop() {
  if (millis() - reset_time > 800*3){
    reset_time = millis();
  }
  else if (millis() - reset_time > 905*2){
    Servo1.write(0);
    Serial.println(millis());
  }
  else if (millis() - reset_time > 615){
    Servo1.write(250);
    Serial.println(millis());
  }

  
  //check if available
  if (radio.available()) {  
    //read data
    radio.read(&comb, sizeof(comb));
  }

  //seeperate data
  x = comb / 10;
  y = comb % 10;

  //interpret x
  if (x < 5){
    up = map(x, 5, 0, 0, 250);
    down = LOW;
  }
  else if (x > 5){
    up = 0;
    down = HIGH;
  }
  else{
    up = 0;
    down = LOW;
  }

  //interpret y
  if (y < 1){
    right = HIGH;
    left = LOW;
  }
  else if (y > 1){
    right = LOW;
    left = HIGH;
  }
  else{
    right = LOW;
    left = LOW;
  }
  

  //control car
  analogWrite(forward, up);
  digitalWrite(backward, down);
  digitalWrite(l, left);
  digitalWrite(r, right);
  
  Serial.println(up);
}
