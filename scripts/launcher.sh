#!/bin/sh
# launcher.sh
#  1) run fcserver
cd /home/pi
nohup /usr/bin/fcserver-rpi &


#  2) run basic light patter 
python /home/pi/github/domelight/patterns/manager.py
