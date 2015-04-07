#!/bin/bash
#
# script that creates databases
#
# file location
DB="/opt/weather_station.rrd"
#

###### description
#rrdtool create _file-name_ \
#  --step _step_time_for_updating_database_in_seconds_ \
#  DS:_database_name_:_HOW_to_measure_TYPE_:_heartbeat_:_minimum_:_maximum_ \
#  RRA:AVERAGE:0.5:1:1200 \
#  RRA:MIN:0.5:12:2400 \
#  RRA:MAX:0.5:12:2400 \
#  RRA:AVERAGE:0.5:12:2400

#
# -- _HOW_to_measure_TYPE_ 
# DS:ds-name:GAUGE | COUNTER | DERIVE | ABSOLUTE:heartbeat:min:max
# or
# DS:ds-name:COMPUTE:rpn-expression
#
# GAUGE is for things like temperatures or number of people in a room or the value of a RedHat share.
# COUNTER is for continuous incrementing counters like the ifInOctets counter in a router. The COUNTER data source assumes that the counter never decreases, except when a counter overflows. The update function takes the overflow into account. The counter is stored as a per-second rate. When the counter overflows, RRDtool checks if the overflow happened at the 32bit or 64bit border and acts accordingly by adding an appropriate value to the result.
# DERIVE will store the derivative of the line going from the last to the current value of the data source. This can be useful for gauges, for example, to measure the rate of people entering or leaving a room. Internally, derive works exactly like COUNTER but without overflow checks. So if your counter does not reset at 32 or 64 bit you might want to use DERIVE and combine it with a MIN value of 0.
# ABSOLUTE is for counters which get reset upon reading. This is used for fast counters which tend to overflow. So instead of reading them normally you reset them after every read to make sure you have a maximum time available before the next overflow. Another usage is for things you count like number of messages since the last update.
# COMPUTE is for storing the result of a formula applied to other data sources in the RRD. This data source is not supplied a value on update, but rather its Primary Data Points (PDPs) are computed from the PDPs of the data sources according to the rpn-expression that defines the formula. Consolidation functions are then applied normally to the PDPs of the COMPUTE data source (that is the rpn-expression is only applied to generate PDPs). In database software, such data sets are referred to as "virtual" or "computed" columns.

# _heartbeat_ defines the maximum number of seconds that may pass between two updates of this data source before the value of the data source is assumed to be *UNKNOWN*.

# _min_ and _max_ define the expected range values for data supplied by a data source. If min and/or max are specified any value outside the defined range will be regarded as *UNKNOWN*. If you do not know or care about min and max, set them to U for unknown. Note that min and max always refer to the processed values of the DS. For a traffic-COUNTER type DS this would be the maximum and minimum data-rate expected from the device.

# _rpn-expression_ defines the formula used to compute the PDPs of a COMPUTE data source from other data sources in the same <RRD>. It is similar to defining a CDEF argument for the graph command. Please refer to that manual page for a list and description of RPN operations supported. For COMPUTE data sources, the following RPN operations are not supported: COUNT, PREV, TIME, and LTIME. In addition, in defining the RPN expression, the COMPUTE data source may only refer to the names of data source listed previously in the create command. This is similar to the restriction that CDEFs must refer only to DEFs and CDEFs previously defined in the same graph command.


# RRA - Round Robin Archive - This parameter describes how long you want to hold your data, and in what resolution. There can be more than on archive. If the time span of an archive is full, the data will be consolidated and saved into the next archive.
# format: RRA:CF:xff:steps:rows


# more info at: http://oss.oetiker.ch/rrdtool/doc/rrdcreate.en.html

if [ -e ${DB} ]
then
    echo "--------"
    echo "Warning: file ${DB} exist. Delete it manually first."
    echo "--------"
    exit 1
fi


echo "Creating set of RRD database in one file 
	is updated every 5 minutes 
	has for data sources that that can save values from 0 to unlimited 
	saves 1 day in 5-minute resolution (288 * (300*1/60) / 60/24) 
	saves 1 week in in 15-minute resolution (672 * (300*3/60) / 60/24) 
	saves 1 month in 1-hour resolution (744 * (300*12/60) / 60/24) 
	saves 1 year in 6-hour resolution (1460 * (300*72/60) / 60/24) "


rrdtool create  ${DB} \
  --step 300 \
  DS:temperature:GAUGE:1200:-44:155 \
  DS:uvindex:GAUGE:1200:0:200 \
  DS:humidity:GAUGE:1200:0:100 \
  DS:pressure:GAUGE:1200:0:1100 \
  DS:rainintensity:GAUGE:1200:0:100 \
  RRA:AVERAGE:0.5:1:288 \
  RRA:AVERAGE:0.5:3:672 \
  RRA:AVERAGE:0.5:12:744 \
  RRA:AVERAGE:0.5:72:1460

if [ -e ${DB} ]
then
    echo " "
    echo " --> OK - database created successfuly..."
    exit 0
else
    echo " "
    echo " --> Warning: file ${DB} does not exist. Some error......"
    exit 1
fi


