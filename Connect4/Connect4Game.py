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
    move = player.makeAMove(board)
    board.changeTheBoard(move, player.playerNumber)
    if ww.checkIfPlayerWon(board, player.playerNumber):
        return player.playerNumber
    return 0


def basicVisuals(board):
    print("")
    print(board.getCurrentState())