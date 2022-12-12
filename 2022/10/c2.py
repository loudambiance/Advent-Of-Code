from time import perf_counter_ns


def main(lines: list[str]):
    regx = 1
    cyclestart = 1
    tempreg = 1
    retval = 0
    pixelposition = 0
    for cycle in range(1, 40*6):
        if cyclestart == 1:
            if (len(lines) != 0):
                command = lines.pop(0).split(" ")
                if command[0] == 'noop':
                    cyclestart = 2
                if command[0] == 'addx':
                    tempreg = regx + int(command[1])
        if pixelposition in range(regx-1, regx+2):
            print("#", end="")
        else:
            print(".", end="")
        if pixelposition == 39:
            print()
            pixelposition = 0
        else:
            pixelposition += 1
        if cyclestart == 2:
            cyclestart = 0
            regx = tempreg
        cyclestart += 1
    print()
    return (retval)


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)
