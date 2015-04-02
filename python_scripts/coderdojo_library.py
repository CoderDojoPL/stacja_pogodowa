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
		self.pin_photoresistor = 15   # A1
		self.pin_uvout = 16			  # A2 - DA
		self.pin_reference3v = 17	  # A3 - DL
		self.pin_bmpsda = 18		  # A4 - DA
		self.pin_bmpsdl = 19		  # A5 - DL
		self.pin_digital_A = 4
		self.pin_digital_B = 7
		self.pin_digital_C = 8
		self.temperature = 0
		self.raw_temperature = 0 # in mV
		self.photoresistor = 0
		self.uvIntensity = 0 # UV/cm2
		self.bmp180_temperature = 0
		self.bmp180_pressure = 0
		# now we will set all analog pins as INPUT
		for pinA in range(14,20):
			self.board.pinMode(pinA, self.board.ANALOG_INPUT)
		# now wi will light OFF all the possible digital leds
		for pinX in range(1,14):
			self.board.pinMode(pinX, self.board.OUTPUT)
			self.board.digitalWrite(pinX, self.board.LOW)
			
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
		self.raw_temperature = value
		return self.temperature
		
	def getLastTemperature(self):
		return self.temperature

	def getPhotoresistor(self):
		value = self.board.analogRead(self.pin_photoresistor)
		self.photoresistor = value
		return value
		
	def getLastPhotoresistor(self):
		return self.photoresistor
		
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
		self.uvIntensity = mapfloat(outputVoltage, 0.99, 2.8, 0.0, 15.0)  
		return self.uvIntensity
		
	def getLastUVIndex(self):
		return self.uvIntensity
		
	def getbmp_180sda(self):
		value = self.board.analogRead(self.pin_bmpsda)
		return value
	
	def getbmp_180sdl(self):
		value = self.board.analogRead(self.pin_bmpsdl)
		return value	

if __name__ == '__main__':
	print "This is module - it sould not be executed itself..."
	

