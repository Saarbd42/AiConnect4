import who_won as ww  # Assuming the module name "WhoWon" is changed to "who_won"
import time


def visual_connect_4_game(board, first_player, second_player):
    print_pretty_board(board, first_player.player_number, second_player.player_number)
    while True:
        for player in [first_player, second_player]:
            possible_winner = make_a_move_and_check_for_victory(board, player)
            print_pretty_board(board, first_player.player_number, second_player.player_number)
            if possible_winner != 0:
                victory_announcement(possible_winner, first_player.player_number, second_player.player_number)
                return possible_winner

            if board.check_for_tie():
                victory_announcement(0, first_player.player_number, second_player.player_number)
                return 0


def no_visual_connect_4_game(board, first_player, second_player):
    player_list = [first_player, second_player]
    while True:
        for player in player_list:
            possible_winner = make_a_move_and_check_for_victory(board, player)
            if possible_winner != 0:
                # victory_announcement(possible_winner, first_player.player_number, second_player.player_number)
                return possible_winner

            if board.check_for_tie():
                # victory_announcement(0, first_player.player_number, second_player.player_number)
                return 0


def victory_announcement(winner, first_player_num, second_player_num):
    if winner != 0:
        if winner == first_player_num:
            print(make_string_blue(f"PLAYER {winner} WON!"))
        elif winner == second_player_num:
            print(make_string_red(f"PLAYER {winner} WON!"))
    else:
        print("TIE")
    input("Press anything to continue ")
    print("")


def make_a_move_and_check_for_victory(board, player):
    move = choose_a_move(board, player)
    board.change_the_board(move, player.player_number)
    if ww.check_if_player_won(board, player.player_number):
        return player.player_number
    return 0


def choose_a_move(board, player):
    legal_move = False
    while not legal_move:
        move = player.make_a_move(board)
        legal_move = full_legality_check(move, board)
    return move


def full_legality_check(player_move, board):
    if first_legality_check(player_move):
        return second_legality_test(player_move, board)
    else:
        return False


def first_legality_check(player_move):
    try:
        player_move = int(player_move)
    except:
        return False
    return True


def second_legality_test(player_move, board):
    if player_move < 0 or player_move > 6:
        return False
    elif board.board_current_state[0][player_move] != 0:
        return False
    else:
        return True


def basic_visuals(board):
    print("")
    print(board.get_current_state())


def print_pretty_board(board, first_player_num, second_player_num):
    current_board = board.get_current_state()
    pretty_board = make_pretty_board_string(current_board, first_player_num, second_player_num)
    print(pretty_board)


def make_pretty_board_string(current_board, first_player_num, second_player_num):
    DELIMITER = "|"
    pretty_board = ""
    for i in range(len(current_board)):
        pretty_board += "\n"
        pretty_board += DELIMITER
        for j in range(len(current_board[0])):
            current_position = int(current_board[i][j])
            pretty_board += draw_the_chip(current_position, first_player_num, second_player_num) + DELIMITER
    return pretty_board


def draw_the_chip(current_position, first_player_num, second_player_num):
    chip = ""
    if current_position == first_player_num:
        chip = make_string_blue("0")
    elif current_position == second_player_num:
        chip = make_string_red("0")
    else:
        chip = "0"
    return chip


def make_string_blue(string):
    return "\033[94m" + string + "\033[0m"


def make_string_red(string):
    return "\033[91m" + string + "\033[0m"

