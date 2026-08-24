# DO NOT MODIFY THE CODE IN THE TESTS
# Run me via: python3 -m unittest test_random_tic_tac_toe_agent

import unittest
import time
from random_tic_tac_toe_agent import RandomTicTacToeAgent


class TestRandomTicTacToeAgent(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A RandomTicTacToeAgent exists.
        """
        try:
            RandomTicTacToeAgent(None, None)
        except NameError:
            self.fail("Could not instantiate RandomTicTacToeAgent")

    """
    Properties
    """

    def test_game(self):
        """
        A RandomTicTacToeAgent has a `game` property.
        """
        agent = RandomTicTacToeAgent("Fake Game", None)
        self.assertEqual("Fake Game", agent.game)

    def test_symbol(self):
        """
        A RandomTicTacToeAgent has a `symbol` property.
        """
        agent = RandomTicTacToeAgent(None, 'O')
        self.assertEqual('O', agent.symbol)

    """
    Agent Function
    """

    def test_action_none(self):
        """
        A RandomTicTacToeAgent returns the only available move when only one
        possible move exists.
        """
        agent = RandomTicTacToeAgent(None, None)
        self.assertEqual(None, agent.action(('X', 'O')))

    def test_action_one(self):
        """
        A RandomTicTacToeAgent returns the only available move when only one
        possible move exists.
        """
        agent = RandomTicTacToeAgent(None, None)
        self.assertEqual(0, agent.action((None, 'X')))
        self.assertEqual(1, agent.action(('X', None)))

    def test_action_random(self):
        """
        A RandomTicTacToeAgent returns any available move at random when more
        than one possible possible move exists.
        """
        agent = RandomTicTacToeAgent(None, None)
        pass # Don't test random things.


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
