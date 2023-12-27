from time import perf_counter_ns


def main(lines: list[str]):
    sum: int = 0
    for line in lines:
        num = ''.join(filter(str.isdigit, strtoint(line)))
        print("scrub: {}".format(num))
        length = len(num)
        finalnum = "{}{}".format(num[0], num[length-1])
        sum += int(finalnum)
        print("{} {}".format(finalnum, sum))
    return (0)


def strtoint(string: str):
    numdict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }
    for key in numdict.keys():
        coord = 0
        while coord > -1:
            coord = string.find(key, coord)
            if coord > -1:
                string = string[:coord+1] + numdict[key] + string[coord+1:]
    return string


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)
