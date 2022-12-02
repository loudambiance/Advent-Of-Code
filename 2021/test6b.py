import numpy

fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
with open('task6.txt') as f:
    tempfishes = [int(x) for x in next(f).split(',')]
    for fishy in tempfishes:
        if fishy == 0:
            fishes[0] += 1
        elif fishy == 1:
            fishes[1] += 1
        elif fishy == 2:
            fishes[2] += 1
        elif fishy == 3:
            fishes[3] += 1
        elif fishy == 4:
            fishes[4] += 1
        elif fishy == 5:
            fishes[5] += 1
        elif fishy == 6:
            fishes[6] += 1
print(fishes)
for days in range(256):
    #print(fishes)
    newfish = fishes[0]
    fishes[0] = fishes[1]
    fishes[1] = fishes[2]
    fishes[2] = fishes[3]
    fishes[3] = fishes[4]
    fishes[4] = fishes[5]
    fishes[5] = fishes[6] 
    fishes[6] = fishes[7] + newfish
    fishes[7] = fishes[8]
    fishes[8] = newfish
    #print("Number of fish on day {}: {} - {}".format(days+1, sum(fishes),','.join([str(x) for x in fishes])))
print("Number of fish: {}".format(sum(fishes)))
    