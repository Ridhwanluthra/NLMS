import bot_movement as bm

try:
    bm.up()
    print "turning left"
    bm.turn_left()
    print "turning right"
    bm.turn_right()
except KeyboardInterrupt:
    print "cleaning ptest.py"
finally:
    print "done execution"
