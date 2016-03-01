# RUN THIS SCRIPT AND THE REST WILL RUN THEMSELVES

#from sys import argv
from traversal import mapping
from first_traversal import first_mapping
from anomaly import correct_the_location, rest
#from edging import edging
rest()
#image_matrix = edging(argv[1]) # convert the picture into edges and return the sub_matrix
# now i have the completed map of the room ready

# add the ultrasonic sensors to find and save from obstacles.
image_matrix = [[0,0,0,0,1,0],[0,0,1,0,0,0],[1,1,1,0,0,0],[1,0,0,0,1,1],[0,0,0,0,0,0]]

first_mapping(image_matrix)

while True:
	if mapping(image_matrix) == True:
                continue
        else:
                correct_the_location(image_matrix)
                continue
