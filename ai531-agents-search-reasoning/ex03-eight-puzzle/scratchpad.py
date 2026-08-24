# Eight Puzzle Agent Scratchpad
# Carson Hansen
# Use this as a "scratchpad" to tinker with your code.
# There are no rules here, and this code will not be evaluated. This file is a
# place for you to experiment.


from eight_puzzle_agent import EightPuzzleAgent
from eight_puzzle_transition_model import EightPuzzleTransitionModel
from eight_puzzle_problem import EightPuzzleProblem
from eight_puzzle_best_first_search_solver import EightPuzzleBestFirstSearchSolver

# Starting at the goal state. Should not print anything.
initial_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
goal_state = (5, 1, 2, 3, 4, None, 6, 7, 8)
transition_model = EightPuzzleTransitionModel()

problem = EightPuzzleProblem(initial_state, goal_state, transition_model)
solver = EightPuzzleBestFirstSearchSolver()
agent = EightPuzzleAgent(initial_state, transition_model, solver.solution(problem))

while agent.has_actions():
    action = agent.action()
    action(agent)
