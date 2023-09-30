import pandas as pd


def print_dfs_details(data, names):
    for i in range(len(data)):
        print(f"{names[i]} shape {data[i].shape}")


def load_game_data():
    X_1 = pd.read_csv("X_1 data", index_col=[0])
    X_2 = pd.read_csv("X_2 data", index_col=[0])
    y_1 = pd.read_csv("y_1 data", index_col=[0])
    y_2 = pd.read_csv("y_2 data", index_col=[0])
    return X_1, X_2, y_1, y_2


def concat_data_to_our_data_frames(current_dfs, new_dfs):
    for i in range(len(current_dfs)):
        current_dfs[i].reset_index(drop=True)
        new_dfs[i].reset_index(drop=True)
    X_df_player_1 = pd.concat([current_dfs[0], new_dfs[0]], ignore_index=True)
    X_df_player_2 = pd.concat([current_dfs[1], new_dfs[1]], ignore_index=True)
    y_df_player_1 = pd.concat([current_dfs[2], new_dfs[2]], ignore_index=True)
    y_df_player_2 = pd.concat([current_dfs[3], new_dfs[3]], ignore_index=True)
    return X_df_player_1, X_df_player_2, y_df_player_1, y_df_player_2


def convert_mtc_data_to_data_frames(data):
    X_df_player_1 = pd.DataFrame(data[0])
    X_df_player_2 = pd.DataFrame(data[1])
    y_df_player_1 = pd.DataFrame(data[2], columns=["MTC_Choice"])
    y_df_player_2 = pd.DataFrame(data[3], columns=["MTC_Choice"])
    return X_df_player_1, X_df_player_2, y_df_player_1, y_df_player_2
