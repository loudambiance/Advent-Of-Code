from decimal import ROUND_HALF_DOWN, Decimal, ROUND_HALF_UP
from math import floor

with open('task3a.txt') as f:
    lines = []
    for ele in f:
        lines.append([int(x) for x in ele.strip('\n\r ')])

def calcVal(lines, flip):
    linez = lines
    loop = 0
    while len(linez) > 1:
        tmp0 = zip(*linez)
        for x in range(-1,loop):
            tmp = next(tmp0)
        tmp2 = Decimal(sum(tmp)/len(tmp)).quantize(8, ROUND_HALF_UP)
        if(flip):
            tmp2 = 1 - tmp2
        linez = [x for x in linez if x[loop] == tmp2]
        loop += 1
    return int(''.join(map(str,linez.pop())),2)


oxygen = calcVal(lines, False)
co2 = calcVal(lines, True)
lifesupport = oxygen*co2
print(oxygen)
print(co2)
print(lifesupport)
