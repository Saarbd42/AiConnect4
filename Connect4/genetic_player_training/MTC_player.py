from connect4 import game_types
from connect4.genetic_player_training.genetic_player import is_move_legal
import numpy as np
from connect4.game_board import CopiedBoard
from connect4 import who_won


class MTCPlayer:
    def __init__(self, player_number, mtc_num):
        self.player_number = player_number
        self.mtc_num = mtc_num

    def score_a_board(self, board, player_move):
        if is_move_legal(board, player_move):
            return self.score_a_board_with_mtc(board, player_move)
        else:
            return -1000

    def score_a_board_with_mtc(self, board, player_move):
        if self.check_for_instant_win(board, player_move):
            return self.mtc_num
        else:
            final_score = self.preform_mtc_algorithm(board, player_move)
            return final_score

    def preform_mtc_algorithm(self, board, player_move):
        final_score = 0
        mtc_played_first = (self.player_number == 1)
        for i in range(self.mtc_num):
            # MAKE THE MOVE
            new_board = CopiedBoard(board.get_current_state())
            new_board.change_the_board(player_move, self.player_number)
            if not new_board.check_for_tie(): # MAKE SURE THERE ISN'T A TIE
                # CHECK HOW IT TURNS UP FOR YOU
                winning_player = game_types.random_vs_random_game(new_board, mtc_played_first=mtc_played_first)
                final_score += self.get_random_game_score(winning_player)
        return final_score

    def get_random_game_score(self, winning_player):
        if winning_player == self.player_number:
            return 1
        elif winning_player == 0:
            return 0
        else:
            return -1

    def check_for_instant_win(self, board, player_move):
        new_board = CopiedBoard(board.get_current_state())
        new_board.change_the_board(player_move, self.player_number)
        if who_won.check_if_player_won(new_board, self.player_number):
            return True
        else:
            return False

    def make_a_move(self, board):
        scores = np.zeros(7)
        for possible_move in range(7):
            scores[possible_move] = self.score_a_board(board, possible_move)
        print(scores)
        return np.argmax(scores)
