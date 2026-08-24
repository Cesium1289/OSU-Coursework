# DO NOT MODIFY THIS FILE
# Run me via: python3 -m unittest test_sensor_model

import unittest
import time
from state import State
from location import Location
from sensor_model import SensorModel


class TestSensorModel(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A SensorModel exists.
        """
        try:
            SensorModel(None)
        except NameError:
            self.fail("Could not instantiate SensorModel")

    """
    Attributes
    """

    def test_state(self):
        """
        A SensorModel has state.
        """
        sensor_model = SensorModel('Fake State')
        self.assertEqual('Fake State', sensor_model.state)

    """
    Methods
    """

    def test_sense_dirt_of_dirty_location(self):
        """
        Sensing dirt when the current location is dirty returns True.
        """
        vacuum_world = State({'A': Location('A', True), 'B': Location('B', True)}, 'A')
        sensor_model = SensorModel(vacuum_world)
        self.assertTrue(sensor_model.sense_dirt())

    def test_sense_dirt_of_clean_location(self):
        """
        Sensing dirt when the current location has no dirt returns False.
        """
        vacuum_world = State({'A': Location('A', None), 'B': Location('B', True)}, 'A')
        sensor_model = SensorModel(vacuum_world)
        self.assertFalse(sensor_model.sense_dirt())

    def test_sense_location_id(self):
        """
        Sensing the location id returns the id of the current location.
        """
        vacuum_world = State({'A': Location('A', True), 'B': Location('B', True)}, 'A')
        sensor_model = SensorModel(vacuum_world)
        self.assertEqual(vacuum_world.current_location().id, sensor_model.sense_location_id())
        vacuum_world.current_location_id = 'B'
        self.assertEqual(vacuum_world.current_location().id, sensor_model.sense_location_id())


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
