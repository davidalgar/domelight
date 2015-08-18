import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

import panel

# one = [[0, 0], [0, 19], [19, 19], [19, 0]]

# two = [[21, 40], [21, 21], [40, 21], [40, 40]]


one = [[40, 10], [40, 0], [30, 0]]

two = [[10, 0], [0, 0], [0, 10]]

three = [[0, 30], [0, 40], [10, 40]]

four = [[30, 40], [40, 40], [40, 30]]

five = [[21, 10], [21, 30], [20, 30], [20, 21], [10, 21], [10, 20], [30, 20], [30, 21], [20, 21], [20, 10]]

# panel:
#
#
#  (0,40)              (40,40)
#
#
#           (20,20)
#
#
#  (0,0)               (40,0)
#

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



str_lines = []
# panel 1
str_lines += panel.movesteps(panel.offset(one, 1, 1))
str_lines += panel.movesteps(panel.offset(two, 1, 1))
str_lines += panel.movesteps(panel.offset(three, 1, 1))
str_lines += panel.movesteps(panel.offset(four, 1, 1))
str_lines += panel.movesteps(panel.offset(five, 1, 1))

# panel 2
#str_lines += panel.movesteps(panel.offset(panel.flip_x(one), -1, 1))
#str_lines += panel.movesteps(panel.offset(panel.flip_x(two), -1, 1))

# panel 3
#str_lines += panel.movesteps(panel.offset(panel.flip_y(one), 1, -1))
#str_lines += panel.movesteps(panel.offset(panel.flip_y(two), 1, -1))

# panel 4
#str_lines += panel.movesteps(panel.offset(panel.flip_x(panel.flip_y(one)), -1, -1))
#str_lines += panel.movesteps(panel.offset(panel.flip_x(panel.flip_y(two)), -1, -1))

print '[\n' + ',\n'.join(str_lines) + '\n]'

print str(len(str_lines))