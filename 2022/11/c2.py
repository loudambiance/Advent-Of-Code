from time import perf_counter_ns
import math
import pprint
pp = pprint.PrettyPrinter(indent=4)


def main(lines: list[str]):
    monkeys = parseData(lines)
    lcmvalues = list()
    for monkey in monkeys.values():
        lcmvalues.append(monkey["test"])
    lcm = math.prod(lcmvalues)
    for x in range(0, 10000):
        for monkey in monkeys.values():
            while monkey["items"]:
                old = monkey["items"].pop(0)
                item = eval(monkey["operation"])
                item = item % lcm
                monkey["runningcount"] += 1
                if item % monkey["test"] == 0:
                    monkeys[monkey["true"]]["items"].append(item)
                else:
                    monkeys[monkey["false"]]["items"].append(item)
    values = list()
    for monkey in monkeys.values():
        values.append(monkey["runningcount"])
    values.sort(reverse=True)
    return (math.prod(values[:2]))


def parseData(lines: list[str]):
    monkeys = dict()
    currmonkey = ""
    for line in lines:
        if line.startswith("Monkey "):
            currmonkey = line.lower().removesuffix(":")
            monkeys[currmonkey] = dict()
            monkeys[currmonkey]["runningcount"] = 0
        elif line.startswith("  Starting items:"):
            monkeys[currmonkey]["items"] = list(map(int, line.replace("  Starting items: ", "").split(", ")))
        elif line.startswith("  Operation: new = "):
            monkeys[currmonkey]["operation"] = line.replace("  Operation: new = ", "")
        elif line.startswith("  Test: divisible by "):
            monkeys[currmonkey]["test"] = int(line.replace("Test: divisible by ", ""))
        elif line.startswith("    If true: throw to "):
            monkeys[currmonkey]["true"] = line.replace("    If true: throw to ", "")
        elif line.startswith("    If false: throw to "):
            monkeys[currmonkey]["false"] = line.replace("    If false: throw to ", "")
    return monkeys


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)
