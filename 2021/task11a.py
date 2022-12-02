import numpy

test = False
file = 'data/task11test.txt' if test else 'data/task11.txt'

with open(file) as f:
    octipi = numpy.array([[int(x) for x in list(y)] for y in f.read().splitlines()])

def incrementNeighbors(y,x):
    ymax = len(octipi)-1
    xmax = len(octipi[0])-1

    for yd in range(-1,1+1):
        for xd in range(-1,1+1):
            if yd == 0 and xd == 0:
                continue
            if y+yd >= 0 and x+xd >= 0 and y+yd <= ymax and x+xd <= xmax:
                octipi[y+yd][x+xd] += 1
                if octipi[y+yd][x+xd] == 10:
                    incrementNeighbors(y+yd,x+xd)
    return

def flash(octipi):
    tmp = numpy.where(octipi > 9)
    coordslist = list(zip(tmp[0],tmp[1]))
    for coords in coordslist:
        incrementNeighbors(coords[0],coords[1])
    return (octipi > 9).sum()

score = 1
loop = 0
while score >0:
    loop += 1
    octipi=octipi+1
    flash(octipi)
    octipi[octipi > 9] = 0
    score = octipi.sum()
print("Loop: {}\tScore: {}".format(loop,score))

    
