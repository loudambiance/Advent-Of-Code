from time import perf_counter_ns


def main(lines: list[str]):
    for line in lines:
        for x in range(0, len([*line])-1):
            if len(set([*line][x:x+4])) == 4:
                print(x+4)
                break
    return(0)


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", t1_stop - t1_start)
