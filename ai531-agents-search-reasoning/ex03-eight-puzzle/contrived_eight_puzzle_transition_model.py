# ContrivedEightPuzzleTransitionModel: An encapsulation of the "movement rules" of
# the classic eight-puzzle. Given a puzzle state and a move, produce the new puzzle
# state. An incomplete example for the ModelReflexEightPuzzleAgent to use.

class ContrivedEightPuzzleTransitionModel:

    def move_left(self, puzzle_state):
        return (None, 1, 2, 3, 4, 5, 6, 7, 8)

    def move_right(self, puzzle_state):
        return (None, 1, 2, 3, 4, 5, 6, 7, 8)

    def move_up(self, puzzle_state):
        return (None, 1, 2, 3, 4, 5, 6, 7, 8)

    def move_down(self, puzzle_state):
        return (None, 1, 2, 3, 4, 5, 6, 7, 8)
