# temple_light_manager.py
#
#  on boot, start time-based patterns
#  ( manager.py will be killed by NodeJS if command is received )
#
#
#

import time

import panel_test
import lava_lamp
import spatial_stripes
import burnin


#F.U.B.U.
import temple_test
import slow_full_panel_fade
import rainbow_diag_stripes
import rainbow_fade
import full_panel_fade

time = time.time()
onehour = 1000 * 60 * 60


def gethour():
    return int(time.time()) % 24


# quick test to identify strips
while True:
    #panel_test.main()
    print("ok")
    temple_test.main()

while True:
    hr = gethour()
    if hr == 13 or hr == 0:
        rainbow_fade.main(10)
    elif hr == 14 or hr == 1:
        rainbow_diag_stripes.main(10)
    elif hr == 15 or hr == 2:
        full_panel_fade.main(10)
    elif hr == 16 or hr == 3:
        slow_full_panel_fade.main()
    elif hr == 17 or hr == 4:
        lava_lamp.main(10)
    elif hr == 18 or hr == 5:
        spatial_stripes.main(10)
    elif hr == 19 or hr == 6:
        lava_lamp.main(10)
    elif hr == 20 or hr == 7:
        rainbow_fade.main()
    elif hr == 21 or hr == 8:
        slow_full_panel_fade.main()
    elif hr == 22 or hr == 9:
        lava_lamp.main(10)
    elif hr == 23 or hr == 10:
        lava_lamp.main(10)
    elif hr == 12 or hr == 1:
        spatial_stripes.main(10)
    else:
        full_panel_fade.main()
    time.sleep(onehour)