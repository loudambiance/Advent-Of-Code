from time import perf_counter_ns


def main(lines: list[str]):
    res = dict()
    count = 0
    for line in lines:
        if len(line) == 0:
            if validate(res):
                count = count+1
                print(res)
            res = dict()
            continue
        res = res | dict(item.split(":") for item in line.split(" "))
    else:
        if validate(res):
            count = count+1
            print(res)
    print(count)


def validate(res: dict):
    ret = True
    fieldspresnet = all(x in res.keys() for x in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    if not fieldspresnet:
        ret = False
    else:
        ret = yearvalidate(res['byr'], 1920, 2002) and \
            yearvalidate(res['iyr'], 2010, 2020) and \
            yearvalidate(res['eyr'], 2020, 2030) and \
            heightvalidate(res['hgt']) and \
            colorvalidate(res['hcl']) and \
            res['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and \
            pidvalidate(res['pid'])
    return ret


def pidvalidate(value: str):
    return len(value) == 9 and set(value).issubset(set('0123456789'))


def colorvalidate(value: str):
    return len(value) == 7 and value.startswith('#') and set(value.removeprefix("#")).issubset(set('01234567890ABCDEFabcdef'))


def heightvalidate(value: str):
    valid = True
    if value.endswith('cm'):
        tmpval = int(value.removesuffix('cm'))
        if not (tmpval >= 150 and tmpval <= 193):
            valid = False
    elif value.endswith('in'):
        tmpval = int(value.removesuffix('in'))
        if not (tmpval >= 59 and tmpval <= 76):
            valid = False
    else:
        valid = False
    return valid


def yearvalidate(val: str, min: int, max: int, length: int = 4):
    valint = int(val)
    valid = False
    if len(val) == length and valint >= min and valint <= max:
        valid = True
    return valid


if __name__ == "__main__":
    files = ("C:\\Projects\\Python\\Advent\\2020\\4\\input_ex.txt", "C:\\Projects\\Python\\Advent\\2020\\4\\input.txt")
    for file in files:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)
