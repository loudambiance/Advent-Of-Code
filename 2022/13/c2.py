from time import perf_counter_ns
from copy import deepcopy


def main(lines: list[str]):
    retval = 0
    sorted = list()
    for line in lines:
        if len(line) == 0:
            continue
        if len(sorted) == 0:
            sorted.append(eval(line))
            continue
        sorted = sort(sorted, eval(line))
    sorted = sort(sorted, eval("[[2]]"))
    sorted = sort(sorted, eval("[[6]]"))
    sorted.reverse()
    retval = (sorted.index([[2]])+1)*(sorted.index([[6]])+1)
    return (retval)


def sort(sorted: list, newitem: list):
    for index, sortedline in enumerate(sorted):
        temp = compare(sortedline, newitem)
        if temp == -1:
            sorted.insert(index, newitem)
            break
        elif temp == 0:
            sorted.insert(index+1, newitem)
            break
    else:
        sorted.append(newitem)

    return sorted


def compare(left, right):
    localleft = deepcopy(left)
    localright = deepcopy(right)
    retval = 1
    if isinstance(localleft, int) and isinstance(localright, int):
        if localleft < localright:
            retval = -1
        elif localleft == localright:
            retval = 0
        else:
            retval = 1
    elif isinstance(localleft, list) and isinstance(localright, list):
        if len(localleft) == 0 and len(localright) > 0:
            retval = -1
        elif len(localright) == 0 and len(localleft) > 0:
            retval = 1
        elif len(localright) == 0 and len(localleft) == 0:
            retval = 0
        else:
            temp = compare(localleft.pop(0), localright.pop(0))
            if temp == 0:
                retval = compare(localleft, localright)
            else:
                retval = temp
    elif isinstance(localleft, int) and isinstance(localright, list):
        retval = compare([localleft], localright)
    elif isinstance(left, list) and isinstance(localright, int):
        retval = compare(localleft, [localright])
    return retval


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files[:]:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)
