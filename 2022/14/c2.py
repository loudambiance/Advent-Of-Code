from time import perf_counter_ns
from time import sleep
import numpy
import os

xMax = 800
xMin = 0
yMax = 184
yMin = 0
numpy.set_printoptions(threshold=numpy.inf, linewidth=(xMax-xMin)*3+30)


def main(lines: list[str]):
    arr = setupArray(lines)
    #print(arr[yMin:yMax, xMin:xMax])
    count = 0
    while dropSand(arr, [500,0]) == 0:
        count += 1
    return (count)


def dropSand(arr: numpy.array, currentpos: list[int]):
    retval = 0
    if arr[currentpos[1]][currentpos[0]] == 1:
        return 1
    try:
        arr[currentpos[1]][currentpos[0]] = 1
        #os.system('clear')
        #print(arr[yMin:yMax, xMin:xMax])
        #sleep(0.010)
        if arr[currentpos[1]+1][currentpos[0]] == 0:
            arr[currentpos[1]][currentpos[0]] = 0
            currentpos[1] += 1
            retval = dropSand(arr, currentpos)
        elif arr[currentpos[1]+1][currentpos[0]-1] == 0:
            arr[currentpos[1]][currentpos[0]] = 0
            currentpos[1] += 1
            currentpos[0] -= 1
            retval = dropSand(arr, currentpos)
        elif arr[currentpos[1]+1][currentpos[0]+1] == 0:
            arr[currentpos[1]][currentpos[0]] = 0
            currentpos[1] += 1
            currentpos[0] += 1
            retval = dropSand(arr, currentpos)
    except:
        retval = 2
    if retval == 2:
        retval = 1
        arr[currentpos[1]][currentpos[0]] = 0
    return retval


def setupArray(lines: list):
    arr = numpy.zeros((yMax, xMax), dtype=int)
    arr[yMax-1,:] = 7
    currentcoord = list()
    nextcoord = list()
    for line in lines:
        points = line.split(' -> ')
        coords = list(map(lambda c: list(map(int, c.split(','))), points))
        first = True
        while len(coords) > 0:
            if first:
                currentcoord = coords.pop(0)
                nextcoord = coords.pop(0)
                first = False
            else:
                currentcoord = [*nextcoord]
                nextcoord = coords.pop(0)
            if currentcoord[0] == nextcoord[0] and currentcoord[1] < nextcoord[1]:
                arr[currentcoord[1]:nextcoord[1]+1, currentcoord[0]] = 7
            elif currentcoord[0] == nextcoord[0] and currentcoord[1] > nextcoord[1]:
                arr[nextcoord[1]:currentcoord[1]+1, currentcoord[0]] = 7
            elif currentcoord[0] < nextcoord[0]:
                arr[currentcoord[1], currentcoord[0]:nextcoord[0]+1] = 7
            else:
                arr[currentcoord[1], nextcoord[0]:currentcoord[0]+1] = 7
    #print(arr[yMin:yMax, xMin:xMax])
    return arr


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files[:]:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)
