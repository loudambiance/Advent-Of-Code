from time import perf_counter_ns
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
        valid_game = True
        for game in games.split(";"):
            if (valid_game is False):
                break
            game = game.strip()
            d = dict(reversed(x.strip().split(" ")) for x in game.split(","))
            valid_game = validate(d)
        validation += int(id) if valid_game else 0
        print("{} : {} : {}".format(id, games, validation))

    print(validation)
    return (0)


def validate(d: dict):
    valid = True
    colors = init_colors.keys()
    for color in colors:
        if (valid is False):
            break
        if (color in d):
            if not ((int(d[color]) <= init_colors[color])):
                valid = False
    return valid


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)
