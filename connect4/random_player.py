import random


class RandomPlayer:
    def __init__(self, player_number):
        self.player_number = player_number

    def make_a_move(self, board):
        legal_moves = self.check_legal_moves(board)
        player_move = random.choice(legal_moves)
        return player_move

    def check_legal_moves(self, board):
        legal_moves = []
        current_board = board.get_current_state()
        for i in range(7):
            if current_board[0][i] == 0:
                legal_moves.append(i)
        return legal_moves
