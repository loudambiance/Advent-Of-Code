from time import perf_counter_ns
import numpy
numpy.set_printoptions(threshold=numpy.inf)
xMax = 505
xMin = 494
yMax = 10
yMin = 0


def main(lines: list[str]):
    arr = setupArray(lines)
    print(arr[yMin:yMax, xMin:xMax])
    return (0)


def dropSand(arr: numpy.array):
    return 0


def setupArray(lines: list):
    arr = numpy.zeros((yMax, xMax), dtype=int)
    print(arr[yMin:yMax, xMin:xMax])
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
                arr[currentcoord[1]:nextcoord[1]+1, currentcoord[0]] = -1
            elif currentcoord[0] == nextcoord[0] and currentcoord[1] > nextcoord[1]:
                arr[nextcoord[1]:currentcoord[1]+1, currentcoord[0]] = -1
            elif currentcoord[0] < nextcoord[0]:
                arr[currentcoord[1], currentcoord[0]:nextcoord[0]+1] = -1
            else:
                arr[currentcoord[1], nextcoord[0]:currentcoord[0]+1] = -1
    return arr


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files[:-1]:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)
