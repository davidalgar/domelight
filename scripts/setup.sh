#!/bin/bash
#
#
# Setup script for any raspbian pi

# Needs root in order to setup cron, etc
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# clone feed candy (for ./fc-server-rpi)

#make sure pi owns everything
#chown -R pi github

# copy fcserver-rpi to /usr/bin
ln -s /home/pi/github/domelight/patterns /var/www/
ln /home/pi/github/domelight/patterns/templelights.php /var/www/templelights.php

# setup cron job to run launcher.sh on boot
result=`crontab -l > newcron`
echo "# launcher for feedcandy domelights on boot" >> newcron
echo "@reboot sh /home/pi/launcher.sh > /home/pi/logs/cronlog 2>&1" >> newcron
echo "OK"

# move launcher.sh and killall.sh to /usr/bin

echo "Manual Tasks"
echo
echo "1. Setup wi-fi broadcast for the pi"
echo "2. ...."

