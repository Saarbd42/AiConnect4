from connect4.connect_4_game import choose_a_move
from connect4 import who_won as ww
from connect4.game_board import CopiedBoard


def connect_4_game_for_data_mining(board, first_player, second_player):
    player_list = [first_player, second_player]
    X_data = []
    y_data = []
    player_num_data = []
    while True:
        for player in player_list:
            print(f"player {player} moves")
            # GET DATA
            move = choose_a_move(board, player)
            copy_of_the_board = CopiedBoard(board)

            # COLLECT DATA
            X_data.append(copy_of_the_board)
            y_data.append(move)
            player_num_data.append(player.player_number)

            # PLAY THE GAME
            board.change_the_board(move, player.player_number)
            possible_winner = check_for_victory(board, player)

            # CHECK IF THE GAME ENDS
            if possible_winner != 0:
                return X_data, y_data, player_num_data

            if board.check_for_tie():
                return X_data, y_data, player_num_data


def check_for_victory(board, player):
    if ww.check_if_player_won(board, player.player_number):
        return player.player_number
    return 0
