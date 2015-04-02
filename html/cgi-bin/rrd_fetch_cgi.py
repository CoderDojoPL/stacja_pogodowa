#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
#
import sys, datetime
from rrdtool import *

time_now = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")

import rrdtool

output = rrdtool.fetch("/opt/weather_station.rrd", 'AVERAGE')
trmaxTuples = output[2]
rrd_header = output[1]
txt_header = "Header fields in RRD : "

for position in rrd_header:
    txt_header += position + ', '

# now generate html page

print "Content-Type: text/html"
print
print "<html><head>"
print "<title>Sensors value</title>"
print "</head>"
print "<body>"
print "<h3>"+ txt_header +"</h3><hr>"
print "Read time: " + time_now +"<hr>"
print "last 3 reads in ascending order:<br>"
for element in trmaxTuples[-3:]:
    print "Element of RRD : " 
    for every_one in element:
        print str(every_one) + ","
    print "<BR>"
print "<hr>"
print "</body>"
print "</html>"
