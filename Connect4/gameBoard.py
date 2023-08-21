import numpy as np


class Board():
    def __init__(self):
        self.boardCurrentState = np.zeros([6, 7])

    def getCurrentState(self):
        return self.boardCurrentState

    def changeTheBoard(self, playerMove, playerNumber):
        if not self.isThereAnError(playerMove):
            for i in range(6):
                if self.boardCurrentState[5 - i][playerMove] == 0:
                    self.boardCurrentState[5 - i][playerMove] = playerNumber
                    break

    def isThereAnError(self, playerMove):
        if self.boardCurrentState[0][playerMove] != 0 or playerMove > 6 or playerMove < 0:
            print("Error!")
            return True
        else:
            return False
