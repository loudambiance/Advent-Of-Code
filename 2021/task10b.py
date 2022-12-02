test = False
file = 'data/task10test.txt' if test else 'data/task10.txt'

with open(file) as f:
    lines = f.read().splitlines()

opencharacters = ['[', '{','\'','<']

def bufferReverse(buffer):
    score = 0
    buffer.reverse()
    for character in buffer:
        if character == '\'':
            score *= 5
            score += 1
        if character == '[':
            score *= 5
            score += 2
        if character == '{':
            score *= 5
            score += 3
        if character == '<':
            score *= 5
            score += 4
    return score

scores = []
for line in lines:
    buffer = []
    for character in line:
        tmp = character.replace('(','\'')
        if tmp == "}":
            i=1
        if tmp in opencharacters:
            buffer.append(tmp)
        else:
            if len(buffer) > 0:
                if ord(buffer[-1])+2 == ord(tmp):
                    buffer.pop()
                    continue
                buffer = []  
                break
    if len(buffer) != 0:
        scores.append(bufferReverse(buffer))
scores.sort()
print(scores[int(len(scores) / 2)])