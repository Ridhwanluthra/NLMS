import picamera
import numpy as np
import argparse
import cv2

camera = picamera.PiCamera()

i_=0
j_=1

camera.vflip=True
camera.contrast=60
camera.resolution=(480,360)
direc='img_{0}{1}.jpg'.format(i_,j_)
camera.capture(direc)
        #analysis of image


def countArray(i, j):
    counter=0
    for row in range(i, i+m):
        for column in range(j, j+n):
            if(inputArray[i][j]==255):
                counter+=1
    return counter
 
# load the image
image = cv2.imread(direc)
# find all the 'black' shapes in the image
lower = np.array([0, 0, 0])
upper = np.array([30, 30, 30])
shapeMask = cv2.inRange(image, lower, upper)
#dir='mask{0}{1}.jpg'.format(i_,j_)
#cv2.imwrite(dir, shapeMask)
oppp=[]
for x in xrange(shapeMask.shape[0]):
    opp=[]
    for y in xrange(shapeMask.shape[1]):
        opp.append(shapeMask[x][y])
        pass
    oppp.append(opp)
    pass
k=60
m=10
n=10
c=[]
inputArray=[]
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

f = open('digit{0}{1}.txt'.format(i_, j_), 'w')
for i in range (outputArrayRows):
    for j in range (outputArrayColumns):
        if countArray(i*m,j*n)>=k:
            sre+='!'
        else:
            sre+='.'
    f.write(sre+'\n')
    sre=''
f.close()
