# Exercise 3: Eight-Puzzle

Demonstrate your comprehension of the A* algorithm, evaluation functions with
heuristics, and goal-based agents. Build an agent that can solve an eight-puzzle
problem.

## What to Do

Implement an EightPuzzleAgent that is a goal-based, problem-solving agent, and
implement a complete EightPuzzleBestFirstSearchSolver that uses the A* algorithm
to generate a solution for the agent to emit. Your implementation should honor the
specficiations of the Problem and Node concepts in the AIMA book. Your implementation
should honor the specification of the BEST-FIRST-SEARCH function and the EXPAND
function found in the AIMA book. Use the concept of an eight-puzzle problem as a
search problem for the domain of your implementation.

## Instructions

We recommend pursuing this exercise in two steps: first is implementing the agent,
and then implementing the solver.

### Step 1: EightPuzzleAgent

Complete the implementation of EightPuzzleAgent found in *eight_puzzle_agent.py*,
and use the test suite in *test_eight_puzzle_agent.py* to guide and verify your
implementation. The agent should reflect the architecture of a goal-based,
problem-solving agent that is "open loop" and merely produces each subsequent,
individual action when asked, via the `action` method.

Each of the four actuator methods, such as `move_left`, should use the transition
model to produce a new state to update `current_state`.

You'll know this is complete when the tests found in *test_eight_puzzle_agent.py*
all pass. Run the test suite with `python3 test_eight_puzzle_agent.py`. Note that,
in the test suite, we hand-feed a list of explicit actions to the EightPuzzleAgent.
However, in real use, the actions provided to the agent should be produced by an
EightPuzzleBestFirstSearchSolver.

### Step 2: EightPuzzleBestFirstSearchSolver

If you take a look at *scratchpad.py*, you will find an example of instantiating
an EightPuzzleProblem and an EightPuzzleBestFirstSearchSolver. Notice that the
solver's `solution` is used upon instantiating an EightPuzzleAgent.

All that is left for you to do is to make `solution` a reality. To do this, you
will need to codify the specification of BEST-FIRST-SEARCH found in the AIMA book.
If you look at *eight_puzzle_best_first_search_solver.py*, you will find the
skeleton of the EightPuzzleBestFirstSearchSolver class. You will need to implement:

- `best_first_search`, per the BEST-FIRST-SEARCH function specification
- `expand`, per the EXPAND function specification
- `cost_so_far_plus_estimated_cost_remaining`, which is your evaluation function, **f**
- `actions_to_reach_solution_node`, a helper method for producing a list of actions to reach a node

You can add helper methods, such as your heuristic functions, to the
EightPuzzleBestFirstSearchSolver class, if you wish.

Note that the EightPuzzleTransitionModel, EightPuzzleProblem, and EightPuzzleNode
are provided for you. See their implementations in their respective *.py* files.
Each class has a corresponding *test_\*.py* file to provide more details. See
the sample code in *scratchpad.py* for examples of usage.

There are some unit tests in *test_eight_puzzle_best_first_search_solver.py*, that
test a few initial simple cases. Try making sure that your solver passes the tests
for these simple cases before trying more complex ones.

Try coming up with some moderately challenging states on your own to test out
your solver, such as states that require a solution of five to ten actions. Remember,
there are many initial states of an EightPuzzle that are not solvable for our
desired goal state, so you shouldn't just produce a random state to test.

After solving a few moderately challenging states, see how well your solver works
on the following states, which produce longer solutions.

```
7 2 4
5 . 6
8 3 1

8 . 6
5 4 7
2 3 1

8 6 7
2 5 4
3 . 1

6 4 7
8 5 .
3 2 1
```

Give your solver some time to 'think' on these!

You'll know you are done when:

1. Your EightPuzzleBestFirstSearchSolver passes the tests in *test_eight_puzzle_best_first_search_solver.py*.
2. You write four example problem-solving demos in _main.py_. (See *scratchpad.py* for inspiration.)

## Notes and Hints

Be sure to review the structure and specification of a problem, agent, search
algorithm, evaluation function, and heuristic function as specified in the AIMA book.

Look at *scratchpad.py* to get a sense of how to create and use the different
pieces of the overall problem-solving workflow.

Look at the tests found in each *test_\*.py* file for the EightPuzzleNode,
EightPuzzleProblem, and EightPuzzleTransitionModel. The tests both describe these
concepts in line with the AIMA book specification, and illustrate how they are used.
The good news is, each of these components are complete, and you can use them in
your EightPuzzleBestFirstSearchSolver.

You will notice that, in this exercise, we do something interesting when invoking
each action:

```
while agent.has_actions():
    action = eight_puzzle_agent.action()
    action(agent)
    #      ^^^^^
```

Notice that we are passing the actuator method, `action`, the `agent` instance
when invoking the method. This is necessary to satisfy the Python runtime. The
EightPuzzleProblem `action` method produces lists of actions in the form of
`EightPuzzleAgent.method_name`. Because we are referencing these action methods
via the class name, and not within an instance of an EightPuzzleAgent, we must
satisfy the Python runtime by passing an EightPuzzleAgent object as the `self`
argument to these methods. We are still just invoking those actuator methods.
We are merely passing along `agent` in order to satisfy the Python interpreter.

If you use a queue.PriorityQueue in your EightPuzzleBestFirstSearchSolver, do not
only `put` the EightPuzzleNode objects directly in the queue. Use a tuple, in the
form of:

```
(cost, node)
```

For example:

```
frontier.put( (23, n) )  # n is an EightPuzzleNode instance
```

This will let you conveniently pop elements off the queue with the lowest cost first,
should you find that necessary.

&copy; 2023 Yong Joseph Bakos. All rights reserved.
