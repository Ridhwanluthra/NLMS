from gpiozero import Motor
#from gpiozero.Pin import
#import RPi.GPIO as GPIO
from encoders import d_move, refresh

mr = Motor(2, 3)
ml = Motor(14, 15)
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
            ml.forward(0.553)
            mr.forward(0.5)

    def sstop():
        ml.stop()
        mr.stop()
        
    def turn_left():
        while d_move()[0] < 14.6 and d_move()[1] < 14.6:
            ml.backward(0.555)
            mr.forward(0.5)
        sstop()
        refresh()

    def turn_right():
        while d_move()[0] < 14.6 and d_move()[1] < 14.6:
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
            #turn_left()
            soft_left()
        elif (direction == 'w'):
            #turn_right()
            soft_right()
        elif (direction == 's'):
            #turn_left()
	    #turn_left()
            soft_left()
            soft_left()
        direction = 'n'

    def look_down():
        global direction
        if (direction == 'n'):
            #turn_left()
            #turn_left()
            soft_left()
            soft_left()
        elif (direction == 'e'):
            #turn_right()
            soft_right()
        elif (direction == 'w'):
            #turn_left()
            soft_left()
        elif (direction == 's'):
            pass
        direction = 's'

    def look_left():
        global direction
        if (direction == 'n'):
            #turn_left()
            soft_left()
        elif (direction == 'e'):
            #turn_left()
            #turn_left()
            soft_left()
            soft_left()
        elif (direction == 'w'):
            pass
        elif (direction == 's'):
            #turn_right()
            soft_right()
        direction = 'w'

    def look_right():
        global direction
        if (direction == 'n'):
            #turn_right()
            soft_right()
        elif (direction == 'e'):
            pass
        elif (direction == 'w'):
            #turn_left()
            #turn_left()
            soft_left()
            soft_left()
        elif (direction == 's'):
            #turn_left()
            soft_left()
        direction = 'e'
except KeyboardInterrupt:
    print "cleaning"
finally:
    #GPIO.cleanup()
    print"check it"
