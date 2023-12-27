from time import perf_counter_ns
import re


def main(lines: list[str]):
    validation = len(lines)
    extralines = list()
    valindex = dict()
    for index, line in enumerate(lines):
        score = grade(line)
        maxindex = index+score if index+score < len(lines) else len(lines)-1
        valindex[index] = score
        for newindex in range(index+1, maxindex+1):
            extralines.append(newindex)
        validation += score
    while len(extralines) > 0:
        index = extralines.pop()
        score = valindex[index]
        maxindex = index+score if index+score < len(lines) else len(lines)-1
        for newindex in range(index+1, maxindex+1):
            extralines.append(newindex)
        validation += score
    return (validation)


def grade(line):
    data = line.split(":")[1].strip().split("|")
    winningnums = re.split("\s+", data[0].strip())
    playernums = re.split("\s+", data[1].strip())
    score = 0
    for num in playernums:
        if num in winningnums:
            score += 1
    return score


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
