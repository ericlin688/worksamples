//This code allows ofr user control of this apparatus:
//https://shop.barnabasrobotics.com/collections/kits-1/products/barnabas-arduino-compatible-robot-arm-kit-with-joystick-control-ages-11

#include <Servo.h>
//claw motor min angle 55 (53:75)
//mainarm min angle 10 max 150 
//extender max angle 120 min angle is mainarm dependant (coupled motors)
Servo claw;
Servo mainarm;
Servo extender;
Servo base;

//m=m+|a-m|/(a-m) PID protocall

//default position for each motor
int claw_motor=55;
int base_motor=90;
int arm_motor=95;
int ext_motor=95;

//set time interval
int wait=10;

void setup() {
  //Serial.begin(9600);test output
  
  //attach motors
  claw.attach(11);
  mainarm.attach(10);
  extender.attach(9);
  base.attach(6);

  //Setup rotor pins
  pinMode(A0,INPUT);
  pinMode(A1,INPUT);
  pinMode(A2,INPUT);
  pinMode(A3,INPUT);

  //Set motors to default values
  claw.write(claw_motor);
  base.write(base_motor);
  mainarm.write(arm_motor);
  extender.write(arm_motor);

}

void loop() {
  //Use PID to move each motor to position set by rotor
  int x=analogRead(A0);
  int claw_angle=map(x,10,1013,50,75);
  if (claw_angle!=claw_motor){
    claw_motor=claw_motor+abs(claw_angle-claw_motor)/(claw_angle-claw_motor);
    claw.write(claw_motor);
  }
  int y=analogRead(A3);
  int base_angle=map(y,10,1013,30,150);
  if (base_angle!=base_motor){
    base_motor=base_motor+abs(base_angle-base_motor)/(base_angle-base_motor);
    base.write(base_motor);
  }
  int z=analogRead(A1);
  int arm_angle=map(z,10,1013,90,120);
  if (arm_angle!=arm_motor){
    arm_motor=arm_motor+abs(arm_angle-arm_motor)/(arm_angle-arm_motor);
    mainarm.write(arm_motor);
    extender.write(arm_motor+(ext_motor-90));
  }
  int w=analogRead(A2);
  int ext_angle=map(w,10,1013,90,285-1.5*arm_motor); //150
  if (ext_angle!=ext_motor){
    ext_motor=ext_motor+abs(ext_angle-ext_motor)/(ext_angle-ext_motor);
    extender.write(arm_motor+(ext_motor-90));
  }
  delay(wait);

}
