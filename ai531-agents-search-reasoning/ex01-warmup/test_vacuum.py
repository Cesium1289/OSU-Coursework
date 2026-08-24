# DO NOT MODIFY THE CODE, OTHER THAN UNCOMMENTING THE NECESSARY TESTS
# Run me via: python3 -m unittest test_vacuum

import unittest
import time
from vacuum import Vacuum


class TestVacuum(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A Vacuum exists.
        """
        try:
            Vacuum()
        except NameError:
            self.fail("Could not instantiate Vacuum")

    """
    Methods
    """

    def test_move_left(self):
        """
        A Vacuum can be told to move left.
        """
        vacuum = Vacuum()
        vacuum.move_left()

    def test_move_right(self):
        """
        A Vacuum can be told to move right.
        """
        vacuum = Vacuum()
        vacuum.move_right()

    def test_sense_is_dirty(self):
        """
        A Vacuum can sense if its location is dirty.
        """
        vacuum = Vacuum()
        vacuum.is_dirty(fake_location())

    def test_sense_clean(self):
        """
        A Vacuum can clean a location.
        """
        vacuum = Vacuum()
        vacuum.clean(fake_location())

    def test_action(self):
        """
        A Vacuum can produce the best action it should take, given what it
        senses in its location.
        """
        vacuum = Vacuum()
        action = vacuum.action(fake_location())


def fake_location():
    return object()

def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
