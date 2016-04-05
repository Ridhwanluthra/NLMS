"""
*
* Project Name: 	House Probing Robot for The Elderly

* Author List: 		Pankaj Baranwal

* Filename: 		click_picture.py

* Functions: 		clicked

* Global Variables:	NONE
*
"""


# import the necessary packages
import numpy as np
import cv2
import picamera


"""
        *
        * Function Name:    clicked
        
        * Input:        None
        
        * Output:       returns the digit which it has recognised on the obstacle
        
        * Logic:        In case robot has moved in the wrong direction due to wrong calliberation,
        				this function will try to reallign the bot in linear direction using ultrasonic sensors.
        
        * Example Call:     linear_callibrate(5, 6, 1, 2, [0, 0, 1])
        *
        """

def clicked():
        try:
                direc='img.jpg'
                camera=picamera.PiCamera()
                camera.resolution=(300,200)
                from time import sleep
                camera.capture(direc)
                sleep(1)
                    #analysis of image
                # load the image
                image = cv2.imread(direc)
                img = image
                img=cv2.medianBlur(img, 9)
                # find all the 'black' shapes in the image
                lower = np.array([0, 0, 0])
                upper = np.array([60, 60, 60])
                shapeMask = cv2.inRange(img, lower, upper)
                # find the contours in the mask
                (contours, _) = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
                 
                for cnt in contours:
                        area = cv2.contourArea(cnt)
                        #print area

                        if area>1200 and area<7000:
                #		print area
                                x,y,w,h = cv2.boundingRect(cnt)
                                cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255), 2)
                                img=img[y:y+h, x:x+w]
                                img = cv2.resize(img, (50, 200)) 
                                break
                lower = np.array([0, 0, 0])
                upper = np.array([60, 60, 60])
                shapeMask = cv2.inRange(img, lower, upper)

                (contours, _) = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)
                for cnt in contours:
                        area = cv2.contourArea(cnt)
                        if (area<5500 and area>4500):
                                return 3
                        elif (area<7500 and area>6900):
                                return 1
                        elif (area<6800 and area>6100):
                                return 6
                        elif (area<3500 and area>2500):
                                return 7
                        elif (area<9100 and area>8000):
                                return 8
                        elif (area<3000 and area>2500):
                                return 2
                        elif (area<4500 and area>3700):
                                return 4
                        else:
                                return 5
        finally:
                camera.close()
