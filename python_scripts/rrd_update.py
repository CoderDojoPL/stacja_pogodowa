#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  
#  
import sys
from rrdtool import *
from rrdtool import update as rrd_update

galileo_path = "/opt/";
if galileo_path not in sys.path:
    sys.path.append(galileo_path);

from coderdojo_library import *


if __name__ == '__main__':
	GalileoBoard = CoderDojoGalileo()
	a = GalileoBoard.getTemperature()
	b = GalileoBoard.getUVIndex()
	c = GalileoBoard.getPressure()
	d = GalileoBoard.getHumidity()
	e = GalileoBoard.getRainIntensity()
	rrd_update('/opt/weather_station.rrd', 'N:' + str(a)+':' + str(b)+':' + str(c)+':' + str(d)+':' + str(e) );




