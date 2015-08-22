import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

import panel

one = [[45, 0], [60, 0], [60, 20]]

two = [[60, 45], [60, 60], [45, 60]]

three = [[15, 60], [0, 60], [0, 45]]

four = [[0, 15], [0, 0], [15, 0]]

five = [[32, 15], [32, 45], [30, 45], [30, 32], [15, 32], [15, 30], [45, 30], [45, 32], [30, 32], [30, 15]]

# panel:
#
#
#  (0,60)              (60,60)
#
#
#           (30,30)
#                       (60,15)
#
#  (0,0)               (60,0)

# all panels:
#
#    a2       a3     a3        a2
#
#        2 b             1 b
#
#    a1       a4     a4        a1
#
#    a1        a4     a4       a1
#
#        3 b             4 b
#
#    a2        a3     a3       a2
#

str_lines = []

# panel 1
for list in [one, two, three, four, five]:
    if list == five:
        str_lines += panel.movesteps(panel.offset(list, 1, 1), 64)
    else:
        str_lines += panel.movesteps(panel.offset(list, 1, 1), 16)

# panel 2
for list in [one, two, three, four, five]:

    if list == five:
        str_lines += panel.movesteps(panel.offset(panel.flip_x(list), -1, 1), 64)
    else:
        str_lines += panel.movesteps(panel.offset(panel.flip_x(list), -1, 1), 16)

# panel 3
for list in [one, two, three, four, five]:
    if list == five:
        str_lines += panel.movesteps(panel.offset(panel.flip_x(panel.flip_y(list)), -1, -1), 64)
    else:
        str_lines += panel.movesteps(panel.offset(panel.flip_x(panel.flip_y(list)), -1, -1), 16)

# panel 4
for list in [one, two, three, four, five]:
    if list == five:
        str_lines += panel.movesteps(panel.offset(panel.flip_y(list), 1, -1), 64)
    else:
        str_lines += panel.movesteps(panel.offset(panel.flip_y(list), 1, -1), 16)


print '[\n' + ',\n'.join(str_lines) + '\n]'
