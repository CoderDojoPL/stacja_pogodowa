#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  

''' 
 ML8511 UV Sensor Read Example
 By: Nathan Seidle
 SparkFun Electronics
 Date: January 15th, 2014
 License: This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).
 
 The ML8511 UV Sensor outputs an analog signal in relation to the amount of UV light it detects.
 
 Connect the following ML8511 breakout board to Arduino:
 3.3V = 3.3V
 OUT = A0
 GND = GND
 EN = 3.3V
 3.3V = A1
 These last two connections are a little different. Connect the EN pin on the breakout to 3.3V on the breakout.
 This will enable the output. Also connect the 3.3V pin of the breakout to Arduino pin 1.
 '''
import time
from wiringx86 import GPIOGalileo as GPIO

'''
PIN mapping for Analog:
	A0 - 14
	A1 - 15
	A2 - 16
	A3 - 17
	A4 - 18
	A5 - 19
'''

# main instance
gpio = GPIO(debug=True)

# Hardware pin definitions
UVOUT = 14  # Analog A0 Output from the sensor
REF_3V3 = 15 # 3.3V power on the Arduino board

# setting pin type
# gpio.pinMode( _pin_, gpio.OUTPUT)
gpio.pinMode(UVOUT, gpio.ANALOG_INPUT)
gpio.pinMode(REF_3V3, gpio.ANALOG_INPUT)

def mapfloat(x, in_min, in_max, out_min, out_max):
	return float((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


def averageAnalogRead(pin,avg=8):
	read_value = 0
	for read in range(1,avg):
		read_value += gpio.analogRead(pin)
	return float(read_value/avg)

while True:
	print "test..."
	uvLevel = averageAnalogRead(UVOUT)
	refLevel = averageAnalogRead(REF_3V3)
  
	# Use the 3.3V power pin as a reference to get a very accurate output value from sensor
	outputVoltage = 3.3 / refLevel * uvLevel
	uvIntensity = mapfloat(outputVoltage, 0.99, 2.8, 0.0, 15.0)  #Convert the voltage to a UV intensity level


	print "output: " + str(refLevel)
	print "ML8511 output: " + str(uvLevel)
	print " / ML8511 voltage: " + str(outputVoltage)
	print " / UV Intensity (mW/cm^2): " + str(uvIntensity);
  





