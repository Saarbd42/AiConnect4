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


class MinMaxAlgo():
    def __init__(self, originalPlayerNumber, originalSecondPlayerNumber, maxForwardSight):
        self.originalPlayerNumber = originalPlayerNumber
        self.originalSecondPlayerNumber = originalSecondPlayerNumber
        self.maxForwardSight = maxForwardSight

    def trySevenMoves(self, board, playerNum, currentForwardSight):
        scores = np.zeros(7)
        for move in range(7):
            scores[move] = self.scoreTheMove(board, move, playerNum, currentForwardSight)
        return self.returnMinOrMax(scores, playerNum)

    def scoreTheMove(self, board, move, playerNum, currentForwardSight):
        if self.isMoveLegal(board, move):
            copiedBoard = self.copyAndChangeCopiedBoard(board, move, playerNum)
            self.scoreALegalMove(copiedBoard, playerNum, currentForwardSight)
        else:
            return -10000

    def scoreALegalMove(self, copiedBoard, playerNum, currentForwardSight):
        if ww.checkIfPlayerWon(copiedBoard, playerNum):
            return self.scoreAWin(self.amITryingToMax(playerNum))
        else:
            if currentForwardSight >= self.maxForwardSight:
                return 0
            else:
                return self.switchPlayerAndTrySevenMoves(copiedBoard, playerNum, currentForwardSight + 1)

    def scoreAWin(self, tryToMax):
        if tryToMax:
            return 1000
        else:
            return -1000

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
        if board[0][playerMove] == 0:
            return True
        else:
            return False
