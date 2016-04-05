"""
*
* Project Name: 	House Probing Robot for The Elderly

* Author List: 		Pankaj Baranwal

* Filename: 		edging.py

* Functions: 		countArray, edging

* Global Variables:	m, n, inputArray
*
"""

import cv2
import numpy as np

m=10
n=10
inputArray=[]


"""
        *
        * Function Name:    countArray
        
        * Input:        i(row number), j(column number)
        
        * Output:       returns counter(the nu,ber of 1s found)
        
        * Logic:        This function is provided with with row and col index and it reduces m*n grid into one cell.
        
        * Example Call:     count_Array(2, 4)
        *
        """
def countArray(i, j):
		counter=0
		for row in range(i, i+m):
			for column in range(j, j+n):
				if(inputArray[i][j]==255):
					counter+=1
		return counter

"""
        *
        * Function Name:    edging
        
        * Input:        directory of image
        
        * Output:       returns final grid of the arena
        
        * Logic:        This function is provided with directory of image, it uses image processing to return matrix of arena
        
        * Example Call:     edging('img.jpg')
        
        """

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
