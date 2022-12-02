test = False
file = 'data/task7test.txt' if test else 'data/task7.txt'

with open(file) as f:
    crabmarines = [int(x) for x in next(f).split(',')]

bestPosition = 9999999999
for position in range(min(crabmarines),max(crabmarines)+1):
    curPosition = sum(list(map(lambda x: abs(position-x)*((abs(position-x)+1)/2), crabmarines)))
    if curPosition < bestPosition:
        bestPosition = curPosition
print(bestPosition)

