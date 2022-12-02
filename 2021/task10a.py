test = False
file = 'data/task10test.txt' if test else 'data/task10.txt'

with open(file) as f:
    lines = f.read().splitlines()

opencharacters = ['[', '{','\'','<']

score = 0
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
                if character == ')':
                    score = score + 3
                if character == ']':
                    score = score + 57
                if character == '}':
                    score = score + 1197
                if character == '>':
                    score = score + 25137  
                break
print(score)