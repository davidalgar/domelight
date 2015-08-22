__author__ = 'david.algar'

import optparse
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
import opc
from colorsys import hsv_to_rgb, rgb_to_hsv
import math
try:
    import json
except ImportError:
    import simplejson as json

n_strips = 8
strip_length = 64

client = 0

fps = 30


# call this before using any other util functions
def init(parse = True):
    if parse:
        parseOpts()
    else:
        #TODO we'll come here when using a pattern as a module
        fps = 30
    connectToServer()
    return init_strip()

# wrapper, shouldn't be necessary IRL but for simulator, can help
def put_pixels(c_strip, channel):
    #client.put_pixels(c_strip[channel-1], channel=channel)
    pixels = []
    for strip in c_strip:
        for pixel in strip:
            pixels.append(pixel)
    client.put_pixels(pixels, channel=0)

def connectToServer():
    global client
    client = opc.Client('127.0.0.1:7890')
    if client.can_connect():
        print '    connected to %s' % '127.0.0.1:7890'
    else:
        # can't connect, but keep running in case the server appears later
        print '    WARNING: could not connect to %s' % '127.0.0.1:7890'
    print
    return client


def parseOpts():
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

    coordinates = []
    for item in json.load(open(options.layout)):
        if 'point' in item:
            coordinates.append(tuple(item['point']))
    return coordinates

# init all strips to red
def color_strip_everyother(color):
    strip = []
    for n in range(n_strips):
        strip.append([])
        for y in range(strip_length):
            if y % 2 == 0:
                strip[n].append(color)
            else:
                strip[n].append([0, 0, 0])
        put_pixels(strip, n)
    return strip

def init_strip(color=None, put=False):
    if not color:
        color = [0, 0, 0]
    global n_strips
    global strip_length
    strip = []
    for n in range(n_strips):
        strip.append([])
        for y in range(strip_length):
            strip[n].append(color)
        if (put):
            put_pixels(strip, n)
    return strip

def get_rainbow_fade(rgb_start_color, rgb_end_color, steps):
    colors = []
    rgb_start_color = [rgb_start_color[0]/256., rgb_start_color[1]/256., rgb_start_color[2]/256.]
    rgb_end_color = [rgb_end_color[0]/256., rgb_end_color[1]/256., rgb_end_color[2]/256.]
    start = rgb_to_hsv(*rgb_start_color)
    end = rgb_to_hsv(*rgb_end_color)

    diff_h = start[0] - end[0]
    single_step_h = diff_h / steps
    diff_s = start[1] - end[1]
    single_step_s = diff_s / steps

    v = start[2]  # won't change

    for i in range(steps):
        step_h = i * single_step_h
        step_s = i * single_step_s
        rgb = hsv_to_rgb(start[0]-step_h, start[1] - step_s, v)
        colors.append((rgb[0] *256, rgb[1] * 256, rgb[2] * 256))
    return colors





