import panel

adjustment = 40


def adjust(list):
    result = []
    for i in list:
        i = [x + adjustment for x in i]
        result.append(i)
    return result


one = [[0, 0], [0, 20], [20, 20], [20, 0]]

two = [[20, 40], [20, 20], [40, 20], [40, 40]]

str_lines = []
str_lines += panel.movesteps(adjust(one))
str_lines += panel.movesteps(adjust(two))
str_lines += panel.movesteps(adjust(panel.translate_x(one)))
str_lines += panel.movesteps(adjust(panel.translate_x(two)))
str_lines += panel.movesteps(adjust(panel.translate_y(one)))
str_lines += panel.movesteps(adjust(panel.translate_y(two)))
str_lines += panel.movesteps(adjust(panel.translate_x(panel.translate_y(one))))
str_lines += panel.movesteps(adjust(panel.translate_y(panel.translate_x(two))))

print '[\n' + ',\n'.join(str_lines) + '\n]'
