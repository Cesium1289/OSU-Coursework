# DO NOT MODIFY THE CODE IN THE TESTS
# Run me via: python3 -m unittest test_minimax_tic_tac_toe_agent

import unittest
import time
from minimax_tic_tac_toe_agent import MinimaxTicTacToeAgent


class TestMinimaxTicTacToeAgent(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A MinimaxTicTacToeAgent exists.
        """
        try:
            MinimaxTicTacToeAgent(None, None)
        except NameError:
            self.fail("Could not instantiate MinimaxTicTacToeAgent")

    """
    Properties
    """

    def test_game(self):
        """
        A MinimaxTicTacToeAgent has a `game` property.
        """
        agent = MinimaxTicTacToeAgent("Fake Game", None)
        self.assertEqual("Fake Game", agent.game)

    def test_symbol(self):
        """
        A MinimaxTicTacToeAgent has a `symbol` property.
        """
        agent = MinimaxTicTacToeAgent(None, 'O')
        self.assertEqual('O', agent.symbol)

    """
    Agent Function
    """

    def test_action(self):
        """
        A MinimaxTicTacToeAgent has an agent function.
        """
        agent = MinimaxTicTacToeAgent(None, None)
        agent.action(('X', None, None, None, None, None, None, None, None))



def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
