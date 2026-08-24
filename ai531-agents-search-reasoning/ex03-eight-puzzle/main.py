# Main
# Carson Hansen
# Demonstrate the use of your EightPuzzleAgent.


#I used this website to generate all my inital and goal states.
#It provides random solvable and unsolvable puzzles
#https://8-puzzle.streamlit.app/




from eight_puzzle_agent import EightPuzzleAgent
from eight_puzzle_transition_model import EightPuzzleTransitionModel
from eight_puzzle_problem import EightPuzzleProblem
from eight_puzzle_best_first_search_solver import EightPuzzleBestFirstSearchSolver

#Starting at the goal state. Should not print anything.
print("Starting first test")
initial_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
goal_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
transition_model = EightPuzzleTransitionModel()

problem = EightPuzzleProblem(initial_state, goal_state, transition_model)
solver = EightPuzzleBestFirstSearchSolver()
agent = EightPuzzleAgent(initial_state, transition_model, solver.solution(problem))

while agent.has_actions():
    action = agent.action()
    action(agent)
   



print("\n\nStarting second test\n")
initial_state = (8,5,4,6,None,1,2,3,7)
goal_state = (1,None,3,2,4,5,6,7,8)
problem = EightPuzzleProblem(initial_state, goal_state, transition_model)
agent = EightPuzzleAgent(initial_state, transition_model, solver.solution(problem))

while agent.has_actions():
    action = agent.action()
    action(agent)



print("\n\nStarting third test\n")
initial_state = (None,7,4,2,5,8,6,1,3)
goal_state = (1,None,3,2,4,5,6,7,8)
problem = EightPuzzleProblem(initial_state, goal_state, transition_model)
agent = EightPuzzleAgent(initial_state, transition_model, solver.solution(problem))

while agent.has_actions():
    action = agent.action()
    action(agent)



print("\n\nStarting Fourth test\n")
initial_state = (3,2,6,7,5,8,1,None,4)
goal_state = (1,None,3,2,4,5,6,7,8)
problem = EightPuzzleProblem(initial_state, goal_state, transition_model)
agent = EightPuzzleAgent(initial_state, transition_model, solver.solution(problem))

while agent.has_actions():
    action = agent.action()
    action(agent)


#this one is unsolvable and should do nothing
print("\n\nStarting Fifth test\n")
initial_state = (1,None,3,2,4,5,6,7,8)
goal_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
problem = EightPuzzleProblem(initial_state, goal_state, transition_model)
agent = EightPuzzleAgent(initial_state, transition_model, solver.solution(problem))

while agent.has_actions():
    action = agent.action()
    action(agent)