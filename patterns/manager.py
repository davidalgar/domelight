# temple_light_manager.py
#
#  on boot, start time-based patterns
#  ( manager.py will be killed by NodeJS if command is received )
#
#
#

import time

import panel_test
import rainbow_diag_stripes
import rainbow_fade
import wooooow

time = time.time()
onehour = 1000 * 60 * 60


def gethour():
    return 1


# quick test to identify strips
while True:
    panel_test.main(looplimit=3)
    wooooow.main(looplimit=1)

while True:
    hr = gethour()
    if hr == 13 or hr == 0:
        rainbow_fade.main()
    elif hr == 14 or hr == 1:
        rainbow_diag_stripes.main()
    elif hr == 15 or hr == 2:
        wooooow.main()
    elif hr == 16 or hr == 3:
        rainbow_fade.main()
    elif hr == 17 or hr == 4:
        rainbow_fade.main()
    elif hr == 18 or hr == 5:
        rainbow_fade.main()
    elif hr == 19 or hr == 6:  # 6am, sunrise, 7pm, sunset
        rainbow_fade.main()
    elif hr == 20 or hr == 7:
        rainbow_fade.main()
    elif hr == 21 or hr == 8:
        rainbow_fade.main()
    elif hr == 22 or hr == 9:
        rainbow_fade.main()
    elif hr == 23 or hr == 10:
        rainbow_fade.main()
    elif hr == 12 or hr == 1:
        rainbow_fade.main()
    else:
        wooooow.main()
    time.sleep(onehour)
