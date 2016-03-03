"""
*
* Project Name: 	House probing robot for the elderly

* Author List: 		Ridhwan Luthra, Utkarsh Mittal

* Filename: 		first_traversal.py

* Functions: 		look, find_path, mapping

* Global Variables:	mapp
*
"""

from bot_globals import bot
import bot_movement as bm
from time import sleep
from callibration import callibrate
#from click_picture import click_picture

mapp=[[]]

def look(cx, cy):
        """
        *
        * Function Name: 	look
        
        * Input: 		cx -> current x coordinate, cy -> current y coordinate
        
        * Output: 		True, False (used to manage flow of control)
        
        * Logic: 		This function when given a matrix of ones and zeros where 0's are possible paths
        *                       and 1's are obstecles. this function recursively finds a way from my current location to
        *                       the final location denoted by 5. after this algorithm is used the matrix has a bunch of 3's
        *                       which the bot can follow and get to the final location. this 3s path is the shortest path
        
        * Example Call:		look(bot.x, bot.y)
        *
        """
        #Variable Name: mapp -> it is the matrix of the imaginary grid of the arena
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
	if (look(cx-1,cy) == True):
		return True
	if (look(cx,cy+1) == True):
		return True
	if (look(cx+1,cy) == True):
		return True
	if (look(cx,cy-1) == True):
		return True
	mapp[cx][cy] = 0
	return False

def find_path(cx, cy):
        """
        *
        * Function Name: 	find_path
        
        * Input: 		cx -> current x coordinate, cy -> current y coordinate
        
        * Output: 		NONE
        
        * Logic: 		this function gets the matrix which has a bunch of 3s that this function uses
                                to move the bot from current location to the final location. this function makes the bot
                                follow the 3s.
                                If there are some blocks that are not where they are supposed it stops the processing
                                and returns False so that the control is returned and the anomaly can be handled
                                it checks everytime to see if there is a block out of its position
                                
        * Example Call:		find_path(bot.x, bot.y)
        *
        """
	global mapp
	print mapp
	rows = len(mapp)
        columns = len(mapp[0])
	if mapp[cx][cy] == 5:
		return True
	else:
		mapp[cx][cy] = 0
	while True:
		if cx-1 >= 0:
			if (mapp[cx-1][cy] == 3 or mapp[cx-1][cy] == 5):
				if bm.up() == True:
                                        cx -= 1
                                        # callibrate function is used by the bot to self callibrate its location
                                        # so that if the encoders go wrong this function will correct it
                                        callibrate(rows, columns, cx, cy, mapp)
                                        if mapp[cx][cy] == 5:
                                            mapp[cx][cy] = 0
                                            print "up"
                                            break
                                        else:
                                            mapp[cx][cy] = 0
                                            print "up"
                                            continue
                                else:
                                        return False
                                
		if cx+1 < rows:
			if (mapp[cx+1][cy] == 3 or mapp[cx+1][cy] == 5):
				if bm.down() == True:
                                        cx += 1
                                        # callibrate function is used by the bot to self callibrate its location
                                        # so that if the encoders go wrong this function will correct it
                                        callibrate(rows, columns, cx, cy, mapp)
                                        if mapp[cx][cy] == 5:
                                            mapp[cx][cy] = 0
                                            print "down"
                                            break
                                        else:
                                            mapp[cx][cy] = 0
                                            print "down"
                                            continue
                                else:
                                        return False
                                
		if cy+1 < columns:
			if (mapp[cx][cy+1] == 3 or mapp[cx][cy+1] == 5):
				if bm.right() == True:
                                        cy += 1
                                        # callibrate function is used by the bot to self callibrate its location
                                        # so that if the encoders go wrong this function will correct it
                                        callibrate(rows, columns, cx, cy, mapp)
                                        if mapp[cx][cy] == 5:
                                            mapp[cx][cy] = 0
                                            print "right"
                                            break
                                        else:
                                            mapp[cx][cy] = 0
                                            print "right"
                                            continue
                                else:
                                        return False
                                
		if cy-1 >=0:
			if (mapp[cx][cy-1] == 3 or mapp[cx][cy-1] == 5):
				if bm.left() == True:
                                        cy -= 1
                                        # callibrate function is used by the bot to self callibrate its location
                                        # so that if the encoders go wrong this function will correct it
                                        callibrate(rows, columns, cx, cy, mapp)
                                        if mapp[cx][cy] == 5:
                                            mapp[cx][cy] = 0
                                            print "left"
                                            break
                                        else:
                                            mapp[cx][cy] = 0
                                            print "left"
                                            continue
                                else:
                                        return False
	else:
		return True

def mapping(maps):
        """
        *
        * Function Name: 	mapping
        
        * Input: 		maps -> the image_matrix generated by image processing of the arena
        
        * Output: 		True -> if the movement took place, False -> if no movement took place
        
        * Logic: 		this function controls the entire motion of the bot using look and find_path.
                                
        * Example Call:		mapping(image_matrix)
        *
        """
	global mapp
	mapp = maps
	rows = len(mapp)
        columns = len(mapp[0])
	for i in range(rows):
		for j in range(columns):
			if (mapp[i][j] != 1):
                                mapp[i][j] = 5;
                                look(bot.x,bot.y)
                                if find_path(bot.x,bot.y) == False:
                                        return False
                                bot.x = i
                                bot.y = j
                                mapp[i][j] = 0
        return True
