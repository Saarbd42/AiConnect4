from connect4 import game_board as gb
from connect4 import human_player as hp
from connect4 import connect_4_game as connect_4_game
from connect4 import random_player as rp
from connect4 import min_max_player as mmp
from connect4.genetic_player_training import mtc_player as mtc
import time


def human_vs_mtc_game(human_turn, mtc_num):
    board = gb.Board()
    first_player, second_player = human_vs_mtc_turns(human_turn, mtc_num)
    winner = connect_4_game.visual_connect_4_game(board, first_player, second_player)
    return winner


def mtc_vs_mtc_game(board, mtc_num):
    first_player = mtc.MTCPlayer(1, mtc_num)
    second_player = mtc.MTCPlayer(2, mtc_num)
    winner = connect_4_game.no_visual_connect_4_game(board, first_player, second_player)
    return winner


def random_vs_random_game(board, mtc_played_first=False):
    if mtc_played_first:
        first_player = rp.RandomPlayer(2)
        second_player = rp.RandomPlayer(1)
    else:
        first_player = rp.RandomPlayer(1)
        second_player = rp.RandomPlayer(2)
    winner = connect_4_game.no_visual_connect_4_game(board, first_player, second_player)
    return winner


def human_vs_human_game():
    board = gb.Board()
    first_player = hp.HumanPlayer(1)
    second_player = hp.HumanPlayer(2)
    winner = connect_4_game.visual_connect_4_game(board, first_player, second_player)
    return winner


def human_vs_random_game(human_turn):
    board = gb.Board()
    first_player, second_player = human_vs_random_turns(human_turn)
    winner = connect_4_game.visual_connect_4_game(board, first_player, second_player)
    return winner


def human_vs_min_max(human_turn, ai_foresight):
    board = gb.Board()
    first_player, second_player = human_vs_min_max_turns(human_turn, ai_foresight)
    winner = connect_4_game.visual_connect_4_game(board, first_player, second_player)
    return winner


def human_vs_random_turns(human_turn):
    if human_turn == 1:
        return hp.HumanPlayer(1), rp.RandomPlayer(2)
    if human_turn == 2:
        return rp.RandomPlayer(1), hp.HumanPlayer(2)


def human_vs_min_max_turns(human_turn, ai_foresight):
    if human_turn == 1:
        return hp.HumanPlayer(1), mmp.MinMaxPlayer(2, 1, ai_foresight)
    if human_turn == 2:
        return mmp.MinMaxPlayer(1, 2, ai_foresight), hp.HumanPlayer(2)


def human_vs_mtc_turns(human_turn, mtc_num):
    if human_turn == 1:
        return hp.HumanPlayer(1), mtc.MTCPlayer(2, mtc_num)
    if human_turn == 2:
        return mtc.MTCPlayer(1, mtc_num), hp.HumanPlayer(2)
