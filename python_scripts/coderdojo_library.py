#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  coderdojo_library.py
#  
#  Copyright 2015 CoderDojo - GPL Licence
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import time
# Import the GPIOEGalileo class from the wiringx86 module.
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


# define our class for project
class CoderDojoGalileo(object):
	
	def __init__(self):
		self.board = GPIO()
		self.pin_temperature = 14     # A0
		self.pin_uvout = 15			  # A1
		self.pin_reference3v = 16	  # A2
		self.pin_humidity = 17	  # A3
		self.pin_pressure = 18		  # A4 - DL
		self.pin_rain_analog = 19	  # A5
		self.pin_rain_digital = 2	  # digital 2 - rain is....
		self.pin_digital_A = 2
		self.pin_digital_B = 4
		self.pin_digital_C = 7
		self.temperature = 0
		self.uvIntensity = 0 # UV/cm2
		self.humidity = 0
		self.rawhumanidity = 0
		self.pressure = 0
		self.rain_intensity = 0
		# now we will set all analog pins as INPUT
		for pinA in range(14,20):
			self.board.pinMode(pinA, self.board.ANALOG_INPUT)
		# now setting pin 2 as INPUT for rain detection
		self.board.pinMode(2, self.board.INPUT)
		# now wi will light OFF all the possible digital leds
		for pinX in range(3,14):
			self.board.pinMode(pinX, self.board.OUTPUT)
			self.board.digitalWrite(pinX, self.board.LOW)
	
	def __str__(self):
		print "Object to read sensors - for CoderDojo by Adam Jurkiewicz"
			
	def ledA_ON(self):
		self.board.digitalWrite(self.pin_digital_A, self.board.HIGH)
		
	def ledB_ON(self):
		self.board.digitalWrite(self.pin_digital_B, self.board.HIGH)
		
	def ledC_ON(self):
		self.board.digitalWrite(self.pin_digital_C, self.board.HIGH)
		
	def ledA_OFF(self):
		self.board.digitalWrite(self.pin_digital_A, self.board.LOW)
		
	def ledB_OFF(self):
		self.board.digitalWrite(self.pin_digital_B, self.board.LOW)
		
	def ledC_OFF(self):
		self.board.digitalWrite(self.pin_digital_C, self.board.LOW)
		
	def getTemperature(self):
		value = self.board.analogRead(self.pin_temperature)
		self.temperature = round ( ( ( ( value * 5 / 1024.0 ) - 0.5 ) / 0.01 ), 2 )
		return self.temperature
	
	def getRawTemperature(self):
		self.raw_temperature = self.board.analogRead(self.pin_temperature)
		return self.raw_temperature	
		
	def getLastTemperature(self):
		return self.temperature

	def getUVIndex(self):
		
		def averageAnalogRead(pin,avg=9):
			read_value = 0
			for read in range(1,avg):
				read_value += self.board.analogRead(pin)
			return float(read_value/avg)
		
		def mapfloat(x, in_min, in_max, out_min, out_max):
			#special function to compute UV Index
			return float((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
		
		uvLevel = averageAnalogRead(self.pin_uvout)
		refLevel = averageAnalogRead(self.pin_reference3v)
		# Use the 3.3V power pin as a reference to get a very accurate output value from sensor
		outputVoltage = 3.3 / refLevel * uvLevel
		# Convert the voltage to a UV intensity level
		# based on information from tutorial:
		# https://learn.sparkfun.com/tutorials/ml8511-uv-sensor-hookup-guide/using-the-ml8511
		self.uvIntensity = round( mapfloat(outputVoltage, 0.99, 2.8, 0.0, 15.0)  ,2)
		return self.uvIntensity
		
	def getLastUVIndex(self):
		return self.uvIntensity
		
	def getHumidity(self):
		value = self.board.analogRead(self.pin_humidity)
		self.humidity = round(value * 0.2 ,2) # change read to %
		return self.humidity # in %
	
	def getRawHumidity(self):
		self.rawhumidity = self.board.analogRead(self.pin_humidity)
		return self.rawhumidity
	
	def getPressure(self):
		raw_value = self.board.analogRead(self.pin_pressure)
		# reads from 0 = 15 kPa to 1023 = 115 kPa
		# so 115-15 = 100, divided by 1023 = 0,097 kPA is 1 read on Analog input
		# analog output shoud be about 4,59 mV / hPa
		pressure_kpa = raw_value * 0.097 # (in kPA)
		pressure_hpa = 150 + ( pressure_kpa * 10 )
		self.pressure = round(pressure_hpa,2)
		return self.pressure
	
	def getRainIntensity(self):
		raw_value = self.board.analogRead(self.pin_rain_analog)
		to_compute = 515 - raw_value   # 515 is the highest value == 0%, total dry
		self.rain_intensity = round(to_compute/5.15,2) # 5.15 is 1% of rain intensity
		return self.rain_intensity

if __name__ == '__main__':
	print "This is module - it sould not be executed itself..."
	

