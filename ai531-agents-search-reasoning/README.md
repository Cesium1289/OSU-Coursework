# AI 531: Agents, Search, and Reasoning

Coursework for AI 531 (Oregon State University), covering intelligent agent design, search algorithms, and reasoning under uncertainty, following the AIMA (Russell & Norvig) textbook structure.

## Exercises

| Exercise | Topic | Result |
|---|---|---|
| [ex01-warmup](ex01-warmup/) | Course tools/workflow warmup: stub out a naive Vacuum class API using `pass` | 6/6 tests passing |
| [ex02-vacuum-world](ex02-vacuum-world/) | Simple reflex agent and model-based reflex agent design, implemented as a two-location robot vacuum (AIMA Ch. 2) | 56/56 tests passing across all 7 suites, including the optional model-based agent test suite |
| [ex03-eight-puzzle](ex03-eight-puzzle/) | Goal-based agent and A* search (best-first search + misplaced-tiles heuristic) for solving the eight-puzzle (AIMA Ch. 3) | 107/107 tests passing across all 5 suites; solves all four "harder" stress-test states in under 3s each |
| [ex05-tic-tac-toe](ex05-tic-tac-toe/) | Game-playing agent using the minimax algorithm for adversarial search (AIMA Ch. 5) | 85/85 tests passing; 0 losses in 50 games against a random opponent; minimax-vs-minimax ends in a draw as expected |

There is no Exercise 4 in this course; numbering goes directly from Exercise 3 to Exercise 5. That exercise number was never assigned, this isn't a missing submission.
