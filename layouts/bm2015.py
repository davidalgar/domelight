import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

import panel

# one = [[0, 0], [0, 19], [19, 19], [19, 0]]

# two = [[21, 40], [21, 21], [40, 21], [40, 40]]


one = [[60, 20], [60, 0], [45, 0]]

two = [[15, 0], [0, 0], [0, 20]]

three = [[0, 45], [0, 60], [15, 60]]

four = [[45, 60], [60, 60], [60, 45]]

# 21 = 32
# 10 = 15
# 20 = 30
# 30 = 45

five = [[32, 15], [32, 45], [30, 45], [30, 32], [15, 32], [15, 30], [45, 30], [45, 32], [30, 32], [30, 15]]

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

# all panels ( i think?)
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
for list in [one, two, three, four, five]:
    str_lines += panel.movesteps(panel.offset(list, 1, 1))
    str_lines = str_lines[:-2]

# panel 2
for list in [one, two, three, four, five]:
    str_lines += panel.movesteps(panel.offset(panel.flip_x(list), -1, 1))
    str_lines = str_lines[:-2]

# panel 3
for list in [one, two, three, four, five]:
    str_lines += panel.movesteps(panel.offset(panel.flip_y(list), 1, -1))
    str_lines = str_lines[:-2]

# panel 4
for list in [one, two, three, four, five]:
    str_lines += panel.movesteps(panel.offset(panel.flip_x(panel.flip_y(list)), -1, -1))
    str_lines = str_lines[:-2]


print '[\n' + ',\n'.join(str_lines) + '\n]'

print str(len(str_lines))
