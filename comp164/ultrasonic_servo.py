import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
servo1 = 17


# method to send a pulse on the ultrasonic sensor and returns the distance in cm
def ultrasonic_():
	GPIO.output(TRIG,True)
	time.sleep(0.00001)
	GPIO.output(TRIG,False)

	while GPIO.input(ECHO) == 0:
		pulse_start = time.time()

	while GPIO.input(ECHO) == 1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start #time
	distance = pulse_duration * 17150
	distance = round(distance,2)
	return distance


#------------------------------------------------------
# this is the start of the main program
#------------------------------------------------------


time.sleep(5)

GPIO.setup(servo1,GPIO.OUT)
my_pwm = GPIO.PWM(servo1,50)
duty_c = 30.0/18.0 + 2 #2.2
my_pwm.start(duty_c) # servo starts full left (0 degree)


GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG,False)

time.sleep(2)
fireDistance = 115 # minimum distance
returnServo1Position = 0


# loop the sensor
cont = True # if set to false, break loop
while cont:
	for i in range (20,100,1): # from left to right
		duty_c = (1.0/18.0)*i  + 2.0
		my_pwm.ChangeDutyCycle(duty_c)
		returnServo1Position = duty_c # position of servo to be returned
		d = ultrasonic_() # ultrasonic sensor check and returns distance
		if d < fireDistance:
			#cont = False
			# need a statement to return the distance and the position of servo
			#print d, " ", returnServo1Position
			#my_pwm.stop()
			#GPIO.cleanup()
			#break # if within range, stop
			subprocess.call("python captureImage.py", shell = True)
			subprocess.call("python send_sms.py" , shell = True)
			execution = "python gun.py FIRE " + str(returnServo1Position)
			subprocess.call(execution, shell = True)
			subprocess.call("python ultrasonic_servo.py", shell = True)
		#fire(d) # continue to fire as long as the object is within range
		time.sleep(0.03)

	if cont == True:
		for i in range (100,20,-1): # from right to left
			duty_c = (1.0/18.0) * i + 2
			my_pwm.ChangeDutyCycle(duty_c)
			returnServo1Position = duty_c
			d = ultrasonic_()
			if d < fireDistance:
				#cont = False
				# idem as above - statement needed
				#print d, " ", returnServo1Position
				#my_pwm.stop()
				#GPIO.cleanup()
				#break
				subprocess.call("python captureImage.py",shell = True)
				subprocess.call("python send_sms.py", shell = True)
				execution = "python gun.py FIRE " + str(returnServo1Position)
				subprocess.call(execution, shell = True)
				subprocess.call("python ultrasonic_servo.py", shell = True)
			#fire(d)
			time.sleep(0.03)

my_pwm.stop()

GPIO.cleanup()
