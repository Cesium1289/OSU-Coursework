# ModelReflexEightPuzzleAgent: A basic, incomplete model-based reflex agent that
# tries to produce actions for solving an eight-puzzle problem.
# See the tests in test_model_reflex_eight_puzzle_agent.py.
# YOUR NAME


class ModelReflexEightPuzzleAgent:

    def __init__(self, initial_state, goal_state, action_cost, transition_model):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.action_cost = action_cost
        self.transition_model = transition_model
        self.current_state = self.initial_state
        self.total_cost = 0

    def in_goal_state(self):
        return self.current_state == self.goal_state

    def report(self):
        return f"Total Cost: {self.total_cost}"

    def noop(self):
        pass

    def move_left(self):
        self.current_state = self.transition_model.move_left(self.current_state)
        self.total_cost += 1

    def move_up(self):
        self.current_state = self.transition_model.move_up(self.current_state)
        self.total_cost += 1

    def action(self):
        if self.current_state == self.goal_state:
            return self.noop
        else:
            return self.move_left
