from time import perf_counter_ns
from collections import OrderedDict


def main(lines: list[str]):
    row = 10
    data = parseInput(lines)
    row_data = dict()
    for set in data:
        sensor = set['s']
        beacon = set['b']
        distance = abs(sensor[0]-beacon[0])+abs(sensor[1]-beacon[1])
        if row in range(sensor[1]-distance, sensor[1]+distance+1):
            row_distance = abs(distance-abs(sensor[1]-row))
            print("Sensor:", sensor, "Beacon:", beacon, "Distance:", distance,
                  "Range:", range(sensor[0]-row_distance, sensor[0]+row_distance+1), "Row Dist:", row_distance)
            for x in range(sensor[0]-row_distance, sensor[0]+row_distance+1):
                # print(x)
                if (x not in row_data.keys()):
                    row_data[x] = '#'
            if sensor[1] == row:
                row_data[sensor[0]] = 'S'
            if beacon[1] == row:
                row_data[beacon[0]] = 'B'
    return sum(1 for value in row_data.values() if value == '#')


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


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files[:]:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)
