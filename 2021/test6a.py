fishes = []
with open('task6.txt') as f:
    fishes = [int(x) for x in next(f).split(',')]

print ("Initial State: {}".format(','.join([str(x) for x in fishes])))
for days in range(80):
    newfish = []
    for index,fish in enumerate(fishes):
        if fish > 0:
            fishes[index] = fish -1
        else:
            fishes[index] = 6
            newfish.append(8)
    fishes.extend(newfish)
print("Number of fish: {}".format(len(fishes)))
    