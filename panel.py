# 18.6 LEDs per 2ft
#
#   (0,40)                      (40,40)
#
#
#               (20,20)
#
#
#   (0,0)                       (40,0)
#


def movesteps(steps, maxLEDs):
    lines = []
    for i in range(len(steps) - 1):
        step = steps[i]
        next = steps[i + 1]
        lines += movestep(step, next)
    lines.append(steps[len(steps) - 1])

    while len(lines) > maxLEDs:
        lines.pop(len(lines)-1)

    str_lines = []
    for point in lines:
        str_lines.append('  {"point": [%.2f, %.2f, %.2f]}' % (point[0] / 30.0, point[1] / 30.0, 0))

    return str_lines


def movestep(start, step_one):
    lines = []
    if start[0] != step_one[0]:
        lines += movex(start[0], step_one[0], start[1])
    elif start[1] != step_one[1]:
        lines += movey(start[1], step_one[1], start[0])
    return lines


def movex(start, end, y):
    lines = []
    step = 2
    if start > end:
        step = -2
    for x in range(start, end, step):
        lines.append([x, y])
    return lines


def movey(start, end, x):
    lines = []
    step = 2
    if start > end:
        step = -2
    for y in range(start, end, step):
        lines.append([x, y])
    return lines


def translate_x(strip):
    new_strip = []
    for point in strip:
        new_strip.append([point[0] * -1, point[1]])
    return new_strip


def translate_y(strip):
    new_strip = []
    for point in strip:
        new_strip.append([point[0], point[1] * -1])
    return new_strip


def rotate90(strip, rotationpoint):
    new_strip = []
    for point in strip:
        curpoint = [point[0] - rotationpoint[0], point[1] - rotationpoint[1]]
        curpoint = [curpoint[1] * -1, curpoint[0]]
        curpoint = [curpoint[0] - rotationpoint[0], curpoint[1] - rotationpoint[1]]
        new_strip.append(curpoint)
    return new_strip


def flip_x(strip):
    new_strip = []
    for point in strip:
        new_strip.append([-1 * point[0], point[1]])
    return new_strip


def flip_y(strip):
    new_strip = []
    for point in strip:
        new_strip.append([point[0], -1 * point[1]])
    return new_strip


def offset(list, x, y):
    new_list = []
    for point in list:
        new_list.append([point[0] + x, point[1] + y])
    return new_list
