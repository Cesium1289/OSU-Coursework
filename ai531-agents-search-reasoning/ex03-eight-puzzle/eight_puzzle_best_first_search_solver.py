# EightPuzzleBestFirstSearchSolver: A problem solver for the eight-puzzle problem
# that can apply best-first search to find a solution node. This class encapsulates
# a best-first search algorithm and an evaluation function. It encapsulates the
# application of the algorithm to the problem, and in the end can produce a
# solution, which is a list of actions.
# Carson Hansen


from queue import PriorityQueue
from eight_puzzle_node import EightPuzzleNode

class EightPuzzleBestFirstSearchSolver:

    def solution(self, problem):
        """
        Return a list of EightPuzzleAgent actuator methods. If the problem
        initial state is the same as the goal state, return an empty list.
        """
        solution_node = self.best_first_search(problem,
            self.cost_so_far_plus_estimated_cost_remaining)
        if solution_node:
            return self.actions_to_reach_solution_node(solution_node)
        else:
            return None

    def best_first_search(self, problem, evaluation_function):
        """
        Return a solution EightPuzzleNode, or None to indicate failure.
        """
        root = EightPuzzleNode(problem.initial_state, None, None, 0)
        if problem.is_goal(root.state):
            return root
        
        frontier = PriorityQueue()
        frontier.put((evaluation_function(problem,root),root))

        explored = set()

        best = {root.state: 0}
        while not frontier.empty():
            _, node = frontier.get()

            #check if node has been explored
            if node.state in explored:
                continue

            #check if we found a solution
            if problem.is_goal(node.state):
                return node
            
            #add node to explored list
            explored.add(node.state)
            
            #keep exploring
            for child in self.expand(problem,node):
                #check if child has already been explored
                if child.state in explored:
                    continue
            
                #check and update if a better cost was found
                prev_best = best.get(child.state)
                if prev_best is None or child.path_cost < prev_best:
                    best[child.state] = child.path_cost
                    frontier.put((evaluation_function(problem,child),child))
        return None


    def expand(self, problem, node):
        """
        Return a list of EightPuzzleNodes that are reachable from `node`.
        """
        childern = []
        for action in problem.actions(node.state):
            child_state = problem.result(node.state,action)
            cost = problem.action_cost(node.state,action,child_state)
            child = EightPuzzleNode(child_state,node,action,node.path_cost + cost)
            childern.append(child)
        return childern

    def cost_so_far_plus_estimated_cost_remaining(self, problem, node):
        """
        The evaluation function, f(n) = g(n) + h(n).
        """

        g = node.path_cost
        goal = problem.goal_state

        h = 0
        for i, tile in enumerate(node.state):
            if tile is None:
                continue
            if tile != goal[i]:
                h += 1

        return g + h
        

    def actions_to_reach_solution_node(self, solution_node):
        """
        Given an EightPuzzleNode goal node, produce a list of in-order actions
        that lead from the initial state to the goal state.
        """
        actions = []
        n = solution_node

        #reverse the list to get the actions the agent must take to get to its goal
        while n.parent is not None:
            actions.append(n.action)
            n = n.parent
        actions.reverse()
        return actions
    
    