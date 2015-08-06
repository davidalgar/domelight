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

lines = []

def makepanel():
    lines = []
    lines += movesteps([top_start, top_step_one, top_step_two])
    lines += movesteps([bottom_start, bottom_step_one, bottom_step_two])

    print '[\n' + ',\n'.join(lines) + '\n]'

def movesteps(steps):
    lines = []
    for i in range(len(steps)-1):
        step = steps[i]
        next = steps[i+1]
        lines += movestep(step, next)
    lines.append(steps[len(steps)-1])

    str_lines = []
    for point in lines:
        str_lines.append('  {"point": [%.2f, %.2f, %.2f]}' % (point[0]/20.0, point[1]/20.0, 0))

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
    step = 1
    if(start>end):
        step = -1
    for x in range(start, end, step):
        lines.append([x, y])
    return lines

def movey(start, end, x):
    lines = []
    step = 1
    if(start>end):
        step = -1
    for y in range(start, end, step):
        lines.append([x, y])
    return lines

#makepanel()

def translate_x(strip):
    new_strip = []
    for point in strip:
        new_strip.append([point[0]*-1, point[1]])
    return new_strip

def translate_y(strip):
    new_strip = []
    for point in strip:
        new_strip.append([point[0], point[1]*-1])
    return new_strip