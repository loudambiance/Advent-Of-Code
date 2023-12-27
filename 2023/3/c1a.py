from time import perf_counter_ns


def main(lines: list[str]):
    input = [list(line.strip()) for line in lines]
    validation = 0
    for y, line in enumerate(input):
        skip = 0
        for x, character in enumerate(line):
            if skip > 0:
                skip -= 1
                continue
            last_digit = get_num(x, line)
            if last_digit > -1:
                skip = len(''.join(line[x:last_digit+1]))-1
                if valid(x, y, skip+1, input):
                    validation += int(''.join(line[x:last_digit+1]))
    return (validation)


def valid(x, y, length, input):
    for y1 in range(y-1, y+1+1):
        if y1 > -1 and y1 < len(input):
            for x1 in range(x-1, x+length+1):
                if x1 > -1 and x1 < len(input[y1])-1:
                    if input[y1][x1] != '.' and not input[y1][x1].isnumeric():
                        return True
    return False


def get_num(start: int, row: list):
    end = -1
    if row[start].isnumeric():
        for index, character in enumerate(row[start:]):
            if character.isnumeric():
                end = index+start
            elif end > -1:
                break
    return end


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        output = str(main(lines))
        t1_stop = perf_counter_ns()
        print(file + ": "+output + "\tElapsed time:",
              (t1_stop - t1_start)/1000000000)
