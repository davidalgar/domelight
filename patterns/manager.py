# temple_light_manager.py
#
#  on boot, start time-based patterns
#  ( manager.py will be killed by NodeJS if command is received )
#
#
#

import time

time = time.time()
onehour = 1000 * 60 * 60


def gethour():
    return 1

while True:
    hr = gethour()
    if hr == 1 or hr == 2:
        rainbow_fade()
    time.sleep(onehour)
