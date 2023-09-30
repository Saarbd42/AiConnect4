from connect4 import game_types
from connect4.genetic_player_training.genetic_player import is_move_legal
import numpy as np
from connect4.game_board import CopiedBoard


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
        final_score = 0
        for i in range(self.mtc_num):
            # MAKE THE MOVE
            new_board = CopiedBoard(board.get_current_state())
            new_board.change_the_board(player_move, self.player_number)
            # CHECK HOW IT TURNS UP FOR YOU
            winning_player = game_types.random_vs_random_game(new_board)
            if winning_player == self.player_number:
                final_score += 1
            elif winning_player == 0:
                final_score = final_score
            else:
                final_score -= 1
        return final_score

    def make_a_move(self, board):
        scores = np.zeros(7)
        for possible_move in range(7):
            scores[possible_move] = self.score_a_board(board, possible_move)
        print(scores)
        return np.argmax(scores)
