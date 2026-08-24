# Tic Tac Toe Agent Scratchpad
# Use this as a "scratchpad" to tinker with your code.
# There are no rules here, and this code will not be evaluated. This file is a
# place for you to experiment.


from tic_tac_toe_game import TicTacToeGame
from tic_tac_toe_board_renderer import TicTacToeBoardRenderer
from random_tic_tac_toe_agent import RandomTicTacToeAgent
from human_tic_tac_toe_agent import HumanTicTacToeAgent


renderer = TicTacToeBoardRenderer()
game = TicTacToeGame((None, None, None, None, None, None, None, None, None), renderer)
human_agent = HumanTicTacToeAgent(game, TicTacToeGame.P1_SYMBOL)
ai_agent = RandomTicTacToeAgent(game, TicTacToeGame.P2_SYMBOL)

print(f"Let's play tic-tac-toe! You are {human_agent.symbol} and I am {ai_agent.symbol}.\n")
print("0 | 1 | 2\n3 | 4 | 5\n6 | 7 | 8\n")

while game.is_not_over():
    print("----------------------------------------------")
    game.state = game.result(game.state, human_agent.action(game.state))
    print(game)
    if game.is_win(game.state, human_agent.symbol):
        print('You win!')
        break
    game.state = game.result(game.state, ai_agent.action(game.state))
    print(game)
    if game.is_win(game.state, ai_agent.symbol):
        print('I win!')
        break

print("Game Over")
