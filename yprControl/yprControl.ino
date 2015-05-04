#include <AutoDriver.h>
#include <dSPINConstants.h>
#include <Servo.h>

//Declare servos
Servo pitchServo;
Servo rollServo;

//Declare stepper motor driver
AutoDriver yawMotor(10, 6);

String command; //Command is yaw:pitch:roll and each is 3 digits at most
int y, p, r;

void setup() {
  //Create a serial connection to the arduino w/ baud rate 9600
  Serial.begin(115200);
  Serial.println("Initialization");
  
  //Pin conigurations and initial angles for servos
  pitchServo.attach(3);
  pitchServo.write(150);
  
  rollServo.attach(2);
  rollServo.write(100);
  
  //Setup stepper motor driver
  yawMotor.configSyncPin(BUSY_PIN, 0);
  yawMotor.configStepMode(STEP_FS_16);
  yawMotor.setMaxSpeed(1000);
  yawMotor.setFullSpeed(1000);
  yawMotor.setAcc(1000);
  yawMotor.setDec(1000);
  yawMotor.setSlewRate(SR_530V_us);
  yawMotor.goHome();
}

void loop() {
  if(Serial.available() != 0)
  {
    y = Serial.parseInt() % 360;
    p = Serial.parseInt();
    r = Serial.parseInt();
    pitchServo.write(p);
    rollServo.write(r);
    yawMotor.goTo(map(y, 0, 360, 0, 3200));
  }
}
