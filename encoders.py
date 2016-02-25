import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)

leften = 18
righten = 17
dps = 30.000/24.000  #distance per spoke
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
        if (a == 1 and b == 0):
            counter_left += 1
            #print "left counter "
            #print counter_left*dps
        if (c == 1 and d == 0):
            counter_right += 1
            #print "right coutner "
            #print counter_right*dps
        return [counter_left*dps, counter_right*dps]
def refresh():
    global a
    global c
    global counter_left
    global counter_right
    counter_left = 0
    counter_right = 0
    c = 0
    a = 0
