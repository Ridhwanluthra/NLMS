from gpiozero import Motor
#from gpiozero.Pin import
#import RPi.GPIO as GPIO
from encoders import d_move, refresh
from ultrasonic import ultra
from anomaly import check
from bot_globals import bot

mr = Motor(2, 3)
ml = Motor(14, 15)
ml.stop()
mr.stop()
"""
I  am assuming that the initial location of the bot
is facing upwards at 0,0
the bot can make only 90 degree turns
"""

lm = 20
rm = 14.6

try:
    def forward():
        ml.forward(0.553)
        mr.forward(0.5)

    def sstop():
        ml.stop()
        mr.stop()

    def turn_left():
        while d_move()[0] < rm and d_move()[1] < rm:
            ml.backward(0.555)
            mr.forward(0.5)
        sstop()
        refresh()

    def turn_right():
        while d_move()[0] < rm and d_move()[1] < rm:
            ml.forward(0.555)
            mr.backward(0.5)
        sstop()
        refresh()
        
    def soft_right():
        while d_move()[0] < 15:
            ml.forward(0.555)
            mr.stop()
        sstop()
        refresh()

    def soft_left():
        while d_move()[0] < 15:
            ml.stop()
            mr.forward(0.5)
        sstop()
        refresh()

    def up():
        look_up()
        if check() == True:
	        while d_move()[0] <= lm and d_move()[1] <= lm:
	            forward()
        	sstop()
        	refresh()
        	return True
        else:
        	return False

    def left():
        look_left()
        if check() == True:
	        while d_move()[0] <= lm and d_move()[1] <= lm:
	            forward()
	        sstop()
	        refresh()
	        return True
	    else:
	    	return False

    def right():
        look_right()
        if check() == True
	        while d_move()[0] <= lm and d_move()[1] <= lm:
	            forward()
	        sstop()
	        refresh()
	        return True
	    else:
	    	return False

    def down():
        look_down()
        if check() == True:
	        while d_move()[0] <= lm and d_move()[1] <= lm:
	            forward()
	        sstop()
	        refresh()
	        return True
	    else:
	    	return False

    def look_up():
        if (bot.direction == 'n'):
            pass
        elif (bot.direction == 'e'):
            turn_left()
            #soft_left()
        elif (bot.direction == 'w'):
            turn_right()
            #soft_right()
        elif (bot.direction == 's'):
            turn_left()
	    turn_left()
            #soft_left()
            #soft_left()
        bot.direction = 'n'

    def look_down():
        if (bot.direction == 'n'):
            turn_left()
            turn_left()
            #soft_left()
            #soft_left()
        elif (bot.direction == 'e'):
            turn_right()
            #soft_right()
        elif (bot.direction == 'w'):
            turn_left()
            #soft_left()
        elif (bot.direction == 's'):
            pass
        bot.direction = 's'

    def look_left():
        if (bot.direction == 'n'):
            turn_left()
            #soft_left()
        elif (bot.direction == 'e'):
            turn_left()
            turn_left()
            #soft_left()
            #soft_left()
        elif (bot.direction == 'w'):
            pass
        elif (bot.direction == 's'):
            turn_right()
            #soft_right()
        bot.direction = 'w'

    def look_right():
        if (bot.direction == 'n'):
            turn_right()
            #soft_right()
        elif (bot.direction == 'e'):
            pass
        elif (bot.direction == 'w'):
            turn_left()
            turn_left()
            #soft_left()
            #soft_left()
        elif (bot.direction == 's'):
            turn_left()
            #soft_left()
        bot.direction = 'e'
except KeyboardInterrupt:
    print "cleaning"
finally:
    #GPIO.cleanup()
    print"check it"
