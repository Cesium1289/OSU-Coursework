# InsufficientModelReflexVacuum: A robot vacuum cleaner modeled as a model-based
# reflex agent. This has some good ideas, but falls short of honoring the
# MODEL-BASED-REFLEX-AGENT specification.


class InsufficientModelReflexVacuum:

    def __init__(self, initial_location):
        self.current_location = initial_location
        self.previous_locations = []

    # Sensors. Represents the "sensor model."

    def sense_dirt(self):
        return self.current_location.dirt is not None

    def sense_location_id(self):
        return self.current_location.id

    # Actuators. Represents the "transition model."

    def suck(self):
        self.current_location.apply_suction()

    def move_left(self):
        self.previous_locations.append(self.current_location)

    def move_right(self):
        self.previous_locations.append(self.current_location)

    # Agent function. Embodies the rules, rule match, and action.

    def action(self, location):
        self.current_location = location
        if self.sense_dirt():
            return self.suck
        elif self.sense_location_id() == 'A':
            return self.move_right
        elif self.sense_location_id() == 'B':
            return self.move_left
        else:
            return None
