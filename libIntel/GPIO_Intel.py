#!/usr/bin/env python

#-------------------------------------------------------#
#                                                       #
#              Name: GPIO_Intel.py                      #
#         Author: James Clarke, Pridopia.               #
#       Website: http://www.pridopia.co.uk              #
#              Date: 05 / 03 / 14                       #
#                Version: 1.01                          #
#                                                       #
#-------------------------------------------------------#
#
#	Patch Notes 1.01:
#
#	Fixed GPIO.cleanup()
#	Added GPIO_Intel to lib folder ( Library ) for organization
#	when more support is added for I2C, SPI, EEPROM?
#
# Copyright 2013 Pridopia (www.pridopia.co.uk)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIC,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either-express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time, sys, os

Pins = {
"IO2":  (0,  31, 32),
"IO3":  (0,  30, 18),
"IO4":  (0,  0,  28),
"IO5":  (0,  0,  17),
"IO6":  (0,  0,  24),
"IO7":  (0,  0,  27),
"IO8":  (0,  0,  26),
"IO9":  (0,  0,  19),
"IO10": (0,  42, 16),
"IO11": (0,  43, 25),
"IO12": (0,  54, 38),
"IO13": (0,  55, 39),
"A0":   (0,  37, 44),
"A1":   (0,  36, 45),
"A2":   (0,  23, 46),
"A3":   (0,  22, 47),
"A4":   (21, 29, 48),
"A5":   (20, 29, 49),
"PWM3": (3,  30, 18),
"PWM5": (5,  0,  17),
"PWM6": (6,  0,  24),
"PWM9": (1,  0,  19),
"PWM10":(7,  42, 16),
"PWM11":(4,  0,  43)
}

PinsEnabled = {
"IO2":  False,
"IO3":  False,
"IO4":  False,
"IO5":  False,
"IO6":  False,
"IO7":  False,
"IO8":  False,
"IO9":  False,
"IO10": False,
"IO11": False,
"IO12": False,
"IO13": False,
"A0":   False,
"A1":   False,
"A2":   False,
"A3":   False,
"A4":   False,
"A5":   False,
"PWM3": False,
"PWM5": False,
"PWM6": False,
"PWM9": False,
"PWM10":False,
"PWM11":False
}


class Intel:

	def __init__(self):
		print "Initial Setup."
		return

	def cmd(self, value, file):
		with open(file, 'w') as File:		# Very slow write speed compared to Raspberry Pi / Compiled Arduino Sketch
			File.write(str(value))
		return

	def setup(self, pin, dir='out'):
		actpin = Pins[pin][2]
		activate = Pins[pin][1]
		self.cmd('1', '/sys/class/gpio/gpio{}/value'.format(activate))
		self.cmd(dir, '/sys/class/gpio/gpio{}/direction'.format(actpin))
		PinsEnabled[pin] = True
		return 1

	def output(self, pin, value='1'):
		actpin = Pins[pin][2]
		if PinsEnabled[pin]:
			self.pullup(pin)
			self.cmd(value, '/sys/class/gpio/gpio{}/value'.format(actpin))
			return 1
		else:
			print "{} has not been set to output.".format(pin)
			return 0

	def input(self, pin):
		actpin = Pins[pin][2]
		if PinsEnabled[pin]:
			self.pullup(pin, 'pullup')
			with open('/sys/class/gpio/gpio{}/value'.format(actpin), 'r') as File:
				return File.readline()[:-1]

	def pullup(self, pin, drive='strong'):
		actpin = Pins[pin][2]
		self.cmd(drive, '/sys/class/gpio/gpio{}/drive'.format(actpin))
		return 1

	def pwm(self, pin, periodsec=0.02, dutysec=0.01):
		actpin = Pins[pin][0]
		periodnano = int(float(periodsec) * 1000000000)	# Should translate it from 0.02 Seconds to the value in Nano seconds
		dutynano = int(float(dutysec) * 1000000000)	# Not accurate enough yet for Servo control. This Linux =/= Realtime OS + Python 'Garbage Collection'
		self.cmd('1', '/sys/class/pwm/pwmchip0/pwm{}/enable'.format(actpin))
		self.cmd(periodnano, '/sys/class/pwm/pwmchip0/pwm{}/period'.format(actpin))
		self.cmd(dutynano, '/sys/class/pwm/pwmchip0/pwm{}/duty_cycle'.format(actpin))
		return 1

	def pwm_shutdown(self, pin):
		actpin = Pins[pin][0]
		self.cmd('0', '/sys/class/pwm/pwmchip0/pwm{}/enable'.format(actpin))
		return 1

	def cleanup(self):
		for Pin in Pins:
			if Pin[:2] == 'IO':
				actpin = Pins[Pin][2]
				self.cmd('0', '/sys/class/gpio/gpio{}/value'.format(actpin))
			elif Pin[:3] == 'PWM':
				actpin = Pins[Pin][0]
				self.cmd('0', '/sys/class/pwm/pwmchip0/pwm{}/enable'.format(actpin))

	def stepper(self, pins, steps, direction, detail="low"):
		if detail == "high":
			pattern = [
				"1000",
				"1100",
				"0100",
				"0110",
				"0010",
				"0011",
				"0001",
				"1001"
			]
		else:
			pattern = [
				"1100",
				"0110",
				"0011",
				"1001"
			]
		for A in pins:
			self.setup(A)
		if direction == "CW":
			while steps:
				for step in pattern:
					steps = steps -1
					for A, Id in enumerate(pins):
						self.output(Id, step[A:A+1])
		elif direction == "CCW":
			while steps:
				for step in reversed(pattern):
					steps = steps -1
					for A, Id in enumerate(pins):
						self.output(Id, step[A:A+1])


#	def ultrasonic(self, trig, echo):	# Do not use, Intel Galileo Read / Write very slow. Distance = Wrong
#		self.setup(trig, "in")		# Response 0.04 instead of sub 0.001 time.
#		self.setup(echo, "out")
#		stop = 0
#		start = 0
#		self.output(trig, "1")
#		time.sleep(0.00001)
#		self.output(trig, "0")
#		start = time.time()
#		timeout = start + 0.05
#		while self.input(echo) == 0 and start <= timeout:
#			start = time.time()
#		while self.input(echo) and time.time() <= timeout:
#			stop = time.time()
#		elapsed = stop - start
#		print elapsed
#		distance = (elapsed * 34300.0) / 2.0
#		return distance
