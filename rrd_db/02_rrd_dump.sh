#!/bin/bash
#
# dumps database to xml file
DB="/opt/weather_station.rrd"


if [ -e ${DB} ]
then
    rrdtool dump ${DB} > /tmp/weather_station_data.xml
else
    echo "--------"
    echo "Warning: file - ${DB} - does not exist."
    echo "--------"
    exit 1
fi




