from time import perf_counter_ns
import numpy


def main(lines: list[str]):
    grid = list()
    visible = dict()
    for line in lines:
        grid.append(list(map(int, [*line])))
    xlen = len(grid[0])
    ylen = len(grid)
    grid = numpy.array(grid)
    for idx, x in numpy.ndenumerate(grid):
        if idx[0] in (0, xlen-1) or idx[1] in (0, ylen-1):
            visible[idx] = True
        else:
            rowpart1 = grid[idx[0], :][:idx[1]].tolist()
            rowpart2 = grid[idx[0], :][idx[1]+1:].tolist()
            columnpart1 = grid[:, idx[1]][:idx[0]].tolist()
            columnpart2 = grid[:, idx[1]][idx[0]+1:].tolist()
            if all(item < x for item in rowpart1) or all(item < x for item in rowpart2) or all(item < x for item in columnpart1) or all(item < x for item in columnpart2):
                visible[idx] = True
    print(len(visible))
    return(0)


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files[:]:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)
