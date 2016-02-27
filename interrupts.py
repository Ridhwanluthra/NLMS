import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)

leften = 18
righten = 17
dps = 30.000/24.000  #distance per spoke
gpio.setup(leften,gpio.IN)
gpio.setup(righten,gpio.IN)
counter_left = 0
counter_right = 0
def d_move():
    gpio.setmode(gpio.BCM)
    while True:
        global counter_left
        global counter_right
        def left_call(channel):
            counter_left += 1
        def right_call(channel):
            counter_right += 1
        gpio.add_event_detect(leften, gpio.both, callback=left_call)
        gpio.add_event_detect(righten, gpio.both, callback = right_call)
        return [counter_left*dps/2, counter_right*dps/2]
def refresh():
    global counter_left
    global counter_right
    counter_left = 0
    counter_right = 0