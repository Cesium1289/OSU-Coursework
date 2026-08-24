# DO NOT MODIFY THIS FILE
# Run me via: python3 -m unittest test_location

import unittest
import time
from location import Location


class TestLocation(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A Location exists.
        """
        try:
            Location('Fake')
        except NameError:
            self.fail("Could not instantiate Location")

    """
    Attributes
    """

    def test_id(self):
        """
        A Location has an id.
        """
        location = Location('Fake')
        self.assertEqual('Fake', location.id)

    def test_dirt(self):
        """
        A Location has a dirt attribute.
        """
        location = Location('Fake', True)
        self.assertTrue(location.dirt)

    """
    Methods
    """

    def test_apply_suction(self):
        """
        Applying suction to a dirty environment makes it clean.
        """
        location = Location('Fake', True)
        location.apply_suction()
        self.assertIsNone(location.dirt)


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
