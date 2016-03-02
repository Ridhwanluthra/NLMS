# import the necessary packages
import numpy as np
import cv2
import picamera
 
# construct the argument parse and parse the arguments
# load the image

m=8
n=8
inputArray=[]

def countArray(i, j):
        global m
	global n
	global inputArray
        counter=0
        for row in range(i, i+m):
                for column in range(j, j+n):
                        if(inputArray[i][j]==255):
                                counter+=1
        return counter


def clicked():
        direc='img.jpg'
        text_dir='img_digit.txt'
        camera=picamera.PiCamera()
        camera.contrast=40
        camera.brightness=40
        camera.saturation=30
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
        upper = np.array([90, 90, 90])
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
                        break
        lower = np.array([0, 0, 0])
        upper = np.array([90, 90, 90])
        shapeMask = cv2.inRange(img, lower, upper)

        # find all the 'black' shapes in the image
	global m
	global n
	global inputArray
        k=35
        c=[]
        s01_=shapeMask.shape[0]
        s02_=shapeMask.shape[1]
        #populating input array with random numbers 0 and 255 for testing purposes
        for i in range (s01_):
                for j in range (s02_):
                        c.append(shapeMask[i][j])
                inputArray.append(c)
                c=[]
        outputArrayRows=(s01_/m)
        outputArrayColumns=(s02_/n)
        sre=''
        f = open(text_dir, 'w')
        for i in range (outputArrayRows):
                for j in range (outputArrayColumns):
                        if countArray(i*m,j*n)>=k:
                                sre+='1'
                        else:
                                sre+='0'
                f.write(sre+'\n')
                sre=''
        f.close()
