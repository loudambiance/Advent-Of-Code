from time import perf_counter_ns


def main(lines: str):
    currentpath = list('/')
    directorystruct = dict()
    directorystruct['/'] = 0
    for line in lines[1:]:
        parts = line.split(' ')
        if parts[0] == '$':
            if parts[1] == 'cd':
                if parts[2] == '..':
                    currentpath.pop()
                else:
                    currentpath.append(parts[2]+'/')
                    directorystruct[''.join(currentpath)] = 0

        elif parts[0] != 'dir':
            temppath = currentpath[:]
            while len(temppath) > 0:
                directorystruct[''.join(temppath)] = directorystruct[''.join(temppath)] + int(parts[0])
                temppath.pop()
    retval = 0
    for value in directorystruct.values():
        if value <= 100000:
            retval += value
    return(retval)


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", t1_stop - t1_start)
