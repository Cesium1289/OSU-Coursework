# Vacuum Scratchpad
# YOUR NAME
# Use this as a "scratchpad" to tinker with your Vacuum objects.
# There are no rules here, and this code will not be evaluated. This file is a
# place for you to experiment.


# Part 1

from simple_reflex_vacuum import SimpleReflexVacuum

simple_reflex_vacuum = SimpleReflexVacuum()
print(simple_reflex_vacuum)
print(simple_reflex_vacuum.action('A', 'Dirt'))


# Part 2

from location import Location
from state import State
from movement_model import MovementModel
from transition_model import TransitionModel
from sensor_model import SensorModel
from model_reflex_vacuum import ModelReflexVacuum

vacuum_world = State({'A': Location('A', True), 'B': Location('B', True)}, 'A')
print(vacuum_world.current_location())

movements = {'A': MovementModel('A', 'B'),
             'B': MovementModel('A', 'B')}

transition_model = TransitionModel(vacuum_world, movements)

sensor_model = SensorModel(vacuum_world)

vacuum = ModelReflexVacuum(vacuum_world, transition_model, sensor_model)
print(vacuum.action()) # suck
print(vacuum.action()) # move right
print(vacuum.action()) # suck
print(vacuum.action()) # move left
print(vacuum.action()) # move right
