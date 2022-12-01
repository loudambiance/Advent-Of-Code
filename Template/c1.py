test = False
file = "input_ex.txt" if test else "input.txt"

with open(file) as f:
    lines = f.read().splitlines()
