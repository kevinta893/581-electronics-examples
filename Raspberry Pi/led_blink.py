import RPi.GPIO as GPIO
import time

ledPin = 11    # pin11

def setup():
  GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
  GPIO.setup(ledPin, GPIO.OUT)   # Set LedPin's mode is output
  GPIO.output(ledPin, GPIO.HIGH) # Set LedPin high(+3.3V) to turn on led

def blink():
  while True:
    GPIO.output(ledPin, GPIO.HIGH)  # led on
    time.sleep(1)
    GPIO.output(ledPin, GPIO.LOW) # led off
    time.sleep(1)





def destroy():
  GPIO.cleanup()                  # Release resource

if __name__ == '__main__':     # Program start from here
  setup()
  try:
    blink()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()