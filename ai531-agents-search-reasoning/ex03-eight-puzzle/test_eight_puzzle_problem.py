# DO NOT MODIFY THE CODE IN THE TESTS
# Run me via: python3 -m unittest test_eight_puzzle_problem

import unittest
import time
from eight_puzzle_problem import EightPuzzleProblem
from eight_puzzle_agent import EightPuzzleAgent
from eight_puzzle_transition_model import EightPuzzleTransitionModel

class TestEightPuzzleProblem(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A EightPuzzleProblem exists.
        """
        try:
            EightPuzzleProblem(None, None, None)
        except NameError:
            self.fail("Could not instantiate EightPuzzleProblem")

    """
    Properties
    """

    def test_initial_state(self):
        """
        An EightPuzzleProblem has an `initial_state` property.
        """
        problem = EightPuzzleProblem("Fake State", None, None)
        self.assertEqual("Fake State", problem.initial_state)

    def test_goal_state(self):
        """
        An EightPuzzleProblem has a `goal_state` property.
        """
        problem = EightPuzzleProblem(None, "Fake Goal State", None)
        self.assertEqual("Fake Goal State", problem.goal_state)

    def test_transition_model(self):
        """
        An EightPuzzleProblem has a `transition_model` property.
        """
        problem = EightPuzzleProblem(None, None, "Fake Transition Model")
        self.assertEqual("Fake Transition Model", problem.transition_model)

    """
    is_goal
    """

    def test_is_goal_true(self):
        """
        The is_goal method returns True when the state is the goal state.
        """
        fake_goal_state = (1, 2, 3)
        problem = EightPuzzleProblem(None, fake_goal_state, None)
        self.assertTrue(problem.is_goal(fake_goal_state))

    def test_is_goal_false(self):
        """
        The is_goal method returns False when the state is not the goal state.
        """
        fake_goal_state = (1, 2, 3)
        non_goal_state = (1, 1, 1)
        problem = EightPuzzleProblem(None, fake_goal_state, None)
        self.assertFalse(problem.is_goal(non_goal_state))

    """
    actions
    """

    def test_actions_0(self):
        """
        Position 0 has actions right and down.
        """
        problem = EightPuzzleProblem(None, None, None)
        self.assertEqual([EightPuzzleAgent.move_right, EightPuzzleAgent.move_down], problem.actions((None, 0, 0, 0, 0, 0, 0, 0, 0)))

    def test_actions_1(self):
        """
        Position 1 has actions left, right and down.
        """
        problem = EightPuzzleProblem(None, None, None)
        self.assertEqual([EightPuzzleAgent.move_left, EightPuzzleAgent.move_right, EightPuzzleAgent.move_down], problem.actions((0, None, 0, 0, 0, 0, 0, 0, 0)))

    def test_actions_2(self):
        """
        Position 2 has actions left and down.
        """
        problem = EightPuzzleProblem(None, None, None)
        self.assertEqual([EightPuzzleAgent.move_left, EightPuzzleAgent.move_down], problem.actions((0, 0, None, 0, 0, 0, 0, 0, 0)))

    def test_actions_3(self):
        """
        Position 3 has actions right, up and down.
        """
        problem = EightPuzzleProblem(None, None, None)
        self.assertEqual([EightPuzzleAgent.move_right, EightPuzzleAgent.move_up, EightPuzzleAgent.move_down], problem.actions((0, 0, 0, None, 0, 0, 0, 0, 0)))

    def test_actions_4(self):
        """
        Position 4 has actions left, right, up and down.
        """
        problem = EightPuzzleProblem(None, None, None)
        self.assertEqual([EightPuzzleAgent.move_left, EightPuzzleAgent.move_right, EightPuzzleAgent.move_up, EightPuzzleAgent.move_down], problem.actions((0, 0, 0, 0, None, 0, 0, 0, 0)))

    def test_actions_5(self):
        """
        Position 5 has actions left, up and down.
        """
        problem = EightPuzzleProblem(None, None, None)
        self.assertEqual([EightPuzzleAgent.move_left, EightPuzzleAgent.move_up, EightPuzzleAgent.move_down], problem.actions((0, 0, 0, 0, 0, None, 0, 0, 0)))

    def test_actions_6(self):
        """
        Position 6 has actions right and up.
        """
        problem = EightPuzzleProblem(None, None, None)
        self.assertEqual([EightPuzzleAgent.move_right, EightPuzzleAgent.move_up], problem.actions((0, 0, 0, 0, 0, 0, None, 0, 0)))

    def test_actions_7(self):
        """
        Position 7 has actions left, right and up.
        """
        problem = EightPuzzleProblem(None, None, None)
        self.assertEqual([EightPuzzleAgent.move_left, EightPuzzleAgent.move_right, EightPuzzleAgent.move_up], problem.actions((0, 0, 0, 0, 0, 0, 0, None, 0)))

    def test_actions_8(self):
        """
        Position 8 has actions left and up.
        """
        problem = EightPuzzleProblem(None, None, None)
        self.assertEqual([EightPuzzleAgent.move_left, EightPuzzleAgent.move_up], problem.actions((0, 0, 0, 0, 0, 0, 0, 0, None)))

    """
    result
    """

    def test_result_0_move_right(self):
        """
        (None, 1, 2, 3, 4, 5, 6, 7, 8) -> right -> (1, None, 2, 3, 4, 5, 6, 7, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, None, 2, 3, 4, 5, 6, 7, 8), problem.result((None, 1, 2, 3, 4, 5, 6, 7, 8), EightPuzzleAgent.move_right))

    def test_result_0_move_down(self):
        """
        (None, 1, 2, 3, 4, 5, 6, 7, 8) -> down -> (3, 1, 2, None, 4, 5, 6, 7, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((3, 1, 2, None, 4, 5, 6, 7, 8), problem.result((None, 1, 2, 3, 4, 5, 6, 7, 8), EightPuzzleAgent.move_down))

    def test_result_1_move_left(self):
        """
        (1, None, 2, 3, 4, 5, 6, 7, 8) -> left -> (None, 1, 2, 3, 4, 5, 6, 7, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((None, 1, 2, 3, 4, 5, 6, 7, 8), problem.result((1, None, 2, 3, 4, 5, 6, 7, 8), EightPuzzleAgent.move_left))

    def test_result_1_move_right(self):
        """
        (1, None, 2, 3, 4, 5, 6, 7, 8) -> right -> (1, 2, None, 3, 4, 5, 6, 7, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, 2, None, 3, 4, 5, 6, 7, 8), problem.result((1, None, 2, 3, 4, 5, 6, 7, 8), EightPuzzleAgent.move_right))

    def test_result_1_move_down(self):
        """
        (1, None, 2, 3, 4, 5, 6, 7, 8) -> down -> (1, 4, 2, 3, None, 5, 6, 7, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, 4, 2, 3, None, 5, 6, 7, 8), problem.result((1, None, 2, 3, 4, 5, 6, 7, 8), EightPuzzleAgent.move_down))

    def test_result_2_move_left(self):
        """
        (1, 2, None, 3, 4, 5, 6, 7, 8) -> left -> (1, None, 2, 3, 4, 5, 6, 7, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, None, 2, 3, 4, 5, 6, 7, 8), problem.result((1, 2, None, 3, 4, 5, 6, 7, 8), EightPuzzleAgent.move_left))

    def test_result_2_move_down(self):
        """
        (1, 2, None, 3, 4, 5, 6, 7, 8) -> down -> (1, 2, 5, 3, 4, None, 6, 7, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, 2, 5, 3, 4, None, 6, 7, 8), problem.result((1, 2, None, 3, 4, 5, 6, 7, 8), EightPuzzleAgent.move_down))

    def test_result_3_move_right(self):
        """
        (1, 2, 3, None, 4, 5, 6, 7, 8) -> right -> (1, 2, 3, 4, None, 5, 6, 7, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, 2, 3, 4, None, 5, 6, 7, 8), problem.result((1, 2, 3, None, 4, 5, 6, 7, 8), EightPuzzleAgent.move_right))

    def test_result_3_move_up(self):
        """
        (1, 2, 3, None, 4, 5, 6, 7, 8) -> up -> (None, 2, 3, 1, 4, 5, 6, 7, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((None, 2, 3, 1, 4, 5, 6, 7, 8), problem.result((1, 2, 3, None, 4, 5, 6, 7, 8), EightPuzzleAgent.move_up))

    def test_result_3_move_down(self):
        """
        (1, 2, 3, None, 4, 5, 6, 7, 8) -> down -> (1, 2, 3, 6, 4, 5, None, 7, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, 2, 3, 6, 4, 5, None, 7, 8), problem.result((1, 2, 3, None, 4, 5, 6, 7, 8), EightPuzzleAgent.move_down))

    def test_result_4_move_left(self):
        """
        (1, 2, 3, 4, None, 5, 6, 7, 8) -> left -> (1, 2, 3, None, 4, 5, 6, 7, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, 2, 3, None, 4, 5, 6, 7, 8), problem.result((1, 2, 3, 4, None, 5, 6, 7, 8), EightPuzzleAgent.move_left))

    def test_result_4_move_right(self):
        """
        (1, 2, 3, 4, None, 5, 6, 7, 8) -> right -> (1, 2, 3, 4, 5, None, 6, 7, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, 2, 3, 4, 5, None, 6, 7, 8), problem.result((1, 2, 3, 4, None, 5, 6, 7, 8), EightPuzzleAgent.move_right))

    def test_result_4_move_up(self):
        """
        (1, 2, 3, 4, None, 5, 6, 7, 8) -> up -> (1, None, 3, 4, 2, 5, 6, 7, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, None, 3, 4, 2, 5, 6, 7, 8), problem.result((1, 2, 3, 4, None, 5, 6, 7, 8), EightPuzzleAgent.move_up))

    def test_result_4_move_down(self):
        """
        (1, 2, 3, 4, None, 5, 6, 7, 8) -> down -> (1, 2, 3, 4, 7, 5, 6, None, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, 2, 3, 4, 7, 5, 6, None, 8), problem.result((1, 2, 3, 4, None, 5, 6, 7, 8), EightPuzzleAgent.move_down))

    def test_result_5_move_left(self):
        """
        (1, 2, 3, 4, 5, None, 6, 7, 8) -> left -> (1, 2, 3, 4, None, 5, 6, 7, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, 2, 3, 4, None, 5, 6, 7, 8), problem.result((1, 2, 3, 4, 5, None, 6, 7, 8), EightPuzzleAgent.move_left))

    def test_result_5_move_up(self):
        """
        (1, 2, 3, 4, 5, None, 6, 7, 8) -> up -> (1, 2, None, 4, 5, 3, 6, 7, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, 2, None, 4, 5, 3, 6, 7, 8), problem.result((1, 2, 3, 4, 5, None, 6, 7, 8), EightPuzzleAgent.move_up))

    def test_result_5_move_down(self):
        """
        (1, 2, 3, 4, 5, None, 6, 7, 8) -> down -> (1, 2, 3, 4, 5, 8, 6, 7, None)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, 2, 3, 4, 5, 8, 6, 7, None), problem.result((1, 2, 3, 4, 5, None, 6, 7, 8), EightPuzzleAgent.move_down))

    def test_result_6_move_right(self):
        """
        (1, 2, 3, 4, 5, 6, None, 7, 8) -> right -> (1, 2, 3, 4, 5, 6, 7, None, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, 2, 3, 4, 5, 6, 7, None, 8), problem.result((1, 2, 3, 4, 5, 6, None, 7, 8), EightPuzzleAgent.move_right))

    def test_result_6_move_up(self):
        """
        (1, 2, 3, 4, 5, 6, None, 7, 8) -> up -> (1, 2, 3, None, 5, 6, 4, 7, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, 2, 3, None, 5, 6, 4, 7, 8), problem.result((1, 2, 3, 4, 5, 6, None, 7, 8), EightPuzzleAgent.move_up))

    def test_result_7_move_left(self):
        """
        (1, 2, 3, 4, 5, 6, 7, None, 8) -> left -> (1, 2, 3, 4, 5, 6, None, 7, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, 2, 3, 4, 5, 6, None, 7, 8), problem.result((1, 2, 3, 4, 5, 6, 7, None, 8), EightPuzzleAgent.move_left))

    def test_result_7_move_right(self):
        """
        (1, 2, 3, 4, 5, 6, 7, None, 8) -> right -> (1, 2, 3, 4, 5, 6, 7, 8, None)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, 2, 3, 4, 5, 6, 7, 8, None), problem.result((1, 2, 3, 4, 5, 6, 7, None, 8), EightPuzzleAgent.move_right))

    def test_result_7_move_up(self):
        """
        (1, 2, 3, 4, 5, 6, 7, None, 8) -> up -> (1, 2, 3, 4, None, 6, 7, 5, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, 2, 3, 4, None, 6, 7, 5, 8), problem.result((1, 2, 3, 4, 5, 6, 7, None, 8), EightPuzzleAgent.move_up))

    def test_result_8_move_left(self):
        """
        (1, 2, 3, 4, 5, 6, 7, 8, None) -> left -> (1, 2, 3, 4, 5, 6, 7, None, 8)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, 2, 3, 4, 5, 6, 7, None, 8), problem.result((1, 2, 3, 4, 5, 6, 7, 8, None), EightPuzzleAgent.move_left))

    def test_result_8_move_up(self):
        """
        (1, 2, 3, 4, 5, 6, 7, 8, None) -> up -> (1, 2, 3, 4, 5, None, 7, 8, 6)
        """
        problem = EightPuzzleProblem(None, None, EightPuzzleTransitionModel())
        self.assertEqual((1, 2, 3, 4, 5, None, 7, 8, 6), problem.result((1, 2, 3, 4, 5, 6, 7, 8, None), EightPuzzleAgent.move_up))


    """
    action_cost
    """

    def test_action_cost_is_always_1(self):
        """
        The action_cost method just naively returns 1 out of convenience since
        each action in the eight puzzle has a cost of 1.
        """
        problem = EightPuzzleProblem(None, None, None)
        self.assertEqual(1, problem.action_cost(None, None, None))


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
