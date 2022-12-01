import itertools
import math

files = ("input_ex.txt", "input.txt")

for file in files:
    with open(file) as f:
        lines = f.read().splitlines()

    vals = [eval(i) for i in lines]

    for subset in itertools.combinations(vals, 3):
        combsum = sum(subset)
        if combsum == 2020:
            print(subset)
            print(math.prod(subset))
