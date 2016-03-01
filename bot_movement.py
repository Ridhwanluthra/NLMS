"""
*
* Project Name: 	House Probing Robot for The Elderly

* Author List: 		Ridhwan Luthra

* Filename: 		bot_movement.py

* Functions: 		forward, backward, sstop, move_forward, move_backward,
                        turn_left, turn_right, soft_left, soft_right, first_up,
                        first_down, first_left, first_right, up, down, left, right,
                        look_up, look_down, look_left, look_right

* Global Variables:	lm, rm
*
"""
from gpiozero import Motor
#from gpiozero.Pin import
#import RPi.GPIO as GPIO
import encoders
from ultrasonic import ultra
import anomaly
from bot_globals import bot
from time import sleep

mr = Motor(3, 2)
ml = Motor(15, 14)
ml.stop()
mr.stop()
"""
I  am assuming that the initial location of the bot
is facing upwards at 0,0
the bot can make only 90 degree turns
"""

lm = 20
rm = 90

try:
    def forward():
        ml.forward(0.553)
        mr.forward(0.5)

    def backward():
        ml.backward(0.553)
        mr.backward(0.5)
        
    def sstop():
        ml.stop()
        mr.stop()

    def move_forward(distance):
        while encoders.d_move()[0] <= distance and encoders.d_move()[1] <= distance:
            forward()
        sstop()
        encoders.refresh()

    def move_backward(distance):
        while encoders.d_move()[0] <= distance and encoders.d_move()[1] <= distance:
            backward()
        sstop()
        encoders.refresh()

    def turn_left(degrees):
        distance = degrees * 0.1876
	print "in turn left"
        while encoders.d_move()[0] < distance and encoders.d_move()[1] < distance:
            ml.backward(0.555)
            mr.forward(0.5)
        sstop()
        encoders.refresh()
        sleep(1)

    def turn_right(degrees):
        distance = (degrees) * 0.1876
        while encoders.d_move()[0] < distance and encoders.d_move()[1] < distance:
            ml.forward(0.6)
            mr.backward(0.5)
        sstop()
        encoders.refresh()
        sleep(1)
        
    def soft_right():
        while encoders.d_move()[0] < 15:
            ml.forward(0.555)
            mr.stop()
        sstop()
        encoders.refresh()
        sleep(1)

    def soft_left():
        while encoders.d_move()[0] < 15:
            ml.stop()
            mr.forward(0.5)
        sstop()
        encoders.refresh()
        sleep(1)

    def first_up():
        look_up()
        while encoders.d_move()[0] <= lm and encoders.d_move()[1] <= lm:
            forward()
        sstop()
        encoders.refresh()

    def first_left():
        look_left()
        while encoders.d_move()[0] <= lm and encoders.d_move()[1] <= lm:
            forward()
        sstop()
        encoders.refresh()

    def first_right():
        look_right()
        while encoders.d_move()[0] <= lm and encoders.d_move()[1] <= lm:
            forward()
        sstop()
        encoders.refresh()

    def first_down():
        look_down()
        while encoders.d_move()[0] <= lm and encoders.d_move()[1] <= lm:
            forward()
        sstop()
        encoders.refresh()

    def up():
        look_up()
        if anomaly.check() == True:
            while encoders.d_move()[0] <= lm and encoders.d_move()[1] <= lm:
                forward()
            sstop()
            encoders.refresh()
            return True
        else:
            return False

    def left():
        look_left()
        if anomaly.check() == True:
            while encoders.d_move()[0] <= lm and encoders.d_move()[1] <= lm:
                forward()
            sstop()
            encoders.refresh()
            return True
        else:
            return False

    def right():
        look_right()
        if anomaly.check() == True:
            while encoders.d_move()[0] <= lm and encoders.d_move()[1] <= lm:
                forward()
            sstop()
            encoders.refresh()
            return True
        else:
            return False

    def down():
        look_down()
        if anomaly.check() == True:
            while encoders.d_move()[0] <= lm and encoders.d_move()[1] <= lm:
                forward()
            sstop()
            encoders.refresh()
            return True
        else:
            return False

    def look_up():
        if (bot.direction == 'n'):
            pass
        elif (bot.direction == 'e'):
            turn_left(rm)
            #soft_left()
        elif (bot.direction == 'w'):
            turn_right(rm)
            #soft_right()
        elif (bot.direction == 's'):
            turn_left(rm)
	    turn_left(rm)
            #soft_left()
            #soft_left()
        bot.direction = 'n'

    def look_down():
        if (bot.direction == 'n'):
            turn_left(rm)
            turn_left(rm)
            #soft_left()
            #soft_left()
        elif (bot.direction == 'e'):
            turn_right(rm)
            #soft_right()
        elif (bot.direction == 'w'):
            turn_left(rm)
            #soft_left()
        elif (bot.direction == 's'):
            pass
        bot.direction = 's'

    def look_left():
        if (bot.direction == 'n'):
            turn_left(rm)
            #soft_left()
        elif (bot.direction == 'e'):
            turn_left(rm)
            turn_left(rm)
            #soft_left()
            #soft_left()
        elif (bot.direction == 'w'):
            pass
        elif (bot.direction == 's'):
            turn_right(rm)
            #soft_right()
        bot.direction = 'w'

    def look_right():
        if (bot.direction == 'n'):
            turn_right(rm)
            #soft_right()
        elif (bot.direction == 'e'):
            pass
        elif (bot.direction == 'w'):
            turn_left(rm)
            turn_left(rm)
            #soft_left()
            #soft_left()
        elif (bot.direction == 's'):
            turn_left(rm)
            #soft_left()
        bot.direction = 'e'
except KeyboardInterrupt:
    print "cleaning"
finally:
    #GPIO.cleanup()
    print"check it"
