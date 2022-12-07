from time import perf_counter_ns
from textwrap import wrap


def main(lines: list[str]):
    parseddata = dict()
    moves = list()
    parsestacks = True
    for line in lines:
        if line == '':
            parsestacks = False
        elif parsestacks:
            chunks = wrap(line, 4, drop_whitespace=False)
            for index, chunk in enumerate(chunks):
                if index+1 not in parseddata.keys():
                    parseddata[index+1] = list()
                parsedchunk = chunk.replace(' ', '').replace('[', '').replace(']', '')
                if parsedchunk != '' and not parsedchunk.isnumeric():
                    parseddata[index+1].insert(0, parsedchunk)
        else:
            preparsed = line.replace('from ', '').replace('move ', '').replace('to ', '').split(' ')
            moves.append(preparsed)
    for move in moves:
        amount = int(move[0])
        fromstack = int(move[1])
        tostack = int(move[2])
        for x in range(0, amount):
            parseddata[tostack].append(parseddata[fromstack].pop())
    returnval = ''
    for key in parseddata:
        if len(parseddata[key]) > 0:
            returnval = returnval + parseddata[key].pop()
    return(returnval)


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)
