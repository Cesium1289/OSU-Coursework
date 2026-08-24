# DO NOT MODIFY THE CODE IN THE TESTS
# Run me via: python3 -m unittest test_tic_tac_toe_board_renderer

import unittest
import time
from tic_tac_toe_board_renderer import TicTacToeBoardRenderer


class TestTicTacToeBoardRenderer(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A TicTacToeBoardRenderer exists.
        """
        try:
            TicTacToeBoardRenderer()
        except NameError:
            self.fail("Could not instantiate TicTacToeBoardRenderer")

    """
    render
    """

    def test_render_empty(self):
        """
        Returns a string representing an empty board.
        """
        state = (None, None, None, None, None, None, None, None, None)
        renderer = TicTacToeBoardRenderer()
        self.assertEqual("  |   |  \n  |   |  \n  |   |  \n", renderer.render(state))

    def test_render_full(self):
        """
        Returns a string representing an full board.
        """
        state = ('X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X')
        renderer = TicTacToeBoardRenderer()
        self.assertEqual("X | O | X\nO | X | O\nX | O | X\n", renderer.render(state))

    """
    render_location
    """

    def test_render_location_none(self):
        """
        Returns a space when the value is None.
        """
        renderer = TicTacToeBoardRenderer()
        self.assertEqual(" ", renderer.render_location(None))

    def test_render_location_x(self):
        """
        Returns an 'X' when the value is 'X'.
        """
        renderer = TicTacToeBoardRenderer()
        self.assertEqual("X", renderer.render_location("X"))

    def test_render_location_o(self):
        """
        Returns an 'O' when the value is 'O'.
        """
        renderer = TicTacToeBoardRenderer()
        self.assertEqual("O", renderer.render_location("O"))


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
