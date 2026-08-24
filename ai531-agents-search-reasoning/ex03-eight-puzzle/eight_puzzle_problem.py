# EightPuzzleProblem: A representation of the Eight Puzzle as a search problem,
# with properties specified by Russell & Norvig. A problem has an initial state,
# a goal state and a transition model. It can produce possible actions for a node
# in the search graph. It can use its transition model to produce the new state
# that is the result of applying an action to a state. It has an action cost
# function that produces the cost of applying an action.
# Abstractly, it also represents the complete state space of the problem
# environment.

from eight_puzzle_agent import EightPuzzleAgent

class EightPuzzleProblemException(Exception):
    pass


class EightPuzzleProblem:

    def __init__(self, initial_state, goal_state, transition_model):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.transition_model = transition_model

    def is_goal(self, state):
        return state == self.goal_state

    def actions(self, state):
        match state.index(None):
            case 0:
                return [EightPuzzleAgent.move_right, EightPuzzleAgent.move_down]
            case 1:
                return [EightPuzzleAgent.move_left, EightPuzzleAgent.move_right, EightPuzzleAgent.move_down]
            case 2:
                return [EightPuzzleAgent.move_left, EightPuzzleAgent.move_down]
            case 3:
                return [EightPuzzleAgent.move_right, EightPuzzleAgent.move_up, EightPuzzleAgent.move_down]
            case 4:
                return [EightPuzzleAgent.move_left, EightPuzzleAgent.move_right, EightPuzzleAgent.move_up, EightPuzzleAgent.move_down]
            case 5:
                return [EightPuzzleAgent.move_left, EightPuzzleAgent.move_up, EightPuzzleAgent.move_down]
            case 6:
                return [EightPuzzleAgent.move_right, EightPuzzleAgent.move_up]
            case 7:
                return [EightPuzzleAgent.move_left, EightPuzzleAgent.move_right, EightPuzzleAgent.move_up]
            case 8:
                return [EightPuzzleAgent.move_left, EightPuzzleAgent.move_up]
            case _:
                raise EightPuzzleProblemException("Empty tile not found within state.")

    def result(self, state, action):
        match action:
            case EightPuzzleAgent.move_left:
                return self.transition_model.move_left(state)
            case EightPuzzleAgent.move_right:
                return self.transition_model.move_right(state)
            case EightPuzzleAgent.move_up:
                return self.transition_model.move_up(state)
            case EightPuzzleAgent.move_down:
                return self.transition_model.move_down(state)
            case _:
                raise EightPuzzleProblemException("Action was not left, right, up or down.")

    def action_cost(self, state, action, result_state):
        return 1
        