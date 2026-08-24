# State: the vacuum world.
# The state of the world consists of all of the locations in the world,
# and the current location of the vacuum.


class State:

    def __init__(self, locations, current_location_id):
        self.locations = locations
        self.current_location_id = current_location_id

    def current_location(self):
        return self.locations[self.current_location_id]
