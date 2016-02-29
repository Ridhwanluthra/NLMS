from ultrasonic import ultra
import click_picture as cp
x=0
y=0
m = [[0,0,0,0,1,0],[0,0,1,0,0,0],[1,1,1,0,0,0],[1,0,0,0,1,1],[0,0,0,0,0,0]]


i=0
while (i<100):
    i+=1
    print ultra()
    if(ultra()<20):
        cp.clicked()
	print "CLICKED!"
        break
#first_mapping(x,y,m)
#mapping(x,y,m)
