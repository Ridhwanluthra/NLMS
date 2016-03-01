#include<Servo.h>

int PIN_WRIST= 11;
int PIN_FINGURE= 12;
int PIN_PI01= 14;
int PIN_PI02= 15;
int PIN_PI03= 16;

Servo fingure, wrist;// declare servo name type servo

  int duration, distance;//declare variable for unltrasonic sensor
  int x=0;
  
void setup() {
  Serial.begin(9600);
  pinMode(PIN_PI01, INPUT_PULLUP);
  pinMode(PIN_PI02, INPUT_PULLUP);
  pinMode(PIN_PI03, INPUT_PULLUP);
  wrist.attach(PIN_WRIST);
  fingure.attach(PIN_FINGURE);
  wrist.writeMicroseconds(1500);
  wrist.write(90);
  fingure.writeMicroseconds(1500);
  fingure.write(0);
}

void loop() {

  if(digitalRead(PIN_PI01)==HIGH && digitalRead(PIN_PI02)==HIGH){
    hold(1200);
    up(50);
    delay(1000);
    delay(1000);
  }
  
  if(digitalRead(PIN_PI01)==LOW && digitalRead(PIN_PI02)==LOW){
    down(50);
    drop(1200);
    delay(1000);
    delay(1000);
  }
  
  if(digitalRead(PIN_PI01)==HIGH && digitalRead(PIN_PI02)==LOW){
    up(5);
    down(50);
    delay(1000);
    delay(1000);
  }
  
}

void up(int unit_delay_time){
  for (int i=90; i<180; i++){
      wrist.write(i); //servo rotates at full speed to the right
      delay(unit_delay_time);
  }
}

void down(int unit_delay_time){
    for (int i=180; i>90; i--){
      wrist.write(i); //servo rotates at full speed to the right
      delay(unit_delay_time);
    }
}

void hold(int delay_time){
    for(int i=0; i<90; i++){
      fingure.write(i);
      delay(25);
      
    }
    delay(delay_time);
}

void drop(int delay_time){
  fingure.write(0);
  delay(delay_time);
}