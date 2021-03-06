#!/usr/bin/rrdcgi
<HTML>
<HEAD><TITLE>RRDCGI - weather_station.rrd data</TITLE></HEAD>
<BODY>
<H1>Datas stored in our RRD</H1>

<!-- Comments: RRD-Graph produces PNG file, but does not show properly, so workaround is to comment it in HTML -->
<!--
 # temperature
 <RRD::GRAPH /var/www/temperature.png --lazy --title="Temperature"
 DEF:cel=/opt/weather_station.rrd:temperature:AVERAGE
 LINE2:cel#00a000:"Temp. Celsius">
 
 # uvindex
 <RRD::GRAPH /var/www/uvindex.png --lazy --title="Density of light"
 DEF:cel=/opt/weather_station.rrd:uvindex:AVERAGE
 LINE2:cel#00a000:"Light in index of mV">
 
 # humidity
 <RRD::GRAPH /var/www/humidity.png --lazy --title="Humanidity"
 DEF:cel=/opt/weather_station.rrd:humidity:AVERAGE
 LINE2:cel#00a000:"humidity in %">
 
 # pressure
 <RRD::GRAPH /var/www/pressure.png --lazy --title="Pressure"
 DEF:cel=/opt/weather_station.rrd:pressure:AVERAGE
 LINE2:cel#00a000:"Pressure in kPa">
 
 # rainintensity
 <RRD::GRAPH /var/www/rainintensity.png --lazy --title="Density of rain"
 DEF:cel=/opt/weather_station.rrd:rainintensity:AVERAGE
 LINE2:cel#00a000:"Intensity of light">
-->
Average values of sensords:<br>
Temperature:<br>
<IMG SRC="/temperature.png" WIDTH="531" HEIGHT="203"><br>
Light density:<br>
<IMG SRC="/uvindex.png" WIDTH="531" HEIGHT="203"><br>
humidity:<br>
<IMG SRC="/humidity.png" WIDTH="531" HEIGHT="203"><br>
Ppressure:<br>
<IMG SRC="/pressure.png" WIDTH="531" HEIGHT="203"><br>
Intensity of Rain:<br>
<IMG SRC="/rainintensity.png" WIDTH="531" HEIGHT="203"><br>
</BODY>
</HTML>
