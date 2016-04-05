"""
*
* Project Name: 	House probing robot for the elderly

* Author List: 		Ridhwan Luthra, Utkarsh Mittal

* Filename: 		first_traversal.py

* Functions: 		first_look, first_find_path, first_mapping

* Global Variables:	mapp
*
"""

from bot_globals import bot
import bot_movement as bm
from time import sleep
import file_handling as file_h
from callibration import linear_callibrate
from click_picture import clicked
import ultrasonic

mapp = [[]]

def first_look(cx, cy):
        """
        *
        * Function Name: 	first_look
        
        * Input: 		cx -> current x coordinate, cy -> current y coordinate
        
        * Output: 		True, False (used to manage flow of control)
        
        * Logic: 				When given a matrix of ones and zeros where 0's are possible paths
        *                       and 1's are obstacles. this function recursively finds a way from bot's current location to
        *                       the final location denoted by 5. After this algorithm is used, the matrix has a bunch of 3s
        *                       which the bot can follow and get to the final location. This 3s path is supposedly the shortest path
        
        * Example Call:		first_look(bot.x, bot.y)
        *
        """

        #Variable Name: mapp -> it is the matrix of the imaginary grid of the arena
	global mapp
        rows = len(mapp)
        columns = len(mapp[0])
    # If current position is not a cell in the matrix, this function returns false
	if (not((cx < rows and cx >= 0) and (cy < columns and cy >= 0))):
		return False
	# If current position is equal to 5, bot has reached the final destination
	if (mapp[cx][cy]==5):
		return True
	if (mapp[cx][cy]!=0):
		return False
	# 3s represent actual path moved
	mapp[cx][cy] = 3
	if (first_look(cx-1,cy) == True):
		return True
	if (first_look(cx,cy-1) == True):
		return True
	if (first_look(cx+1,cy) == True):
		return True
	if (first_look(cx,cy+1) == True):
		return True
	# This is the path which could have been a 3 but didn't result in the final destination
	mapp[cx][cy] = 0
	return False

def first_find_path(cx, cy):
        """
        *
        * Function Name: 	first_find_path
        
        * Input: 		cx -> current x coordinate, cy -> current y coordinate
        
        * Output: 		NONE
        
        * Logic: 		this function gets the matrix which has a bunch of 3s that this function uses
                                to move the bot from current location to the final location. this function makes the bot
                                follow the 3s.
                                
        * Example Call:		first_find_path(bot.x, bot.y)
        *
        """
	global mapp
#	print mapp
	rows = len(mapp)
        columns = len(mapp[0])
	mapp[cx][cy] = 0
	while True:
		if cx-1 >= 0:
			if (mapp[cx-1][cy] == 3 or mapp[cx-1][cy] == 5):
				# The bot should face North
				bm.first_up()
				cx -= 1
				# callibrate function is used by the bot to self callibrate its location
				# so that if the encoders go wrong this function will correct it
				#linear_callibrate(rows, columns, cx, cy, mapp)
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
				# The bot should face South
				bm.first_down()
				cx += 1
				# callibrate function is used by the bot to self callibrate its location
				# so that if the encoders go wrong this function will correct it
				#linear_callibrate(rows, columns, cx, cy, mapp)
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
				# The bot should face East
				bm.first_right()
				cy += 1
				# callibrate function is used by the bot to self callibrate its location
				# so that if the encoders go wrong this function will correct it
				#linear_callibrate(rows, columns, cx, cy, mapp)
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
				# The bot should face West
				bm.first_left()
				cy -= 1
				# callibrate function is used by the bot to self callibrate its location
				# so that if the encoders go wrong this function will correct it
				#linear_callibrate(rows, columns, cx, cy, mapp)
				if mapp[cx][cy] == 5:
                                    mapp[cx][cy] = 0
				    print "left"
                                    break
                                else:
                                    mapp[cx][cy] = 0
                                    print "left"
                                    continue

