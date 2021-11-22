#include <Wire.h>
#include <VL53L0X.h>

VL53L0X sensor;

#define drive_bourd 3

int right_sensor;

void setup(){
  Serial.begin(9600);
  Wire.begin();

  //initalize sensor
  sensor.init();
  sensor.setTimeout(500);
  sensor.startContinuous();

  //initalize pins
  pinMode(drive_bourd, OUTPUT);
}

void loop(){
  if (sensor.timeoutOccurred()) { Serial.print(" TIMEOUT"); }

  right_sensor = map(sensor.readRangeContinuousMillimeters(), 0, 1300, 0, 250);

  if (right_sensor > 250){
    right_sensor = 255;
  }

  analogWrite(drive_bourd, right_sensor);
  
  Serial.println(right_sensor);
}
