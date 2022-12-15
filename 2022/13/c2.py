from time import perf_counter_ns


def main(lines: list[str]):
    index = 0
    retval = 0
    for x in range(0,len(lines),3):
        index += 1
        templist = eval(lines[x])
        templist2 = eval(lines[x+1])
        if compare(templist,templist2) == 0:
            retval += index
    return(retval)


def compare(left, right):
    retval = 2
    if isinstance(left,int) and isinstance(right, int):
        if left < right:
            retval = 0
        elif left == right:
            retval = 1
        else:
            retval = 2
    elif isinstance(left, list) and isinstance(right, list):
        if len(left) == 0 and len(right) > 0:
            retval = 0
        elif len(right) == 0 and len(left) > 0:
            retval = 2
        elif len(right) == 0 and len(left) == 0:
            retval = 1
        else:
            temp = compare(left.pop(0), right.pop(0))
            if temp == 1:
                retval = compare(left, right)
            else:
                retval = temp
    elif isinstance(left, int) and isinstance(right, list):
        retval = compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        retval = compare(left, [right])
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
