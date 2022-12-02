with open('readme.txt') as f:
    lines = f.read().splitlines()

count = 0
a = lines.pop(0)
b = lines.pop(0)
c = lines.pop(0)
for line in lines:
    sum1 = int(a) + int(b) + int(c)
    sum2 = int(b) + int(c) + int(line)
    if sum2 > sum1:
        count = count + 1
    a = b
    b = c
    c = line

print(count)