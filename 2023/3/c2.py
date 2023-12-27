from time import perf_counter_ns
import numpy
import re


def main(lines: list[str]):
    input = numpy.array([[x for x in list(y)] for y in lines])
    validation = 0
    for idx, x in numpy.ndenumerate(input):
        if x == '*':
            retstr = ""
            for row in input[idx[0]-1:idx[0]+2, idx[1]-3:idx[1]+4]:
                if not row[4].isnumeric():
                    row = row[:4]
                elif not row[5].isnumeric():
                    row = row[:5]
                if not row[2].isnumeric():
                    row = row[3:]
                elif not row[1].isnumeric():
                    row = row[2:]
                rowstr = re.sub("\D+", "#", "".join(row))
                retstr += "#"+rowstr+"#"
            nums = re.sub(
                "#+", "#", retstr).removeprefix("#").removesuffix("#").split("#")
            if len(nums) == 2:
                validation += int(nums[0])*int(nums[1])
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
