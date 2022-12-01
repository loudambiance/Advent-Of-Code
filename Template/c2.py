files = ("input_ex.txt", "input.txt")

for file in files:

    with open(file) as f:
        lines = f.read().splitlines()
