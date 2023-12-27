from time import perf_counter_ns
from functools import reduce
init_colors = {
    'green': 13,
    'red': 12,
    'blue': 14
}


def main(lines: list[str]):
    validation = 0
    for line in lines:
        line = line.removeprefix("Game ")
        id, games = line.split(":")
        colors = {'red': 0, 'green': 0, 'blue': 0}
        for game in games.split(";"):
            game = game.strip()
            d = dict(reversed(x.strip().split(" ")) for x in game.split(","))
            for color in init_colors:
                if (color in d):
                    colors[color] = int(d[color]) if int(
                        d[color]) > colors[color] else colors[color]
        validation += reduce((lambda x, y: x * y), colors.values())
        print("{} : {} : {}".format(id, games, validation))

    print(validation)
    return (0)


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)
