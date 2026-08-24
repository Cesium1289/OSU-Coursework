# DO NOT MODIFY THE CODE IN THE TESTS
# Run me via: python3 -m unittest test_tic_tac_toe_game

import unittest
import time
from tic_tac_toe_game import TicTacToeGame, IllegalTicTacToeMoveException


class TestTicTacToeGame(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A TicTacToeGame exists.
        """
        try:
            TicTacToeGame(None, None)
        except NameError:
            self.fail("Could not instantiate TicTacToeGame")

    """
    Properties
    """

    def test_state(self):
        """
        A RandomTicTacToeAgent has a `state` property.
        """
        game = TicTacToeGame("Fake State", None)
        self.assertEqual("Fake State", game.state)

    def test_renderer(self):
        """
        A RandomTicTacToeAgent has a `renderer` property.
        """
        game = TicTacToeGame(None, "Fake Renderer")
        self.assertEqual("Fake Renderer", game.renderer)

    """
    is_not_over
    """

    def test_is_not_over_empty(self):
        """
        A game is not over when the board is empty.
        """
        state = (None, None, None, None, None, None, None, None, None)
        game = TicTacToeGame(state, None)
        self.assertTrue(game.is_not_over())

    def test_is_not_over_when_moves_remain(self):
        """
        A game is not over when there is one move available.
        """
        state = ('X', 'X', 'O', 'O', 'O', 'X', 'X', 'O', None)
        game = TicTacToeGame(state, None)
        self.assertTrue(game.is_not_over())

    def test_is_over_full(self):
        """
        A game is over when there are no more moves available.
        """
        state = ('X', 'X', 'O', 'O', 'O', 'X', 'X', 'O', 'X')
        game = TicTacToeGame(state, None)
        self.assertFalse(game.is_not_over())

    """
    is_terminal
    """

    def test_is_terminal_empty(self):
        """
        A state is not terminal when the board is empty.
        """
        state = (None, None, None, None, None, None, None, None, None)
        game = TicTacToeGame(None, None)
        self.assertFalse(game.is_terminal(state))

    def test_is_terminal_when_moves_remain(self):
        """
        A state is not terminal when the there is one move available.
        """
        state = ('X', 'X', 'O', 'O', 'O', 'X', 'X', 'O', None)
        game = TicTacToeGame(None, None)
        self.assertFalse(game.is_terminal(state))

    def test_is_terminal_full(self):
        """
        A state is terminal when there are no more moves available.
        """
        state = ('X', 'X', 'O', 'O', 'O', 'X', 'X', 'O', 'X')
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_terminal(state))

    def test_is_terminal_x_win_row_1(self):
        """
        XXX
        ... is terminal
        ...
        """
        state = ('X', 'X', 'X', None, None, None, None, None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_terminal(state))

    def test_is_terminal_x_win_row_2(self):
        """
        ...
        XXX is terminal
        ...
        """
        state = (None, None, None, 'X', 'X', 'X', None, None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_terminal(state))

    def test_is_terminal_x_win_row_3(self):
        """
        ...
        ... is terminal
        XXX
        """
        state = (None, None, None, None, None, None, 'X', 'X', 'X')
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_terminal(state))

    def test_is_terminal_x_win_col_1(self):
        """
        X..
        X.. is terminal
        X..
        """
        state = ('X', None, None, 'X', None, None, 'X', None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_terminal(state))

    def test_is_terminal_x_win_col_2(self):
        """
        .X.
        .X. is terminal
        .X.
        """
        state = (None, 'X', None, None, 'X', None, None, 'X', None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_terminal(state))

    def test_is_terminal_x_win_col_3(self):
        """
        ..X
        ..X is terminal
        ..X
        """
        state = (None, None, 'X', None, None, 'X', None, None, 'X')
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_terminal(state))

    def test_is_terminal_x_win_top_left_bottom_right(self):
        """
        X..
        .X. is terminal
        ..X
        """
        state = ('X', None, None, None, 'X', None, None, None, 'X')
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_terminal(state))

    def test_is_terminal_x_win_top_right_bottom_left(self):
        """
        ..X
        .X. is terminal
        X..
        """
        state = (None, None, 'X', None, 'X', None, 'X', None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_terminal(state))

    def test_is_terminal_o_win_row_1(self):
        """
        OOO
        ... is terminal
        ...
        """
        state = ('O', 'O', 'O', None, None, None, None, None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_terminal(state))

    def test_is_terminal_o_win_row_2(self):
        """
        ...
        OOO is terminal
        ...
        """
        state = (None, None, None, 'O', 'O', 'O', None, None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_terminal(state))

    def test_is_terminal_o_win_row_3(self):
        """
        ...
        ... is terminal
        OOO
        """
        state = (None, None, None, None, None, None, 'O', 'O', 'O')
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_terminal(state))

    def test_is_terminal_o_win_col_1(self):
        """
        O..
        O.. is terminal
        O..
        """
        state = ('O', None, None, 'O', None, None, 'O', None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_terminal(state))

    def test_is_terminal_o_win_col_2(self):
        """
        .O.
        .O. is terminal
        .O.
        """
        state = (None, 'O', None, None, 'O', None, None, 'O', None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_terminal(state))

    def test_is_terminal_o_win_col_3(self):
        """
        ..O
        ..O is terminal
        ..O
        """
        state = (None, None, 'O', None, None, 'O', None, None, 'O')
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_terminal(state))

    def test_is_terminal_o_win_top_left_bottom_right(self):
        """
        O..
        .O. is terminal
        ..O
        """
        state = ('O', None, None, None, 'O', None, None, None, 'O')
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_terminal(state))

    def test_is_terminal_o_win_top_right_bottom_left(self):
        """
        ..O
        .O. is terminal
        O..
        """
        state = (None, None, 'O', None, 'O', None, 'O', None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_terminal(state))

    def test_is_terminal_x_win_o_loses(self):
        """
        XOO
        .X. is terminal
        ..X
        """
        state = ('X', 'O', 'O', None, 'X', None, None, None, 'X')
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_terminal(state))

    def test_is_terminal_o_wins_x_loses(self):
        """
        OXX
        .O. is terminal
        X.O
        """
        state = ('O', 'X', 'X', None, 'O', None, 'X', None, 'O')
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_terminal(state))

    """
    to_move
    """

    def test_to_move_empty(self):
        """
        Player 1 (X) goes first.
        """
        state = (None, None, None, None, None, None, None, None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue('X', game.to_move(state))

    def test_to_move_full(self):
        """
        None when there are no moves left.
        """
        state = ('X', 'X', 'O', 'O', 'O', 'X', 'X', 'O', 'X')
        game = TicTacToeGame(None, None)
        self.assertIsNone(game.to_move(state))

    def test_to_move_x(self):
        """
        Player 1's (X) turn.
        """
        state = ('X', 'O', None, None, None, None, None, None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue('X', game.to_move(state))

    def test_to_move_o(self):
        """
        Player 2's (O) turn.
        """
        state = ('X', 'O', 'X', None, None, None, None, None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue('O', game.to_move(state))

    """
    actions
    """

    def test_actions_empty(self):
        """
        The actions for an empty board are (0, 1, 2, 3, 4, 5, 6, 7, 8)
        """
        state = (None, None, None, None, None, None, None, None, None)
        game = TicTacToeGame(None, None)
        self.assertEqual((0, 1, 2, 3, 4, 5, 6, 7, 8), game.actions(state))

    def test_actions_full(self):
        """
        The actions for a full board is ()
        """
        state = ('X', 'X', 'O', 'O', 'O', 'X', 'X', 'O', 'X')
        game = TicTacToeGame(None, None)
        self.assertEqual((), game.actions(state))

    def test_actions_arbitrary(self):
        """
        The actions for a board is the set of indexes of unoccupied locations.
        """
        state = (None, 'X', 'O', None, 'O', 'X', None, None, 'X')
        game = TicTacToeGame(None, None)
        self.assertEqual((0, 3, 6, 7), game.actions(state))

    """
    result
    """

    def test_result_empty(self):
        """
        ...       X..
        ... =(0)> ...
        ...       ...
        """
        state = (None, None, None, None, None, None, None, None, None)
        action = 0
        expected = ('X', None, None, None, None, None, None, None, None)
        game = TicTacToeGame(None, None)
        self.assertEqual(expected, game.result(state, action))

    def test_result_full_raises_exception(self):
        """
        XXO       XXO
        OOX =(0)> OOX
        XOX       XOX
        """
        state = ('X', 'X', 'O', 'O', 'O', 'X', 'X', 'O', 'X')
        action = 0
        game = TicTacToeGame(None, None)
        with self.assertRaises(IllegalTicTacToeMoveException):
             game.result(state, action)

    def test_result_x(self):
        """
        .XO       .XO
        .OX =(8)> .OX
        ...       ..X
        """
        state = (None, 'X', 'O', None, 'O', 'X', None, None, None)
        action = 8
        expected = (None, 'X', 'O', None, 'O', 'X', None, None, 'X')
        game = TicTacToeGame(None, None)
        self.assertEqual(expected, game.result(state, action))

    def test_result_o(self):
        """
        .XO       .XO
        .OX =(7)> .OX
        ..X       .OX
        """
        state = (None, 'X', 'O', None, 'O', 'X', None, None, 'X')
        action = 7
        expected = (None, 'X', 'O', None, 'O', 'X', None, 'O', 'X')
        game = TicTacToeGame(None, None)
        self.assertEqual(expected, game.result(state, action))

    def test_result_illegal_action(self):
        """
        .XO       .XO
        .OX =(7)> .OX
        ..X       .OX
        """
        state = ('X', None, None, None, None, None, None, None, None)
        action = 0
        game = TicTacToeGame(None, None)
        with self.assertRaises(IllegalTicTacToeMoveException):
             game.result(state, action)

    """
    no_moves_left
    """

    def test_no_moves_left_empty(self):
        """
        There are moves left when the board is empty.
        """
        state = (None, None, None, None, None, None, None, None, None)
        game = TicTacToeGame(None, None)
        self.assertFalse(game.no_moves_left(state))

    def test_no_moves_left_full(self):
        """
        There are no moves left when the board is full.
        """
        state = ('X', 'X', 'O', 'O', 'O', 'X', 'X', 'O', 'X')
        game = TicTacToeGame(None, None)
        self.assertTrue(game.no_moves_left(state))

    def test_no_moves_left_x_won(self):
        """
        There are no moves left when X has won.
        """
        state = ('X', 'X', 'X', None, None, None, None, None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.no_moves_left(state))

    def test_no_moves_left_o_won(self):
        """
        There are no moves left when O has won.
        """
        state = ('O', 'O', 'O', None, None, None, None, None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.no_moves_left(state))

    def test_no_moves_left_in_play(self):
        """
        There are moves left when neither player has won but empty spaces remain.
        """
        state = ('X', 'X', 'O', 'O', 'O', 'X', 'X', 'O', None)
        game = TicTacToeGame(None, None)
        self.assertFalse(game.no_moves_left(state))

    """
    is_win
    """

    def test_is_win_empty(self):
        """
        A state is not a winning state when the board is empty.
        """
        state = (None, None, None, None, None, None, None, None, None)
        game = TicTacToeGame(None, None)
        self.assertFalse(game.is_win(state, 'X'))
        self.assertFalse(game.is_win(state, 'O'))

    def test_is_win_when_moves_remain(self):
        """
        A state is not a winning state when there is no winnter and there are moves
        available.
        """
        state = ('X', 'X', 'O', 'O', 'O', 'X', 'X', 'O', None)
        game = TicTacToeGame(None, None)
        self.assertFalse(game.is_win(state, 'X'))
        self.assertFalse(game.is_win(state, 'O'))

    def test_is_win_full(self):
        """
        A state is not a winning state when it is a draw.
        """
        state = ('X', 'X', 'O', 'O', 'O', 'X', 'X', 'O', 'X')
        game = TicTacToeGame(None, None)
        self.assertFalse(game.is_win(state, 'X'))
        self.assertFalse(game.is_win(state, 'O'))

    def test_is_win_x_win_row_1(self):
        """
        XXX
        ... is a winning state
        ...
        """
        state = ('X', 'X', 'X', None, None, None, None, None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_win(state, 'X'))
        self.assertFalse(game.is_win(state, 'O'))

    def test_is_win_x_win_row_2(self):
        """
        ...
        XXX is a winning state
        ...
        """
        state = (None, None, None, 'X', 'X', 'X', None, None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_win(state, 'X'))
        self.assertFalse(game.is_win(state, 'O'))

    def test_is_win_x_win_row_3(self):
        """
        ...
        ... is a winning state
        XXX
        """
        state = (None, None, None, None, None, None, 'X', 'X', 'X')
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_win(state, 'X'))
        self.assertFalse(game.is_win(state, 'O'))

    def test_is_win_x_win_col_1(self):
        """
        X..
        X.. is a winning state
        X..
        """
        state = ('X', None, None, 'X', None, None, 'X', None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_win(state, 'X'))
        self.assertFalse(game.is_win(state, 'O'))

    def test_is_win_x_win_col_2(self):
        """
        .X.
        .X. is a winning state
        .X.
        """
        state = (None, 'X', None, None, 'X', None, None, 'X', None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_win(state, 'X'))
        self.assertFalse(game.is_win(state, 'O'))

    def test_is_win_x_win_col_3(self):
        """
        ..X
        ..X is a winning state
        ..X
        """
        state = (None, None, 'X', None, None, 'X', None, None, 'X')
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_win(state, 'X'))
        self.assertFalse(game.is_win(state, 'O'))

    def test_is_win_x_win_top_left_bottom_right(self):
        """
        X..
        .X. is a winning state
        ..X
        """
        state = ('X', None, None, None, 'X', None, None, None, 'X')
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_win(state, 'X'))
        self.assertFalse(game.is_win(state, 'O'))

    def test_is_win_x_win_top_right_bottom_left(self):
        """
        ..X
        .X. is a winning state
        X..
        """
        state = (None, None, 'X', None, 'X', None, 'X', None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_win(state, 'X'))
        self.assertFalse(game.is_win(state, 'O'))

    def test_is_win_o_win_row_1(self):
        """
        OOO
        ... is a winning state
        ...
        """
        state = ('O', 'O', 'O', None, None, None, None, None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_win(state, 'O'))
        self.assertFalse(game.is_win(state, 'X'))

    def test_is_win_o_win_row_2(self):
        """
        ...
        OOO is a winning state
        ...
        """
        state = (None, None, None, 'O', 'O', 'O', None, None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_win(state, 'O'))
        self.assertFalse(game.is_win(state, 'X'))

    def test_is_win_o_win_row_3(self):
        """
        ...
        ... is a winning state
        OOO
        """
        state = (None, None, None, None, None, None, 'O', 'O', 'O')
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_win(state, 'O'))
        self.assertFalse(game.is_win(state, 'X'))

    def test_is_win_o_win_col_1(self):
        """
        O..
        O.. is a winning state
        O..
        """
        state = ('O', None, None, 'O', None, None, 'O', None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_win(state, 'O'))
        self.assertFalse(game.is_win(state, 'X'))

    def test_is_win_o_win_col_2(self):
        """
        .O.
        .O. is a winning state
        .O.
        """
        state = (None, 'O', None, None, 'O', None, None, 'O', None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_win(state, 'O'))
        self.assertFalse(game.is_win(state, 'X'))

    def test_is_win_o_win_col_3(self):
        """
        ..O
        ..O is a winning state
        ..O
        """
        state = (None, None, 'O', None, None, 'O', None, None, 'O')
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_win(state, 'O'))
        self.assertFalse(game.is_win(state, 'X'))

    def test_is_win_o_win_top_left_bottom_right(self):
        """
        O..
        .O. is a winning state
        ..O
        """
        state = ('O', None, None, None, 'O', None, None, None, 'O')
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_win(state, 'O'))
        self.assertFalse(game.is_win(state, 'X'))

    def test_is_win_o_win_top_right_bottom_left(self):
        """
        ..O
        .O. is a winning state
        O..
        """
        state = (None, None, 'O', None, 'O', None, 'O', None, None)
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_win(state, 'O'))
        self.assertFalse(game.is_win(state, 'X'))

    def test_is_win_x_win_o_loses(self):
        """
        XOO
        .X. is a winning state
        ..X
        """
        state = ('X', 'O', 'O', None, 'X', None, None, None, 'X')
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_win(state, 'X'))
        self.assertFalse(game.is_win(state, 'O'))

    def test_is_win_o_wins_x_loses(self):
        """
        OXX
        .O. is a winning state
        X.O
        """
        state = ('O', 'X', 'X', None, 'O', None, 'X', None, 'O')
        game = TicTacToeGame(None, None)
        self.assertTrue(game.is_win(state, 'O'))
        self.assertFalse(game.is_win(state, 'X'))

def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
