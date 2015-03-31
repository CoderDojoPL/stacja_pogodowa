#!/bin/bash
#
# installing python Galileo library
#
#.
cd /root
# next line cloning repository (copying files from remote to local)
echo "I will copy from remote...."
git clone https://github.com/galileo-chofrock/pyGalileo
cd pyGalileo
mv __init__.py pyGalileo.py
mkdir -p /opt/pyGalileo
cp *.py /opt/pyGalileo/.
echo "Done....."
