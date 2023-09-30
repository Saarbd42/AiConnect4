class HumanPlayer:
    def __init__(self, player_number):
        self.player_number = player_number

    def make_a_move(self, board):
        player_move = input(f"Player {self.player_number}: ")
        if self.check_if_legal_move(player_move, board):
            return self.format_player_move(player_move)
        else:
            print("Error")
            return -1  # Signals error

    def check_if_legal_move(self, player_move, board):
        if self.first_legality_test(player_move):
            player_move = self.format_player_move(player_move)
            return self.second_legality_test(player_move, board)
        else:
            return False

    def first_legality_test(self, player_move):
        try:
            player_move = int(player_move)
        except:
            return False
        return True

    def format_player_move(self, player_move):
        player_move = int(player_move)
        player_move -= 1  # Format
        return player_move

    def second_legality_test(self, player_move, board):
        if player_move < 0 or player_move > 6:
            return False
        elif board.board_current_state[0][player_move] != 0:
            return False
        else:
            return True
