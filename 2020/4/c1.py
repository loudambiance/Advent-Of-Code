from time import perf_counter_ns


def main(lines: list[str]):
    res = dict()
    count = 0
    for line in lines:
        if len(line) == 0:
            count = count+1 if validate(res) else count
            res = dict()
            continue
        res = res | dict(item.split(":") for item in line.split(" "))
    else:
        count = count+1 if validate(res) else count
    print(count)


def validate(res: dict):
    return all(x in res.keys() for x in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)
