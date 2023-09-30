import pandas as pd
import numpy as np
import data_generator_functions as dgf
from mtc_game import connect_4_game_for_data_mining
from connect4.game_board import Board
from mtc_player import MTCPlayer

MTC_STRENGTH = 100
HOW_MANY_GAMES = 100
LOAD_DATA = True
first_time = False

# LOAD DATA
if LOAD_DATA:
    X_1, X_2, y_1, y_2 = dgf.load_game_data()
    dgf.print_dfs_details([X_1, X_2, y_1, y_2], ["X_1", "X_2", "y_1", "y_2"])

# CREATE OUR PLAYERS
first_mtc = MTCPlayer(1, MTC_STRENGTH)
second_mtc = MTCPlayer(2, MTC_STRENGTH)

for i in range(HOW_MANY_GAMES):
    print(f"game {i + 1} out of {HOW_MANY_GAMES}")
    clean_board = Board()
    X_player_1, X_player_2, y_player_1, y_player_2 = connect_4_game_for_data_mining(clean_board, first_mtc, second_mtc)
    data = [X_player_1, X_player_2, y_player_1, y_player_2]

    if first_time:  # CREATE OUR MAIN DATA FRAMES
        print("what")
        X_1, X_2, y_1, y_2 = dgf.convert_mtc_data_to_data_frames(data)
        first_time = False

    else:  # concat the new information into our data frame
        new_X_1, new_X_2, new_y_1, new_y_2 = dgf.convert_mtc_data_to_data_frames(data)
        current_dfs = [X_1, X_2, y_1, y_2]
        new_dfs = [new_X_1, new_X_2, new_y_1, new_y_2]
        X_1, X_2, y_1, y_2 = dgf.concat_data_to_our_data_frames(current_dfs, new_dfs)

        print(X_1.head())
        print(X_1.tail())

    dgf.print_dfs_details([X_1, X_2, y_1, y_2], ["X_1", "X_2", "y_1", "y_2"])

X_1.to_csv("X_1 data")
X_2.to_csv("X_2 data")
y_1.to_csv("y_1 data")
y_2.to_csv("y_2 data")
