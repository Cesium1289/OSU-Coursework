# DO NOT MODIFY THIS FILE
# Run me via: python3 -m unittest test_state

import unittest
import time
from state import State


class TestState(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A State exists.
        """
        try:
            State(None, None)
        except NameError:
            self.fail("Could not instantiate State")

    """
    Attributes
    """

    def test_locations(self):
        """
        A State has locations.
        """
        state = State('Fake Locations', 'Fake Location Id')
        self.assertEqual('Fake Locations', state.locations)

    def test_current_location_id(self):
        """
        A State has a current location id.
        """
        state = State('Fake Locations', 'Fake Location Id')
        self.assertEqual('Fake Location Id', state.current_location_id)

    """
    Methods
    """

    def test_current_location(self):
        """
        The current location is a Location whose id matches current_location_id
        """
        state = State({'A': 'Fake Location A', 'B': 'Fake Location B'}, 'A')
        self.assertEqual('Fake Location A', state.current_location())


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
