"""
*
* Project Name: 	House Probing Robot for The Elderly

* Author List: 		Ridhwan Luthra

* Filename: 		main.py

* Functions: 		NONE

* Global Variables:	NONE
*
"""
# RUN THIS SCRIPT AND THE REST WILL RUN THEMSELVES

from traversal import mapping
from first_traversal import first_mapping
from anomaly import correct_the_location, rest
# Variable Name: image_matrix -> this is the translation of the image taken from above
# 				 				 into a matrix where 1's represent the obstacles.

image_matrix = [[0,1,0,0],[0,0,0,0],[0,1,0,0],[0,0,0,1]]

first_mapping(image_matrix)

while True:
	if mapping(image_matrix) == True:
                continue
        else:
                correct_the_location(image_matrix)
                continue
