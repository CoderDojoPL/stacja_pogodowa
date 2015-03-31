#/bin/bash
#
# plik z komendami pakietów, jakie trzeba do instalacji w systemie
#
# all commands with packages needed to be installed on the system to work.
#
apt-get update
# remember to answer T (Yes) to install additional packages, which are needed
# python specific packages 
apt-get install python-pip python-flask ipython rrdtool python-rrdtool git
# webserver package
apt-get install lighttpd 
# system specyfic packages
apt-get install tree htop iftop iptraf vim-nox joe
#


