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
n_strips = 8
strip_length = 64

strip = []

# init all strips to red
def init_strip(color):
    global strip
    for n in range(n_strips):
        strip.append([])
        for y in range(strip_length):
            strip[n].append(color)
        put_pixels(strip[n], n)

# order of strips to fade when fading
progression = [1, 4, 0, 5, 2, 3, 7, 6]
colors = [red, orange, yellow, green, blue, purple]
color = 0

panel = 0
panels = [0, 1, 2, 3]

init_strip(white)

# -------------------------------------------------------------------------------
# run pattern

print '    sending pixels forever (control-c to exit)...'

def rainbow_fade():
    global strip
    print "FADE"
    while True:
        print "1"
        next_color()
        print range(len(strip))
        for i in range(len(strip)):
            print "i: "+str(i)
            if i % 2 == 0:
                print "fade strip " + str(i)
                fade_strip(progression[i], colors[color])

def fade_strip(strip_index, color):
    global strip
    start_color = strip[strip_index][0]
    delta_x = (color[0] - start_color[0])
    delta_g = (color[1] - start_color[1])
    delta_b = (color[2] - start_color[2])
    print "from " + str(start_color) + " to " + str(color) + "  dx: " + str(delta_x) + " dg: " + str(delta_g) + " db: " + str(delta_b)
    for t in range(0, 11):
        if t < 10:
            anim_color = [start_color[0] + (delta_x/10)*t, start_color[1] + (delta_g / 10)*t, start_color[2] + (delta_b / 10)*t]
        else:
            anim_color = color
        for x in range(len(strip[strip_index])):
            strip[strip_index][x] = anim_color
            strip[strip_index+1][x] = anim_color
        put_pixels(strip[strip_index], strip_index)
        put_pixels(strip[strip_index+1], strip_index+1)
        time.sleep(1 / 2)


def next_color():
    global color
    color = (color + 1) % len(colors)

rainbow_fade()

# ----------------------------------------------------------
# showcase pattern

def show_tiger():
    tiger_strips = [0, 1]
    show_panel(tiger_strips, orange)


def show_elephant():
    elephant_strips = [2, 3]
    show_panel(elephant_strips, elephant_blue)


def show_nautilus():
    nautilus_strips = [4,5]
    show_panel(nautilus_strips, dark_blue)


def show_octopus():
    octopus_strips = [6,7]
    show_panel(octopus_strips, red)


def show_panel(panel_strips, color):
    global strip
    global strip_length
    global n_strips
    for n in range(n_strips):
        for x in range(strip_length):
            if n in panel_strips:
                strip[n][x] = color
            else:
                strip[n][x] = off
        put_pixels(strip[n], 0)


def panel_spotlight():
    while True:
        show_tiger()
        time.sleep(5)
        show_elephant()
        time.sleep(5)
        show_octopus()
        time.sleep(5)
        show_nautilus()
        time.sleep(5)

#panel_spotlight()
