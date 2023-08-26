import gameBoard as gb
import humanPlayer as hp
import Connect4Game as Connect4Game
import RandomPlayer as rp
import MinMaxPlayer as mmp
import time


def humanVsHumanGame():
    board = gb.Board()
    firstPlayer = hp.HumanPlayer(1)
    secondPlayer = hp.HumanPlayer(2)
    winner = Connect4Game.visualConnect4Game(board, firstPlayer, secondPlayer)
    return winner

def humanVsRandomGame(humanTurn):
    board = gb.Board()
    firstPlayer, secondPlayer = humanVsRandomTurns(humanTurn)
    winner = Connect4Game.visualConnect4Game(board, firstPlayer, secondPlayer)
    return winner

def humanVsMinMax(humanTurn, AiForesight):
    board = gb.Board()
    firstPlayer, secondPlayer = humanVsMinMaxTurns(humanTurn, AiForesight)
    winner = Connect4Game.visualConnect4Game(board, firstPlayer, secondPlayer)
    return winner


def humanVsRandomTurns(humanTurn):
    if humanTurn == 1:
        return hp.HumanPlayer(1), rp.RandomPlayer(2)
    if humanTurn == 2:
        return rp.RandomPlayer(1), hp.HumanPlayer(2)


def humanVsMinMaxTurns(humanTurn, AiForesight):
    if humanTurn == 1:
        return hp.HumanPlayer(1), mmp.MinMaxPlayer(2, 1, AiForesight)
    if humanTurn == 2:
        return mmp.MinMaxPlayer(1, 2, AiForesight), hp.HumanPlayer(2)
