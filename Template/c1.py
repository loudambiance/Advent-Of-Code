from time import perf_counter_ns

def main(lines: str):
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
