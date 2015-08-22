#!/usr/bin/env python

import time
import pattern_utils as utils

white = [255, 255, 255]
green = [0, 255, 0]
off = [0, 0, 0]
light_red = [100, 0, 0]

strip = []

def main(parseOpts = False):
    global strip

    strip = utils.init(parseOpts)

    panel_test()


def panel_test():
    global strip
    for x in range(5):
        for i in range(len(strip)):
            strip = utils.color_strip_everyother(light_red)
            for x in range(i+1):
                strip[i][x] = white
                strip[i][63-x] = green
            utils.put_pixels(strip, i)
            time.sleep(1)


if __name__ == "__main__":
    main(True)
