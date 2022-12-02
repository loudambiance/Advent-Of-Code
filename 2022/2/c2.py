

def main(lines):
    score = 0
    for line in lines:
        player1 = line.split(' ')[0]
        player2 = line.split(' ')[1]
        score += getScore(player1, player2)
    return(score)


def getScore(player1, player2):
    score = 0
    # Rock = A,M, Paper = B,N, Scissors = C,O
    options = {"A": 1, "B": 2, "C": 3, "M": 1, "N": 2, "O": 3}
    loss = {"A": "O", "B": "M", "C": "N"}
    win = {"A": "N", "B": "O", "C": "M"}
    tie = {"A": "M", "B": "N", "C": "O"}
    if player2 == "X":
        score += options[loss[player1]] + 0
    elif player2 == "Y":
        score += options[tie[player1]] + 3
    elif player2 == "Z":
        score += options[win[player1]] + 6
    return score


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files:

        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
