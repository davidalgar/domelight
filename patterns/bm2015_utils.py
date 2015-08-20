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

def get_panels():
    panels = []

    for i in range(4):
        base = i * 128
        panels.append([])
        panels[i] = panels[i] + [(base + 0, base + 15), (base + 16, base + 31), (base + 32, base + 47), (base + 48, base + 63),
                       (base + 64, base + 127)]
    return panels


def diagonal_strips():
    panels = get_panels()

    strips = []

    # top left corner
    strips.append([panels[1][1]])
    print "Panels: "+str(panels[1][1])
    print "strips: "+str(strips)

    # next strip
    strips.append(panels[2][0] + panels[1][0] + panels[1][4] + panels[1][2] + panels[0][2])

    #middle, biggest strip
    strips.append(panels[2][1] + panels[2][4] + panels[2][3] + panels [3][3] + panels[0][3] + panels[1][3] + panels[0][4] + panels[0][1])

    #next strip
    strips.append(panels[2][2] + panels[3][2] + panels[3][4] + panels[3][0] + panels[0][0])

    #bottom right corner
    strips.append(panels[3][1])

    print "Len Strips: "+str(len(strips))
    print "Len Strips[0] "+str(len(strips[0]))

    return strips


def color_diagonal_strip(strip_index, color, pixels):
    strips = diagonal_strips()

    strip = strips[strip_index]

    for i in range(len(strip)):
        print "strip["+str(i) + "]"+ str(strip[i])
        for x in range(strip[i][0], strip[i][1]+1):
            pixels[x] = color
    return pixels