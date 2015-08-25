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

import random
import time
import sys
import optparse

import opc
import color_utils
import pattern_utils as utils

try:
    import json
except ImportError:
    import simplejson as json

# -------------------------------------------------------------------------------
# connect to server


# -------------------------------------------------------------------------------
# color variables (TODO share)

white = [255, 255, 255]
red = [255, 0, 0]
orange = [255, 140, 0]
yellow = [255, 220, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
dark_blue = [0, 0, 255]
elephant_blue = [25,25,50]
purple = [128, 0, 128]
off = [0, 0, 0]

light_red = [100, 0, 0]

# -------------------------------------------------------------------------------
# run pattern


# ----------------------------------------------------------
# showcase pattern

strip = []

def show_tiger():
    tiger_strips = [6,7]
    show_panel(tiger_strips, orange)


def show_elephant():
    elephant_strips = [2, 3]
    show_panel(elephant_strips, elephant_blue)


def show_nautilus():
    nautilus_strips = [4,5]
    show_panel(nautilus_strips, dark_blue)


def show_octopus():
    octopus_strips = [0, 1]
    show_panel(octopus_strips, red)


def show_panel(panel_strips, color):
    global strip
    for n in range(utils.n_strips):
        for x in range(utils.strip_length):
            if n in panel_strips:
                strip[n][x] = color
            else:
                strip[n][x] = off
        utils.put_pixels(strip, 0)


def main(parseOpts = False, looplimit=5):
    global strip

    strip = utils.init(parseOpts)

    for x in range(looplimit):
        show_tiger()
        time.sleep(5)
        show_elephant()
        time.sleep(5)
        show_octopus()
        time.sleep(5)
        show_nautilus()
        time.sleep(5)


if __name__ == "__main__":
    while True:
        main(True)