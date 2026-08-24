# DO NOT MODIFY THE CODE IN THE TESTS
# Run me via: python3 -m unittest test_eight_puzzle_transition_model

import unittest
import time
from eight_puzzle_transition_model import EightPuzzleTransitionModel
from eight_puzzle_transition_model import EightPuzzleTransitionException

class TestEightPuzzleTransitionModel(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A EightPuzzleTransitionModel exists.
        """
        try:
            EightPuzzleTransitionModel()
        except NameError:
            self.fail("Could not instantiate EightPuzzleTransitionModel")

    """
    can_move_left
    """

    def test_can_move_left_false(self):
        transition_model = EightPuzzleTransitionModel()
        self.assertFalse(transition_model.can_move_left((None, 0, 0, 0, 0, 0, 0, 0, 0)))
        self.assertFalse(transition_model.can_move_left((0, 0, 0, None, 0, 0, 0, 0, 0)))
        self.assertFalse(transition_model.can_move_left((0, 0, 0, 0, 0, 0, None, 0, 0)))

    def test_can_move_left_true(self):
        transition_model = EightPuzzleTransitionModel()
        self.assertTrue(transition_model.can_move_left((0, None, 0, 0, 0, 0, 0, 0, 0)))
        self.assertTrue(transition_model.can_move_left((0, 0, None, 0, 0, 0, 0, 0, 0)))
        self.assertTrue(transition_model.can_move_left((0, 0, 0, 0, None, 0, 0, 0, 0)))
        self.assertTrue(transition_model.can_move_left((0, 0, 0, 0, 0, None, 0, 0, 0)))
        self.assertTrue(transition_model.can_move_left((0, 0, 0, 0, 0, 0, 0, None, 0)))
        self.assertTrue(transition_model.can_move_left((0, 0, 0, 0, 0, 0, 0, 0, None)))

    """
    can_move_right
    """

    def test_can_move_right_false(self):
        transition_model = EightPuzzleTransitionModel()
        self.assertFalse(transition_model.can_move_right((0, 0, None, 0, 0, 0, 0, 0, 0)))
        self.assertFalse(transition_model.can_move_right((0, 0, 0, 0, 0, None, 0, 0, 0)))
        self.assertFalse(transition_model.can_move_right((0, 0, 0, 0, 0, 0, 0, 0, None)))

    def test_can_move_right_true(self):
        transition_model = EightPuzzleTransitionModel()
        self.assertTrue(transition_model.can_move_right((None, 0, 0, 0, 0, 0, 0, 0, 0)))
        self.assertTrue(transition_model.can_move_right((0, None, 0, 0, 0, 0, 0, 0, 0)))
        self.assertTrue(transition_model.can_move_right((0, 0, 0, None, 0, 0, 0, 0, 0)))
        self.assertTrue(transition_model.can_move_right((0, 0, 0, 0, None, 0, 0, 0, 0)))
        self.assertTrue(transition_model.can_move_right((0, 0, 0, 0, 0, 0, None, 0, 0)))
        self.assertTrue(transition_model.can_move_right((0, 0, 0, 0, 0, 0, 0, None, 0)))

    """
    can_move_up
    """

    def test_can_move_up_false(self):
        transition_model = EightPuzzleTransitionModel()
        self.assertFalse(transition_model.can_move_up((None, 0, 0, 0, 0, 0, 0, 0, 0)))
        self.assertFalse(transition_model.can_move_up((0, None, 0, 0, 0, 0, 0, 0, 0)))
        self.assertFalse(transition_model.can_move_up((0, 0, None, 0, 0, 0, 0, 0, 0)))

    def test_can_move_up_true(self):
        transition_model = EightPuzzleTransitionModel()
        self.assertTrue(transition_model.can_move_up((0, 0, 0, None, 0, 0, 0, 0, 0)))
        self.assertTrue(transition_model.can_move_up((0, 0, 0, 0, None, 0, 0, 0, 0)))
        self.assertTrue(transition_model.can_move_up((0, 0, 0, 0, 0, None, 0, 0, 0)))
        self.assertTrue(transition_model.can_move_up((0, 0, 0, 0, 0, 0, None, 0, 0)))
        self.assertTrue(transition_model.can_move_up((0, 0, 0, 0, 0, 0, 0, None, 0)))
        self.assertTrue(transition_model.can_move_up((0, 0, 0, 0, 0, 0, 0, 0, None)))

    """
    can_move_down
    """

    def test_can_move_down_false(self):
        transition_model = EightPuzzleTransitionModel()
        self.assertFalse(transition_model.can_move_down((0, 0, 0, 0, 0, 0, None, 0, 0)))
        self.assertFalse(transition_model.can_move_down((0, 0, 0, 0, 0, 0, 0, None, 0)))
        self.assertFalse(transition_model.can_move_down((0, 0, 0, 0, 0, 0, 0, 0, None)))

    def test_can_move_down_true(self):
        transition_model = EightPuzzleTransitionModel()
        self.assertTrue(transition_model.can_move_down((None, 0, 0, 0, 0, 0, 0, 0, 0)))
        self.assertTrue(transition_model.can_move_down((0, None, 0, 0, 0, 0, 0, 0, 0)))
        self.assertTrue(transition_model.can_move_down((0, 0, None, 0, 0, 0, 0, 0, 0)))
        self.assertTrue(transition_model.can_move_down((0, 0, 0, None, 0, 0, 0, 0, 0)))
        self.assertTrue(transition_model.can_move_down((0, 0, 0, 0, None, 0, 0, 0, 0)))
        self.assertTrue(transition_model.can_move_down((0, 0, 0, 0, 0, None, 0, 0, 0)))

    """
    move_left
    """

    def test_move_left_invalid_for_positions_0_3_6(self):
        transition_model = EightPuzzleTransitionModel()
        with self.assertRaises(EightPuzzleTransitionException):
            state = (None, 0, 0, 0, 0, 0, 0, 0, 0)
            transition_model.move_left(state)
        with self.assertRaises(EightPuzzleTransitionException):
            state = (0, 0, 0, None, 0, 0, 0, 0, 0)
            transition_model.move_left(state)
        with self.assertRaises(EightPuzzleTransitionException):
            state = (0, 0, 0, 0, 0, 0, None, 0, 0)
            transition_model.move_left(state)

    def test_move_left_1(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, None, 2, 3, 4, 5, 6, 7, 8)
        expected = (None, 1, 2, 3, 4, 5, 6, 7, 8)
        self.assertEqual(expected, transition_model.move_left(state))

    def test_move_left_2(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, 2, None, 3, 4, 5, 6, 7, 8)
        expected = (1, None, 2, 3, 4, 5, 6, 7, 8)
        self.assertEqual(expected, transition_model.move_left(state))

    def test_move_left_4(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, 2, 3, 4, None, 5, 6, 7, 8)
        expected = (1, 2, 3, None, 4, 5, 6, 7, 8)
        self.assertEqual(expected, transition_model.move_left(state))

    def test_move_left_5(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, 2, 3, 4, 5, None, 6, 7, 8)
        expected = (1, 2, 3, 4, None, 5, 6, 7, 8)
        self.assertEqual(expected, transition_model.move_left(state))

    def test_move_left_7(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, 2, 3, 4, 5, 6, 7, None, 8)
        expected = (1, 2, 3, 4, 5, 6, None, 7, 8)
        self.assertEqual(expected, transition_model.move_left(state))

    def test_move_left_8(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, 2, 3, 4, 5, 6, 7, 8, None)
        expected = (1, 2, 3, 4, 5, 6, 7, None, 8)
        self.assertEqual(expected, transition_model.move_left(state))

    """
    move_right
    """

    def test_move_right_invalid_for_positions_2_5_8(self):
        transition_model = EightPuzzleTransitionModel()
        with self.assertRaises(EightPuzzleTransitionException):
            state = (0, 0, None, 0, 0, 0, 0, 0, 0)
            transition_model.move_right(state)
        with self.assertRaises(EightPuzzleTransitionException):
            state = (0, 0, 0, 0, 0, None, 0, 0, 0)
            transition_model.move_right(state)
        with self.assertRaises(EightPuzzleTransitionException):
            state = (0, 0, 0, 0, 0, 0, 0, 0, None)
            transition_model.move_right(state)

    def test_move_right_0(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (None, 1, 2, 3, 4, 5, 6, 7, 8)
        expected = (1, None, 2, 3, 4, 5, 6, 7, 8)
        self.assertEqual(expected, transition_model.move_right(state))

    def test_move_right_1(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, None, 2, 3, 4, 5, 6, 7, 8)
        expected = (1, 2, None, 3, 4, 5, 6, 7, 8)
        self.assertEqual(expected, transition_model.move_right(state))

    def test_move_right_3(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, 2, 3, None, 4, 5, 6, 7, 8)
        expected = (1, 2, 3, 4, None, 5, 6, 7, 8)
        self.assertEqual(expected, transition_model.move_right(state))

    def test_move_right_4(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, 2, 3, 4, None, 5, 6, 7, 8)
        expected = (1, 2, 3, 4, 5, None, 6, 7, 8)
        self.assertEqual(expected, transition_model.move_right(state))

    def test_move_right_6(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, 2, 3, 4, 5, 6, None, 7, 8)
        expected = (1, 2, 3, 4, 5, 6, 7, None, 8)
        self.assertEqual(expected, transition_model.move_right(state))

    def test_move_right_7(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, 2, 3, 4, 5, 6, 7, None, 8)
        expected = (1, 2, 3, 4, 5, 6, 7, 8, None)
        self.assertEqual(expected, transition_model.move_right(state))

    """
    move_up
    """

    def test_move_up_invalid_for_positions_0_1_2(self):
        transition_model = EightPuzzleTransitionModel()
        with self.assertRaises(EightPuzzleTransitionException):
            state = (None, 0, 0, 0, 0, 0, 0, 0, 0)
            transition_model.move_up(state)
        with self.assertRaises(EightPuzzleTransitionException):
            state = (0, None, 0, 0, 0, 0, 0, 0, 0)
            transition_model.move_up(state)
        with self.assertRaises(EightPuzzleTransitionException):
            state = (0, 0, None, 0, 0, 0, 0, 0, 0)
            transition_model.move_up(state)

    def test_move_up_3(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, 2, 3, None, 4, 5, 6, 7, 8)
        expected = (None, 2, 3, 1, 4, 5, 6, 7, 8)
        self.assertEqual(expected, transition_model.move_up(state))

    def test_move_up_4(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, 2, 3, 4, None, 5, 6, 7, 8)
        expected = (1, None, 3, 4, 2, 5, 6, 7, 8)
        self.assertEqual(expected, transition_model.move_up(state))

    def test_move_up_5(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, 2, 3, 4, 5, None, 6, 7, 8)
        expected = (1, 2, None, 4, 5, 3, 6, 7, 8)
        self.assertEqual(expected, transition_model.move_up(state))

    def test_move_up_6(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, 2, 3, 4, 5, 6, None, 7, 8)
        expected = (1, 2, 3, None, 5, 6, 4, 7, 8)
        self.assertEqual(expected, transition_model.move_up(state))

    def test_move_up_7(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, 2, 3, 4, 5, 6, 7, None, 8)
        expected = (1, 2, 3, 4, None, 6, 7, 5, 8)
        self.assertEqual(expected, transition_model.move_up(state))

    def test_move_up_8(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, 2, 3, 4, 5, 6, 7, 8, None)
        expected = (1, 2, 3, 4, 5, None, 7, 8, 6)
        self.assertEqual(expected, transition_model.move_up(state))


    """
    move_down
    """

    def test_move_down_invalid_for_positions_6_7_8(self):
        transition_model = EightPuzzleTransitionModel()
        with self.assertRaises(EightPuzzleTransitionException):
            state = (0, 0, 0, 0, 0, 0, None, 0, 0)
            transition_model.move_down(state)
        with self.assertRaises(EightPuzzleTransitionException):
            state = (0, 0, 0, 0, 0, 0, 0, None, 0)
            transition_model.move_down(state)
        with self.assertRaises(EightPuzzleTransitionException):
            state = (0, 0, 0, 0, 0, 0, 0, 0, None)
            transition_model.move_down(state)

    def test_move_down_0(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (None, 1, 2, 3, 4, 5, 6, 7, 8)
        expected = (3, 1, 2, None, 4, 5, 6, 7, 8)
        self.assertEqual(expected, transition_model.move_down(state))

    def test_move_down_1(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, None, 2, 3, 4, 5, 6, 7, 8)
        expected = (1, 4, 2, 3, None, 5, 6, 7, 8)
        self.assertEqual(expected, transition_model.move_down(state))

    def test_move_down_2(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, 2, None, 3, 4, 5, 6, 7, 8)
        expected = (1, 2, 5, 3, 4, None, 6, 7, 8)
        self.assertEqual(expected, transition_model.move_down(state))

    def test_move_down_3(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, 2, 3, None, 4, 5, 6, 7, 8)
        expected = (1, 2, 3, 6, 4, 5, None, 7, 8)
        self.assertEqual(expected, transition_model.move_down(state))

    def test_move_down_4(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, 2, 3, 4, None, 5, 6, 7, 8)
        expected = (1, 2, 3, 4, 7, 5, 6, None, 8)
        self.assertEqual(expected, transition_model.move_down(state))

    def test_move_down_5(self):
        transition_model = EightPuzzleTransitionModel()
        state =    (1, 2, 3, 4, 5, None, 6, 7, 8)
        expected = (1, 2, 3, 4, 5, 8, 6, 7, None)
        self.assertEqual(expected, transition_model.move_down(state))


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
