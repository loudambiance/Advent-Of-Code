from time import perf_counter_ns


def main(lines: list[str]):
    score = 0
    for line in lines:
        player1 = line.split(' ')[0]
        player2 = line.split(' ')[1]
        score += getScore(player1, player2)
    return(score)


def getScore(player1: list, player2: list):
    score = 0
    # Rock = A,X, Paper = B,Y, Scissors = C,Z
    options = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    loss = [["A", "Z"], ["B", "X"], ["C", "Y"]]
    win = [["A", "Y"], ["B", "Z"], ["C", "X"]]
    player1score = options[player1]
    player2score = options[player2]
    if player1score == player2score:
        score += player2score + 3
    elif [player1, player2] in loss:
        score += player2score + 0
    elif [player1, player2] in win:
        score += player2score + 6
    return score


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files:
        t1_start = perf_counter_ns()
        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
        t1_stop = perf_counter_ns()
        print(file + " Elapsed time:", (t1_stop - t1_start)/1000000000)