import panel

one = [[5, 0], [0, 0], [0, 5]]

two = [[35, 40], [40, 40], [40, 35]]

three = [[9, 21], [19, 21], [19, 31]]

four = [[21, 31], [21, 21], [31, 21]]

five = [[9, 19], [19, 19], [19, 9]]

six = [[21, 9], [21, 19], [31, 19]]

panels = []
panels += panel.movesteps(panel.offset(one, 1, 1))
panels += panel.movesteps(panel.offset(two, 1, 1))
panels += panel.movesteps(panel.offset(three, 1, 1))
panels += panel.movesteps(panel.offset(four, 1, 1))
panels += panel.movesteps(panel.offset(five, 1, 1))
panels += panel.movesteps(panel.offset(six, 1, 1))

panels += panel.movesteps(panel.offset(panel.flip_x(one), -1, 1))
panels += panel.movesteps(panel.offset(panel.flip_x(two), -1, 1))
panels += panel.movesteps(panel.offset(panel.flip_x(three), -1, 1))
panels += panel.movesteps(panel.offset(panel.flip_x(four), -1, 1))
panels += panel.movesteps(panel.offset(panel.flip_x(five), -1, 1))
panels += panel.movesteps(panel.offset(panel.flip_x(six), -1, 1))


panels += panel.movesteps(panel.offset(panel.flip_y(one), 1, -1))
panels += panel.movesteps(panel.offset(panel.flip_y(two), 1, -1))
panels += panel.movesteps(panel.offset(panel.flip_y(three), 1, -1))
panels += panel.movesteps(panel.offset(panel.flip_y(four), 1, -1))
panels += panel.movesteps(panel.offset(panel.flip_y(five), 1, -1))
panels += panel.movesteps(panel.offset(panel.flip_y(six), 1, -1))

panels += panel.movesteps(panel.offset(panel.flip_x(panel.flip_y(one)), -1, -1))
panels += panel.movesteps(panel.offset(panel.flip_x(panel.flip_y(two)), -1, -1))
panels += panel.movesteps(panel.offset(panel.flip_x(panel.flip_y(three)), -1, -1))
panels += panel.movesteps(panel.offset(panel.flip_x(panel.flip_y(four)), -1, -1))
panels += panel.movesteps(panel.offset(panel.flip_x(panel.flip_y(five)), -1, -1))
panels += panel.movesteps(panel.offset(panel.flip_x(panel.flip_y(six)), -1, -1))

print '[\n' + ',\n'.join(panels) + '\n]'