# DO NOT MODIFY THE CODE IN THE TESTS
# Run me via: python3 -m unittest test_eight_puzzle_best_first_search_solver

import unittest
import time
from eight_puzzle_best_first_search_solver import EightPuzzleBestFirstSearchSolver
from eight_puzzle_agent import EightPuzzleAgent
from eight_puzzle_transition_model import EightPuzzleTransitionModel
from eight_puzzle_problem import EightPuzzleProblem


class TestEightPuzzleBestFirstSearchSolver(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A EightPuzzleBestFirstSearchSolver exists.
        """
        try:
            EightPuzzleBestFirstSearchSolver()
        except NameError:
            self.fail("Could not instantiate EightPuzzleBestFirstSearchSolver")

    """
    solution
    """

    def test_initial_state_goal_state(self):
        """
        The solution for (None, 1, 2, 3, 4, 5, 6, 7, 8) is an empty list of actions.
        """
        initial_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
        goal_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
        transition_model = EightPuzzleTransitionModel()
        problem = EightPuzzleProblem(initial_state, goal_state, transition_model)
        solver = EightPuzzleBestFirstSearchSolver()
        expected = []
        self.assertEqual(expected, solver.solution(problem))

    def test_1_None_2_3_4_5_6_7_8(self):
        """
        The solution for (1, None, 2, 3, 4, 5, 6, 7, 8) is [EightPuzzleAgent.move_left].
        """
        initial_state = (1, None, 2, 3, 4, 5, 6, 7, 8)
        goal_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
        transition_model = EightPuzzleTransitionModel()
        problem = EightPuzzleProblem(initial_state, goal_state, transition_model)
        solver = EightPuzzleBestFirstSearchSolver()
        expected = [EightPuzzleAgent.move_left]
        self.assertEqual(expected, solver.solution(problem))

    def test_3_1_2_None_4_5_6_7_8(self):
        """
        The solution for (3, 1, 2, None, 4, 5, 6, 7, 8) is [EightPuzzleAgent.move_up].
        """
        initial_state = (3, 1, 2, None, 4, 5, 6, 7, 8)
        goal_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
        transition_model = EightPuzzleTransitionModel()
        problem = EightPuzzleProblem(initial_state, goal_state, transition_model)
        solver = EightPuzzleBestFirstSearchSolver()
        expected = [EightPuzzleAgent.move_up]
        self.assertEqual(expected, solver.solution(problem))

    def test_1_2_None_3_4_5_6_7_8(self):
        """
        The solution for (1, 2, None, 3, 4, 5, 6, 7, 8) is [move_left, move_left].
        """
        initial_state = (1, 2, None, 3, 4, 5, 6, 7, 8)
        goal_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
        transition_model = EightPuzzleTransitionModel()
        problem = EightPuzzleProblem(initial_state, goal_state, transition_model)
        solver = EightPuzzleBestFirstSearchSolver()
        expected = [EightPuzzleAgent.move_left, EightPuzzleAgent.move_left]
        self.assertEqual(expected, solver.solution(problem))

    def test_3_1_2_6_4_5_None_7_8(self):
        """
        The solution for (3, 1, 2, 6, 4, 5, None, 7, 8) is [move_up, move_up].
        """
        initial_state = (3, 1, 2, 6, 4, 5, None, 7, 8)
        goal_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
        transition_model = EightPuzzleTransitionModel()
        problem = EightPuzzleProblem(initial_state, goal_state, transition_model)
        solver = EightPuzzleBestFirstSearchSolver()
        expected = [EightPuzzleAgent.move_up, EightPuzzleAgent.move_up]
        self.assertEqual(expected, solver.solution(problem))


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
