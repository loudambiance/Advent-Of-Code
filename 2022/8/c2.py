from time import perf_counter_ns
import numpy


def main(lines: list[str]):
    grid = list()
    visible = dict()
    for line in lines:
        grid.append(list(map(int, [*line])))
    grid = numpy.array(grid)
    for idx, x in numpy.ndenumerate(grid):
        left = getViewDistanceReverse(grid[idx[0], :][:idx[1]].tolist(), x)
        right = getViewDistance(grid[idx[0], :][idx[1]+1:].tolist(), x)
        top = getViewDistanceReverse(grid[:, idx[1]][:idx[0]].tolist(), x)
        bottom = getViewDistance(grid[:, idx[1]][idx[0]+1:].tolist(), x)
        visible[idx] = left * right * top * bottom
    print(max(visible.values()))
    return(0)


def getViewDistanceReverse(listpart: list[int], currenttree: int):
    listpart.reverse()
    return getViewDistance(listpart, currenttree)


def getViewDistance(listpart: list[int], currenttree: int):
    retval = 0
    for index, value in enumerate(listpart):
        if value >= currenttree:
            retval = index+1
            break
    else:
        retval = len(listpart)
    return retval


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files[:]:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)
