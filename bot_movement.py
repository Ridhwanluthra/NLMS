from gpiozero import Motor
#from gpiozero.Pin import
#import RPi.GPIO as GPIO
from encoders import d_move, refresh

ml = Motor(2, 3)
mr = Motor(14, 15)
ml.stop()
mr.stop()
"""
I  am assuming that the initial location of the bot
is facing upwards at 0,0
the bot can make only 90 degree turns
"""



direction = 'n' # n,e,w,s for different locations that it is facing
usfront = 20

try:
	# ADD SOMETHING TO DO WHEN US IS LESS THAN 5;
    def forward():
    	if usfront <= 5:
            print "error"
    	else:
            ml.forward()
            mr.forward()

    def sstop():
        ml.stop()
        mr.stop()
    def turn_left():
        while d_move()[0] < 12 and d_move()[1] < 12:
            ml.backward()
            mr.forward()
        sstop()
        refresh()

    def turn_right():
        while d_move()[0] < 12 and d_move()[1] < 12:
            ml.forward()
            mr.backward()
        sstop()
        refresh()

    def up():
        look_up()
        while d_move()[0] <= 20 and d_move()[1] <= 20:
            forward()
        sstop()
        refresh()

    def left():
        look_left()
        while d_move()[0] <= 20 and d_move()[1] <= 20:
            forward()
        sstop()
        refresh()

    def right():
        look_right()
        while d_move()[0] <= 20 and d_move()[1] <= 20:
            forward()
        sstop()
        refresh()

    def down():
        look_down()
        while d_move()[0] <= 20 and d_move()[1] <= 20:
            forward()
        sstop()
        refresh()

    def look_up():
        global direction
        if (direction == 'n'):
            pass
        elif (direction == 'e'):
            turn_left()
        elif (direction == 'w'):
            turn_right()
        elif (drection == 's'):
            turn_left()
	    turn_left()
        direction = 'n'

    def look_down():
        global direction
        if (direction == 'n'):
            turn_left()
            turn_left()
        elif (direction == 'e'):
            turn_right()
        elif (direction == 'w'):
            turn_left()
        elif (drection == 's'):
            pass
        direction = 's'

    def look_left():
        global direction
        if (direction == 'n'):
            turn_left()
        elif (direction == 'e'):
            turn_left()
            turn_left()
        elif (direction == 'w'):
            pass
        elif (drection == 's'):
            turn_right()
        direction = 'w'

    def look_right():
        global direction
        if (direction == 'n'):
            turn_right()
        elif (direction == 'e'):
            pass
        elif (direction == 'w'):
            turn_left()
            turn_left()
        elif (drection == 's'):
            turn_left()
        direction = 'e'
except KeyboardInterrupt:
    print "cleaning"
finally:
    #GPIO.cleanup()
    print"check it"
