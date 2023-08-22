import gameBoard as gb
import humanPlayer as hp
import Connect4Game as Connect4Game
import RandomPlayer as rp
import time

def humanVsHumanGame():
    board = gb.Board()
    firstPlayer = hp.HumanPlayer(1)
    secondPlayer = hp.HumanPlayer(2)
    winner = Connect4Game.visualConnect4Game(board, firstPlayer, secondPlayer)
    victoryAnnouncement(winner)


def humanVsRandomGame(humanTurn):
    board = gb.Board()
    firstPlayer, secondPlayer = humanVsRandomTurns(humanTurn)
    winner = Connect4Game.visualConnect4Game(board, firstPlayer, secondPlayer)
    victoryAnnouncement(winner)


def victoryAnnouncement(winner):
    print("")
    if winner != 0:
        print(f"PLAYER {winner} WON!")
    else:
        print("TIE")
    print("")
    time.sleep(1)


def humanVsRandomTurns(humanTurn):
    if humanTurn == 1:
        return hp.HumanPlayer(1), rp.RandomPlayer(2)
    if humanTurn == 2:
        return rp.RandomPlayer(1), hp.HumanPlayer(2)
