# Exercise 3: Eight-Puzzle

**Course:** AI 531 (Agents, Search, and Reasoning), Oregon State University
**Assignment:** Canvas exercise, [course site](https://canvas.oregonstate.edu/courses/2030143) (Canvas requires OSU login; original instructions are preserved in [`EXERCISE_INSTRUCTIONS.md`](EXERCISE_INSTRUCTIONS.md))
**Task:** Implement a goal-based, problem-solving agent that solves the classic eight-puzzle (a 3x3 sliding tile puzzle) using A* search, following AIMA (Russell & Norvig) Chapter 3. The puzzle state is represented as a 9-tuple, with `None` standing in for the blank tile. This exercise builds on Exercise 2's agent design work by shifting from reflex agents to a goal-based agent that emits a pre-computed solution one action at a time, and from ad hoc rules to formal search.

The exercise has two steps:
1. Complete `EightPuzzleAgent`: an "open loop" goal-based agent that holds a list of actions (produced elsewhere, by the solver) and emits them one at a time via `action()`. Each actuator (`move_left`, `move_right`, `move_up`, `move_down`) updates the agent's internal state using the provided transition model. Required, test-driven against `test_eight_puzzle_agent.py`.
2. Complete `EightPuzzleBestFirstSearchSolver`: an A* search implementation, meaning `BEST-FIRST-SEARCH` (AIMA figure) plus an evaluation function f(n) = g(n) + h(n), where g is path cost so far and h is a heuristic estimate of the remaining cost. This submission uses a misplaced-tiles heuristic (count of tiles not in their goal position, ignoring the blank). Required, test-driven against `test_eight_puzzle_best_first_search_solver.py`.

## Results

All 5 test suites required by this exercise pass, 107 tests total:

| Test suite | Tests | Result |
|---|---|---|
| `test_eight_puzzle_node` | 7 | pass |
| `test_eight_puzzle_transition_model` | 37 | pass |
| `test_eight_puzzle_problem` | 40 | pass |
| `test_eight_puzzle_agent` | 17 | pass |
| `test_eight_puzzle_best_first_search_solver` | 6 | pass |

The bundled-but-not-required `test_model_reflex_eight_puzzle_agent.py` (see the section below on `model_reflex_eight_puzzle_agent.py`) is not part of this exercise's requirements; it's noted separately since it fails 1 of its 12 tests, by design, as it's deliberately incomplete provided code.

`main.py` runs five demonstration cases (already-at-goal, two moderately-challenging states, one requiring a longer solution, and one deliberately unsolvable state) in under 4 seconds total. The already-at-goal and unsolvable cases both correctly produce no actions and no errors, confirmed by rerunning the script:

| Case | Result |
|---|---|
| Already at goal state | 0 actions (no output), as expected |
| Moderately challenging state (2nd test) | 25 actions |
| Moderately challenging state (3rd test) | 21 actions |
| Longer-solution state (4th test) | 26 actions |
| Deliberately unsolvable state (5th test) | 0 actions (no output), as expected |

The README also calls out four specific "harder" states to stress-test the solver against, with a warning to "give your solver some time to think." Timed by directly instantiating the solver against each:

| State | Solution length | Time |
|---|---|---|
| `7 2 4 / 5 . 6 / 8 3 1` | 26 actions | 0.76s |
| `8 . 6 / 5 4 7 / 2 3 1` | 31 actions | 2.18s |
| `8 6 7 / 2 5 4 / 3 . 1` | 27 actions | 0.75s |
| `6 4 7 / 8 5 . / 3 2 1` | 25 actions | 0.37s |

All four solve in a few seconds at most on this machine, using the misplaced-tiles heuristic. The assignment's extension section suggests also trying a Manhattan-distance heuristic and comparing computation time; that comparison isn't implemented here (see "Extensions not attempted" below).

## Repo layout

Kept flat, same reasoning as Exercises 1 and 2: the test files import modules directly by name and are meant to run via `python3 -m unittest test_X` from the same directory.

```
ex03-eight-puzzle/
├── EXERCISE_INSTRUCTIONS.md              # original assignment README from Canvas, unmodified
├── eight_puzzle_node.py                  # EightPuzzleNode: state, parent, action, path_cost (provided)
├── eight_puzzle_transition_model.py      # movement rules for the 3x3 sliding puzzle (provided)
├── eight_puzzle_problem.py               # EightPuzzleProblem: actions, result, action_cost (provided)
├── eight_puzzle_agent.py                 # goal-based agent that emits actions (student-implemented)
├── eight_puzzle_best_first_search_solver.py  # A* search + misplaced-tiles heuristic (student-implemented)
├── main.py                               # five demonstration cases, incl. unsolvable state
├── scratchpad.py                         # informal exploration script, not graded
├── test_eight_puzzle_node.py             # provided, do not modify
├── test_eight_puzzle_transition_model.py # provided, do not modify
├── test_eight_puzzle_problem.py          # provided, do not modify
├── test_eight_puzzle_agent.py            # provided, do not modify
├── test_eight_puzzle_best_first_search_solver.py  # provided, do not modify
├── model_reflex_eight_puzzle_agent.py    # provided, deliberately incomplete reference code (see below)
├── contrived_eight_puzzle_transition_model.py  # provided, minimal stub transition model (see below)
├── model_reflex_scratchpad.py            # informal exploration script for the model-reflex reference code
└── test_model_reflex_eight_puzzle_agent.py  # provided, do not modify
```

## How to reproduce

```bash
# Run any individual test suite
python3 -m unittest test_eight_puzzle_agent
python3 -m unittest test_eight_puzzle_best_first_search_solver

# Run everything
python3 -m unittest discover -p "test_*.py"

# See the agent solve five puzzles, including one unsolvable one
python3 main.py
```

No dependencies beyond the Python standard library (`unittest`, `queue.PriorityQueue`).

## Notes on the implementation

**`EightPuzzleAgent`** is intentionally simple: it holds a list of already-computed actions and pops them off one at a time via `action()`, returning `None` once exhausted. It does no reasoning of its own; all the intelligence lives in the solver. This is the "open loop" goal-based agent design the assignment asks for: plan once, then blindly execute the plan.

**`EightPuzzleBestFirstSearchSolver`** implements `BEST-FIRST-SEARCH` with a `PriorityQueue` of `(f-value, node)` tuples, an `explored` set to avoid re-expanding states, and a `best` dict tracking the lowest known path cost per state so a cheaper path to an already-frontier state can replace a costlier one. The evaluation function `cost_so_far_plus_estimated_cost_remaining` computes g(n) directly from `node.path_cost` and h(n) by counting misplaced tiles against `problem.goal_state`, skipping the blank tile (a blank "out of place" isn't a meaningful part of the heuristic).

## `model_reflex_eight_puzzle_agent.py` and related files

`model_reflex_eight_puzzle_agent.py`, `contrived_eight_puzzle_transition_model.py`, `test_model_reflex_eight_puzzle_agent.py`, and `model_reflex_scratchpad.py` came bundled with the rest of this exercise's files but aren't mentioned anywhere in `EXERCISE_INSTRUCTIONS.md` or referenced in the Canvas assignment text, and aren't part of Step 1 or Step 2 as described there. They're included here for completeness since they were part of the original download.

This code is genuinely incomplete, confirmed by running its own test suite: 11 of 12 tests in `test_model_reflex_eight_puzzle_agent.py` pass, but `action()` only ever returns `move_left` or `noop` and never implements `move_up` (despite `move_up` existing as a method), so it fails the one test that expects a `move_up` action. This matches the file's own docstring, which describes it as "a basic, **incomplete** model-based reflex agent." It reads as provided-but-unfinished reference or preview code, similar in spirit to `insufficient_model_reflex_vacuum.py` from Exercise 2, just not called out explicitly in this exercise's README the way that one was.

## Extensions not attempted

The assignment lists four optional extensions: printing the puzzle as a 3x3 grid instead of raw tuples, comparing a misplaced-tiles heuristic against a Manhattan-distance heuristic (including timing), fuller unit test coverage of the solver's own methods, and an iterative-deepening search variant. None of these are implemented here; this submission uses the misplaced-tiles heuristic only and meets the base requirements.
