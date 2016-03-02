# code for making the bot move in the grid

# ALL BLOCK COMMENTS ANSWER THE QUESTION "WHAT DO I HAVE AT THIS POINT?"

# take input of the matrix of the image
# store this x,y in a different variable

# take input of the start and the end point

from bot_globals import bot
from first_bot_movement import *
from time import sleep
import file_handling as file_h
#from click_picture import click_picture

"""
I get a matrix which has some 0's and 1's
I get a start point and an end point
"""

"""
I have a way to move in different directions
I still have to configure these functions
I am working on it lets see what happens.
so now it just becomes a problem of changing my control
from one location to the other in a matrix
"""
"""
/* values represent:
0=free path
1=blocked path
3=valid path
4=invalid path
5=goal
"""
"""
This program gives the best path to move from source to destination.
"""

mapp=[[]]

def first_look(cx, cy):
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
	if (first_look(cx-1,cy) == True):
		return True
	if (first_look(cx,cy+1) == True):
		return True
	if (first_look(cx+1,cy) == True):
		return True
	if (first_look(cx,cy-1) == True):
		return True
	mapp[cx][cy] = 0
	return False

"""
Now I can create a matrix which has a path path of 3's
which i can follow to get my bot to the final location
"""

def first_find_path(cx, cy):
	global mapp
	print mapp
	rows = len(mapp)
        columns = len(mapp[0])
	mapp[cx][cy] = 0
	while True:
		if cx-1 >= 0:
			if (mapp[cx-1][cy] == 3 or mapp[cx-1][cy] == 5):
				up()
				cx -= 1
				callibrate(rows, columns, cx, cy, mapp)
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
				down()
				cx += 1
				callibrate(rows, columns, cx, cy, mapp)
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
				right()
				cy += 1
				callibrate(rows, columns, cx, cy, mapp)
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
				left()
				cy -= 1
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
		return "you have reached your destination" # put a different kind of result

"""
I have reached my final destination
using the matrix with 3's 
I found where there was 3 and accordingly
I moved the bot to the location needed
"""
"""
def go_to_origin(x,y):
        global mapp
        global x
        global y
        mapp[0][0] = 5;
        look(x,y)
        find_path(x,y)
        x = 0
        y = 0
        mapp[i][j] = 0
"""
"""
Now i need to create a function that can make
each location i have to go to 5 in turn so that
i can go and take pictures of each obstacle
"""

# x and y being the current position of the bot
def first_mapping(maps):
        #ADD A FILE SAVING MECHANISM
	global mapp
	mapp = maps
	rows = len(mapp)
        columns = len(mapp[0])
        #first_look(x,y)
	#first_find_path(x,y)
	for i in range(rows):
		for j in range(columns):
			if (mapp[i][j] == 1):
				if (i-1 >= 0 and mapp[i-1][j] == 0):
                                        global mapp
					mapp[i-1][j] = 5;
					first_look(bot.x, bot.y)
					first_find_path(bot.x, bot.y)
					look_down()
					sleep(2)
					bot.x = i-1
					bot.y = j
					"""
					digit = click_picture(i, j)
					file_h.write_in_file(digit, i, j)
					"""
					mapp[i-1][j] = 0
				elif (j+1 < columns and mapp[i][j+1] == 0):
                                        global mapp
					mapp[i][j+1] = 5;
					first_look(bot.x,bot.y)
					first_find_path(bot.x,bot.y)
					look_left()
					sleep(2)
					bot.x = i
					bot.y = j+1
					"""
					digit = click_picture(i, j)
					file_h.write_in_file(digit, i, j)
					"""
					mapp[i][j+1] = 0
				elif (i+1 < rows and mapp[i+1][j] == 0):
                                        global mapp
					mapp[i+1][j] = 5;
					first_look(bot.x,bot.y)
					first_find_path(bot.x,bot.y)
					look_up()
					sleep(2)
					bot.x = i+1
					bot.y = j
					"""
					digit = click_picture(i, j)
					file_h.write_in_file(digit, i, j)
					"""
					mapp[i+1][j] = 0
				elif (j-1 >= 0 and mapp[i][j-1] == 0):
                                        global mapp
					mapp[i][j-1] = 5;
					first_look(bot.x,bot.y)
					first_find_path(bot.x,bot.y)
					look_right()
					sleep(2)
					bot.x = i
					bot.y = j-1
					"""
					digit = click_picture(i, j)
					file_h.write_in_file(digit, i, j)
					"""
					mapp[i][j-1] = 0
				else:
					print "there is some error in mapping function in file traversal.py"
        #first_go_to_origin(x,y)
	#return [x,y]
