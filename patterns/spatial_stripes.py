#!/usr/bin/env python

"""A demo client for Open Pixel Control
http://github.com/zestyping/openpixelcontrol

Creates moving stripes visualizing the x, y, and z coordinates
mapped to r, g, and b, respectively.  Also draws a moving white
spot which shows the order of the pixels in the layout file.

To run:
First start the gl simulator using, for example, the included "wall" layout

    make
    bin/gl_server layouts/wall.json

Then run this script in another shell to send colors to the simulator

    python_clients/spatial_stripes.py --layout layouts/wall.json

"""

from __future__ import division
import time
import sys
import optparse
try:
    import json
except ImportError:
    import simplejson as json

import opc
import color_utils
import pattern_utils as utils



#-------------------------------------------------------------------------------
# color function

def pixel_color(t, coord, ii, n_pixels):
    """Compute the color of a given pixel.

    t: time in seconds since the program started.
    ii: which pixel this is, starting at 0
    coord: the (x, y, z) position of the pixel as a tuple
    n_pixels: the total number of pixels

    Returns an (r, g, b) tuple in the range 0-255

    """
    # make moving stripes for x, y, and z
    x, y, z = coord
    r = color_utils.cos(x, offset=t / 4, period=1, minn=0, maxx=0.7)
    g = color_utils.cos(y, offset=t / 4, period=1, minn=0, maxx=0.7)
    b = color_utils.cos(z, offset=t / 4, period=1, minn=0, maxx=0.7)
    r, g, b = color_utils.contrast((r, g, b), 0.5, 2)

    # make a moving white dot showing the order of the pixels in the layout file
    spark_ii = (t*80) % n_pixels
    spark_rad = 8
    spark_val = max(0, (spark_rad - color_utils.mod_dist(ii, spark_ii, n_pixels)) / spark_rad)
    spark_val = min(1, spark_val*2)
    r += spark_val
    g += spark_val
    b += spark_val

    # apply gamma curve
    # only do this on live leds, not in the simulator
    #r, g, b = color_utils.gamma((r, g, b), 2.2)

    return (r*256, g*256, b*256)


#-------------------------------------------------------------------------------
# send pixels

def main(parseOpts = False, looplimit=10):
    coordinates = utils.getCoordinates("/home/pi/bm2015.json")

    client = utils.connectToServer()

    print '    sending pixels forever (control-c to exit)...'
    print

    n_pixels = utils.strip_length * utils.n_strips
    start_time = time.time()
    for i in range(looplimit * utils.fps):
        t = time.time() - start_time
        pixels = [pixel_color(t, coord, ii, n_pixels) for ii, coord in enumerate(coordinates)]
        client.put_pixels(pixels, channel=0)
        time.sleep(1 / utils.fps)

if __name__ == "__main__":
    while True:
        main(True)