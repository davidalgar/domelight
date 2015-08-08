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
orange = [255, 140, 0]
yellow = [255, 220, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
purple = [128, 0, 128]
off = [0, 0, 0]

light_red = [100, 0, 0]


def put_pixels(c_strip, channel):
    # TODO swap implementation
    # client.put_pixels(c_strip, channel=channel)
    pixels = []
    for single_strip in strip:
        for pixel in single_strip:
            pixels.append(pixel)
    client.put_pixels(pixels, channel=0)


# -------------------------------------------------------------------------------
# setup strip model

# strip layout:
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

strips = [[4, 2],
          [3, 1],
          [7, 5],
          [8, 6]
          ]

n_strips = 8
strip_length = 64

# init all strips to red
strip = []
for n in range(n_strips):
    strip.append([])
    for y in range(strip_length):
        strip[n].append(light_red)
    put_pixels(strip[n], n)

# order of strips to fade when fading
progression = [1, 4, 8, 5, 2, 3, 7, 6]
colors = [red, orange, yellow, green, blue, purple]
color = 0


# -------------------------------------------------------------------------------
# run pattern

print '    sending pixels forever (control-c to exit)...'
print


def rainbow_fade():
    while True:
        next_color()
        for i in range(len(progression)):
            fade_strip(i, colors[color])


def fade_strip(strip_index, color):
    for x in range(len(strip[strip_index])):
        strip[strip_index][x] = color
        put_pixels(strip[strip_index], strip_index)
        time.sleep(1 / options.fps)


def next_color():
    global color
    color = (color + 1) % len(colors)


rainbow_fade()