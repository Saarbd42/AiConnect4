import numpy as np
import WhoWon as ww
import gameBoard as gb


class MinMaxPlayer():
    def __init__(self, playerNumber, secondPlayerNum, maxForwardPredictions):
        self.playerNumber = playerNumber
        self.originalPlayerNumber = playerNumber
        self.originalSecondPlayerNumber = secondPlayerNum
        self.forwardPredictions = 0
        self.maxForwardPredictions = maxForwardPredictions

    # Check All possible options as it's own playerNum
    # Try the Options
    # See if there is an option for victory
    # Switch to The Other Player
    # Check All possible options
    # Try the Options
    # See if there is an option for lose
    # Switch to It own playerNum

    def tryAMove(self, board):
        legalMoves = self.checkLegalMoves(board)
        scoresTable = [0, 0, 0, 0, 0, 0, 0]
        for i in range(len(legalMoves)):
            copyOfTheBoard = self.copyBoard(board)
            copyOfTheBoard.changeTheBoard(legalMoves[i], self.playerNumber)
            score = self.scoreTheBoard(copyOfTheBoard)
            self.switchPlayer()
            return self.returnAScore(score, copyOfTheBoard)

    def returnAScore(self, score, copyOfTheBoard):
        if score == 0 and self.forwardPredictions <= self.maxForwardPredictions:
            return self.tryAMove(copyOfTheBoard)
        else:
            return score

    def scoreTheBoard(self, board):
        if ww.checkIfPlayerWon(board, self.playerNumber):
            if self.playerNumber == self.originalPlayerNumber:
                return 1000
            else:
                return -1000
        return 0

    def copyBoard(self, board):
        boardCurrentState = board.getCurrentState()
        aCopyOfTheBoard = gb.CopiedBoard(boardCurrentState)
        return aCopyOfTheBoard

    def checkLegalMoves(self, board):
        legalMoves = []
        currentBoard = board.getCurrentState()
        for i in range(7):
            if currentBoard[0][i] == 0:
                legalMoves.append(i)
        return legalMoves

    def switchPlayer(self):
        if self.playerNumber == self.originalPlayerNumber:
            self.playerNumber = self.originalSecondPlayerNumber
        else:
            self.playerNumber = self.originalPlayerNumber
