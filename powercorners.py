import panel

adjustment = 40

def adjust(list):
    result = []
    for i in list:
        i = [x+adjustment for x in i]
        result.append(i)
    return result

one = []
one.append([35, 0])
one.append([40, 0])
one.append([40, 5])

two = []
two.append([0, 35])
two.append([0, 40])
two.append([5, 40])

three = []
three.append([9, 21])
three.append([19, 21])
three.append([19, 31])

four = []
four.append([21, 31])
four.append([21, 21])
four.append([31, 21])

five = []
five.append([9, 19])
five.append([19, 19])
five.append([19, 9])

six = []
six.append([21, 9])
six.append([21, 19])
six.append([31, 19])

str_lines = []
str_lines += panel.movesteps(one)
str_lines += panel.movesteps(panel.translate_x(panel.translate_y(one)))
str_lines += panel.movesteps(three)
str_lines += panel.movesteps(panel.translate_x(three))
str_lines += panel.movesteps(panel.translate_y(three))
str_lines += panel.movesteps(panel.translate_x(panel.translate_y(three)))
str_lines += panel.movesteps(panel.translate_y(panel.translate_x(three)))
