bingoBoards = []
bingoNumbers = []
previousWinner = []
winningCall = '0'
with open('task4a.txt') as f:
    bingoNumbers = f.readline().strip('\n\r ').split(',')
    f.readline()
    while(True):
        bingoBoard = []
        for x in range(5):
            line = []
            for square in f.readline().strip('\n\r').split(' '):
                if square == '':
                    continue
                line.append({'square': square, 'marked': False})
            bingoBoard.append(line)
        bingoBoards.append(bingoBoard)
        if not f.readline():
            break


def markSquare(boards, number):
    for board in boards:
        for line in board:
            for square in line:
                if square['square'] == number:
                    square['marked'] = True
    checkWin(boards, number)


def checkWin(boards, number):
    for board in boards[:]:
        # row check
        if innerLoop(boards, board, number, False):
            continue

        # column check
        if innerLoop(boards, board, number, True):
            continue
    return


def innerLoop(boards, board, number, column):
    global previousWinner
    global winningCall
    if(column):
        lines = zip(*board)
    else:
        lines = board
    for line in lines:
        if checkListWin(list(line)):
            boards.remove(board)
            previousWinner = board
            winningCall = number
            return True
    return False


def checkListWin(list):
    win = True
    for square in list:
        if square['marked'] == False:
            win = False
    return win


def calcWinValue(board):
    global winningCall
    squares = [item for x in board for item in x]
    score = 0
    for square in squares:
        if square['marked'] == False:
            score += int(square['square'])
    return score*int(winningCall)


for nextnumber in bingoNumbers:
    if len(bingoBoards) == 0:
        break
    markSquare(bingoBoards, nextnumber)
winval = calcWinValue(previousWinner)
print(winval)
