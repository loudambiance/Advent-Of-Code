from time import perf_counter_ns
import math


def main(lines: list[str]):
    head = [0, 0]
    tail = [0, 0]
    tailhistory = dict()
    tailhistory[tuple(tail)] = 1
    for line in lines:
        direction, distance = [int(i) if i.isdigit() else i for i in line.split(' ')]
        move(head, tail, direction, distance, tailhistory)
    return (len(tailhistory.values()))


def move(head: list[int], tail: list[int], direction: str, distance: int, tailhistory: dict):
    step = 1 if direction in ('R', 'D') else -1
    index = 0 if direction in ('R', 'L') else 1
    for x in range(0, distance):
        head[index] = head[index] + step
        if math.dist(head, tail) > 1.5:
            updateTailPosition(head, tail, direction, step, tailhistory)
    return


def updateTailPosition(head: list[int], tail: list[int], direction: str, step: int, tailhistory: dict):
    if direction in ('R', 'L'):
        tail[0] = head[0]-step
        tail[1] = head[1]
    elif direction in ('U', 'D'):
        tail[0] = head[0]
        tail[1] = head[1]-step
    if tuple(tail) not in tailhistory.keys():
        tailhistory[tuple(tail)] = 1
    else:
        tailhistory[tuple(tail)] += 1
    return


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files[:]:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)
