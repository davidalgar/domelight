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
import pattern_utils as utils

strip = []

white = [255, 255, 255]
red = [255, 0, 0]
orange = [255, 140, 0]
yellow = [255, 255, 5]
green = [0, 255, 0]
blue = [15, 15, 200]
dark_blue = [0, 0, 255]
elephant_blue = [25, 25, 50]
purple = [128, 0, 128]
off = [0, 0, 0]
light_red = [100, 0, 0]


# order of strips to fade when fading
colors = [red, orange, yellow, green, blue, purple]
color = 0

panel = 0
panels = [0, 1, 2, 3]


# -------------------------------------------------------------------------------
# run pattern

def main(parseOpts = False, looplimit=10):
    global strip

    print '    sending pixels forever (control-c to exit)...'

    strip = utils.init(parseOpts)
    print "OK"

    for x in range(looplimit):
        for i in range(len(colors)):
            next_color()
            fade_to(colors[color])


def fade_to(color):
    global strip

    start_color = strip[0][0]

    anim_colors = utils.get_rainbow_fade(start_color, color)
    for t in range(len(anim_colors)):
        anim_color = anim_colors[t]
        for strip_index in range(len(strip)):
            for x in range(len(strip[strip_index])):
                strip[strip_index][x] = anim_color
            utils.put_pixels(strip, strip_index)
        time.sleep(1/utils.fps)


def next_color():
    global color
    color = (color + 1) % len(colors)


if __name__ == "__main__":
    while True:
        main(True)