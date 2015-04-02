#!/usr/bin/rrdcgi
<HTML>
<HEAD><TITLE>RRDCGI - weather_station.rrd data</TITLE></HEAD>
<BODY>
<H1>Datas stored in our RRD</H1>

<!-- Comments: RRD-Graph produces PNG file, but does not show properly, so workaround is to comment it in HTML -->
<!--
 <RRD::GRAPH /var/www/temperature.png --lazy --title="Temperature"
 DEF:cel=/opt/weather_station.rrd:temperature:AVERAGE
 LINE2:cel#00a000:"Temp. Celsius">
  <RRD::GRAPH /var/www/photoresistor.png --lazy --title="Density of light"
 DEF:cel=/opt/weather_station.rrd:photoresistor:AVERAGE
 LINE2:cel#00a000:"Light in index of mV">
-->

Average Temperature:<br>
<IMG SRC="/temperature.png" WIDTH="531" HEIGHT="203"><br>
Average light density:<br>
<IMG SRC="/photoresistor.png" WIDTH="531" HEIGHT="203">

</BODY>
</HTML>
