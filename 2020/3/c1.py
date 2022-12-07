from time import perf_counter_ns


def main(lines: list[str]):
    x, index, trees = 3, 0, 0
    for line in lines[1:]:
        index = index + x if index + x < len(line) else index + x - len(line)
        trees += 1 if [*line][index] == '#' else 0
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
