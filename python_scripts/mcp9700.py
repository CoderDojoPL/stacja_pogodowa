# -*- coding: utf-8 -*-
#

# Import the time module enable sleeps between turning the led on and off.
import time

# Import the GPIOEdison class from the wiringx86 module.
from wiringx86 import GPIOGalileo as GPIO

# Create a new instance of the GPIOEdison class.
# Setting debug=True gives information about the interaction with sysfs.
gpio = GPIO(debug=True)
pin = 4
analogpin = 16  # 13 digital, Analog inputs: 14-A0,15-A1,16-A2,17-A3,18-A4,19-A5 
state = gpio.HIGH

# Set pin 13 to be used as an output GPIO pin.
print 'Setting up pin %d' % pin
gpio.pinMode(pin, gpio.OUTPUT)
gpio.pinMode(analogpin, gpio.ANALOG_INPUT)

print 'Blinking pin %d now...' % pin
try:
    while(True):
        # Write a state to the pin. ON or OFF.
        gpio.digitalWrite(pin, state)
        value = gpio.analogRead(analogpin)
        temp = value*5/1024.0
        temp_2 = temp - 0.5
        temp_3 = (temp_2 / 0.01)
        print "Value from "+ str(analogpin) + " is: "+ str(value) + " | temp: "+ str(temp_3)

        # Toggle the state.
        state = gpio.LOW if state == gpio.HIGH else gpio.HIGH

        # Sleep for a while.
        time.sleep(0.5)

# When you get tired of seeing the led blinking kill the loop with Ctrl-C.
except KeyboardInterrupt:
    # Leave the led turned off.
    print '\nCleaning up...'
    gpio.digitalWrite(pin, gpio.LOW)

    # Do a general cleanup. Calling this function is not mandatory.
    gpio.cleanup()
