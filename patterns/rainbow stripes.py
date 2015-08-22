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
import bm2015_utils

try:
    import json
except ImportError:
    import simplejson as json


# -------------------------------------------------------------------------------
# command line

parser = optparse.OptionParser()
parser.add_option('-l', '--layout', dest='layout',
                  action='store', type='string',
                  help='layout file')
parser.add_option('-s', '--server', dest='server', default='127.0.0.1:7890',
                  action='store', type='string',
                  help='ip and port of server')
# 32fps default will get through 1 strip of 64 in exactly 2s
parser.add_option('-f', '--fps', dest='fps', default=32,
                  action='store', type='int',
                  help='frames per second')

options, args = parser.parse_args()

if not options.layout:
    parser.print_help()
    print
    print 'ERROR: you must specify a layout file using --layout'
    print
    sys.exit(1)


# -------------------------------------------------------------------------------
# parse layout file

print
print '    parsing layout file'
print

coordinates = []
for item in json.load(open(options.layout)):
    if 'point' in item:
        coordinates.append(tuple(item['point']))


# -------------------------------------------------------------------------------
# connect to server

client = opc.Client(options.server)
if client.can_connect():
    print '    connected to %s' % options.server
else:
    # can't connect, but keep running in case the server appears later
    print '    WARNING: could not connect to %s' % options.server
print


# -------------------------------------------------------------------------------
# color variables (TODO share)

white = [255, 255, 255]
red = [255, 0, 0]
orange = [255, 97, 0]
yellow = [255, 255, 5]
green = [0, 255, 0]
blue = [15, 15, 200]
dark_blue = [0, 0, 255]
elephant_blue = [25,25,50]
purple = [128, 0, 128]
off = [0, 0, 0]

light_red = [100, 0, 0]


def put_pixels(c_strip, channel):
    #client.put_pixels(c_strip, channel=channel)
    pixels = []
    for single_strip in strip:
        for pixel in single_strip:
            pixels.append(pixel)
    client.put_pixels(pixels, channel=0)


# -------------------------------------------------------------------------------
# setup strip model

n_strips = 8
strip_length = 64

strip = []

colors = [red, orange, yellow, green, blue, purple]
color = 0

panel = 0
panels = [0, 1, 2, 3]

# init all strips to red
def init_strip(color):
    global strip
    for n in range(n_strips):
        strip.append([])
        for y in range(strip_length):
            strip[n].append(color)
        #put_pixels(strip[n], n)


init_strip(off)


# -------------------------------------------------------------------------------
# run pattern

print '    sending pixels forever (control-c to exit)...'

def rainbow_fade():
    global strip
    global color
    while True:
        for diag_strip in range(5):
            next_color()
            strip = bm2015_utils.color_diagonal_strip(diag_strip, colors[color], strip)
            for x in range(len(strip)):
                put_pixels(strip[x], x)
            time.sleep(1 / 10)

def white_wipe():
    global strip
    global color
    for diag_strip in range(5):
        strip = bm2015_utils.color_diagonal_strip(diag_strip, white, strip)
        for x in range(len(strip)):
            put_pixels(strip[x], x)
        time.sleep(1 / 4)

def next_color():
    global color
    color = (color + 1) % len(colors)

white_wipe()

rainbow_fade()

# strip[0][0] = white
# strip[1][0] = white
# strip[2][0] = white
# strip[2][15] = white
# strip[3][0] = white
# #strip[4][17] = white
# #strip[4][32] = white
# #strip[4][47] = white
# put_pixels(strip[0],1)
# put_pixels(strip[1],2)
# put_pixels(strip[2],3)
# put_pixels(strip[3],4)
# put_pixels(strip[4],5)