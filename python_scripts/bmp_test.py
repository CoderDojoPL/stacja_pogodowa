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
		sda = GalileoBoard.getbmp_180sda()
		sdl = GalileoBoard.getbmp_180sdl()
		# wait half a second
		print "sda: "+ str(sda) + " sdl: "+ str(sdl)
		time.sleep(0.5)
		# turn OFF led B
		GalileoBoard.ledA_OFF()
		time.sleep(0.5)
	

