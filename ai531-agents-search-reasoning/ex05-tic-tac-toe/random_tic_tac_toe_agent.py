# RandomTicTacToeAgent
# A game-playing tic tac toe agent that selects a random board position for its
# move.

import random

class RandomTicTacToeAgent:

    def __init__(self, game, symbol):
        self.game = game
        self.symbol = symbol

    def action(self, state):
        print("My turn!")
        valid_moves = [i for i in range(len(state)) if state[i] == None]
        if bool(valid_moves):
            return random.choice(valid_moves)
        else:
            return None
