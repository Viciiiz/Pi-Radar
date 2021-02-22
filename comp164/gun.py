#!/usr/bin/python
import time
import RPi.GPIO as GPIO
import sys

#create 3 function:
	# safe()
	# fire()
	# rifle()

def safe():
	print ("9")
	time.sleep(10)

def fire():
	count = 0
	while count < 3:
		for i in range (90, 20, -1):	# take a bullet (servo 4)
			duty_c = i/18.0 + 2.0
			my_pwm4.ChangeDutyCycle(duty_c)
			time.sleep(0.03)

		time.sleep(2)

		for i in range (20, 90, 1):
			duty_c = i/18.0 + 2.0
			my_pwm4.ChangeDutyCycle(duty_c)
			time.sleep(0.03)

		time.sleep(4)

		distance = ultrasonic()
		#print distance
		if distance > 90:
			break
		else:
			count+=1

	if count == 3: # if we shoot three times and the object is still there, rifle
		distance = ultrasonic()
		if distance < 90:
			rifle()
			count+=1

	print (count)

def ultrasonic():
	GPIO.output(TRIG,True)
	time.sleep(0.00001)
	GPIO.output(TRIG,False)
	while GPIO.input(ECHO) == 0:
		pulse_start = time.time()

	while GPIO.input(ECHO) == 1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance = round(distance,2)
	return distance


def rifle():
	for i in range (90, 150, 1): # take multiple bullets
		duty_c = i/18.0 + 2
		my_pwm4.ChangeDutyCycle(duty_c)
		time.sleep(0.03)

	time.sleep(5)

	for i in range (150,90, -1):
		duty_c = i/18.0 + 2
		my_pwm4.ChangeDutyCycle(duty_c)
		time.sleep(0.03)

	print("5")
	time.sleep(1)

#---------------------------------------------------
# BEGINNING OF MAIN
#--------------------------------------------------

GPIO.setmode(GPIO.BCM)

#ultrasonic set up
TRIG = 23
ECHO = 24
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG,False)

# servo 2 set up (gun aim)
servo2 = 27
GPIO.setup(servo2,GPIO.OUT)
my_pwm2 = GPIO.PWM(servo2,50)
my_pwm2.start((75/18.0)+2.0) # gun aims straight (90 degree)

# take input from command line
gunStatus = sys.argv[1]
servoPos = float(sys.argv[2])

# make sure to deactivate gun (servo 3)
servo3 = 22
GPIO.setup(servo3,GPIO.OUT)
my_pwm3 = GPIO.PWM(servo3,50)
my_pwm3.start((80/18.0)+2.0) # servo at around 160 degree

# set up servo 4 (for adding bullets)
servo4 = 18
GPIO.setup(servo4,GPIO.OUT)
my_pwm4 = GPIO.PWM(servo4,50)
my_pwm4.start((90.0/18.0)+2.0) # servo at 90 degree


# aim
pos = 75
increment = 0
servo1Angle = (servoPos - 2) * 18.0
servo1Angle = int(servo1Angle)
if pos > servo1Angle:
	for i in range (pos,servo1Angle,-1):
		duty_c = (i+15)/18.0 + 2.0
		my_pwm2.ChangeDutyCycle(duty_c)
		increment+=1
		time.sleep(0.03)
	pos-=increment

elif pos < servo1Angle:
	for i in range (pos,servo1Angle,1):
		duty_c = (i+15)/18.0 + 2.0
		my_pwm2.ChangeDutyCycle(duty_c)
		increment += 1
		time.sleep(0.03)
	pos+=increment

time.sleep(1)

# activate gun according to user input
if gunStatus == "SAFE":
	safe()
elif gunStatus == "FIRE":
	for i in range (80, 15, -1): # activate switch (servo 3)
		duty_c = i/18.0 + 2.0
		my_pwm3.ChangeDutyCycle(duty_c)
		time.sleep(0.03)

	time.sleep(1)
	fire()

	for i in range (15, 80, 1): # deactivate switch (servo 3)
		duty_c = i/18.0 + 2.0
		my_pwm3.ChangeDutyCycle(duty_c)
		time.sleep(0.03)

elif gunStatus == "RIFLE":
	for i in range (80, 15, -1): # activate switch (servo 3)
		duty_c = i/18.0 + 2.0
		my_pwm3.ChangeDutyCycle(duty_c)
		time.sleep(0.03)

	time.sleep(1)
	rifle()

	for i in range (15, 80, 1): # deactivate switch (servo 3)
		duty_c = i/18.0 + 2.0
		my_pwm3.ChangeDutyCycle(duty_c)
		time.sleep(0.03)

# gun aims back at the center
if pos > 75:
	for i in range (pos,75,-1):
		duty_c = i/18.0 + 2
		my_pwm2.ChangeDutyCycle(duty_c)
		time.sleep(0.03)

elif pos < 75:
	for i in range (pos,75,1):
		duty_c = i/18.0 + 2
		my_pwm2.ChangeDutyCycle(duty_c)
		time.sleep(0.03)

my_pwm2.stop()
my_pwm3.stop()
my_pwm4.stop()

GPIO.cleanup()
