test = False
file = "input_ex.txt" if test else "input.txt"

with open(file) as f:
    lines = f.read().splitlines()
runningsum = 0
maxvalue = 0
maxvalue2 = 0
maxvalue3 = 0
for line in lines:
    if line == "":
        print("Running Sum: " + str(runningsum))
        if runningsum > maxvalue:
            maxvalue3 = maxvalue2
            maxvalue2 = maxvalue
            maxvalue = runningsum
        elif runningsum > maxvalue2:
            maxvalue3 = maxvalue2
            maxvalue2 = runningsum
        elif runningsum > maxvalue3:
            maxvalue3 = runningsum
        runningsum = 0
    else:
        runningsum += int(line)
else:
    if runningsum > maxvalue:
        maxvalue3 = maxvalue2
        maxvalue2 = maxvalue
        maxvalue = runningsum
    elif runningsum > maxvalue2:
        maxvalue3 = maxvalue2
        maxvalue2 = runningsum
    elif runningsum > maxvalue3:
        maxvalue3 = runningsum

print(maxvalue)
print(maxvalue2)
print(maxvalue3)
print(maxvalue+maxvalue2+maxvalue3)
