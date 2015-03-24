#/usr/bin/env python

__author__ = "Matt Anderson"

#Servos will use pins 21, 22 and 23 for servo pwm signals
#PWM will be generated using the pi-blaster: https://github.com/sarfata/pi-blaster

#Scalar values to scale pwm duty cycles to degrees
maxServoPwm = 0.3 #30%
minServoPwm = 0.05 #5%
maxServoDegrees = 180
minServoDegrees = 0

#Servo pin numbers
yawServo = 21
pitchServo = 22
rollServo = 23

def init(): 
    f = open('/dev/pi-blaster', 'w')
    f.write(str(yawServo) + '=0.1\n') #initialize yawServo
    f.write(str(pitchServo) + '=0.1\n') #initialize pitchServo
    f.write(str(rollServo) + '=0.1\n') #initialize rollServo
    f.close()
    
def setServo(servo, degree):
    f = open('/dev/pi-blaster', 'w')
    degreeRange = maxServoDegrees - minServoDegrees
    pwmRange = maxServoPwm - minServoDegrees
    pwm = (((degree - minServoDegrees) * pwmRange) / degreeRange) + minServoPwm
    servoCommand = str(servo) + '=' + str(pwm) + '\n'
    f.write(servoCommand)
    f.close()
    
def exit():
    f = open('/dev/pi-blaster', 'w') 
    f.write('release ' + str(yawServo) + '\n')
    f.write('release ' + str(pitchServo) + '\n')
    f.write('release ' + str(rollServo) + '\n')
    f.close()

if __name__ == "__main__":
    init() 
    command = ''

    print('y angle for yaw servo')
    print('p angle for pitch servo')
    print('r angle for roll servo')
    while command != 'exit':
        command = raw_input('command: ') 
        if command != 'exit':
            angle = int(command[2:])
            if command[0] == 'y':
                setServo(yawServo, angle)
                print('Setting yaw servo to ' + str(angle) + ' degrees')
            elif command[0] == 'p':
                setServo(pitchServo, angle)
                print('Setting pitch servo to ' + str(angle) + ' degrees')
            elif command[0] == 'r':
                setServo(rollServo, angle)
                print('Setting roll servo to ' + str(angle) + ' degrees')
    
    exit()
