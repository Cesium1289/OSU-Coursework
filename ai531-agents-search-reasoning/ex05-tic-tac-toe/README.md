# Exercise 5: Tic-Tac-Toe

**Course:** AI 531 (Agents, Search, and Reasoning), Oregon State University
**Assignment:** [Canvas exercise](https://canvas.oregonstate.edu/courses/2030143) (login required; instructions preserved in [`EXERCISE_INSTRUCTIONS.md`](EXERCISE_INSTRUCTIONS.md)), starter code from [osu-ai531-w24/exercise05-tic-tac-toe](https://github.com/osu-ai531-w24/exercise05-tic-tac-toe)
**Task:** Build a game-playing agent that plays tic-tac-toe using the minimax algorithm, following AIMA (Russell & Norvig)'s treatment of adversarial search and games. This shifts from single-agent search (Exercise 3's eight-puzzle) to a two-player, zero-sum, perfect-information game, where the agent has to plan around an opponent actively working against it rather than just navigating toward a fixed goal.

Two things needed completing:
1. `TicTacToeGame.utility(state, player)`: the objective function, returning 1 if `player` has won, -1 if the other player has won, 0 otherwise. Everything else in `TicTacToeGame` (state representation, `actions`, `result`, `is_terminal`, `to_move`, `is_win`) was provided.
2. `MinimaxTicTacToeAgent`: a full implementation of `MINIMAX-SEARCH` (the top-level `minimax` method plus mutually recursive `max_value`/`min_value` helpers), honoring the AIMA specification. Alpha-beta pruning was explicitly optional; this submission uses plain minimax without pruning.

## Results

All required test suites pass, 85 tests total:

| Test suite | Tests | Result |
|---|---|---|
| `test_tic_tac_toe_board_renderer` | 6 | pass |
| `test_tic_tac_toe_game` | 65 | pass |
| `test_random_tic_tac_toe_agent` | 6 | pass |
| `test_human_tic_tac_toe_agent` | 4 | pass |
| `test_minimax_tic_tac_toe_agent` | 4 | pass |

`test_human_tic_tac_toe_agent.py`'s `test_action` is genuinely interactive: it prints `"TEST: input a 1"` and blocks on real keyboard input, since `HumanTicTacToeAgent` reads moves from `input()` by design. Running it with no stdin attached hangs; running it non-interactively requires piping in the expected value:

```bash
echo "1" | python3 -m unittest test_human_tic_tac_toe_agent
```

All 4 tests in that suite pass when run this way. This isn't a bug, just something to know before running the full suite unattended (e.g. `python3 -m unittest discover` will also hang on this one test without input piped in).

### Verifying minimax actually plays correctly

Beyond the provided unit tests (which only check a few individual states), I ran two automated games to confirm the agent's actual play quality, not just its test-suite compliance:

- **50 games, `MinimaxTicTacToeAgent` (O, second) vs. `RandomTicTacToeAgent` (X, first):** 39 wins, 11 draws, **0 losses**. A correct minimax agent should never lose regardless of the opponent's strategy, and it didn't.
- **`MinimaxTicTacToeAgent` vs. itself, from an empty board:** ended in a draw (`X|X|O / O|O|X / X|O|X`), the expected outcome of tic-tac-toe under perfect play from both sides. Took about **4.9 seconds** to complete the full game, since this implementation searches the entire game tree from the empty board with no pruning or memoization, exploring on the order of hundreds of thousands of terminal states for the opening move alone. This is fine for tic-tac-toe's small state space but is the kind of cost the optional alpha-beta extension exists to cut down.

## Repo layout

Kept flat, same reasoning as prior exercises: the test files import modules directly by name and are meant to run via `python3 -m unittest test_X` from the same directory.

```
ex05-tic-tac-toe/
├── EXERCISE_INSTRUCTIONS.md          # original assignment README from Canvas, unmodified
├── tic_tac_toe_game.py               # Game: state, transition model, utility (student completed `utility`)
├── tic_tac_toe_board_renderer.py     # renders board state as text (provided)
├── human_tic_tac_toe_agent.py        # reads a move from stdin (provided)
├── random_tic_tac_toe_agent.py       # picks a uniformly random legal move (provided)
├── minimax_tic_tac_toe_agent.py      # MINIMAX-SEARCH implementation (student-implemented)
├── main.py                           # play a full game: you (X) vs. MinimaxTicTacToeAgent (O)
├── scratchpad.py                     # play a full game: you (X) vs. RandomTicTacToeAgent (O), not graded
├── test_tic_tac_toe_game.py          # provided, do not modify
├── test_tic_tac_toe_board_renderer.py  # provided, do not modify
├── test_human_tic_tac_toe_agent.py   # provided, do not modify (interactive, see above)
├── test_random_tic_tac_toe_agent.py  # provided, do not modify
└── test_minimax_tic_tac_toe_agent.py # provided, do not modify
```

## How to reproduce

```bash
# Run any individual test suite
python3 -m unittest test_minimax_tic_tac_toe_agent
python3 -m unittest test_tic_tac_toe_game

# Run everything (pipe in "1" so the interactive human-agent test doesn't hang)
echo "1" | python3 -m unittest discover -p "test_*.py"

# Play against the minimax agent yourself (you are X, always moves first)
python3 main.py

# Play against the random agent instead
python3 scratchpad.py
```

No dependencies beyond the Python standard library.

## Notes on the implementation

**`TicTacToeGame.utility`** determines the other player from `player` (there are only two symbols, `X` and `O`), then returns `1` if `player` won, `-1` if the other player won, and `0` for anything else (draw or non-terminal state, though `utility` is only ever called by the agent once `is_terminal` is already `True`).

**`MinimaxTicTacToeAgent`** follows the standard three-function minimax structure: `minimax` (the entry point, called from `action`) tries every legal move from the current state and keeps whichever leads to the highest value via `min_value`; `max_value` and `min_value` are mutually recursive, alternating whose turn it is to try to maximize or minimize the eventual utility, with `is_terminal` as the recursion's base case. This matches the `MINIMAX-SEARCH` specification directly: no pruning, no depth limit, full lookahead to every terminal state reachable from the current position.

## Notes on this course's exercise numbering

There is no Exercise 4 in this course; numbering goes directly from Exercise 3 (eight-puzzle, A* search) to Exercise 5 (this one). This isn't a missing submission, that exercise number was never assigned in the course.
