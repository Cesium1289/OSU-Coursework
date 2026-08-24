# DO NOT MODIFY THE CODE WITHIN EACH TEST
# Run me via: python3 -m unittest test_simple_reflex_vacuum

import unittest
import time
import contextlib
import io
from simple_reflex_vacuum import SimpleReflexVacuum


class TestSimpleReflexVacuum(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A SimpleReflexVacuum exists.
        """
        try:
            SimpleReflexVacuum()
        except NameError:
            self.fail("Could not instantiate SimpleReflexVacuum")

    """
    Actuators
    """

    def test_suck(self):
        """
        A SimpleReflexVacuum can create suction.
        """
        vacuum = SimpleReflexVacuum()
        vacuum.suck()

    def test_suck_side_effect(self):
        """
        A SimpleReflexVacuum `suck` actuator causes a side effect in the
        environment, which is simulated as printed output to the console.
        """
        vacuum = SimpleReflexVacuum()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            vacuum.suck()
            output = f.getvalue()
        self.assertEqual("side effect: cause hardware to suck\n", output)

    def test_move_left(self):
        """
        A SimpleReflexVacuum can move left.
        """
        vacuum = SimpleReflexVacuum()
        vacuum.move_left()

    def test_suck_move_left_side_effect(self):
        """
        A SimpleReflexVacuum `move_left` actuator causes a side effect in the
        environment, which is simulated as printed output to the console.
        """
        vacuum = SimpleReflexVacuum()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            vacuum.move_left()
            output = f.getvalue()
        self.assertEqual("side effect: cause hardware to move left\n", output)

    def test_move_right(self):
        """
        A SimpleReflexVacuum can move right.
        """
        vacuum = SimpleReflexVacuum()
        vacuum.move_right()

    def test_suck_move_right_side_effect(self):
        """
        A SimpleReflexVacuum `move_right` actuator causes a side effect in the
        environment, which is simulated as printed output to the console.
        """
        vacuum = SimpleReflexVacuum()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            vacuum.move_right()
            output = f.getvalue()
        self.assertEqual("side effect: cause hardware to move right\n", output)

    # """
    # Agent function
    # """

    def test_action_for_dirty_location(self):
        """
        The action for a dirty location is the `suck` function.
        """
        vacuum = SimpleReflexVacuum()
        self.assertEqual(vacuum.suck, vacuum.action('A', 'Dirt'))

    def test_action_for_clean_location_a(self):
        """
        The action for a clean location A is the `move_right` function.
        """
        vacuum = SimpleReflexVacuum()
        self.assertEqual(vacuum.move_right, vacuum.action('A', None))

    def test_action_for_clean_location_b(self):
        """
        The action for a clean location B is the `move_left` function.
        """
        vacuum = SimpleReflexVacuum()
        self.assertEqual(vacuum.move_left, vacuum.action('B', None))


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
