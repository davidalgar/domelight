import panel.py

one = []
one[0] = [0,0]
one[1] = [0,20]
one[2] = [20,20]
one[3] = [20,0]

two = []
two[0] = [20,40]
two[1] = [20,20]
two[2] = [40,20]
two[3] = [40,40]

str_lines = []
str_lines += panel.movesteps(one)
str_lines += panel.movesteps(two)


print '[\n' + ',\n'.join(str_lines) + '\n]'