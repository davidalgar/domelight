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
import random
import time
import sys
import optparse

import opc

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
orange = [255, 255, 255]
yellow = [0, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
purple = [0, 0, 0]
off = [0, 0, 0]

# panels:
#
#    b                 b
#       2           1
#          a     a
#
#          a     a
#       4           3
#     b                 b
#
#

# -------------------------------------------------------------------------------
# setup strip model

strips = [[4, 2],
          [3, 1],
          [7, 5],
          [8, 6]
          ]

n_strips = 8

# init all strips to red
strip = []
for n in range(8):
    for y in range(64):
        strip[0][y] = red

# order of strips to fade when fading
progression = [1, 4, 8, 5, 2, 3, 7, 6]
colors = [red, orange, yellow, green, blue, purple, off]


print '    sending pixels forever (control-c to exit)...'
print


def rainbow_fade():
    start_time = time.time()
    while True:
        t = time.time() - start_time
        # fade to new color
        for i in range(len(progression)):
            color = next_color()
            fade_strip(i, color)

        # wait before next fade
        time.sleep(5)


def fade_strip(strip_index, color):
    for x in range(len(strip[strip_index])):
        strip[strip_index][x] = color
        client.put_pixels(strip[strip_index], channel=strip_index)
        time.sleep(1 / options.fps)


def next_color():
    return red