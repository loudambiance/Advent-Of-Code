from time import perf_counter_ns
import re


def main(lines: list[str]):
    validation = 0
    for line in lines:
        data = line.split(":")[1].strip().split("|")
        winningnums = re.split("\s+", data[0].strip())
        playernums = re.split("\s+", data[1].strip())
        score = 0
        for num in playernums:
            if num in winningnums:
                if score == 0:
                    score = 1
                else:
                    score = score << 1
        validation += score
    return (validation)


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
