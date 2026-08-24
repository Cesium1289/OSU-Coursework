# SensorModel: a definition of how the current location is reflected in the
# agent percepts. This decouples the ModelReflexVacuum from the actual state of
# the world, and encapsulates how a sensor might be exposed as a percept API.


class SensorModel:

    def __init__(self, state):
        self.state = state

    def sense_dirt(self):
        return self.state.current_location().dirt is not None

    def sense_location_id(self):
        return self.state.current_location().id
