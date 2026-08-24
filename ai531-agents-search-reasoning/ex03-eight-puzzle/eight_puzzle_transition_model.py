# EightPuzzleTransitionModel: An encapsulation of the "movement rules" of the
# classic eight-puzzle. Given a puzzle state and a move, produce the new puzzle
# state.


class EightPuzzleTransitionException(Exception):
    pass


class EightPuzzleTransitionModel:

    def can_move_left(self, puzzle_state):
        return puzzle_state.index(None) in (1, 2, 4, 5, 7, 8)

    def can_move_right(self, puzzle_state):
        return puzzle_state.index(None) in (0, 1, 3, 4, 6, 7)

    def can_move_up(self, puzzle_state):
        return puzzle_state.index(None) in (3, 4, 5, 6, 7, 8)

    def can_move_down(self, puzzle_state):
        return puzzle_state.index(None) in (0, 1, 2, 3, 4, 5)

    def move_left(self, puzzle_state):
        if not self.can_move_left(puzzle_state):
            raise EightPuzzleTransitionException(f"Cannot move left for state {puzzle_state}")
        index_of_blank_tile = puzzle_state.index(None)
        new_state = [None] * 9
        for i in range(len(puzzle_state)):
            if i == index_of_blank_tile:
                new_state[i] = puzzle_state[i - 1]
                new_state[i - 1] = None
            else:
                new_state[i] = puzzle_state[i]
        return tuple(new_state)

    def move_right(self, puzzle_state):
        if not self.can_move_right(puzzle_state):
            raise EightPuzzleTransitionException(f"Cannot move right for state {puzzle_state}")
        index_to_right_of_blank_tile = puzzle_state.index(None) + 1
        new_state = [None] * 9
        for i in range(len(puzzle_state)):
            if i == index_to_right_of_blank_tile:
                new_state[i] = None
                new_state[i - 1] = puzzle_state[i]
            else:
                new_state[i] = puzzle_state[i]
        return tuple(new_state)

    def move_up(self, puzzle_state):
        if not self.can_move_up(puzzle_state):
            raise EightPuzzleTransitionException(f"Cannot move up for state {puzzle_state}")
        index_of_blank_tile = puzzle_state.index(None)
        new_state = [None] * 9
        for i in range(len(puzzle_state)):
            if i == index_of_blank_tile:
                new_state[i] = puzzle_state[i - 3]
                new_state[i - 3] = None
            else:
                new_state[i] = puzzle_state[i]
        return tuple(new_state)

    def move_down(self, puzzle_state):
        if not self.can_move_down(puzzle_state):
            raise EightPuzzleTransitionException(f"Cannot move down for state {puzzle_state}")
        index_below_blank_tile = puzzle_state.index(None) + 3
        new_state = [None] * 9
        for i in range(len(puzzle_state)):
            if i == index_below_blank_tile:
                new_state[i] = None
                new_state[i - 3] = puzzle_state[i]
            else:
                new_state[i] = puzzle_state[i]
        return tuple(new_state)
