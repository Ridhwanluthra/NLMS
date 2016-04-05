"""
*
* Project Name: 	House Probing Robot for The Elderly

* Author List: 		Ridhwan Luthra

* Filename: 		anomaly.py

* Functions: 		check, anomaly_look, anomaly_find_path, pick_the_block,
                        drop_the_block, rest, go_to_location, correct_the_location,

* Global Variables:	mapp, pin1, pin2
*
"""
from  bot_globals import bot
from ultrasonic import ultra
import RPi.GPIO as gpio
from time import sleep
import file_handling as file_h
import bot_movement as bm
import callibration as c
from click_picture import clicked

# Pins which connect Raspberry Pi to the Arduino
pin1 = 7
pin2 = 8
gpio.setmode(gpio.BCM)
# Setting these pins to OUTPUT
gpio.setup(pin1, gpio.OUT)
gpio.setup(pin2, gpio.OUT)

# Map of the arena
mapp = [[]]

def check():
	"""
        *
        * Function Name: 	check
        
        * Input: 		None
        
        * Output: 		True, False (Check if obstacle is at the right distance)
        
        * Logic: 				If ultrasonic reading is less than 20, then proper image cannot be taken
        *                       So this function checks the reading and gives a boolean accordingly
        
        * Example Call:		check()
        *
        """
	if ultra() <= 20:
		return False
	else:
		return True

def anomaly_look(cx, cy):
	"""
        *
        * Function Name: 	anomaly_look
        
        * Input: 		cx -> current x coordinate, cy -> current y coordinate
        
        * Output: 		True, False (used to manage flow of control)
        
        * Logic: 				When given a matrix of ones and zeros where 0's are possible paths
        *                       and 1's are obstacles. this function recursively finds a way from bot's current location to
        *                       the final location denoted by 5. After this algorithm is used, the matrix has a bunch of 3s
        *                       which the bot can follow and get to the final location. This 3s path is supposedly the shortest path
        
        * Example Call:		anomaly_look(bot.x, bot.y)
        *
        """
	global mapp
        rows = len(mapp)
        columns = len(mapp[0])
	if (not((cx < rows and cx >= 0) and (cy < columns and cy >= 0))):
		return False
	if (mapp[cx][cy]==5):
		return True
	if (mapp[cx][cy]!=0):
		return False
	mapp[cx][cy] = 3
	if (anomaly_look(cx-1,cy) == True):
		return True
	if (anomaly_look(cx,cy+1) == True):
		return True
	if (anomaly_look(cx+1,cy) == True):
		return True
	if (anomaly_look(cx,cy-1) == True):
		return True
	# This is the path which could have been a 3 but didn't result in the final destination
	mapp[cx][cy] = 0
	return False

def anomaly_find_path(cx, cy):
	"""
        *
        * Function Name: 	anomaly_find_path
        
        * Input: 		cx -> current x coordinate, cy -> current y coordinate
        
        * Output: 		NONE
        
        * Logic: 		this function gets the matrix which has a bunch of 3s that this function uses
                                to move the bot from current location to the final location. this function makes the bot
                                follow the 3s.
                                
        * Example Call:		anomaly_find_path(bot.x, bot.y)
        *
        """
	global mapp
	print mapp
	rows = len(mapp)
        columns = len(mapp[0])
	mapp[cx][cy] = 0
	while True:
		if cx-1 >= 0:
			if (mapp[cx-1][cy] == 3 or mapp[cx-1][cy] == 5):
				bm.up()
				cx -= 1
				#c.callibrate(rows, columns, cx, cy, mapp)
				if mapp[cx][cy] == 5:
                                    mapp[cx][cy] = 0
				    print "up"
                                    break
                                else:
                                    mapp[cx][cy] = 0
                                    print "up"
                                    continue
		if cx+1 < rows:
			if (mapp[cx+1][cy] == 3 or mapp[cx+1][cy] == 5):
				bm.down()
				cx += 1
				#c.callibrate(rows, columns, cx, cy, mapp)
				if mapp[cx][cy] == 5:
                                    mapp[cx][cy] = 0
				    print "down"
                                    break
                                else:
                                    mapp[cx][cy] = 0
                                    print "down"
                                    continue
		if cy+1 < columns:
			if (mapp[cx][cy+1] == 3 or mapp[cx][cy+1] == 5):
				bm.right()
				cy += 1
				#c.callibrate(rows, columns, cx, cy, mapp)
				if mapp[cx][cy] == 5:
                                    mapp[cx][cy] = 0
				    print "right"
                                    break
                                else:
                                    mapp[cx][cy] = 0
                                    print "right"
                                    continue
		if cy-1 >=0:
			if (mapp[cx][cy-1] == 3 or mapp[cx][cy-1] == 5):
				bm.left()
				cy -= 1
				#c.callibrate(rows, columns, cx, cy, mapp)
				if mapp[cx][cy] == 5:
                                    mapp[cx][cy] = 0
				    print "left"
                                    break
                                else:
                                    mapp[cx][cy] = 0
                                    print "left"
                                    continue
	else:
		return "you have reached your destination" # put a different kind of result

