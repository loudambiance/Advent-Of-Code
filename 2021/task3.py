with open('task3atest.txt') as f:
    lines = f.read().splitlines()

x = 0
y = 0
for line in lines:
    tmp = line.split(" ")
    if tmp[0] == 'forward':
        x = x + int(tmp[1])
    elif tmp[0] == 'up':
        y = y - int(tmp[1])
    elif tmp[0] == 'down':
        y = y + int(tmp[1])
print (x*y)
