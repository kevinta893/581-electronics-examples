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

def setup():
    global mcp
    mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


def loop():
    while True:
        values = read_mcp_analog()
        # Print the ADC values.
        print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
        # Pause for half a second.
        time.sleep(0.5)




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
