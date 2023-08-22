import numpy as np
import WhoWon as ww
import gameBoard as gb

class MinMaxPlayer():
    def __init__(self, playerNumber, howManyForwardPredictions):
        self.playerNumber = playerNumber

    def makeAMove(self, board, howManyForwardPredictions, currentForwardPrediction):
        legalMoves = self.checkLegalMoves(board)
        for i in range(len(legalMoves)):  # TODO: CONTINUE
            return  # TODO: CONTINUE

    def checkAllOptions(self, currentBoard, playerNum):
        legalMoves = self.checkLegalMoves(currentBoard)
        for i in range(len(legalMoves)):
            copiedBoard = self.makeACopyOfTheBoard(currentBoard)
            self.makeAMoveAndCheckForVictory(copiedBoard, legalMoves[i], playerNum)

        return # TODO: CONTINUE

    def makeAMoveAndCheckForVictory(self, fakeBoard, move, playerNum):
        fakeBoard.changeTheBoard(move, playerNum)
        if ww.checkIfPlayerWon(fakeBoard, playerNum):
            return 1000
        else:
            return 0

    def makeACopyOfTheBoard(self, board):
        copiedBoard = gb.Board
        currentBoard = board.getCurrentState
        copiedBoardCurrentState = np.copy(currentBoard)
        copiedBoard.switchToANewBoard(copiedBoardCurrentState)
        return copiedBoard

    def checkLegalMoves(self, board):
        legalMoves = []
        currentBoard = board.getCurrentState()
        for i in range(7):
            if currentBoard[0][i] == 0:
                legalMoves.append(i)
        return legalMoves
