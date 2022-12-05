from time import perf_counter_ns

def main(lines: str):
    runningsum = 0
    for line1,line2,line3 in zip(*[iter(lines)]*3):
        sac = [*line1]
        sac2 = [*line2]
        sac3 = [*line3]
        for duplicate in set.intersection(set(sac),set(sac2),set(sac3)):
            value = ord(duplicate)
            if value in range(65,91):
                value -= 38
            elif value in range(97,123):
                value -= 96 
            runningsum += value
    return(runningsum)


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", t1_stop - t1_start)
