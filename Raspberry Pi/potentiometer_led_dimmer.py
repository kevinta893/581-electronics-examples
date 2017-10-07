import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import time


#Hardware SPI config (turn on SPI in raspi-config Interfaces)
SPI_PORT = 0
SPI_DEVICE = 0
mcp = None

#need to install adafruit-mcp3008
#see: https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008
#Example from: https://github.com/adafruit/Adafruit_Python_MCP3008/blob/master/examples/simpletest.py


ledPin = 12
outputLed = None


def setup():
    global mcp
    mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(ledPin, GPIO.OUT)  # Set LedPin's mode is output

    global outputLed
    outputLed = GPIO.PWM(ledPin, 100)
    outputLed.start(0)

def loop():
    while True:
        values = read_mcp_analog()                          #returns all channels analog readings [0,1023]
        # Print the ADC values.

        global outputLed
        analogValue = (values[0]/1023.0) * 100.0
        print str(analogValue)
        outputLed.ChangeDutyCycle(analogValue);          #ChangeDutyCycle takes in a value from [0,100]
        time.sleep(0.100)                               #led can be a bit flickery


def read_mcp_analog():
    # Read all the ADC channel values in a list.
    global mcp
    values = [0] * 8
    for i in range(8):
        # The read_adc function will get the value of the specified channel (0-7).
        values[i] = mcp.read_adc(i)

    return values





def destroy():
    GPIO.cleanup()                  # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
