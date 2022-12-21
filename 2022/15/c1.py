from time import perf_counter_ns
import numpy


def main(lines: list[str]):
    data = parseInput(lines)
    minmax = getMinMax(data)
    data = offsetData(data, minmax)
    print(minmax)
    grid = numpy.empty((minmax['xmax']+minmax['offset']+5, minmax['ymax']+minmax['offset']+5), dtype='uint8')
    y2, x2 = numpy.ogrid[0:minmax['xmax']+minmax['offset']+5, 0:minmax['ymax']+minmax['offset']+5]
    for set in data:
        sensor = set['s']
        beacon = set['b']
        distance = abs(sensor[0]-beacon[0])+abs(sensor[1]-beacon[1])
        mask = abs(sensor[0]-x2) + abs(sensor[1]-y2) <= distance
        grid[mask] = 1
    for set in data:
        sensor = set['s']
        beacon = set['b']
        grid[sensor[1], sensor[0]] = 2
        grid[beacon[1], beacon[0]] = 3
    return (grid[10 + minmax['offset'], :] == 1).sum()


def offsetData(data: list[dict[str, int]], minmax:  dict[str, int]) -> dict[str, int]:
    retval = data
    offset = minmax['offset']
    for datum in retval:
        datum['s'][0] = datum['s'][0] + offset
        datum['b'][0] = datum['b'][0] + offset
        datum['s'][1] = datum['s'][1] + offset
        datum['b'][1] = datum['b'][1] + offset
    return retval


def parseInput(lines: list[str]) -> list[dict[str, int]]:
    data = list()
    for line in lines:
        datum = {}
        coords = (line.replace('Sensor at ', '')
                  .replace(' closest beacon is at ', '')
                  .replace('x=', '')
                  .replace(' y=', '')
                  .split(':'))
        datum['s'] = list(map(int, coords[0].split(',')))
        datum['b'] = list(map(int, coords[1].split(',')))
        data.append(datum)
    return data


def getMinMax(data: list[dict[str, int]]) -> dict[str, int]:
    xmin = min([min([item[0] for item in dictitem.values()]) for dictitem in data])
    ymin = min([min([item[1] for item in dictitem.values()]) for dictitem in data])
    xmax = max([max([item[0] for item in dictitem.values()]) for dictitem in data])
    ymax = max([max([item[1] for item in dictitem.values()]) for dictitem in data])
    dmax = max([abs(item['s'][0]-item['b'][0])+abs(item['s'][1]-item['b'][1]) for item in data])
    if xmin-dmax > 0 and ymin-dmax > 0:
        offset = xmin-dmax if xmin > ymin else ymin-dmax
        xmax = xmax - offset
        ymax = ymax - offset
    else:
        offset = xmin+dmax if xmin > ymin else ymin+dmax
    return {'xmax': xmax, 'ymax': ymax, 'offset': offset}


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files[:]:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)
