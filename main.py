# RUN THIS SCRIPT AND THE REST WILL RUN THEMSELVES

#from sys import argv
from traversal import mapping
#from edging import edging

#image_matrix = edging(argv[1]) # convert the picture into edges and return the sub_matrix
x=0
y=0
# now i have the completed map of the room ready

# add the ultrasonic sensors to find and save from obstacles.
image_matrix = [[0,0,0,0,1,0],[0,0,1,0,0,0],[1,1,1,0,0,0],[1,0,0,0,1,1],[0,0,0,0,0,0]]

while True:
	mapping(x, y, image_matrix)
