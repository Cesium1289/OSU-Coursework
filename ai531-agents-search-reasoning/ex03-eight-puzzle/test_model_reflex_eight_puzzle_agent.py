# DO NOT MODIFY THE CODE IN THE TESTS
# Run me via: python3 -m unittest test_model_reflex_eight_puzzle_agent

import unittest
import time
from model_reflex_eight_puzzle_agent import ModelReflexEightPuzzleAgent
from contrived_eight_puzzle_transition_model import ContrivedEightPuzzleTransitionModel


class TestModelReflexEightPuzzleAgent(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A ModelReflexEightPuzzleAgent exists.
        """
        try:
            ModelReflexEightPuzzleAgent(None, None, None, None)
        except NameError:
            self.fail("Could not instantiate ModelReflexEightPuzzleAgent")

    """
    Properties
    """

    def test_initial_state(self):
        """
        An ModelReflexEightPuzzleAgent has an `initial_state` property
        """
        agent = ModelReflexEightPuzzleAgent("Fake State", None, None, None)
        self.assertEqual("Fake State", agent.initial_state)

    def test_goal_state(self):
        """
        An ModelReflexEightPuzzleAgent has a `goal_state` property
        """
        agent = ModelReflexEightPuzzleAgent(None, "Goal State", None, None)
        self.assertEqual("Goal State", agent.goal_state)

    def test_action_cost(self):
        """
        An ModelReflexEightPuzzleAgent has an `action_cost` property
        """
        agent = ModelReflexEightPuzzleAgent(None, None, 42, None)
        self.assertEqual(42, agent.action_cost)

    def test_transition_model(self):
        """
        An ModelReflexEightPuzzleAgent has a `transition_model` property
        """
        agent = ModelReflexEightPuzzleAgent(None, None, None, "Fake Transition Model")
        self.assertEqual("Fake Transition Model", agent.transition_model)

    def test_current_state(self):
        """
        An ModelReflexEightPuzzleAgent has a `current_state` property that is the same as the
        `initial_state` when first instantiated.
        """
        agent = ModelReflexEightPuzzleAgent("Fake State", None, None, None)
        self.assertEqual("Fake State", agent.current_state)

    def test_total_cost(self):
        """
        An ModelReflexEightPuzzleAgent has a `total_cost` property that is initially 0.
        """
        agent = ModelReflexEightPuzzleAgent(None, None, None, None)
        self.assertEqual(0, agent.total_cost)

    """
    Actions (agent function)
    """

    def test_noop_when_at_goal(self):
        """
        The action is `noop` if the agent is at the goal state.
        """
        initial_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
        goal_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
        action_cost = 1
        agent = ModelReflexEightPuzzleAgent(initial_state, goal_state, action_cost, None)
        self.assertEqual(agent.noop, agent.action())

    def test_move_left_when_1_None_2_3_4_5_6_7_8(self):
        """
        The action is `move_left` if the state is (1, None, 2, 3, 4, 5, 6, 7, 8)
        """
        initial_state = (1, None, 2, 3, 4, 5, 6, 7, 8)
        goal_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
        action_cost = 1
        agent = ModelReflexEightPuzzleAgent(initial_state, goal_state, action_cost, None)
        self.assertEqual(agent.move_left, agent.action())

    def test_move_up_when_3_1_2_None_4_5_6_7_8(self):
        """
        The action is `move_up` if the state is (3, 1, 2, None, 4, 5, 6, 7, 8)
        """
        initial_state = (3, 1, 2, None, 4, 5, 6, 7, 8)
        goal_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
        action_cost = 1
        agent = ModelReflexEightPuzzleAgent(initial_state, goal_state, action_cost, None)
        self.assertEqual(agent.move_up, agent.action())


    """
    End-to-end tests
    """

    def test_starting_at_goal(self):
        """
        The total cost of starting at the goal is 0.
        """
        initial_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
        goal_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
        action_cost = 1
        agent = ModelReflexEightPuzzleAgent(initial_state, goal_state, action_cost, None)
        while not agent.in_goal_state():
            action = agent.action()
            action()
        self.assertEqual(0, agent.total_cost)

    def test_starting_at_one_step_away(self):
        """
        The total cost of starting one step away from the goal is 1.
        """
        initial_state = (1, None, 2, 3, 4, 5, 6, 7, 8)
        goal_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
        action_cost = 1
        transition_model = ContrivedEightPuzzleTransitionModel()
        agent = ModelReflexEightPuzzleAgent(initial_state, goal_state, action_cost, transition_model)
        while not agent.in_goal_state():
            action = agent.action()
            action()
        self.assertEqual(1, agent.total_cost)


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
