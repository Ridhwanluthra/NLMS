import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trig = 20
echo = 21

print "Distance Measurement In Progress"

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.output(trig, False)

try:
	print "Waiting For Sensor To Settle"

	time.sleep(2)

	GPIO.output(trig, True)
	time.sleep(0.00001)
	GPIO.output(trig, False)

	while GPIO.input(echo)==0:
	  pulse_start = time.time()

	while GPIO.input(echo)==1:
	  pulse_end = time.time()      

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration x 17150

	distance = round(distance, 2)

	print "Distance:",distance,"cm"
except:
	print "reading was interrupted"
finally:
	GPIO.cleanup()