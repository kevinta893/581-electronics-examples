import RPi.GPIO as GPIO
import time

ledPin = 11
buttonPin = 13

def setup():
  GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
  GPIO.setup(ledPin, GPIO.OUT)   # Set LedPin's mode is output
  GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.output(ledPin, GPIO.LOW) # Set LedPin high(+3.3V) to turn on led

def loop():
  while True:
      if(GPIO.input(buttonPin) == False):
        print "Button pressed!"
        GPIO.output(ledPin, GPIO.HIGH)  # led on
        time.sleep(0.2)
        GPIO.output(ledPin, GPIO.LOW) # led off
        time.sleep(0.2)

        GPIO.output(ledPin, GPIO.HIGH)  # led on
        time.sleep(0.2)
        GPIO.output(ledPin, GPIO.LOW) # led off
        time.sleep(0.2)
		
		
		
		

def destroy():
  GPIO.cleanup()                  # Release resource

if __name__ == '__main__':     # Program start from here
  setup()
  try:
    loop()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()