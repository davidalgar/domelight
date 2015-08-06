import panel

one = []
one.append([0,0])
one.append([0,20])
one.append([20,20])
one.append([20,0])

two = []
two.append([20,40])
two.append([20,20])
two.append([40,20])
two.append([40,40])

str_lines = []
str_lines += panel.movesteps(one)
str_lines += panel.movesteps(two)
str_lines += panel.movesteps(panel.translate_x(one))
str_lines += panel.movesteps(panel.translate_x(two))
str_lines += panel.movesteps(panel.translate_y(one))
str_lines += panel.movesteps(panel.translate_y(two))
str_lines += panel.movesteps(panel.translate_x(panel.translate_y(one)))
str_lines += panel.movesteps(panel.translate_y(panel.translate_x(two)))

print '[\n' + ',\n'.join(str_lines) + '\n]'