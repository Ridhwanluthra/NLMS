"""
*
* Project Name: 	House Probing Robot for The Elderly

* Author List: 		Ridhwan Luthra

* Filename: 		encoders.py

* Functions: 		d_move, refresh

* Global Variables:	new_righten, new_leften, counter_left, counter_right
*
"""

import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)

leften = 17
righten = 18
dps = 38.000/18.000  #distance per spoke
gpio.setup(leften,gpio.IN)
gpio.setup(righten,gpio.IN)
counter_left = 0
counter_right = 0
new_righten = 0
new_leften = 0
def d_move():
	"""
    *
    * Function Name: 		d_move
    
    * Input: 				NONE
    
    * Output: 				[,] -> distance covered by left and right wheel in a list 
    
    * Logic: 				this function detects the change in the state of the position encoders
    						for every change in state a counter is increased using which the distance covered
    						at any instance can be calculated
    
    * Example Call:			d_move()
    *
    """
    gpio.setmode(gpio.BCM)
    while True:
        global new_leften
        global new_righten
        global counter_left
        global counter_right
        old_leften = new_leften
        old_righten = new_righten
        new_leften = gpio.input(leften)
        new_righten = gpio.input(righten)
        if ((new_leften == 1 and old_leften == 0) or (new_leften == 0 and old_leften == 1)):
            counter_left += 1
            #print "left counter "
            #print counter_left*dps/2
        if ((new_righten == 1 and old_righten == 0) or (new_righten == 0 and old_righten == 1)):
            counter_right += 1
            #print "right coutner "
            #print counter_right*dps/2
        return [counter_left*dps/2, counter_right*dps/2]

def refresh():
	"""
    *
    * Function Name: 		refresh
    
    * Input: 				NONE
    
    * Output: 				NONE
    
    * Logic: 				this function resets the values of counter and the state of the encoders
    
    * Example Call:			refresh()
    *
    """
    global new_leften
    global new_righten
    global counter_left
    global counter_right
    counter_left = 0
    counter_right = 0
    new_righten = 0
    new_leften = 0
