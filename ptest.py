import bot_movement as bm
import ultrasonic as u

try:
	while True:
        	if u.ultra() < 20:
                	bm.turn_right()
        	else:
                	bm.up()
except:
        print "cleaning ptest.py"
finally:
        print "done execution"
