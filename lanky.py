import panel

adjustment = 40


def adjust(list):
    result = []
    for i in list:
        i = [x + adjustment for x in i]
        result.append(i)
    return result


one = [[0, 0], [0, 19], [19, 19], [19, 0]]

two = [[21, 40], [21, 21], [40, 21], [40, 40]]


# panels:
#
#   2   1
#
#   4   3
#


str_lines = []
# first panel
str_lines += panel.movesteps(adjust(one))
str_lines += panel.movesteps(adjust(two))

str_lines += panel.movesteps(adjust(panel.flip_x(one)))
str_lines += panel.movesteps(adjust(panel.flip_x(two)))

str_lines += panel.movesteps(adjust(panel.flip_y(one)))
str_lines += panel.movesteps(adjust(panel.flip_y(two)))

# second panel
# str_lines += panel.movesteps(adjust(panel.translate_x(one)))
# str_lines += panel.movesteps(adjust(panel.translate_x(two)))

# panel 3
# str_lines += panel.movesteps(adjust(panel.translate_y(one)))
# str_lines += panel.movesteps(adjust(panel.translate_y(two)))

# panel 4
# str_lines += panel.movesteps(adjust(panel.translate_x(panel.translate_y(one))))
# str_lines += panel.movesteps(adjust(panel.translate_y(panel.translate_x(two))))


print '[\n' + ',\n'.join(str_lines) + '\n]'
