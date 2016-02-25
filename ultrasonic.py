import RPi.GPIO as gpio
import time

print "Distance Measurement In Progress"
def ultra():
        try:
                gpio.setmode(gpio.BCM)

                trig = 20
                echo = 21

                gpio.setup(trig,gpio.OUT)
                gpio.setup(echo,gpio.IN)
                gpio.output(trig, False)

                time.sleep(2)

                gpio.output(trig, True)
                time.sleep(0.00001)
                gpio.output(trig, False)

                while gpio.input(echo)==0:
                  pulse_start = time.time()

                while gpio.input(echo)==1:
                  pulse_end = time.time()      

                pulse_duration = pulse_end - pulse_start
                distance = pulse_duration*17150
                distance = round(distance, 2)
                return distance
        except:
                print "reading was interrupted"
        finally:
                gpio.cleanup(trig)
                gpio.cleanup(echo)