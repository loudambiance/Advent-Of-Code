import numpy

test = False
file = 'data/task9test.txt' if test else 'data/task9.txt'

with open(file) as f:
    depthmap = numpy.array([[int(x) for x in list(y)] for y in f.read().splitlines()])
print(depthmap)
risk = 0

def getValue(x,y,direction):
    ymax = len(depthmap)-1
    xmax = len(depthmap[0])-1
    if y == ymax and direction=='RIGHT':
        return 99
    if y == 0 and direction=='LEFT':
        return 99
    if x == xmax and direction=='DOWN':
        return 99
    if x == 0 and direction=='UP':
        return 99
    if direction=='UP':
        return depthmap[y][x-1]
    elif direction=='DOWN':
        return depthmap[y][x+1]
    elif direction=='LEFT':
        return depthmap[y-1][x]
    elif direction=='RIGHT':
        return depthmap[y+1][x]


for idx, x in numpy.ndenumerate(depthmap):
    isrisk = False
    left = getValue(idx[1],idx[0],"LEFT")
    right = getValue(idx[1],idx[0],"RIGHT")
    up = getValue(idx[1],idx[0],"UP")
    down = getValue(idx[1],idx[0],"DOWN")
    if x < right and x < left and x < up and x < down:
        risk = risk + x + 1
        isrisk = True
    print("Current: {}\tUp: {}\tDown: {}\tRight: {}\tLeft:{}\tRisk: {}\tIs Risk:{}".format(x,up,down,right,left,risk,isrisk))
print(risk)
    