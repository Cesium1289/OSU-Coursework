# HumanTicTacToeAgent
# A codified representation of a human tic tac toe game player.
# Encapsulates the prompting of a human to specify a move, and uses the player
# input as the agent action.

class HumanTicTacToeAgent:

    def __init__(self, game, symbol):
        self.game = game
        self.symbol = symbol

    def action(self, state):
        location = int(input(f"Specify the location of your ({self.symbol}) move (0 - 8): "))
        return location
