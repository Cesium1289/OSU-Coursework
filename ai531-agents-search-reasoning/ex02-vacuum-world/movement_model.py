# MovementModel: a helper class for the TransitionModel, encapsulating what the
# new location is when moving right or left.


class MovementModel:

    def __init__(self, left, right):
        self.left = left
        self.right = right
