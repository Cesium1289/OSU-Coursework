# DO NOT MODIFY THE CODE IN THE TESTS
# Run me via: python3 -m unittest test_eight_puzzle_node

import unittest
import time
from eight_puzzle_node import EightPuzzleNode


class TestEightPuzzleNode(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A EightPuzzleNode exists.
        """
        try:
            EightPuzzleNode(None, None, None, None)
        except NameError:
            self.fail("Could not instantiate EightPuzzleNode")

    """
    Properties
    """

    def test_state(self):
        """
        An EightPuzzleNode has a `state` property.
        """
        node = EightPuzzleNode("Fake State", None, None, None)
        self.assertEqual("Fake State", node.state)

    def test_parent(self):
        """
        An EightPuzzleNode has a `parent` property.
        """
        node = EightPuzzleNode(None, "Fake Parent Node", None, None)
        self.assertEqual("Fake Parent Node", node.parent)

    def test_action(self):
        """
        An EightPuzzleNode has a `action` property.
        """
        node = EightPuzzleNode(None, None, "Fake Action", None)
        self.assertEqual("Fake Action", node.action)

    def test_path_cost(self):
        """
        An EightPuzzleNode has a `path_cost` property.
        """
        node = EightPuzzleNode(None, None, None, "Fake Path Cost")
        self.assertEqual("Fake Path Cost", node.path_cost)

    """
    Behaviors
    """

    def test_less_than_more_expensive(self):
        """
        An EightPuzzleNode with a path_cost less than another is considered to
        be "less than" another EightPuzzleNode.
        """
        less_expensive_node = EightPuzzleNode(None, None, None, 1)
        more_expensive_node = EightPuzzleNode(None, None, None, 2)
        self.assertTrue(less_expensive_node < more_expensive_node)

    def test_less_than_less_espensive(self):
        """
        An EightPuzzleNode with a path_cost more than another is considered to
        not be "less than" another EightPuzzleNode.
        """
        less_expensive_node = EightPuzzleNode(None, None, None, 1)
        more_expensive_node = EightPuzzleNode(None, None, None, 2)
        self.assertFalse(more_expensive_node < less_expensive_node)


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
