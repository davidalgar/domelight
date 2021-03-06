#!/usr/bin/env python
"""
A demo client for Open Pixel Control
Modified from the raver_plaid client by 
    David Wallace / https://github.com/longears

Sets all pixels in strip to red, then green, then blue, then dark.
Useful for diagnosing color input order issues with LED strips that
may expect input orders other than RGB (e.g. WS2801).

Usage:
    python_clients/rgb_test_pattern.py
"""

from __future__ import division

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

import time
import bm2015_utils as bm2015
import pattern_utils as utils


# -------------------------------------------------------------------------------
# color variables

white = [255, 255, 255]
red = [255, 0, 0]
orange = [255, 97, 0]
yellow = [255, 255, 5]
green = [0, 255, 0]
blue = [15, 15, 200]
dark_blue = [0, 0, 255]
elephant_blue = [25, 25, 50]
purple = [128, 0, 128]
off = [0, 0, 0]
light_red = [100, 0, 0]

strip = []
colors = [red, orange, yellow, green, blue, purple, off, off]
color = 0

panel = 0
panels = [0, 1, 2, 3]


def rainbow_stripes(looplimit):
    global strip
    global color
    for i in range(looplimit * 5):
        for diag_strip in range(5):
            next_color()
            strip = bm2015.color_diagonal_strip(diag_strip, colors[color], strip)
            for x in range(len(strip)):
                utils.put_pixels(strip, x)
            time.sleep(1 / utils.fps)
        #for diag_strip in reversed(range(5)):
        #    prev_color()
        #    strip = bm2015.color_diagonal_strip(diag_strip, colors[color], strip)
        #    for x in range(len(strip)):
        #        utils.put_pixels(strip, x)
        #    time.sleep(1 / utils.fps)



def white_wipe():
    global strip
    global color
    for diag_strip in range(5):
        strip = bm2015.color_diagonal_strip(diag_strip, white, strip)
        for x in range(len(strip)):
            utils.put_pixels(strip, x)
        time.sleep(1 / 4)

def next_color():
    global color
    color = (color + 1) % len(colors)

def prev_color():
    global color
    color = (color - 1) % len(colors)

def main(parseOpts = False, looplimit = 100000):
    print '    sending pixels forever  ~~ (control-c to exit)...'
    global strip

    strip = utils.init(parseOpts)

    # forever rainbow stripes
    rainbow_stripes(looplimit)


if __name__ == "__main__":\
    main(True)