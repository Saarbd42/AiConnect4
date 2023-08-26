import WhoWon as ww
import time

def visualConnect4Game(board, firstPlayer, secondPlayer):
    printPrettyBoard(board, firstPlayer.playerNumber, secondPlayer.playerNumber)
    while True:
        possibleWinner = makeAMoveAndCheckForVictory(board, firstPlayer)
        printPrettyBoard(board, firstPlayer.playerNumber, secondPlayer.playerNumber)
        if possibleWinner != 0:
            victoryAnnouncement(possibleWinner, firstPlayer.playerNumber, secondPlayer.playerNumber)
            return possibleWinner

        possibleWinner = makeAMoveAndCheckForVictory(board, secondPlayer)
        printPrettyBoard(board, firstPlayer.playerNumber, secondPlayer.playerNumber)
        if possibleWinner != 0:
            victoryAnnouncement(possibleWinner, firstPlayer.playerNumber, secondPlayer.playerNumber)
            return possibleWinner

        if board.checkForTie():
            victoryAnnouncement(0, firstPlayer.playerNumber, secondPlayer.playerNumber)
            return 0


def noVisualConnect4Game(board, firstPlayer, secondPlayer):
    while True:
        possibleWinner = makeAMoveAndCheckForVictory(board, firstPlayer) != 0
        if possibleWinner != 0:
            return possibleWinner

        possibleWinner = makeAMoveAndCheckForVictory(board, secondPlayer) != 0
        if possibleWinner != 0:
            return possibleWinner

        if board.checkForTie():
            return 0


def victoryAnnouncement(winner, firstPlayerNum, secondPlayerNum):
    # print("")
    if winner != 0:
        if winner == firstPlayerNum:
            print(makeStringBlue(f"PLAYER {winner} WON!"))
        elif winner == secondPlayerNum:
            print(makeStringRed(f"PLAYER {winner} WON!"))
    else:
        print("TIE")
    input("Press anything to continue ")
    print("")


def makeAMoveAndCheckForVictory(board, player):
    move = makeAMoveAndMakeSureItsLegal(board, player)
    board.changeTheBoard(move, player.playerNumber)
    if ww.checkIfPlayerWon(board, player.playerNumber):
        return player.playerNumber
    return 0


def makeAMoveAndMakeSureItsLegal(board, player):
    legalMove = False
    while not legalMove:
        move = player.makeAMove(board)
        legalMove = fullLegalityCheck(move, board)
    return move


def fullLegalityCheck(playerMove, board):
    if firstLegalityCheck(playerMove):
        return secondLegalityTest(playerMove, board)
    else:
        return False


def firstLegalityCheck(playerMove):
    try:
        playerMove = int(playerMove)
    except:
        return False
    return True


def secondLegalityTest(playerMove, board):
    if playerMove < 0 or playerMove > 6:
        return False
    elif board.boardCurrentState[0][playerMove] != 0:
        return False
    else:
        return True


def basicVisuals(board):
    print("")
    print(board.getCurrentState())


def printPrettyBoard(board, firstPlayerNum, secondPlayerNum):
    currentBoard = board.getCurrentState()
    prettyBoard = makePrettyBoardString(currentBoard, firstPlayerNum, secondPlayerNum)
    print(prettyBoard)


def makePrettyBoardString(currentBoard, firstPlayerNum, secondPlayerNum):
    DELIMITER = "|"
    prettyBoard = ""
    for i in range(len(currentBoard)):
        prettyBoard += "\n"
        prettyBoard += DELIMITER
        for j in range(len(currentBoard[0])):
            currentPosition = int(currentBoard[i][j])
            prettyBoard += drawTheChip(currentPosition, firstPlayerNum, secondPlayerNum) + DELIMITER
    return prettyBoard


def drawTheChip(currentPosition, firstPlayerNum, secondPlayerNum):
    chip = ""
    if currentPosition == firstPlayerNum:
        chip = makeStringBlue("0")
    elif currentPosition == secondPlayerNum:
        chip = makeStringRed("0")
    else:
        chip = "0"
    return chip


def makeStringBlue(string):
    return "\033[94m" + string + "\033[0m"


def makeStringRed(string):
    return "\033[91m" + string + "\033[0m"
