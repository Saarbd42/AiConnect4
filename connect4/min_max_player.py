import numpy as np
from connect4 import who_won as ww
from connect4 import game_board as gb


class MinMaxPlayer:
    def __init__(self, original_player_number, original_second_player_number, max_forward_sight):
        self.player_number = original_player_number
        self.original_player_number = original_player_number
        self.original_second_player_number = original_second_player_number
        self.max_forward_sight = max_forward_sight

    def make_a_move(self, board):
        scores = np.zeros(7)
        for i in range(7):
            scores[i] = self.score_the_move(board, i, self.player_number, 1)
        scores += self.center_sized_array()
        return np.argmax(scores)

    def center_sized_array(self):
        return np.array([0, 1, 2, 3, 2, 1, 0])

    def try_seven_moves(self, board, player_num, current_forward_sight):
        scores = np.zeros(7)
        for i in range(7):
            scores[i] = self.score_the_move(board, i, player_num, current_forward_sight)
        return self.return_min_or_max(scores, player_num)

    def score_the_move(self, board, move, player_num, current_forward_sight):
        if self.is_move_legal(board, move):
            copied_board = self.copy_and_change_copied_board(board, move, player_num)
            return self.score_a_legal_move(copied_board, player_num, current_forward_sight)
        else:
            if self.am_i_trying_to_max(player_num):
                return -10000
            else:
                return 10000

    def score_a_legal_move(self, copied_board, player_num, current_forward_sight):
        if ww.check_if_player_won(copied_board, player_num):
            return self.score_a_win(player_num, current_forward_sight)
        else:
            if current_forward_sight >= self.max_forward_sight:
                return 0
            else:
                return self.switch_player_and_try_seven_moves(copied_board, player_num, current_forward_sight + 1)

    def score_a_win(self, player_num, current_forward_sight):
        if self.am_i_trying_to_max(player_num):
            return 1000 - self.penalize_long_wins(current_forward_sight)
        else:
            return -1000 + self.penalize_long_wins(current_forward_sight)

    def penalize_long_wins(self, current_forward_sight):
        result = current_forward_sight * 5
        return result

    def return_min_or_max(self, scores, player_num):
        if self.am_i_trying_to_max(player_num):
            return np.max(scores)
        else:
            return np.min(scores)

    def am_i_trying_to_max(self, player_number):
        if player_number == self.original_player_number:
            return True
        else:
            return False

    def switch_player_and_try_seven_moves(self, copied_board, player_num, updated_forward_sight):
        new_player_num = self.switch_player(player_num)
        return self.try_seven_moves(copied_board, new_player_num, updated_forward_sight)

    def switch_player(self, player_num):
        if player_num == self.original_player_number:
            return self.original_second_player_number
        else:
            return self.original_player_number

    def copy_and_change_copied_board(self, board, move, player_num):
        copied_board = self.copy_board(board)
        copied_board.change_the_board(move, player_num)
        return copied_board

    def copy_board(self, board):
        board_current_state = board.get_current_state()
        a_copy_of_the_board = gb.CopiedBoard(board_current_state)
        return a_copy_of_the_board

    def is_move_legal(self, board, player_move):
        current_board = board.get_current_state()
        if current_board[0][player_move] == 0:
            return True
        else:
            return False
