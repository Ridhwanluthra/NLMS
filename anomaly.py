import bot_movement as bm
from ultrasonic import ultra
import RPi.GPIO as gpio
from time import sleep
#from traversal import go_to_origin

pin1 = 7
pin2 = 8     
gpio.setmode(gpio.BCM)
gpio.setup(pin1, gpio.OUT)
gpio.setup(pin2, gpio.OUT)


def check():
	if ultra() <= 20:
		return False
	else:
		return True

"""
now i will first chec the distance and then get to a certain distance
then i will go down and hold and lift and then
start movement
when reached the location then drop and go to origin #for now
later go to the same place and start again
"""

def pick_the_block():
        global pin1
        global pin2
        gpio.output(pin1, 1)
        gpio.output(pin2, 1)
        #for the time that is enough
        sleep(15)

def drop_the_block():
        global pin1
        global pin2
        gpio.output(pin1, 0)
        gpio.output(pin2, 0)
        #for the time that is enough
        sleep(15)

def rest():
        global pin1
        global pin2
        gpio.output(pin1, 1)
        gpio.output(pin2, 0)
        #if needed
        sleep(10)

def correct_the_location():
        global pin1
        global pin2
        try:
                gpio.output(pin1, 0)
                gpio.output(pin2, 0)

                distance = ultra()
                the_required_distance = 10
                if distance <= the_required_distance-3:
                        #have to create this function in bot_movement
                        backward(distance - the_required_distance+3)
                else:
                        #have to create this function in bot_movement
                        forward(distance - the_required_distance+3)
		pick_the_block()
		#add going to the correct location first
		drop_the_block()
		rest()
		"""                
		if(ultra()<the_required_distance):
                        print "gone in"
                        pick_the_block()
                        sleep(10)
                        drop_the_block()
                        sleep(10)
                        rest()
                        sleep(10)
                else:
                        rest()
                        print "gone out"
		"""
                #go_to_origin()
        except KeyboardInterrupt:
                gpio.cleanup()
        finally:
                gpio.cleanup()
