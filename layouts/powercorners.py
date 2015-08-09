import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

import panel

# Outside corners - 4ft length
one = [[10, 0], [0, 0], [0, 10]]
two = [[30, 40], [40, 40], [40, 30]]

# Outside corners - 2ft length
three = [[35, 0], [40, 0], [40, 5]]
four = [[0, 35], [0, 40], [5, 40]]

# Inside corners - 4ft length
five = [[9, 21], [19, 21], [19, 31]]
six = [[21, 31], [21, 21], [31, 21]]
seven = [[9, 19], [19, 19], [19, 9]]
eight = [[21, 9], [21, 19], [31, 19]]

strips = [one, two, three, four, five, six, seven, eight]

panels = []

for strip in strips:
    panels += panel.movesteps(panel.offset(strip, 1, 1))
    panels += panel.movesteps(panel.offset(panel.flip_x(strip), -1, 1))
    panels += panel.movesteps(panel.offset(panel.flip_y(strip), 1, -1))
    panels += panel.movesteps(panel.offset(panel.flip_x(panel.flip_y(strip)), -1, -1))

print '[\n' + ',\n'.join(panels) + '\n]'