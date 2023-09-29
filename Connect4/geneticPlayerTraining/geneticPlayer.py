import random


class GeneticPlayer():
    def __init__(self, playerNumber):
        self.playerNumber = playerNumber

    def makeAMove(self, board):
        legalMoves = self.checkLegalMoves(board)
        playerMove = random.choice(legalMoves)
        return playerMove

    def checkLegalMoves(self, board):
        legalMoves = []
        currentBoard = board.getCurrentState()
        for i in range(7):
            if currentBoard[0][i] == 0:
                legalMoves.append(i)
        return legalMoves
