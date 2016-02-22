import picamera

camera = picamera.PiCamera()

"""
i need ultrasonic reading
usfront, usleft, usright, usback
if any are less than lets say 10cm click
"""

def click_picture(int k,int l):
        camera.capture('img_%d_%d.jpg'%k %l)

        #analysis of image
