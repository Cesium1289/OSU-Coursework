# DO NOT MODIFY THE CODE IN THE TESTS
# Run me via: python3 -m unittest test_eight_puzzle_agent

import unittest
import time
from eight_puzzle_agent import EightPuzzleAgent
from eight_puzzle_transition_model import EightPuzzleTransitionModel


class TestEightPuzzleAgent(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A EightPuzzleAgent exists.
        """
        try:
            EightPuzzleAgent(None, None, None)
        except NameError:
            self.fail("Could not instantiate EightPuzzleAgent")

    """
    Properties
    """

    def test_current_state(self):
        """
        An EightPuzzleAgent has an `current_state` property.
        """
        agent = EightPuzzleAgent("Fake State", None, None)
        self.assertEqual("Fake State", agent.current_state)

    def test_transition_model(self):
        """
        An EightPuzzleAgent has a `transition_model` property.
        """
        agent = EightPuzzleAgent(None, "Fake Transition Model", None)
        self.assertEqual("Fake Transition Model", agent.transition_model)

    def test_actions(self):
        """
        An EightPuzzleAgent has an `actions` property.
        """
        agent = EightPuzzleAgent(None, None, "Fake List of Actions")
        self.assertEqual("Fake List of Actions", agent.actions)

    """
    Behaviors
    """

    def test_has_actions(self):
        """
        An EightPuzzleAgent has actions if its list of actions is not empty.
        """
        agent = EightPuzzleAgent(None, None, ["Fake Action"])
        self.assertTrue(agent.has_actions())

    def test_has_no_actions(self):
        """
        An EightPuzzleAgent has no actions if its list of actions is empty.
        """
        agent = EightPuzzleAgent(None, None, [])
        self.assertFalse(agent.has_actions())

    """
    Actuators
    """

    def test_move_left(self):
        pass

    def test_move_right(self):
        pass

    def test_move_up(self):
        pass

    def test_move_down(self):
        pass


    """
    Actions (agent function)
    """

    def test_action(self):
        """
        An EightPuzzleAgent produces an action from its non-empty list of actions.
        """
        agent = EightPuzzleAgent(None, None, ["Fake Action"])
        self.assertEqual("Fake Action", agent.action())

    def test_action_none(self):
        """
        An EightPuzzleAgent produces None from when it has an empty list of actions.
        """
        agent = EightPuzzleAgent(None, None, [])
        self.assertIsNone(agent.action())

    def test_action_pop(self):
        """
        An EightPuzzleAgent action method removes the first action from the list of actions.
        """
        agent = EightPuzzleAgent(None, None, ["First Action", "Second Action"])
        agent.action()
        self.assertEqual(["Second Action"], agent.actions)

    """
    End-to-end tests for a few simple solutions.
    """

    def test_starting_at_goal(self):
        """
        After completing all actions, the current_state is the goal state.
        """
        initial_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
        goal_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
        transition_model = EightPuzzleTransitionModel()
        actions = []
        agent = EightPuzzleAgent(initial_state, transition_model, actions)
        while agent.has_actions():
            action = agent.action()
            action(agent)
        self.assertEqual(goal_state, agent.current_state)

    def test_starting_at_1_None_2_3_4_5_6_7_8(self):
        """
        After completing all actions, the current_state is the goal state.
        """
        initial_state = (1, None, 2, 3, 4, 5, 6, 7, 8)
        goal_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
        transition_model = EightPuzzleTransitionModel()
        actions = [EightPuzzleAgent.move_left]
        agent = EightPuzzleAgent(initial_state, transition_model, actions)
        while agent.has_actions():
            action = agent.action()
            action(agent)
        self.assertEqual(goal_state, agent.current_state)

    def test_starting_at_1_2_None_3_4_5_6_7_8(self):
        """
        After completing all actions, the current_state is the goal state.
        """
        initial_state = (1, 2, None, 3, 4, 5, 6, 7, 8)
        goal_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
        transition_model = EightPuzzleTransitionModel()
        actions = [EightPuzzleAgent.move_left, EightPuzzleAgent.move_left]
        agent = EightPuzzleAgent(initial_state, transition_model, actions)
        while agent.has_actions():
            action = agent.action()
            action(agent)
        self.assertEqual(goal_state, agent.current_state)

    def test_starting_at_3_1_2_6_4_5_None_7_8(self):
        """
        After completing all actions, the current_state is the goal state.
        """
        initial_state = (3, 1, 2, 6, 4, 5, None, 7, 8)
        goal_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
        transition_model = EightPuzzleTransitionModel()
        actions = [EightPuzzleAgent.move_up, EightPuzzleAgent.move_up]
        agent = EightPuzzleAgent(initial_state, transition_model, actions)
        while agent.has_actions():
            action = agent.action()
            action(agent)
        self.assertEqual(goal_state, agent.current_state)


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
