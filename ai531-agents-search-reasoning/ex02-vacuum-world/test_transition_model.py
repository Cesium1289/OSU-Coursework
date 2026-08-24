# DO NOT MODIFY THIS FILE
# Run me via: python3 -m unittest test_transition_model

import unittest
import time
from state import State
from location import Location
from movement_model import MovementModel
from transition_model import TransitionModel


class TestTransitionModel(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A TransitionModel exists.
        """
        try:
            TransitionModel(None, None)
        except NameError:
            self.fail("Could not instantiate TransitionModel")

    """
    Attributes
    """

    def test_state(self):
        """
        A TransitionModel has state.
        """
        transition_model = TransitionModel('Fake State', 'Fake Movements')
        self.assertEqual('Fake State', transition_model.state)

    def test_movements(self):
        """
        A TransitionModel has movements.
        """
        transition_model = TransitionModel('Fake State', 'Fake Movements')
        self.assertEqual('Fake Movements', transition_model.movements)

    """
    Methods
    """

    def test_apply_suction(self):
        """
        Applying suction results in the current location of the world state to
        no longer have dirt.
        """
        vacuum_world = State({'A': Location('A', True), 'B': Location('B', True)}, 'A')
        transition_model = TransitionModel(vacuum_world, None)
        self.assertIsNotNone(vacuum_world.current_location().dirt)
        transition_model.apply_suction()
        self.assertIsNone(vacuum_world.current_location().dirt)

    def test_move_left_from_location_a(self):
        """
        Moving left from location A results in staying in location A.
        """
        vacuum_world = State({'A': Location('A', True), 'B': Location('B', True)}, 'A')
        movements = {'A': MovementModel('A', 'B'), 'B': MovementModel('A', 'B')}
        transition_model = TransitionModel(vacuum_world, movements)
        self.assertEqual('A', vacuum_world.current_location().id)
        transition_model.move_left()
        self.assertEqual('A', vacuum_world.current_location().id)

    def test_move_left_from_location_b(self):
        """
        Moving left from location B results in arriving in location B.
        """
        vacuum_world = State({'A': Location('A', True), 'B': Location('B', True)}, 'B')
        movements = {'A': MovementModel('A', 'B'), 'B': MovementModel('A', 'B')}
        transition_model = TransitionModel(vacuum_world, movements)
        self.assertEqual('B', vacuum_world.current_location().id)
        transition_model.move_left()
        self.assertEqual('A', vacuum_world.current_location().id)

    def test_move_right_from_location_a(self):
        """
        Moving right from location A results in arriving in location B.
        """
        vacuum_world = State({'A': Location('A', True), 'B': Location('B', True)}, 'A')
        movements = {'A': MovementModel('A', 'B'), 'B': MovementModel('A', 'B')}
        transition_model = TransitionModel(vacuum_world, movements)
        self.assertEqual('A', vacuum_world.current_location().id)
        transition_model.move_right()
        self.assertEqual('B', vacuum_world.current_location().id)

    def test_move_right_from_location_b(self):
        """
        Moving right from location B results in staying in location B.
        """
        vacuum_world = State({'A': Location('A', True), 'B': Location('B', True)}, 'B')
        movements = {'A': MovementModel('A', 'B'), 'B': MovementModel('A', 'B')}
        transition_model = TransitionModel(vacuum_world, movements)
        self.assertEqual('B', vacuum_world.current_location().id)
        transition_model.move_right()
        self.assertEqual('B', vacuum_world.current_location().id)


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
