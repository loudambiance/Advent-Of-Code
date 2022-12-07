from time import perf_counter_ns


def main(lines: list[str]):
    count = 0
    for line in lines:
        elfassign1 = line.split(',')[0].split('-')
        elfrange1 = range(int(elfassign1[0]), int(elfassign1[1])+1)
        elfassign2 = line.split(',')[1].split('-')
        elfrange2 = range(int(elfassign2[0]), int(elfassign2[1])+1)
        if any(zone in elfrange1 for zone in elfrange2) or any(zone in elfrange2 for zone in elfrange1):
            count += 1
    return(count)


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)
