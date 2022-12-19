from time import perf_counter_ns
import math


def main(lines: list[str]):
    knots: dict[list[int]] = {0: [0, 0], 1: [0, 0], 2: [0, 0], 3: [
        0, 0], 4: [0, 0], 5: [0, 0], 6: [0, 0], 7: [0, 0], 8: [0, 0], 9: [0, 0]}
    tailhistory = dict()
    tailhistory[tuple(knots[8])] = 1
    for line in lines:
        direction, distance = [int(i) if i.isdigit() else i for i in line.split(' ')]
        moveHead(knots, direction, distance, tailhistory)
    # print(tailhistory)
    return (len(tailhistory.values()))


def moveHead(knots: dict[list[int]], direction: str, distance: int, tailhistory: dict):
    step = 1 if direction in ('R', 'D') else -1
    axis = 0 if direction in ('R', 'L') else 1
    for x in range(0, distance):
        knots[0][axis] = knots[0][axis] + step
        #print(0, knots[0])
        if math.dist(knots[0], knots[1]) > 1.5:
            updateKnotPosition(knots, 1, direction, step, tailhistory)
    return


def updateKnotPosition(knots: dict[list[int]], knot: int, direction: str, step: int, tailhistory: dict):
    prevloc = [*knots[knot]]
    if (math.dist(knots[knot], knots[knot-1]) == 2):
        if direction in ('R', 'L'):
            knots[knot][0] = knots[knot-1][0]-step
            knots[knot][1] = knots[knot-1][1]
        elif direction in ('U', 'D'):
            knots[knot][0] = knots[knot-1][0]
            knots[knot][1] = knots[knot-1][1]-step
    if (math.dist(knots[knot], knots[knot-1]) > 2):
        if direction in ('R', 'L'):
            knots[knot][0] = knots[knot-1][0]-step
            knots[knot][1] = knots[knot][1]-math.ceil(abs(knots[knot-1][1]-knots[knot][1])/2)*step
        elif direction in ('U', 'D'):
            knots[knot][0] = knots[knot][0]-math.ceil(abs(knots[knot-1][0]-knots[knot][0])/2)*step
            knots[knot][1] = knots[knot-1][1]-step
    if knot == 9 and tuple(knots[knot]) not in tailhistory.keys():
        tailhistory[tuple(knots[knot])] = 1
    elif knot == 9:
        tailhistory[tuple(knots[knot])] += 1
    else:
        #print(direction, step, knot, knots[knot-1], prevloc, knots[knot])
        if knot < len(knots.keys())-1 and math.dist(knots[knot], knots[knot+1]) > 1.5:
            updateKnotPosition(knots, knot+1, direction, step, tailhistory)
    return


if __name__ == "__main__":
    files = ("input_ex.txt", "input_ex2.txt", "input.txt")
    for file in files[:-1]:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)
