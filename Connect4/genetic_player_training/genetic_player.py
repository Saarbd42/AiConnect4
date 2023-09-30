import random
import numpy as np
from connect4.game_board import Board


def is_move_legal(board, player_move):
    current_board = board.get_current_state()
    if current_board[0][player_move] == 0:
        return True
    else:
        return False


class GeneticPlayer:
    def __init__(self, player_number, parameters):
        self.player_number = player_number
        self.parameters = parameters

    def score_a_board(self, board, player_move):
        if is_move_legal(board, player_move):
            features = self.extract_features(board)
            return self.score_a_board_with_genetics(features)
        else:
            return -1000

    def score_a_board_with_genetics(self, features):
        final_score = 0
        for i in range(len(self.parameters)):
            final_score += features[i] * self.parameters[i]
        return final_score

    def make_a_move(self, board):
        scores = np.zeros(7)
        for possible_move in range(7):
            scores[possible_move] = self.score_a_board(board, possible_move)
        return np.argmax(scores)

    def extract_features(self, board):
        flatten_board = board.get_current_state()
        flatten_board = flatten_board.flatten()
        flatten_board = self.normalize_flatten_board(flatten_board)
        return flatten_board

    def normalize_flatten_board(self, flatten_board):
        for i in range(len(flatten_board)):
            if flatten_board[i] == self.player_number:
                flatten_board[i] = 1
            elif flatten_board[i] != 0:
                flatten_board[i] = -1
        return flatten_board
