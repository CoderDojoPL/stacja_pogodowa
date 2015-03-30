#!/usr/bin/env python

#-------------------------------------------------------#
#                                                       #
#              Name: Test.py                            #
#         Author: James Clarke, Pridopia.               #
#       Website: http://www.pridopia.co.uk              #
#              Date: 05 / 03 / 14                       #
#                Version: 1.01                          #
#                                                       #
#-------------------------------------------------------#
#
#	Patch Notes 1.01:
#
#	Capture Keyboard Interrupt ( Ctrl + C ) to clean up GPIO Pins.
#	Corrected the PWM 
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

import lib.GPIO_Intel as GPIO
import time, sys, os

Gpio = GPIO.Intel()
Gpio.setup('IO2')
Gpio.setup('IO3')
Gpio.setup('IO4')
Gpio.setup('IO5')
Gpio.setup('IO6', 'in')

Gpio.pullup('IO6', 'strong')
Gpio.output('IO2', '1')
Gpio.output('IO3', '1')

try:
	while True:
		Gpio.output('IO2', '1')
		Gpio.output('IO3', '0')
		time.sleep(1)
		Gpio.output('IO3', '1')
		Gpio.output('IO2', '0')
		time.sleep(1)
		#Gpio.pwm('PWM3', dutysec='0.2')
		#time.sleep(0.2)
		#Gpio.pwm('PWM3', dutysec='0.1')
		#time.sleep(0.2)
		#Gpio.pwm('PWM3', dutysec='0.05')
		#time.sleep(0.2)
		#Gpio.pwm('PWM3', dutysec='0.025')
		#time.sleep(0.2)
except KeyboardInterrupt:
	Gpio.cleanup()
	Gpio.pwm_shutdown('PWM3')

