import bot_movement as bm
from ultrasonic import ultra
import RPi.GPIO as gpio
from time import sleep
from traversal import go_to_origin

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
        gpio.output(pin1, 1)
        gpio.output(pin2, 1)
        #for the time that is enough
        sleep(15)

def drop_the_block():
        gpio.output(pin1, 0)
        gpio.output(pin2, 0)
        #for the time that is enough
        sleep(15)

def rest():
        gpio.output(pin1, 1)
        gpio.output(pin2, 0)
        #if needed
        sleep(10)

def correct_the_location():
        try:
                pin1 = 5
                pin2 = 6

                gpio.setmode(gpio.BCM)

                gpio.setup(pin1, gpio.OUT)
                gpio.setup(pin2, gpio.OUT)
                gpio.output(pin1, 0)
                gpio.output(pin2, 0)

                distance = ultra()
                if distance <= the_required_distance:
                        #have to create this function in bot_movement
                        backward(distance - the_required_distance)
                else:
                        #have to create this function in bot_movement
                        forward(distance - the_required_distance)

                pick_the_block()
                drop_the_block()
                rest()
                go_to_origin()
        except KeyboardInterrupt:
                gpio.cleanup()
        finally:
                gpio.cleanup()
