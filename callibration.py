"""
*
* Project Name: 	House Probing Robot for The Elderly

* Author List: 		Ridhwan Luthra

* Filename: 		callibration.py

* Functions: 		linear_callibrate, angle_callibrate, callibrate

* Global Variables:	NONE
*
"""
from ultrasonic import callibration_ultra
from time import sleep
import bot_movement as bm
from bot_globals import bot
from math import asin, degrees, sqrt, pow

def linear_callibrate(reading, distance):
    # center is actually extra spacing on the sides
    center = 4
    error = 2

    distance = distance + center
    
    if reading > distance + error:
        bm.move_forward(reading - distance)
    elif reading < distance - error:
        bm.move_backward(distance - reading)
    else:
        print "no need for ultrasonic callibration, good work encoders"

def angle_callibrate(read, distance):
    ultra_diff = 12.7
    #center more than linear to incorporate the tires and ultra position
    center = 9
    distance_error = 4
    angle_error = 1

    distance = distance + center

    average_reading = (read[1] + read[2])/2

    difference = read[2] - read[1]
    degree = asin(difference / sqrt(pow(ultra_diff, 2)+pow(difference, 2)))
    degree = degrees(degree)

    #correcting the distance from left
    if average_reading < distance - distance_error:
        # can add the below commented if angle correction wanted before
        """if read[1] > read[2] + angle_error:
            bm.turn_left(degree)
        elif read[1] < read[2] - angle_error:
            bm.turn_right(degree)"""
        bm.turn_right(90)
        bm.move_forward(distance - average_reading)
        bm.turn_left(90)
            
    elif average_reading > distance + distance_error:
        # can add the below commented if angle correction wanted before
        """if read[1] > read[2] + angle_error:
            bm.turn_left(degree)
        elif read[1] < read[2] - angle_error:
            bm.turn_right(degree)"""
        bm.turn_left(90)
        bm.move_forward(average_reading - distance)
        bm.turn_right(90)

    #now correcting the angle
    while read[1] > read[2] + angle_error or read[1] < read[2] - angle_error:
        if read[1] > read[2] + angle_error:
            bm.turn_left(degree)
            read = callibration_ultra()
            
        elif read[1] < read[2] - angle_error:
            bm.turn_right(degree)
            read = callibration_ultra()

def callibrate(rows, columns, cx, cy, mapp):
    # [0] = move_forward, [1] = left, [2] = back
    readings = callibration_ultra()
    read = readings
    while read[1] >= read[2] + 20:
        bm.move_backward(2)
        read = callibration_ultra()
        
    while read[1] <= read[2] - 20:
        bm.move_forward(2)
        read = callibration_ultra()

    grid_size = 30
    
    #for linear callibration
    if bot.direction == 'n':
        if cx == 0:
            distance = 0
        else:
            found_obstacle = False
            for i in range(1, cx):
                if mapp[i][cy] == 1:
                    found_obstacle = True
                    distance = (cx - i - 1) * grid_size
                    break
            if found_obstacle==False:
                distance = cx * grid_size
        
    elif bot.direction == 's':
        if cx == rows:
            distance = 0
        else:
            found_obstacle = False
            for i in range(cx, rows):
                if mapp[i][cy] == 1:
                    found_obstacle = True
                    distance = (i - cx - 1) * grid_size
                    break
            if found_obstacle==False:
                distance = (rows - cx - 1) * grid_size
        
    elif bot.direction == 'w':
        if cy == 0:
            distance = 0
        else:
            found_obstacle = False
            for i in range(1, cy):
                if mapp[cx][i] == 1:
                    found_obstacle = True
                    distance = (cy - i - 1) * grid_size
                    break
            if found_obstacle==False:
                distance = cy * grid_size

    elif bot.direction == 'e':
        if cy == columns:
            distance = 0
        else:
            found_obstacle = False
            for i in range(cy, columns):
                if mapp[cx][i] == 1:
                    found_obstacle = True
                    distance = (i - cy - 1) * grid_size
                    break
            if found_obstacle==False:
                distance = (columns - cy - 1) * grid_size
    
    linear_callibrate(readings[0], distance)

    # for angle callibration
    if bot.direction == 'n':
        if cy == 0:
            distance = 0
        else:
            found_obstacle = False
            for i in range(1, cy):
                if mapp[cx][i] == 1:
                    found_obstacle = True
                    distance = (cy - i - 1) * grid_size
                    break
            if found_obstacle==False:
                distance = cy * grid_size
        
    elif bot.direction == 's':
        if cy == columns:
            distance = 0
        else:
            found_obstacle = False
            for i in range(cy, columns):
                if mapp[cx][i] == 1:
                    found_obstacle = True
                    distance = (i - cy - 1) * grid_size
                    break
            if found_obstacle==False:
                distance = (columns - cy - 1) * grid_size
        
    elif bot.direction == 'w':
        if cx == rows:
            distance = 0
        else:
            found_obstacle = False
            for i in range(cx, rows):
                if mapp[i][cy] == 1:
                    found_obstacle = True
                    distance = (i - cx - 1) * grid_size
                    break
            if found_obstacle==False:
                distance = (rows - cx - 1) * grid_size

    elif bot.direction == 'e':
        if cx == 0:
            distance = 0
        else:
            found_obstacle = False
            for i in range(1, cx):
                if mapp[i][cy] == 1:
                    found_obstacle = True
                    distance = (cx - i - 1) * grid_size
                    break
            if found_obstacle==False:
                distance = cx * grid_size

    angle_callibrate(readings, distance)
