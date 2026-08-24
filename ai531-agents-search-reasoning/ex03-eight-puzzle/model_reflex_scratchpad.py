# Eight Puzzle Agent Scratchpad
# YOUR NAME
# Use this as a "scratchpad" to tinker with your code.
# There are no rules here, and this code will not be evaluated. This file is a
# place for you to experiment.


from model_reflex_eight_puzzle_agent import ModelReflexEightPuzzleAgent
from contrived_eight_puzzle_transition_model import ContrivedEightPuzzleTransitionModel

initial_state = (1, None, 2, 3, 4, 5, 6, 7, 8)
goal_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
action_cost = 1

transition_model = ContrivedEightPuzzleTransitionModel()

eight_puzzle_agent = ModelReflexEightPuzzleAgent(initial_state, goal_state, action_cost, transition_model)

while not eight_puzzle_agent.in_goal_state():
    action = eight_puzzle_agent.action()
    action()

print(eight_puzzle_agent.report())