"""
now i will first check the distance and then get to a certain distance
then i will go down and hold and lift and then
start movement
when reached the location then drop and go to origin #for now
later go to the same place and start again
"""

def pick_the_block():
	"""
        *
        * Function Name: 	pick_the_block
        
        * Input: 		None
        
        * Output: 		NONE
        
        * Logic: 		This function gives two HIGH values to Arduino which it deduces as signal to lift the object
                                
        * Example Call:		pick_the_block()
        *
        """

        global pin1
        global pin2
        gpio.output(pin1, 1)
        gpio.output(pin2, 1)
        # Sleep for the time that is enough for completion of Arduino tasks
        sleep(5)

def drop_the_block():
	"""
        *
        * Function Name: 	drop_the_block
        
        * Input: 		None
        
        * Output: 		NONE
        
        * Logic: 		This function gives two LOW values to Arduino which it deduces as signal to drop the object
                                
        * Example Call:		drop_the_block()
        *
        """
        global pin1
        global pin2
        gpio.output(pin1, 0)
        gpio.output(pin2, 0)
        # Sleep for the time that is enough for completion of Arduino tasks
        sleep(5)

def rest():
	"""
        *
        * Function Name: 	rest
        
        * Input: 		None
        
        * Output: 		NONE
        
        * Logic: 		This function gives a HIGH and a LOW value to Arduino which it deduces as signal to rest in its mean position
                                
        * Example Call:		rest()
        *
        """
        global pin1
        global pin2
        gpio.output(pin1, 1)
        gpio.output(pin2, 0)
        #if needed
        sleep(5)

def go_to_location(digit):
	"""
        *
        * Function Name: 	go_to_location
        
        * Input: 		a number between 1 and 8 which represents the number found on the obstacle in front of it
        
        * Output: 		NONE
        
        * Logic: 		The bot uses the digit to get the correct location of the block then the bot creates a path
        				from current location to a block next to the correct location and faces the correct location
                                
        * Example Call:		go_to_location(5)
        *
        """
        global mapp
        #Vaiable Name: cx -> current coordinate of x , cy -> current coordintate of y
        cx = getcoords(digit)[0]
        cy = getcoords(digit)[1]
        if cx-1 >= 0:
                if mapp[cx-1][cy] == 0:
                        anomaly_look(cx, cy)
                        anomaly_find_path(cx, cy)
                        bm.look_down()
                        
        elif cx+1 < rows:
                if mapp[cx+1][cy] == 0:
                        anomaly_look(cx, cy)
                        anomaly_find_path(cx, cy)
                        bm.look_up()
                        
        elif cy+1 < columns:
                if mapp[cx][cy+1] == 0:
                        anomaly_look(cx, cy)
                        anomaly_find_path(cx, cy)
                        bm.look_left()
                        
        elif cy-1 >=0:
                if mapp[cx][cy-1] == 0:
                        anomaly_look(cx, cy)
                        anomaly_find_path(cx, cy)
                        bm.look_right()
                        
	else:
                print "there is no place from where i can place the block"

def correct_the_location(image_matrix):
	"""
        *
        * Function Name: 	correct_the_location
        
        * Input: 		image_matrix is the matrix representation of the arena 
        				in the form of 0s(free path) and 1s(obstacles)
        
        * Output: 		NONE
        
        * Logic: 		This function takes ultrasonic reading of the object in front. 
        				If it is not in sync with where the bot should be,
        				then it moves back and forward to calliberate itself. It then clicks 
        				the image of the obstacle and if it finds it in the wrong place,
        				then it finds its correct place from the database, picks it up
        				and puts it back to its correct location.
                                
        * Example Call:			correct_the_location([[0, 0, 1],[1, 0, 0], [0, 0, 0]])
        *
        """
        global mapp
        mapp = image_matrix
        global pin1
        global pin2
        try:
                gpio.output(pin1, 0)
                gpio.output(pin2, 0)

                distance = ultra()
                the_required_distance = 10
                the_required_distance_picture = 15
                if distance <= the_required_distance_picture:
                        bm.backward(the_required_distance_picture - distance)
                else:
                        bm.forward(distance - the_required_distance_picture)
                        
                digit = clicked()
                distance = ultra()
                
                if distance <= the_required_distance-8:
                        bm.backward(the_required_distance - distance-8)
                else:
                        bm.forward(distance - the_required_distance+8)
        # Functions to pick up the object, go to the right location and then drop it.
		pick_the_block()
		go_to_location(digit)
		drop_the_block()
		rest()
                #go_to_origin()
        except KeyboardInterrupt:
        	# Frees up the pins used in this program
                gpio.cleanup()
        finally:
                gpio.cleanup()
