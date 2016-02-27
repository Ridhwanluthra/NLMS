from gpiozero import Motor
#from gpiozero.Pin import
import RPi.GPIO as gpio
#from encoders import d_move, refresh

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

leften = 18
righten = 17
dps = 30.000/24.000  #distance per spoke
gpio.setup(leften,gpio.IN)
gpio.setup(righten,gpio.IN)
counter_left = 0
counter_right = 0

def left_call(channel):
    counter_left += 1

def right_call(channel):
    counter_right += 1

def refresh():
    global counter_left
    global counter_right
    counter_left = 0
    counter_right = 0

gpio.add_event_detect(leften, gpio.both, callback=left_call)
gpio.add_event_detect(righten, gpio.both, callback = right_call)

try:
	# ADD SOMETHING TO DO WHEN US IS LESS THAN 5;
    def forward():
    	if usfront <= 5:
            print "error"
    	else:
            ml.forward(0.5)
            mr.forward(0.5)

    def sstop():
        ml.stop()
        mr.stop()
    def turn_left():
        global counter_left
        global counter_right
        ml.backward(0.5)
        mr.forward(0.5)
        while True:
            if counter_left >= 10 and counter_right >= 10:
                break    
        sstop()
        refresh()

    def turn_right():
        global counter_left
        global counter_right
        ml.forward(0.5)
        mr.backward(0.5)
        while True:
            if counter_left >= 10 and counter_right >= 10:
                break
        sstop()
        refresh()

    def up():
        global counter_left
        global counter_right
        look_up()
        forward()
        while True:
            if counter_left >= 24 and counter_right >= 24:
                break
        sstop()
        refresh()

    def left():
        global counter_left
        global counter_right
        look_left()
        forward()
        while True:
            if counter_left >= 24 and counter_right >= 24:
                break
        sstop()
        refresh()

    def right():
        global counter_left
        global counter_right
        look_right()
        forward()
        while True:
            if counter_left >= 24 and counter_right >= 24:
                break
        sstop()
        refresh()

    def down():
        global counter_left
        global counter_right
        look_down()
        forward()
        while True:
            if counter_left >= 24 and counter_right >= 24:
                break
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
        elif (direction == 's'):
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
        elif (direction == 's'):
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
        elif (direction == 's'):
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
        elif (direction == 's'):
            turn_left()
        direction = 'e'
except KeyboardInterrupt:
    print "cleaning"
finally:
    #GPIO.cleanup()
    print"check it"
