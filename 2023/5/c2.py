from time import perf_counter_ns


def main(lines: list[str]):
    validation = 9999999999
    datatype = 0
    seeds = list()  # id 0
    seedtosoil = dict()  # id 1
    soiltofert = dict()  # id 2
    ferttowater = dict()  # id 3
    watertolight = dict()  # id 4
    lighttotemp = dict()  # id 5
    temptohumid = dict()  # id 6
    humidtoloc = dict()  # id 7

    for line in lines:
        if line == "":
            datatype += 1
            continue

        if datatype == 0:
            tempseeds = line.removeprefix("seeds: ").split(" ")
            while len(tempseeds) > 0:
                start = int(tempseeds.pop(0))
                step = int(tempseeds.pop(0))
                seeds.append(range(start, start+step-1))
            continue

        if datatype == 1:
            if line.find(":") != -1:
                continue
            val1, val2, val3 = line.split(" ")
            seedtosoil[range(int(val2), int(val2)+int(val3)+1)
                       ] = range(int(val1), int(val1)+int(val3)+1)
            continue

        if datatype == 2:
            if line.find(":") != -1:
                continue
            val1, val2, val3 = line.split(" ")
            soiltofert[range(int(val2), int(val2)+int(val3)+1)
                       ] = range(int(val1), int(val1)+int(val3)+1)
            continue

        if datatype == 3:
            if line.find(":") != -1:
                continue
            val1, val2, val3 = line.split(" ")
            ferttowater[range(int(val2), int(val2)+int(val3)+1)
                        ] = range(int(val1), int(val1)+int(val3)+1)
            continue

        if datatype == 4:
            if line.find(":") != -1:
                continue
            val1, val2, val3 = line.split(" ")
            watertolight[range(int(val2), int(val2)+int(val3)+1)
                         ] = range(int(val1), int(val1)+int(val3)+1)
            continue

        if datatype == 5:
            if line.find(":") != -1:
                continue
            val1, val2, val3 = line.split(" ")
            lighttotemp[range(int(val2), int(val2)+int(val3)+1)
                        ] = range(int(val1), int(val1)+int(val3)+1)
            continue

        if datatype == 6:
            if line.find(":") != -1:
                continue
            val1, val2, val3 = line.split(" ")
            temptohumid[range(int(val2), int(val2)+int(val3)+1)
                        ] = range(int(val1), int(val1)+int(val3)+1)
            continue

        if datatype == 7:
            if line.find(":") != -1:
                continue
            val1, val2, val3 = line.split(" ")
            humidtoloc[range(int(val2), int(val2)+int(val3)+1)
                       ] = range(int(val1), int(val1)+int(val3)+1)
            continue

    for seedrange in seeds:
        for seed in seedrange:
            soil = mapval(seed, seedtosoil)
            fert = mapval(soil, soiltofert)
            water = mapval(fert, ferttowater)
            light = mapval(water, watertolight)
            temp = mapval(light, lighttotemp)
            humid = mapval(temp, temptohumid)
            loc = mapval(humid, humidtoloc)
            validation = loc if loc < validation else validation

    return (validation)


def mapval(input, mapdict: dict):
    retval = input
    for key in mapdict.keys():
        if int(input) in key:
            retval = mapdict[key][key.index(int(input))]
            break
    return retval


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        output = str(main(lines))
        t1_stop = perf_counter_ns()
        print(file + ": "+output + "\tElapsed time:",
              (t1_stop - t1_start)/1000000000)
