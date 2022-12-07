from time import perf_counter_ns


def main(lines: list[str]):
    returnval = trees(1, 1, lines)
    returnval *= trees(3, 1, lines)
    returnval *= trees(5, 1, lines)
    returnval *= trees(7, 1, lines)
    returnval *= trees(1, 2, lines)
    return(returnval)


def trees(x: int, y: int, lines: list[str]):
    xpos, index, trees = 0, 0, 0
    for index, line in enumerate(lines[1:]):
        if (index+1) % y == 0:
            xpos = xpos + x if xpos + x < len(line) else xpos + x - len(line)
            trees += 1 if [*line][xpos] == '#' else 0
    return(trees)


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)
