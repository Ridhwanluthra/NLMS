import cv2
import numpy as np

def countArray(i, j):
		counter=0
		for row in range(i, i+m):
			for column in range(j, j+n):
				if(inputArray[i][j]==255):
					counter+=1
		return counter

def edging(dir):
	img = cv2.imread(dir, cv2.IMREAD_COLOR)
	edges=cv2.Canny(img,100,200)
	oppp=[]
	for x in xrange(edges.shape[0]):
		opp=[]
		for y in xrange(edges.shape[1]):
			opp.append(edges[x][y])
			pass
		oppp.append(opp)
		pass
	#Save image to storage with a pseudo-unique name
	cv2.imwrite('img.png', edges)

	#if the number of cells in inputArray having value 255 are greater than "K",then value is 1 in output
	#here I am setting k=50
	k=20
	s01_=edges.shape[0]
	s02_=edges.shape[1]
	m=edges.shape[0]/10
	n=edges.shape[1]/10

	c=[]
	inputArray=[]
	#populating input array with random numbers 0 and 255 for testing purposes
	for i in range (s01_):
		for j in range (s02_):
			c.append(edges[i][j])
		inputArray.append(c)
		c=[]
	outputArrayRows=s01_/m
	outputArrayColumns=s02_/n
	outputArray=[[] for i in range (outputArrayColumns)]
	for i in range (outputArrayRows):
		for j in range (outputArrayColumns):
			if countArray(i*m,j*n)>=k:
				outputArray[i].append(1)
			else:
				outputArray[i].append(0)
	return outputArray
