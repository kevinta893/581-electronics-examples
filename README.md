# 581 Electronics Examples

A number of examples of basic electronics on both Arduino and Raspberry Pi. This also includes wiring diagrams and some templates. Intended for students in CPSC 581 at the University of Calgary.


See [Fritzing](http://fritzing.org/home/) to edit wiring diagrams.


## Sample Code
All sample code has some wiring documentation. Raspberry Pi code has been written in an Arduino style layout with setup(), loop(), and destory() functions.

Sample code has been tested on:
* **Arduino Mega 2560** 
* **Raspberry Pi 1 Model A**


### Raspberry Pi:
1. **led_blink** - A basic blink an LED 
2. **button_blink** - A button, when pushed, that makes an LED blink twice
3. **potentiometer_led_dimmer** - An example of how to use a Potentiometer, Photo Resistor, Force sensitive resistor, and other resistive components to dim LEDs. Look here if you want to learn how to use Analog Input (MCP3008 ADC converter) and PWM output on the Raspberry Pi
4. **adc_mcp3008_reader** - An example of how to use the MCP3008 ADC converter. A useful tool for looking at input values on the ADC
5. **servo** - A simple example of how to use a servo, servo waves back and forth
6. **template** - A template for Arduino style code in python for the Raspberry Pi


### Arduino:
1. **blink_led** - A basic blink an LED 
2. **button_led** - A button, when pushed, that makes an LED blink twice
3. **potentiometer_led_dimmer** - An example of how to use a Potentiometer, Photo Resistor, Force sensitive resistor, and other resistive components to dim LEDs. Look here if you would like to learn how to use PWM output.
2. **banana_meter** - A simple example of how to make a "makey-makey" from just an arduino
3. **servo_demo** - A simple example of how to use a servo, servo waves back and forth
