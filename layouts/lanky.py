import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

import panel

one = [[0, 0], [0, 19], [19, 19], [19, 0]]

two = [[21, 40], [21, 21], [40, 21], [40, 40]]


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

# panel 2
str_lines += panel.movesteps(panel.offset(panel.flip_x(one), -1, 1))
str_lines += panel.movesteps(panel.offset(panel.flip_x(two), -1, 1))

# panel 3
str_lines += panel.movesteps(panel.offset(panel.flip_y(one), 1, -1))
str_lines += panel.movesteps(panel.offset(panel.flip_y(two), 1, -1))

# panel 4
str_lines += panel.movesteps(panel.offset(panel.flip_x(panel.flip_y(one)), -1, -1))
str_lines += panel.movesteps(panel.offset(panel.flip_x(panel.flip_y(two)), -1, -1))


print '[\n' + ',\n'.join(str_lines) + '\n]'
