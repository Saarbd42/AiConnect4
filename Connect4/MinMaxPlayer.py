import numpy as np
import WhoWon as ww
import gameBoard as gb


class MinMaxPlayer():
    def __init__(self, originalPlayerNumber, originalSecondPlayerNumber, maxForwardSight):
        self.playerNumber = originalPlayerNumber
        self.originalPlayerNumber = originalPlayerNumber
        self.originalSecondPlayerNumber = originalSecondPlayerNumber
        self.maxForwardSight = maxForwardSight

    def makeAMove(self, board):
        scores = np.zeros(7)
        for i in range(7):
            scores[i] = self.scoreTheMove(board, i, self.playerNumber, 1)
        scores += self.centersizedArray()
        return np.argmax(scores)

    def centersizedArray(self):
        return np.array([0,1,2,3,2,1,0])

    def trySevenMoves(self, board, playerNum, currentForwardSight):
        scores = np.zeros(7)
        for i in range(7):
            scores[i] = self.scoreTheMove(board, i, playerNum, currentForwardSight)
        return self.returnMinOrMax(scores, playerNum)

    def scoreTheMove(self, board, move, playerNum, currentForwardSight):
        if self.isMoveLegal(board, move):
            copiedBoard = self.copyAndChangeCopiedBoard(board, move, playerNum)
            return self.scoreALegalMove(copiedBoard, playerNum, currentForwardSight)
        else:
            if self.amITryingToMax(playerNum):
                return -10000
            else:
                return 10000

    def scoreALegalMove(self, copiedBoard, playerNum, currentForwardSight):
        if ww.checkIfPlayerWon(copiedBoard, playerNum):
            return self.scoreAWin(playerNum, currentForwardSight)
        else:
            if currentForwardSight >= self.maxForwardSight:
                return 0
            else:
                return self.switchPlayerAndTrySevenMoves(copiedBoard, playerNum, currentForwardSight + 1)

    def scoreAWin(self, playerNum, currentForwardSight):
        if self.amITryingToMax(playerNum):
            return 1000 - self.penalizeLongWins(currentForwardSight)
        else:
            return -1000 + self.penalizeLongWins(currentForwardSight)

    def penalizeLongWins(self, currentForwardSight):
        result = currentForwardSight*5
        return result

    def returnMinOrMax(self, scores, playerNum):
        if self.amITryingToMax(playerNum):
            return np.max(scores)
        else:
            return np.min(scores)

    def amITryingToMax(self, playerNumber):
        if playerNumber == self.originalPlayerNumber:
            return True
        else:
            return False

    def switchPlayerAndTrySevenMoves(self, copiedBoard, playerNum, updatedForwardSight):
        newPlayerNum = self.switchPlayer(playerNum)
        return self.trySevenMoves(copiedBoard, newPlayerNum, updatedForwardSight)

    def switchPlayer(self, playerNum):
        if playerNum == self.originalPlayerNumber:
            return self.originalSecondPlayerNumber
        else:
            return self.originalPlayerNumber

    def copyAndChangeCopiedBoard(self, board, move, playerNum):
        copiedBoard = self.copyBoard(board)
        copiedBoard.changeTheBoard(move, playerNum)
        return copiedBoard

    def copyBoard(self, board):
        boardCurrentState = board.getCurrentState()
        aCopyOfTheBoard = gb.CopiedBoard(boardCurrentState)
        return aCopyOfTheBoard

    def isMoveLegal(self, board, playerMove):
        currentBoard = board.getCurrentState()
        if currentBoard[0][playerMove] == 0:
            return True
        else:
            return False
