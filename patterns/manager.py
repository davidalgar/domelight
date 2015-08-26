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

#F.U.B.U.
import temple_test
import slow_full_panel_fade
import rainbow_diag_stripes
import rainbow_fade
import full_panel_fade


def gethour():
    return (int(time.time()) % 24)

n = 1

while True:
    hr = gethour()
    if hr == 13 or hr == 0:
        print "rainbow fade"
        rainbow_fade.main(False, n)
    elif hr == 14 or hr == 1:
        print "diag stripes"
        rainbow_diag_stripes.main(False, n)
    elif hr == 15 or hr == 2:
        print "full panel fade"
        full_panel_fade.main(False, n)
    elif hr == 16 or hr == 3:
        print "slow full panel fade"
        slow_full_panel_fade.main(False, n)
    elif hr == 17 or hr == 4:
        print "lava lamp"
        lava_lamp.main(False, n)
    elif hr == 18 or hr == 5:
        print "spatial stripes"
        spatial_stripes.main(False, n*2)
    elif hr == 19 or hr == 6:
        print "lava lamp"
        lava_lamp.main(False, n)
    elif hr == 20 or hr == 7:
        print "rainbow fade"
        rainbow_fade.main(False, n)
    elif hr == 21 or hr == 8:
        print "slow full panel fade"
        slow_full_panel_fade.main(False, n)
    elif hr == 22 or hr == 9:
        print "lava lamp"
        lava_lamp.main(False, n)
    elif hr == 23 or hr == 10:
        print "lava lamp"
        lava_lamp.main(False, n)
    elif hr == 12 or hr == 1:
        print "spatial stripes"
        spatial_stripes.main(False, n*2)
    else:
        print "full panel fade"
        full_panel_fade.main()