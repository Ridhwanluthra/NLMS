"""
*
* Project Name: 	House Probing Robot for The Elderly

* Author List: 		Ridhwan Luthra

* Filename: 		anomaly.py

* Functions: 		check, anomaly_look, anomaly_find_path, pick_the_block,
                        drop_the_block, rest, go_to_location, correct_the_location,

* Global Variables:	mapp
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

pin1 = 7
pin2 = 8     
gpio.setmode(gpio.BCM)
gpio.setup(pin1, gpio.OUT)
gpio.setup(pin2, gpio.OUT)

mapp = [[]]

def check():
	if ultra() <= 20:
		return False
	else:
		return True

def anomaly_look(cx, cy):
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
	mapp[cx][cy] = 0
	return False

def anomaly_find_path(cx, cy):
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
				c.callibrate(rows, columns, cx, cy, mapp)
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
				c.callibrate(rows, columns, cx, cy, mapp)
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
				c.callibrate(rows, columns, cx, cy, mapp)
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
				c.callibrate(rows, columns, cx, cy, mapp)
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
now i will first chec the distance and then get to a certain distance
then i will go down and hold and lift and then
start movement
when reached the location then drop and go to origin #for now
later go to the same place and start again
"""

def pick_the_block():
        global pin1
        global pin2
        gpio.output(pin1, 1)
        gpio.output(pin2, 1)
        #for the time that is enough
        sleep(15)

def drop_the_block():
        global pin1
        global pin2
        gpio.output(pin1, 0)
        gpio.output(pin2, 0)
        #for the time that is enough
        sleep(15)

def rest():
        global pin1
        global pin2
        gpio.output(pin1, 1)
        gpio.output(pin2, 0)
        #if needed
        sleep(10)

def go_to_location(digit):
        global mapp
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
                
                if distance <= the_required_distance:
                        bm.backward(the_required_distance - distance)
                else:
                        bm.forward(distance - the_required_distance)

		pick_the_block()
		go_to_location(digit)
		drop_the_block()
		rest()
		"""                
		if(ultra()<the_required_distance):
                        print "gone in"
                        pick_the_block()
                        sleep(10)
                        drop_the_block()
                        sleep(10)
                        rest()
                        sleep(10)
                else:
                        rest()
                        print "gone out"
		"""
                #go_to_origin()
        except KeyboardInterrupt:
                gpio.cleanup()
        finally:
                gpio.cleanup()
