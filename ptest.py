import bot_movement as bm
import ultrasonic as u

try:
        if u.ultra() < 20:
                bm.turn_right()
                bm.up()
        else:
                bm.up()
except:
        print "cleaning ptest.py"
finally:
        print "done execution"
