__author__ = 'david.algar'

import optparse
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
import opc

try:
    import json
except ImportError:
    import simplejson as json

n_strips = 8
strip_length = 64

client = 0


# call this before using any other util functions
def init():
    parseOpts()
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
