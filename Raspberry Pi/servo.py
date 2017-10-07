import RPi.GPIO as GPIO
import time

servo1 = None
servoPin = 12

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPin, GPIO.OUT)

    servo1 = GPIO.PWM(servoPin, 50)	#channel (pin), frequency
    servo1.start(7.5)


def loop():
    while True:
        servo1.ChangeDutyCycle(7.5)  # turn towards 90 degree
        time.sleep(1)               # sleep 1 second
        servo1.ChangeDutyCycle(2.5)  # turn towards 0 degree
        time.sleep(1)               # sleep 1 second
        servo1.ChangeDutyCycle(12.5) # turn towards 180 degree
        time.sleep(1)               # sleep 1 second





def destroy():
    GPIO.cleanup()                  # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
