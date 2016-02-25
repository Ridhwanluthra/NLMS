import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)

leften = 17
righten = 18
dps = 33.800/24.000  #distance per spoke
gpio.setup(leften,gpio.IN)
gpio.setup(righten,gpio.IN)
counter_left = 0
counter_right = 0
c = 0
a = 0
def d_move():
    gpio.setmode(gpio.BCM)
    while True:
        global a
        global c
        global counter_left
        global counter_right
        b = a
        d = c
        a = gpio.input(leften)
        c = gpio.input(righten)
        if ((a == 1 and b == 0) or (a == 0 and b == 1)):
            counter_left += 1
            print "left counter "
            print counter_left*dps/2
        if ((c == 1 and d == 0) or (c == 0 and d == 1)):
            counter_right += 1
            print "right coutner "
            print counter_right*dps/2
        return [counter_left*dps/2, counter_right*dps/2]
def refresh():
    global a
    global c
    global counter_left
    global counter_right
    counter_left = 0
    counter_right = 0
    c = 0
    a = 0
