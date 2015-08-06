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

top_start = [0, 40]
top_step_one = [20, 40]
top_step_two = [20, 20]

bottom_start = [40, 20]
bottom_step_one = [20, 20]
bottom_step_two = [20, 0]

lines = []

def makepanel():
    print '1 ' + str(len(lines))
    movestep(top_start, top_step_one)
    print '2 ' + str(len(lines))
    movestep(top_step_one, top_step_two)

    print '3 ' + str(len(lines))
    movestep(bottom_start, bottom_step_one)
    print '4 ' + str(len(lines))
    movestep(bottom_step_one, bottom_step_two)
    print '5 ' +  str(len(lines))

def movestep(start, step_one):
    if start[0] != step_one[0]:
        print 'a'
        movex(start[0], step_one[0], start[1])
    elif start[1] != step_one[1]:
        print 'b'
        movey(start[1], step_one[1], start[0])
    else:
        print 'c'

def movex(start, end, y):
    for x in range(start, end):
        lines.append([x, y])

def movey(start, end, x):
    for y in range(start, end):
        lines.append([x, y])

makepanel()

for point in lines:
    print ' ( ' + str(point[0]) + ', ' + str(point[1]) + ', 0)'