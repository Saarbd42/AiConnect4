import gameBoard as gb
import humanPlayer as hp
import Connect4Game as Connect4Game


def humanVsHumanGame():
    board = gb.Board()
    firstPlayer = hp.HumanPlayer(1)
    secondPlayer = hp.HumanPlayer(2)
    winner = Connect4Game.visualConnect4Game(board, firstPlayer, secondPlayer)
    if winner != 0:
        print(f"Player {winner} Won!")
    else:
        print("Tie")