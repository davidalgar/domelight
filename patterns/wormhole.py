#!/usr/bin/env python

"""
A client for Open Pixel Control

Fades from the outside edges inward, converging in the center.

To run:
First start the gl simulator and provide the layout file to use.

    gl_server your_layout_file.json

Then run this script in another shell to send colors to the simulator

    wormhole.py -l your_layout_file.json

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
# color functions

# Method used from Miami pattern by ColinHarrington
# https://github.com/zestyping/openpixelcontrol/blob/master/python_clients/miami.py
def pixel_color(t, id, coord, n_pixels):
    """
    Compute the color of a given pixel.

    Returns an (r, g, b) tuple in the range 0-255
    """

    x, y, z = coord

    y += color_utils.cos(x + 0.2*z, offset=0, period=1, minn=0, maxx=0.6)
    z += color_utils.cos(x, offset=0, period=1, minn=0, maxx=0.3)
    x += color_utils.cos(y + z, offset=0, period=1.5, minn=0, maxx=0.2)

    r = color_utils.cos(x, offset=t/8, period=2.5, minn=0, maxx=1)
    g = color_utils.cos(y, offset=t/8, period=2.5, minn=0, maxx=1)
    b = color_utils.cos(z, offset=t/8, period=2.5, minn=0, maxx=1)
    r, g, b = color_utils.contrast((r, g, b), 0.5, 1.4)

    return (r*256, g*256, b*256)


# -------------------------------------------------------------------------------
# run pattern

print '    sending pixels forever (control-c to exit)...'
print

n_pixels = len(coordinates)
n_short_strips = 2
n_long_strips = 6
short_strip = 9
long_strip = 18
start_time = time.time()

while True:
    t = time.time() - start_time
    pixels = [pixel_color(t, id, coord, n_pixels) for id, coord in enumerate(coordinates)]
    client.put_pixels(pixels, channel=0)