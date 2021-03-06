#/bin/bash
#
# plik z komendami pakietów, jakie trzeba do instalacji w systemie
#
# all commands with packages needed to be installed on the system to work.
#
apt-get update
# remember to answer T (Yes) to install additional packages, which are needed
# system specyfic packages
apt-get install lighttpd tree htop iftop iptraf vim-nox joe
# python specific packages 
apt-get install python-pip python-flask ipython rrdtool python-rrdtool git python-smbus python-requests
#
# creating necessary lighttpd configuration, directories and change ownership to satisfy lighttpd
# students can do it manually from hand or just execute this script
# it is up to teacher ;-)
echo "python JSON-RPC library"
pip install python-jsonrpc
echo "-------- links in web server config directory ---"
mkdir -p /var/www/cgi-bin
chown www-data.www-data /var/www/ -R
chmod g+w /var/www/ -R
cd /etc/lighttpd/conf-enabled
ln -s ../conf-available/10-cgi.conf
ln -s ../conf-available/10-rrdtool.conf
ln -s ../conf-available/10-status.conf
cd /
echo "Lighttpd features enabled..."
# 
cd /root
echo "wiring-x86 python library for coderdojo library"
git clone https://github.com/emutex/wiring-x86.git
cd wiring-x86
python setup.py install
echo "done."

