#include<Servo.h>

int PIN_WRIST= 12;
int PIN_FINGURE= 11;
int PIN_PI01= 5;
int PIN_PI02= 6;

Servo fingure, wrist;// declare servo name type servo

  int duration, distance;//declare variable for unltrasonic sensor
  int x=0;
  char pos;
  int pos_v=0;
  int pos_h=0;
  int ended=0;
  int maximum=180;
    int minimum=95;
  int previous=12;
void setup() {
  Serial.begin(9600);
  pinMode(PIN_PI01, INPUT);
  pinMode(PIN_PI02, INPUT);
  wrist.attach(PIN_WRIST);
  fingure.attach(PIN_FINGURE);
  wrist.writeMicroseconds(1500);
  wrist.write(maximum);
    delay(1000);
  fingure.writeMicroseconds(1500);
  fingure.write(90);
    delay(1000);
}

void loop() {
  if(ended!=1){
  Serial.println(digitalRead(PIN_PI01));
  Serial.println(digitalRead(PIN_PI02));
  if(digitalRead(PIN_PI01)==HIGH && digitalRead(PIN_PI02)==HIGH && previous!=11){
    Serial.println("HIGH!");
    previous=11;
        if(pos_h!=0) leave(20);
        if(pos_v!=1) down(50);
    hold(30);
    up(50);
    delay(1000);
  }
  
  if(digitalRead(PIN_PI01)==LOW && digitalRead(PIN_PI02)==LOW  && previous!=0){
        Serial.println("LOW!");
        previous=0;
    if(pos_h!=1) hold(30);
    if(pos_v!=0) up(30); 
    down(50);
    leave(1200);
  }
  
  if(digitalRead(PIN_PI01)==HIGH && digitalRead(PIN_PI02)==LOW  && previous!=10){
        Serial.println("MIXED!");
        previous=10;
    ended=1;
        if(pos_v!=0) up(30);
    if(pos_h!=1) hold(30);
    delay(1000);
  }
  }
  else{
    if(digitalRead(PIN_PI01)!=LOW || digitalRead(PIN_PI02)!=LOW)
    ended=0;
  }
  
}

void up(int unit_delay_time){
  for (int i=minimum; i<maximum; i++){
      wrist.write(i); //servo rotates at full speed to the right
      delay(unit_delay_time);
  }
  pos_v=0;
}

void down(int unit_delay_time){
    for (int i=maximum; i>minimum; i--){
      wrist.write(i); //servo rotates at full speed to the right
      delay(unit_delay_time);
    }
  pos_v=1;
}

void hold(int unit_delay_time){
    for(int i=0; i<90; i++){
      fingure.write(i);
      delay(unit_delay_time);
    }
    delay(800);
  pos_h=1;
}

void leave(int delay_time){
  fingure.write(0);
  delay(delay_time);
  pos_h=0;
}
