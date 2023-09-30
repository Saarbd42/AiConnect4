def check_if_player_won(board, player_num):
    if check_rows(board, player_num) or check_columns(board, player_num) or check_diagonals(board, player_num):
        return True
    else:
        return False


def check_diagonals(board, player_num):
    current_board = board.get_current_state()
    if check_downward_diagonals(current_board, player_num) or check_upward_diagonals(current_board, player_num):
        return True
    return False


def check_columns(board, player_num):
    current_board = board.get_current_state()
    for column_num in range(len(current_board[0])):
        if check_specific_column(current_board, player_num, column_num):
            return True
    return False


def check_rows(board, player_num):
    current_board = board.get_current_state()
    for row_num in range(len(current_board)):
        if check_specific_row(current_board, player_num, row_num):
            return True
    return False


def check_downward_diagonals(current_board, player_num):
    for row_num in range(3):
        for j in range(4):
            count = 0
            for i in range(4):
                if current_board[i + row_num][i + j] == player_num:
                    count += 1
            if count >= 4:
                return True
    return False


def check_upward_diagonals(current_board, player_num):
    for row_num in range(3):
        for j in range(4):
            count = 0
            for i in range(4):
                if current_board[5 - (i + row_num)][i + j] == player_num:
                    count += 1
            if count >= 4:
                return True
    return False


def check_specific_column(current_board, player_num, column_num):
    if current_board[2][column_num] == player_num and current_board[3][column_num] == player_num:
        return check_column_continuity_sum(current_board, player_num, column_num)
    else:
        return False


def check_column_continuity_sum(current_board, player_num, column_num):
    up_continuity = check_continuity(
        [current_board[4][column_num], current_board[5][column_num]],
        player_num)
    down_continuity = check_continuity(
        [current_board[1][column_num], current_board[0][column_num]],
        player_num)
    return check_if_sum_bigger_than_one(up_continuity, down_continuity)


def check_if_sum_bigger_than_one(num1, num2):
    sum_the_sides = num1 + num2
    if sum_the_sides >= 2:
        return True
    else:
        return False


def check_specific_row(current_board, player_num, row_num):
    if current_board[row_num][3] == player_num:
        return check_row_continuity_sum(current_board, player_num, row_num)
    else:
        return False


def check_row_continuity_sum(current_board, player_num, row_num):
    left_side_continuity = check_continuity(
        [current_board[row_num][2], current_board[row_num][1], current_board[row_num][0]],
        player_num)
    right_side_continuity = check_continuity(
        [current_board[row_num][4], current_board[row_num][5], current_board[row_num][6]],
        player_num)
    return check_if_sum_bigger_than_two(left_side_continuity, right_side_continuity)


def check_if_sum_bigger_than_two(num1, num2):
    sum_the_sides = num1 + num2
    if sum_the_sides >= 3:
        return True
    else:
        return False


def check_continuity(spots, player_num):
    count = 0
    for i in range(len(spots)):
        if spots[i] == player_num:
            count += 1
        else:
            break
    return count
