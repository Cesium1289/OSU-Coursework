# TransitionModel: a definition of how actions affect the state of the world.
# A TransitionModel has access to the state of the world, and a dictionary of
# MovementModels to help define what happens when moving right or left from
# a location.


class TransitionModel:

    def __init__(self, state, movements):
        self.state = state
        self.movements = movements

    def apply_suction(self):
        self.state.current_location().dirt = None

    def move_left(self):
        self.state.current_location_id = self.movements[self.state.current_location_id].left

    def move_right(self):
        self.state.current_location_id = self.movements[self.state.current_location_id].right
