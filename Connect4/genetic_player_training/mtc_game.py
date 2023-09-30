from connect4.connect_4_game import choose_a_move
from connect4 import who_won as ww
from connect4.game_board import CopiedBoard


def connect_4_game_for_data_mining(board, first_player, second_player):
    player_list = [first_player, second_player]
    X_data_player_1 = []
    X_data_player_2 = []
    y_data_player_1 = []
    y_data_player_2 = []
    while True:
        for player in player_list:
            # print(f"player {player.player_number} turn")
            # GET DATA
            move = choose_a_move(board, player)
            copy_of_the_board = CopiedBoard(board.get_current_state())
            copy_of_the_board_current_state = copy_of_the_board.get_current_state()
            copy_of_the_board_current_state = copy_of_the_board_current_state.flatten()

            # COLLECT DATA
            if player == first_player:
                X_data_player_1.append(copy_of_the_board_current_state)
                y_data_player_1.append(move)
            else:
                X_data_player_2.append(copy_of_the_board_current_state)
                y_data_player_2.append(move)

            # PLAY THE GAME
            board.change_the_board(move, player.player_number)
            possible_winner = check_for_victory(board, player)

            # CHECK IF THE GAME ENDS
            if possible_winner != 0 or board.check_for_tie():
                print(f"player {possible_winner} won")
                # print(f"Tie = {board.check_for_tie()}")
                return X_data_player_1, X_data_player_2, y_data_player_1, y_data_player_2


def check_for_victory(board, player):
    if ww.check_if_player_won(board, player.player_number):
        return player.player_number
    return 0
