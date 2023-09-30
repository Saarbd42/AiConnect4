import numpy as np


class Board():
    def __init__(self):
        self.board_current_state = np.zeros([6, 7])

    def get_current_state(self):
        return self.board_current_state

    def check_for_tie(self):
        count = 0
        for i in range(7):
            if self.board_current_state[0][i] != 0:
                count += 1
        if count == 7:
            return True
        return False

    def change_the_board(self, player_move, player_number):
        if not self.is_there_an_error(player_move):
            for i in range(6):
                if self.board_current_state[5 - i][player_move] == 0:
                    self.board_current_state[5 - i][player_move] = player_number
                    break

    def is_there_an_error(self, player_move):
        if self.board_current_state[0][player_move] != 0 or player_move > 6 or player_move < 0:
            print("Error!")
            return True
        else:
            return False


class CopiedBoard():
    def __init__(self, board_current_state):
        self.board_current_state = np.copy(board_current_state)

    def get_current_state(self):
        return self.board_current_state

    def check_for_tie(self):
        count = 0
        for i in range(7):
            if self.board_current_state[0][i] != 0:
                count += 1
        if count == 7:
            return True
        return False

    def change_the_board(self, player_move, player_number):
        if not self.is_there_an_error(player_move):
            for i in range(6):
                if self.board_current_state[5 - i][player_move] == 0:
                    self.board_current_state[5 - i][player_move] = player_number
                    break

    def is_there_an_error(self, player_move):
        if self.board_current_state[0][player_move] != 0 or player_move > 6 or player_move < 0:
            print("Error!")
            return True
        else:
            return False
