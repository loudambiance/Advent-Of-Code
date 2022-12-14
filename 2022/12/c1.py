from time import perf_counter_ns
import networkx


def main(lines: list[str]):
    elfmap = list()
    elfgraph = networkx.DiGraph()
    start = ""
    end = ""

    for line in lines:
        elfmap.append(list(map(mapValues, [*line])))

    for y, row in enumerate(elfmap):
        for x, cell in enumerate(row):
            nodename = "{val}-{xcoord}-{ycoord}".format(val=cell, xcoord=x, ycoord=y)
            if cell == 0:
                start = nodename
            elif cell == 27:
                end = nodename
            for neighbor in getNeighbors(elfmap, xcurrent=x, ycurrent=y, yrange=len(elfmap), xrange=len(row)):
                elfgraph.add_edge(nodename, neighbor)
    return (networkx.shortest_path_length(elfgraph, source=start, target=end))


def getNeighbors(elfmap: list[list[int]], xcurrent: int, ycurrent: int, xrange: int, yrange: int):
    retvals = list()
    currentval = elfmap[ycurrent][xcurrent]
    if xcurrent > 0:
        leftval = elfmap[ycurrent][xcurrent-1]
        left = "{val}-{xcoord}-{ycoord}".format(val=leftval, xcoord=xcurrent-1, ycoord=ycurrent)
        if leftval == currentval or leftval == currentval + 1 or leftval < currentval:
            retvals.append(left)
    if ycurrent > 0:
        downval = elfmap[ycurrent-1][xcurrent]
        down = "{val}-{xcoord}-{ycoord}".format(val=downval, xcoord=xcurrent, ycoord=ycurrent-1)
        if downval == currentval or downval == currentval + 1 or downval < currentval:
            retvals.append(down)
    if xcurrent < xrange-1:
        rightval = elfmap[ycurrent][xcurrent+1]
        right = "{val}-{xcoord}-{ycoord}".format(val=rightval, xcoord=xcurrent+1, ycoord=ycurrent)
        if rightval == currentval or rightval == currentval + 1 or rightval < currentval:
            retvals.append(right)
    if ycurrent < yrange-1:
        upval = elfmap[ycurrent+1][xcurrent]
        up = "{val}-{xcoord}-{ycoord}".format(val=upval, xcoord=xcurrent, ycoord=ycurrent+1)
        if upval == currentval or upval == currentval + 1 or upval < currentval:
            retvals.append(up)
    return retvals


def mapValues(char: str):
    if char == "E":
        val = 27
    elif char == "S":
        val = 0
    else:
        val = ord(char)-96
    return val


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files[:]:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)
