class HumanPlayer():
    def __init__(self, playerNumber):
        self.playerNumber = playerNumber

    def makeAMove(self, board):
        playerMove = input(f"Player {self.playerNumber}: ")
        if self.checkIfLegalMove(playerMove, board):
            return self.formatPlayerMove(playerMove)
        else:
            print("Error")
            return -1  # Signals error

    def checkIfLegalMove(self, playerMove, board):
        if self.firstLegalityTest(playerMove):
            playerMove = self.formatPlayerMove(playerMove)
            return self.secondLegalityTest(playerMove, board)
        else:
            return False

    def firstLegalityTest(self, playerMove):
        try:
            playerMove = int(playerMove)
        except:
            # print("Error")
            return False
        return True

    def formatPlayerMove(self, playerMove):
        playerMove = int(playerMove)
        playerMove -= 1  # Format
        return playerMove

    def secondLegalityTest(self, playerMove, board):
        if playerMove < 0 or playerMove > 6:
            return False
        elif board.boardCurrentState[0][playerMove] != 0:
            return False
        else:
            return True
