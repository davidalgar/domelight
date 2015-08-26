__author__ = 'david.algar'

# strip layout:  ( b = panel[x][4] )
#
#    a1       a2     a2        a1
#
#        1 4             0 b
#
#    a0       a3     a3        a0
#
#    a0        a3     a3       a0
#
#        2 b             3 b
#
#    a1        a2     a2       a1
#

import time
# returns a list of panels, size 4
#   each panel in the list is a list of size 5 sections - 4 corners, followed by the center
#     each entry is a tuple - (first_led, last_led) representing the range of pixels for that section
def get_panels():
    panels = []

    for i in range(4):
        base = i * 128
        panels.append([])
        panels[i] = panels[i] + [(base + 0, base + 15), (base + 16, base + 31), (base + 32, base + 47),
                                 (base + 48, base + 63),
                                 (base + 64, base + 127)]
    return panels


# Returns 5 diagonal "strips" that can be colored to make cool patterns
def diagonal_strips():
    panels = get_panels()

    strips = []

    # top left corner
    strips.append([])
    strips[0] = [panels[1][1]]

    # next strip  (do them this way)
    strips.append([])
    strips[1] = [panels[2][0]] + [panels[1][0]] + [panels[1][4]] + [panels[1][2]] + [panels[0][2]]

    # middle, biggest strip
    strips.append([])
    strips[2] = [panels[2][1]] + [panels[2][4]] + [panels[2][3]] + [panels[3][3]] + [panels[0][3]] + [panels[1][3]] + [
        panels[0][4]] + [panels[0][1]]

    # next strip
    strips.append([])
    strips[3] = [panels[2][2]] + [panels[3][2]] + [panels[3][4]] + [panels[3][0]] + [panels[0][0]]

    # bottom right corner
    strips.append([])
    strips[4] = [panels[3][1]]

    return strips


# Returns a matrix representing the 16 'pixels' of the panels
def pixel_grid():
    grid = [[0 for x in range(4)] for x in range(5)]
    return grid


import pattern_utils as utils

def color_diagonal_strip(strip_index, color, pixels):
    strips = diagonal_strips()

    strip = strips[strip_index]

    tmp = strip[0][0]
    ss = tmp / 64
    pi = tmp % 64
    anim_colors = utils.get_rainbow_fade(pixels[ss][pi], color)
    total_wait = len(anim_colors) * (1/utils.fps)
    desired_time = 1
    offset = 0
    if(total_wait < desired_time):
        offset = (1.0-total_wait) / len(anim_colors) * 1.0
    for t in range(len(anim_colors)):
        anim_color = anim_colors[t]
        for i in range(len(strip)):
            for x in range(strip[i][0], strip[i][1] + 1):
                substrip = x / 64
                pixel_index = x % 64
                #print "substrip " + str(substrip)
                #print "pixel index " + str(pixel_index)
                #print "len pixels: " + str(len(pixels))
                #print "len subpixels: " + str(len(pixels[substrip]))
                pixels[substrip][pixel_index] = anim_color
        for i in range(utils.n_strips):
            utils.put_pixels(pixels, i)
        time.sleep(1/utils.fps)
        time.sleep(offset)
    return pixels
