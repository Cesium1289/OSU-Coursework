# DO NOT MODIFY THE CODE IN THE TESTS
# Run me via: python3 -m unittest test_human_tic_tac_toe_agent

import unittest
import time
from human_tic_tac_toe_agent import HumanTicTacToeAgent


class TestHumanTicTacToeAgent(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A HumanTicTacToeAgent exists.
        """
        try:
            HumanTicTacToeAgent(None, None)
        except NameError:
            self.fail("Could not instantiate HumanTicTacToeAgent")

    """
    Properties
    """

    def test_game(self):
        """
        A HumanTicTacToeAgent has a `game` property.
        """
        agent = HumanTicTacToeAgent("Fake Game", None)
        self.assertEqual("Fake Game", agent.game)

    def test_symbol(self):
        """
        A HumanTicTacToeAgent has a `symbol` property.
        """
        agent = HumanTicTacToeAgent(None, 'X')
        self.assertEqual('X', agent.symbol)

    """
    Agent Function
    """

    def test_action(self):
        """
        A HumanTicTacToeAgent has an agent method that returns a numeric board
        position representing the move or action.
        """
        agent = HumanTicTacToeAgent(None, None)
        print("TEST: input a 1")
        self.assertEqual(1, agent.action(None))


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
