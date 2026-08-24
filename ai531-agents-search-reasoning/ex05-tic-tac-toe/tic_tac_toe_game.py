# TicTacToeGame
# A formal representation of a game of Tic Tac Toe, aligned with the specification
# from the AIMA text. The Game encapsulates the state, transition model,
# objective function, and other game mechanics.
# It uses a TicTacToeBoardRenderer to 'draw' itself when necessary.

class IllegalTicTacToeMoveException(Exception):
    pass

class TicTacToeGame:

    P1_SYMBOL = 'X'
    P2_SYMBOL = 'O'

    def __init__(self, initial_state, renderer):
        self.state = initial_state
        self.renderer = renderer

    def utility(self, state, player):
        """
        The objective function. Returns a value (1, 0, -1) for a game `state`
        with respect to `player`. Assume `state` is a tuple representing the
        tic-tac-toe board state, and `player` is 'X' or 'O'.
        """
        other_player = self.P2_SYMBOL if player == self.P1_SYMBOL else self.P1_SYMBOL
        if self.is_win(state,player):
            return 1
        elif self.is_win(state,other_player):
            return -1
        else:
            return 0

    def is_not_over(self):
        """
        Is the game over, given the current state?
        """
        return not self.is_terminal(self.state)

    def is_terminal(self, state):
        """
        Is this `state` a terminal state?
        A state is terminal if no more moves can be made (a player won, or the
        board is full).
        """
        return self.no_moves_left(state)

    def to_move(self, state):
        """
        Given `state`, whose move is it?
        """
        if self.no_moves_left(state):
            return None
        elif state.count(self.P1_SYMBOL) == state.count(self.P2_SYMBOL):
            return self.P1_SYMBOL
        else:
            return self.P2_SYMBOL

    def actions(self, state):
        """
        A set (tuple) of possible actions for `state`. An action is an integer
        representing a location on the tic-tac-toe game board.
        """
        return tuple([i for i in range(len(state)) if state[i] is None])

    def result(self, state, action):
        """
        Return a new state that is a result of applying `action` to `state`.
        """
        if state[action] is not None:
            raise IllegalTicTacToeMoveException(f"Cannot use {action} for state {state}.")
        state = list(state)
        state[action] = self.to_move(state)
        return tuple(state)

    def no_moves_left(self, state):
        """
        Are there moves that can be made by either player?
        There are no moves left if a player has won or the board is full.
        """
        return (None not in state) or self.is_win(state, self.P1_SYMBOL) or self.is_win(state, self.P2_SYMBOL)

    def is_win(self, state, player):
        """
        Is the `state` a winning state for `player` ?
        """
        if [0, 1, 2] == [i for i in [0, 1, 2] if state[i] == player] or\
           [3, 4, 5] == [i for i in [3, 4, 5] if state[i] == player] or\
           [6, 7, 8] == [i for i in [6, 7, 8] if state[i] == player] or\
           [0, 3, 6] == [i for i in [0, 3, 6] if state[i] == player] or\
           [1, 4, 7] == [i for i in [1, 4, 7] if state[i] == player] or\
           [2, 5, 8] == [i for i in [2, 5, 8] if state[i] == player] or\
           [0, 4, 8] == [i for i in [0, 4, 8] if state[i] == player] or\
           [2, 4, 6] == [i for i in [2, 4, 6] if state[i] == player]:
            return True
        else:
            return False

    def __str__(self):
        return self.renderer.render(self.state)
