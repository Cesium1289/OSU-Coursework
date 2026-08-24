# DO NOT MODIFY THIS FILE
# Run me via: python3 -m unittest test_movement_model

import unittest
import time
from movement_model import MovementModel


class TestMovementModel(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A MovementModel exists.
        """
        try:
            MovementModel(None, None)
        except NameError:
            self.fail("Could not instantiate MovementModel")

    """
    Attributes
    """

    def test_left(self):
        """
        A MovementModel has a right.
        """
        movement_model = MovementModel('L', 'R')
        self.assertEqual('L', movement_model.left)

    def test_right(self):
        """
        A MovementModel has a left.
        """
        movement_model = MovementModel('L', 'R')
        self.assertEqual('R', movement_model.right)


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
