#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#define forward 5
#define backward 4
#define r 2
#define l 3

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
}

void loop() {
  //check if available
  if (radio.available()) {  
    //read data
    radio.read(&comb, sizeof(comb));
  }
  //clean data
  else if (num_times < 0){
    comb = 0;
    num_times = num_times + 1;
  }
  else{
    num_times = 0;
  }
  
  

  //inturpret data
  if (comb > 999){
    up = true;
    down = false;

    if (comb - 1000 > 9){
      left = true;
      right = false;
    }
    else if (comb - 1000 > 0){
      right = true;
      left = false;
    }
  }
  else if (comb > 99){
    down = true;
    up = false;

    if (comb - 100 > 9){
      left = true;
      right = false;
    }
    else if (comb - 100 > 0){
      right = true;
      left = false;
    }
  }
  else if (comb > 9){
    left = true;
    right = false; 
  }
  else if (comb > 0){
    right = true;
    left = false;
  }
  else{
    up = false;
    down = false;
    left = false;
    right = false;
  }

  //print 
  Serial.print(left);
  
  //control car
  if (up == true){
    digitalWrite(forward, HIGH);
    digitalWrite(backward, LOW);
  }
  else if (down == true){
    digitalWrite(backward, HIGH);
    digitalWrite(forward, LOW);
  }
  else{
    digitalWrite(forward, LOW);
    digitalWrite(backward, LOW);
  }

  if (right == true){
    digitalWrite(l, LOW);
    digitalWrite(r, HIGH); 
  }
  else if (left == true){
    digitalWrite(l, HIGH);
    digitalWrite(r, LOW);
  }
  else{
    digitalWrite(l, LOW);
    digitalWrite(r, LOW);
  }

  delay(9);
}
