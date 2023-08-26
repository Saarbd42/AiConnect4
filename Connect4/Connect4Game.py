import WhoWon as ww


def visualConnect4Game(board, firstPlayer, secondPlayer):
    basicVisuals(board)
    while True:
        possibleWinner = makeAMoveAndCheckForVictory(board, firstPlayer)
        basicVisuals(board)
        if possibleWinner != 0:
            return possibleWinner

        possibleWinner = makeAMoveAndCheckForVictory(board, secondPlayer)
        basicVisuals(board)
        if possibleWinner != 0:
            return possibleWinner

        if board.checkForTie():
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
