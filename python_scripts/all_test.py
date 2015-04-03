#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  skeleton_coderdojo.py
#  
#  Copyright 2015 CoderDojo.org.pl
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

import sys, time, datetime

# importing special library for Galielo Project
galileo_path = "/opt/";
if galileo_path not in sys.path:
    sys.path.append(galileo_path);
from coderdojo_library import *
####



if __name__ == '__main__':
	# here main part of application
	
	# create object of our BOARD.....
	GalileoBoard = CoderDojoGalileo()
	# turn ON led B
	while True:
		GalileoBoard.ledA_ON()
		# read temperature from MCP9700 
		o1 = GalileoBoard.getPhotoresistor()
		o0 = GalileoBoard.getTemperature()
		o2 = GalileoBoard.getUVIndex()
		o3 = GalileoBoard.getPressure()
		o4 = GalileoBoard.getHumanidity()
		hum_percent = ( o4 * 100 ) / 1023.0
		# wait half a second
		print "Photoresisor : "+ str(o1) # + " sdl: "+ str(sdl)
		print "Temperature : "+ str(o0)
		print "UVIndex : " + str(o2)
		print "Pressure : " + str(o3)
		print "Humanidity: " + str(o4) + " = " + str(hum_percent) + " %"
		print "----------------------------------------------------"
		time.sleep(1)
		# turn OFF led B
		GalileoBoard.ledA_OFF()
		time.sleep(0.5)
	

