#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  
#  
import sys, requests
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
	c = GalileoBoard.getHumidity()
	d = GalileoBoard.getPressure()
	e = GalileoBoard.getRainIntensity()
	rrd_update('/opt/weather_station.rrd', 'N:' + str(a)+':' + str(b)+':' + str(c)+':' + str(d)+':' + str(e) );
	# now create data and POST to OpenWeatherMap
	wheather_data = {
	# Zambrów coordinates from http://dateandtime.info/citycoordinates.php?id=753895
	'lat' : '52.9855000', # your lattitide
	'long' : '22.2431900', # longitude
	'name' : 'Station_of_CoderDojo_Team',
	'temp' : str(a),
	'uv' : str(b),
	'humidity' : str(c),
	'pressure' : str(d),
	}
	# Basic AUTH to POST
	weather_auth = ('abix_pl','abixpl2015')
	# now POST
	r = requests.post("http://openweathermap.org/data/post", data = weather_data, auth = weather_auth )
	# for later, we can test or show codes of execute
	# print "Long execution code is: " + r.text





