def checkIfPlayerWon(board, playerNum):
    if checkRows(board, playerNum) or checkColumns(board, playerNum) or checkDiagonals(board, playerNum):
        return True
    else:
        return False


def checkDiagonals(board, playerNum):
    currentBoard = board.getCurrentState()
    if checkDownwardDiagonals(currentBoard, playerNum) or checkUpwardDiagonals(currentBoard, playerNum):
        return True
    return False

def checkColumns(board, playerNum):
    currentBoard = board.getCurrentState()
    for columnNum in range(len(currentBoard[0])):
        if checkSpecificColumn(currentBoard, playerNum, columnNum):
            return True
    return False


def checkRows(board, playerNum):
    currentBoard = board.getCurrentState()
    for rowNum in range(len(currentBoard)):
        if checkSpecificRow(currentBoard, playerNum, rowNum):
            return True
    return False


def checkDownwardDiagonals(currentBoard, playerNum):
    for rowNum in range(3):
        for j in range(4):
            count = 0
            for i in range(4):
                if currentBoard[i + rowNum][i + j] == playerNum:
                    count += 1
            if count >= 4:
                return True
    return False


def checkUpwardDiagonals(currentBoard, playerNum):
    for rowNum in range(3):
        for j in range(4):
            count = 0
            for i in range(4):
                if currentBoard[5 - (i + rowNum)][i + j] == playerNum:
                    count += 1
            if count >= 4:
                return True
    return False


def checkSpecificColumn(currentBoard, playerNum, columnNum):
    if currentBoard[2][columnNum] == playerNum and currentBoard[3][columnNum] == playerNum:
        return checkTheColumnContinuitySum(currentBoard, playerNum, columnNum)
    else:
        return False


def checkTheColumnContinuitySum(currentBoard, playerNum, columnNum):
    upContinuity = checkContinuity(
        [currentBoard[4][columnNum], currentBoard[5][columnNum]],
        playerNum)
    downContinuity = checkContinuity(
        [currentBoard[1][columnNum], currentBoard[0][columnNum]],
        playerNum)
    return checkIfSumBiggerThanOne(upContinuity, downContinuity)


def checkIfSumBiggerThanOne(num1, num2):
    sumTheSides = num1 + num2
    if sumTheSides >= 2:
        return True
    else:
        return False


def checkSpecificRow(currentBoard, playerNum, rowNum):
    if currentBoard[rowNum][3] == playerNum:
        return checkTheRowContinuitySum(currentBoard, playerNum, rowNum)
    else:
        return False


def checkTheRowContinuitySum(currentBoard, playerNum, rowNum):
    leftSideContinuity = checkContinuity(
        [currentBoard[rowNum][2], currentBoard[rowNum][1], currentBoard[rowNum][0]],
        playerNum)
    rightSideContinuity = checkContinuity(
        [currentBoard[rowNum][4], currentBoard[rowNum][5], currentBoard[rowNum][6]],
        playerNum)
    return checkIfSumBiggerThanTwo(leftSideContinuity, rightSideContinuity)

def checkIfSumBiggerThanTwo(num1, num2):
    sumTheSides = num1 + num2
    if sumTheSides >= 3:
        return True
    else:
        return False

def checkContinuity(spots, playerNum):
    count = 0
    for i in range(len(spots)):
        if spots[i] == playerNum:
            count += 1
        else:
            break
    return count


# FOR TEST
import gameBoard as gb

board = gb.Board()
board.changeTheBoard(0, 0)
board.changeTheBoard(1, 1)
board.changeTheBoard(1, 2)
board.changeTheBoard(2, 1)
board.changeTheBoard(2, 1)
board.changeTheBoard(3, 2)
board.changeTheBoard(3, 2)
board.changeTheBoard(3, 1)
board.changeTheBoard(4, 2)
board.changeTheBoard(4, 2)
board.changeTheBoard(4, 2)
board.changeTheBoard(4, 1)


print(board.getCurrentState())
print(checkIfPlayerWon(board, 1))
