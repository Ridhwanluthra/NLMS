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
"""
# Linear distance between each cell
lm = 32
# Rotational distance in degree for 90 degree turns. It differs due to calliberaton errors
rm = 95

try:

    """
        *
        * Function Name:    forward
        
        * Input:        None
        
        * Output:       None
        
        * Logic:        Makes both motors move forward at a specific speed.
        
        * Example Call:     forward()
        *
        """
    def forward():
        ml.forward(0.3)
        mr.forward(0.3)


    """
        *
        * Function Name:    backward
        
        * Input:        None
        
        * Output:       None
        
        * Logic:        Makes both motors move backward at a specific speed.
        
        * Example Call:     backward()
        *
        """

    def backward():
        ml.backward(0.3)
        mr.backward(0.3)
        

    """
        *
        * Function Name:    sstop
        
        * Input:        None
        
        * Output:       None
        
        * Logic:        Makes both motors stop.
        
        * Example Call:     sstop()
        *
        """

    def sstop():
        ml.stop()
        mr.stop()

    """
        *
        * Function Name:    move_forward
        
        * Input:        distance to be travelled in forward direction
        
        * Output:       None
        
        * Logic:        We have used position encoders to give us the exact distance moved by the wheels.
                        So, we use their data to make to bot move a particular distance in forward direction.
        
        * Example Call:     move_forward(40)
        *
        """

    def move_forward(distance):
        while encoders.d_move()[0] <= distance and encoders.d_move()[1] <= distance:
            forward()
        sstop()
        # Refreshing encoders to better calliberate their readings.
        encoders.refresh()


    """
        *
        * Function Name:    move_backward
        
        * Input:        distance to be travelled in backward direction
        
        * Output:       None
        
        * Logic:        We have used position encoders to give us the exact distance moved by the wheels.
                        So, we use their data to make to bot move a particular distance in backward direction.
        
        * Example Call:     move_backward(40)
        *
        """

    def move_backward(distance):
        while encoders.d_move()[0] <= distance and encoders.d_move()[1] <= distance:
            backward()
        sstop()
        # Refreshing encoders to better calliberate their readings.
        encoders.refresh()

     """
        *
        * Function Name:    turn_left
        
        * Input:        degrees you want to make the robot turn in left direction
        
        * Output:       None
        
        * Logic:        We have used position encoders to give us the exact distance moved by the wheels.
                        So, we use their data to make to bot turn certain degrees in left direction.
        
        * Example Call:     turn_left(90)
        *
        """

    def turn_left(degrees):
        # Because of calliberation errors and battery discharge rate, 
        #we move the bot more degrees than specified to calliberate the movement
        distance = (degrees + 3) * 0.1876
	print "in turn left"
        while encoders.d_move()[0] < distance and encoders.d_move()[1] < distance:
            ml.backward(0.3)
            mr.forward(0.3)
        sstop()
        encoders.refresh()
        # Giving the bot some time to recover from this movement
        sleep(1)

"""
        *
        * Function Name:    turn_right
        
        * Input:        degrees you want to make the robot turn in right direction
        
        * Output:       None
        
        * Logic:        We have used position encoders to give us the exact distance moved by the wheels.
                        So, we use their data to make to bot turn certain degrees in right direction.
        
        * Example Call:     turn_right(90)
        *
        """

    def turn_right(degrees):
        distance = (degrees + 4) * 0.1876
        while encoders.d_move()[0] < distance and encoders.d_move()[1] < distance:
            ml.forward(0.3)
            mr.backward(0.3)
        sstop()
        encoders.refresh()
        sleep(1)


"""
        *
        * Function Name:    first_up
        
        * Input:        None
        
        * Output:       None
        
        * Logic:        We first make our bot look in the right direction.
                        We have used position encoders to give us the exact distance moved by the wheels.
                        So, we use their data to make to bot make the bot move distance equivalent to one cell.
        
        * Example Call:     first_up()
        *
        """

    def first_up():
        look_up()
        while encoders.d_move()[0] <= lm and encoders.d_move()[1] <= lm:
            forward()
        sstop()
        encoders.refresh()
	sleep(1)

"""
        *
        * Function Name:    first_left
        
        * Input:        None
        
        * Output:       None
        
        * Logic:        We first make our bot look in the correct direction.
                        We have used position encoders to give us the exact distance moved by the wheels.
                        So, we use their data to make to bot make the bot move distance equivalent to one cell.
        
        * Example Call:     first_left()
        *
        """

    def first_left():
        look_left()
        while encoders.d_move()[0] <= lm and encoders.d_move()[1] <= lm:
            forward()
        sstop()
        encoders.refresh()
	sleep(1)

    """
        *
        * Function Name:    first_right
        
        * Input:        None
        
        * Output:       None
        
        * Logic:        We first make our bot look in the correct direction.
                        We have used position encoders to give us the exact distance moved by the wheels.
                        So, we use their data to make to bot make the bot move distance equivalent to one cell.
        
        * Example Call:     first_right()
        *
        """

    def first_right():
        look_right()
        while encoders.d_move()[0] <= lm and encoders.d_move()[1] <= lm:
            forward()
        sstop()
        encoders.refresh()
	sleep(1)

"""
        *
        * Function Name:    first_down
        
        * Input:        None
        
        * Output:       None
        
        * Logic:        We first make our bot look in the correct direction.
                        We have used position encoders to give us the exact distance moved by the wheels.
                        So, we use their data to make to bot make the bot move distance equivalent to one cell.
        
        * Example Call:     first_down()
        *
        """

    def first_down():
        look_down()
        while encoders.d_move()[0] <= lm and encoders.d_move()[1] <= lm:
            forward()
        sstop()
        encoders.refresh()
	sleep(1)

    """
        *
        * Function Name:    up
        
        * Input:        None
        
        * Output:       Returns true or false depending on presence of anomaly
        
        * Logic:        We first make our bot look in the correct direction.
                        We then check for presence of anomaly. If not found, then we move up.
        
        * Example Call:     up()
        *
        """

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

    """
        *
        * Function Name:    left
        
        * Input:        None
        
        * Output:       Returns true or false depending on presence of anomaly
        
        * Logic:        We first make our bot look in the correct direction.
                        We then check for presence of anomaly. If not found, then we move up.
        
        * Example Call:     left()
        *
        """

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

    """
        *
        * Function Name:    right
        
        * Input:        None
        
        * Output:       Returns true or false depending on presence of anomaly
        
        * Logic:        We first make our bot look in the correct direction.
                        We then check for presence of anomaly. If not found, then we move up.
        
        * Example Call:     right()
        *
        """

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

    """
        *
        * Function Name:    down
        
        * Input:        None
        
        * Output:       Returns true or false depending on presence of anomaly
        
        * Logic:        We first make our bot look in the correct direction.
                        We then check for presence of anomaly. If not found, then we move up.
        
        * Example Call:     down()
        *
        """

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

    """
        *
        * Function Name:    look_up
        
        * Input:        None
        
        * Output:       None
        
        * Logic:        Depending on bot's current direction, it makes it turn towards north
        
        * Example Call:     look_up()
        *
        """

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

    """
        *
        * Function Name:    look_down
        
        * Input:        None
        
        * Output:       None
        
        * Logic:        Depending on bot's current direction, it makes it turn towards south
        
        * Example Call:     look_down()
        *
        """

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

    """
        *
        * Function Name:    look_left
        
        * Input:        None
        
        * Output:       None
        
        * Logic:        Depending on bot's current direction, it makes it turn towards west
        
        * Example Call:     look_left()
        *
        """

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

    """
        *
        * Function Name:    look_right
        
        * Input:        None
        
        * Output:       None
        
        * Logic:        Depending on bot's current direction, it makes it turn towards east
        
        * Example Call:     look_right()
        *
        """

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
