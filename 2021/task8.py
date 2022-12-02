import copy

test = False
file = 'data/task8test.txt' if test else 'data/task8.txt'

data = []
with open(file) as f:
    lines = f.read().splitlines()
    for line in lines:
        tmp1 = []
        tmp2 = []
        for word in line.split(' | ')[1].split(' '):
            tmp1.append("".join(sorted(word)))
        for word in line.split(' | ')[0].split(' '):
            tmp2.append("".join(sorted(word)))
        data.append([tmp1,tmp2])

def findOne(data, numbers):
    findUnique(data, numbers, 2, 1)
    return

def findTwo(data, numbers):
    almost = "".join(set(numbers[4]+numbers[3]))
    for signal in data:
        if len(signal) != 5:
            continue
        numbers[2] = signal
        data.remove(signal)
        break
    return

def findThree(data, numbers):
    for signal in data:
        if len(signal) != 5:
            continue
        diff = set(signal).symmetric_difference(set(numbers[1]))
        if len(diff) == 3:
            numbers[3] = signal
            data.remove(signal)
            break
    return

def findFour(data, numbers):
    findUnique(data, numbers, 4, 4)
    return

def findFive(data, numbers):
    almost = "".join(set(numbers[4]+numbers[3]))
    for signal in data:
        if len(signal) != 5:
            continue
        diff = set(signal).symmetric_difference(almost)
        
        if len(diff) == 1:
             numbers[5] = signal
             data.remove(signal)
             break

def findSix(data, numbers):
    almost = "".join(set(numbers[4]+numbers[7]))
    for signal in data:
        if len(signal) != 6:
            continue
        brc = set(almost).symmetric_difference(set(numbers[8]))
        diff = set(signal).symmetric_difference(set(almost))
        diff2 = diff.symmetric_difference(brc)
        if diff2.pop() in numbers[1]:
             numbers[6] = signal
             data.remove(signal)
             break
    return

def findSeven(data, numbers):
    findUnique(data, numbers, 3, 7)
    return

def findEight(data, numbers):
    findUnique(data, numbers, 7, 8)
    return

def findNine(data, numbers):
    almostnine = "".join(set(numbers[4]+numbers[7]))
    for signal in data:
        if len(signal) != 6:
            continue
        diff = set(signal).symmetric_difference(set(almostnine))
        if len(diff) == 1:
            numbers[9] = signal
            data.remove(signal)
            break
    return

def findZero(data, numbers):
    for signal in data:
        if len(signal) != 6:
            continue
        numbers[0] = signal
        data.remove(signal)
        break
    return

def findUnique(data, numbers, length, index):
    for signal in data:
        if len(signal) == length:
            numbers[index] = signal;
            data.remove(signal)
            break
    return

def solve(data):
    datadisposable=copy.deepcopy(data)
    displayNumbers = ['','','','','','','','','','']
    findOne(datadisposable[1], displayNumbers)
    findFour(datadisposable[1],displayNumbers)
    findSeven(datadisposable[1],displayNumbers)
    findEight(datadisposable[1],displayNumbers)
    findNine(datadisposable[1],displayNumbers)
    findSix(datadisposable[1],displayNumbers)
    findZero(datadisposable[1],displayNumbers)
    findThree(datadisposable[1],displayNumbers)
    findFive(datadisposable[1],displayNumbers)
    findTwo(datadisposable[1],displayNumbers)
    outputval = ''
    for output in data[0]:
        outputval = '{}{}'.format(outputval,displayNumbers.index(output))
    return int(outputval)

total = 0
for dataset in data:
    total += solve(dataset)

print(total)