import RPi.GPIO as GPIO
import time

ledPin = 11

def setup():
  GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
  GPIO.setup(ledPin, GPIO.OUT)   # Set ledPin's mode is output

def loop():
  while True:
	

def destroy():
  GPIO.output(ledPin, GPIO.LOW)   # led off
  GPIO.cleanup()                  # Release resource

if __name__ == '__main__':     # Program start from here
  setup()
  try:
    loop()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()