def first_mapping(maps):
        """
        *
        * Function Name: 	first_mapping
        
        * Input: 		maps -> the image_matrix generated by image processing of the arena
        
        * Output: 		NONE
        
        * Logic: 		this function controls the entire motion of the bot using first_look and first_find_path.
                                it also finds the location near the obstacles from where the picture can be taken
                                it calls the function to take the picture then process it and return the digit
                                then it stores that information with the location of the obstacle for use later
                                
        * Example Call:		first_mapping([[0, 0, 1], [1, 0, 0], [0, 0, 0]])
        *
        """
	global mapp
	mapp = maps
	the_required_distance_picture = 15
	rows = len(mapp)
        columns = len(mapp[0])
	for i in range(rows):
		for j in range(columns):
			if (mapp[i][j] == 1):
				if (i-1 >= 0 and mapp[i-1][j] == 0):
                                        global mapp
					mapp[i-1][j] = 5;
					first_look(bot.x, bot.y)
					first_find_path(bot.x, bot.y)
					#looking in the direction of the block
					bm.look_down()
					sleep(2)
					# Updating the current location of the bot
					bot.x = i-1
					bot.y = j
					distance = ultrasonic.ultra()
					if distance <= the_required_distance_picture:
                                                bm.move_backward(the_required_distance_picture - distance)
                                        else:
                                                bm.move_forward(distance - the_required_distance_picture)
                    # Click image of the obstacle, use image processing to get the digit, and then write it to a file.
					digit = clicked()
					file_h.write_in_file(digit, i, j)
					
					mapp[i-1][j] = 0
				elif (j+1 < columns and mapp[i][j+1] == 0):
                                        global mapp
					mapp[i][j+1] = 5;
					first_look(bot.x,bot.y)
					first_find_path(bot.x,bot.y)
					#looking in the direction of the block
					bm.look_left()
					sleep(2)
					# Updating the current location of the bot
					bot.x = i
					bot.y = j+1
					distance = ultrasonic.ultra()
					if distance <= the_required_distance_picture:
                                                bm.move_backward(the_required_distance_picture - distance)
                                        else:
                                                bm.move_forward(distance - the_required_distance_picture)
                    # Click image of the obstacle, use image processing to get the digit, and then write it to a file.
					digit = clicked()
					file_h.write_in_file(digit, i, j)
					mapp[i][j+1] = 0
				elif (i+1 < rows and mapp[i+1][j] == 0):
                                        global mapp
					mapp[i+1][j] = 5;
					first_look(bot.x,bot.y)
					first_find_path(bot.x,bot.y)
					#looking in the direction of the block
					bm.look_up()
					sleep(2)
					# Updating the current location of the bot
					bot.x = i+1
					bot.y = j
					distance = ultrasonic.ultra()
					if distance <= the_required_distance_picture:
                                                bm.move_backward(the_required_distance_picture - distance)
                                        else:
                                                bm.move_forward(distance - the_required_distance_picture)
                    # Click image of the obstacle, use image processing to get the digit, and then write it to a file.
					digit = clicked()
					file_h.write_in_file(digit, i, j)
					
					mapp[i+1][j] = 0
				elif (j-1 >= 0 and mapp[i][j-1] == 0):
                                        global mapp
					mapp[i][j-1] = 5;
					first_look(bot.x,bot.y)
					first_find_path(bot.x,bot.y)
					#looking in the direction of the block
					bm.look_right()
					sleep(2)
					# Updating the current location of the bot
					bot.x = i
					bot.y = j-1
					# Getting data from ultasonic sensor
					distance = ultrasonic.ultra()
					# Adjusting the distance between bot and obstacle to take a good quality picture
					if distance <= the_required_distance_picture:
                                                bm.move_backward(the_required_distance_picture - distance)
                                        else:
                                                bm.move_forward(distance - the_required_distance_picture)
                    # Click image of the obstacle, use image processing to get the digit, and then write it to a file.
					digit = clicked()
					file_h.write_in_file(digit, i, j)
					
					mapp[i][j-1] = 0
				else:
					print "there is some error in mapping function in file traversal.py"
