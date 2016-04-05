"""
*
* Project Name: 	House Probing Robot for The Elderly

* Author List: 		Ridhwan Luthra

* Filename: 		callibration.py

* Functions: 		linear_callibrate, angle_callibrate, callibrate

* Global Variables:	NONE
*
"""
from ultrasonic import callibration_ultra, ultra
from time import sleep
import bot_movement as bm
from bot_globals import bot
from math import asin, degrees, sqrt, pow

"""
        *
        * Function Name:    linear_callibrate
        
        * Input:        rows, columns, cx(bot's current position in x direction), cy(bot's current position in y direction), mapp(matrix of 0s and 1s)
        
        * Output:       None
        
        * Logic:        In case robot has moved in the wrong direction due to wrong calliberation,
        				this function will try to reallign the bot in linear direction using ultrasonic sensors.
        
        * Example Call:     linear_callibrate(5, 6, 1, 2, [0, 0, 1])
        *
        """

def linear_callibrate(rows, columns, cx, cy, mapp):
    print "entered linear"
    # center is actually extra spacing on the sides
    center = 4
    error = 1
    grid_size = 30
    
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
    
    distance = distance + center

    reading = ultra()
    print "ultra calli: " + str(reading)
    print "required distance: " + st(reading)
    
    if reading > distance + error:
        bm.move_forward(reading - distance)
    elif reading < distance - error:
        bm.move_backward(distance - reading)
    else:
        print "no need for ultrasonic callibration, good work encoders"
    sleep(1)

"""
        *
        * Function Name:    angle_callibrate
        
        * Input:        read(list containing ultrasonic readings), distance(distance in front where the bot should be if everything goes right)
        
        * Output:       None
        
        * Logic:        In case robot has turned some angle due to wrong calliberation,
        				this function will try to reallign the angular position of bot  using ultrasonic sensors.
        
        * Example Call:     angular_callibrate([12, 23, 34], 23)
        *
        """

def angle_callibrate(read, distance):
    print "entered angle"
    ultra_diff = 12.7
    #center more than linear to incorporate the tires and ultra position
    center = 8
    distance_error = 2
    angle_error = 2

    distance = distance + center

    #now correcting the angle
    while read[1] > read[2] + angle_error or read[1] < read[2] - angle_error:
        print "entered while"
        if read[1] > read[2] + angle_error:
            difference = read[1] - read[2]
            degree = asin(difference / sqrt(pow(ultra_diff, 2)+pow(difference, 2)))
            degree = degrees(degree)
            if degree > 4:
                print "degree greater"
                bm.turn_left(degree - 4)
                read = callibration_ultra()
            else:
                print "degree less"
                bm.turn_left(degree)
                read = callibration_ultra()
                
        elif read[1] < read[2] - angle_error:
            difference = read[2] - read[1]
            degree = asin(difference / sqrt(pow(ultra_diff, 2)+pow(difference, 2)))
            degree = degrees(degree)
            if degree > 4:
                print "degree greater"
                bm.turn_right(degree - 4)
                print "turned right"
                read = callibration_ultra()
            else:
                print "degree less"
                bm.turn_right(degree)
                read = callibration_ultra()
    print "exited while"

"""
        *
        * Function Name:    callibrate
        
        * Input:        rows, columns, cx(bot's current position in x direction), cy(bot's current position in y direction), mapp(matrix of 0s and 1s)
        
        * Output:       None
        
        * Logic:        In case robot has moved in the wrong direction due to wrong calliberation,
        				this function will try to reallign the bot in both linear and angular direction using ultrasonic sensors.
        
        * Example Call:     linear_callibrate(5, 6, 1, 2, [0, 0, 1])
        *
        """

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
