files = ("input_ex.txt", "input.txt")

for file in files:

    with open(file) as f:
        lines = f.read().splitlines()
    runningsum = 0
    maxvalue = 0
    for line in lines:
        if line == "":
            if runningsum > maxvalue:
                maxvalue = runningsum
            runningsum = 0
        else:
            runningsum += int(line)
    else:
        if runningsum > maxvalue:
            maxvalue = runningsum
            runningsum = 0

    print(maxvalue)
