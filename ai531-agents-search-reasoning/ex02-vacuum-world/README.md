# Exercise 2: Vacuum-Cleaner World

**Course:** AI 531 (Agents, Search, and Reasoning), Oregon State University
**Assignment:** Canvas exercise, [course site](https://canvas.oregonstate.edu/courses/2030143) (Canvas requires OSU login, so there's no public link to the assignment page; the original instructions are preserved in [`EXERCISE_INSTRUCTIONS.md`](EXERCISE_INSTRUCTIONS.md))
**Task:** Build a simple reflex agent and a model-based reflex agent, both operating as a robot vacuum in a two-location "Vacuum-Cleaner World," following AIMA (Russell & Norvig) Chapter 2. The goal isn't just working code, it's honoring the specific SIMPLE-REFLEX-AGENT and MODEL-BASED-REFLEX-AGENT function specifications (AIMA figures 2.8, 2.10, and 2.12) closely enough that the difference between the two agent designs is visible in the implementation, not just the outcome.

The exercise has two parts:
1. Complete `SimpleReflexVacuum`: three actuators (`suck`, `move_left`, `move_right`) and an `action` function that takes a location id and a dirt percept directly (no internal state), and returns the rational action as a function reference. Required, and test-driven against `test_simple_reflex_vacuum.py`.
2. Complete `ModelReflexVacuum`: a full model-based reflex agent with an internal `state`, a `transition_model` (how actions change the world), and a `sensor_model` (how the world is perceived), that updates its internal model on every call to `action()`. This part is explicitly open-ended: passing `test_model_reflex_vacuum.py` is optional, since the assignment cares more about faithfully implementing the MODEL-BASED-REFLEX-AGENT structure than about satisfying a fixed test suite.

## Results

All 7 provided test suites pass, 56 tests total, confirmed by rerunning `python3 -m unittest <module>` for each:

| Test suite | Tests | Result |
|---|---|---|
| `test_location` | 4 | pass |
| `test_movement_model` | 3 | pass |
| `test_sensor_model` | 5 | pass |
| `test_state` | 4 | pass |
| `test_transition_model` | 8 | pass |
| `test_simple_reflex_vacuum` (Part 1, required) | 10 | pass |
| `test_model_reflex_vacuum` (Part 2, optional) | 22 | pass |

Passing all 22 tests in `test_model_reflex_vacuum.py` goes beyond what the exercise requires. It's listed as an optional "Extension" in the assignment ("Implement a ModelReflexVacuum that passes the tests in test_model_reflex_vacuum.py"), not a baseline expectation. The test file itself also has 9 additional test methods still commented out (mostly earlier, superseded drafts of tests that were later rewritten and uncommented further down in the file, in a section labeled "New tests added by unit-test workflow"). Those 9 remain inactive and weren't run.

Both `main.py` and `scratchpad.py` (not graded, but included per the assignment's "demonstrate the use of your agent" requirement) run cleanly and print the expected actuator side effects. Sample output from `scratchpad.py`, starting at location A with both locations dirty:

```
side effect: cause hardware to suck        # A was dirty
side effect: cause hardware to move right  # A is now clean, move to B
side effect: cause hardware to suck        # B was dirty
side effect: cause hardware to move left   # B is now clean, move to A
side effect: cause hardware to move right  # A is still clean, move to B
```

This is the expected long-run behavior for a two-location vacuum world once both locations are clean: the agent oscillates between A and B indefinitely, since neither the sensor model nor the rule set gives it a way to know it's already achieved a clean world and should stop.

## Repo layout

This is intentionally kept flat rather than split into `src/`/`tests/` subfolders. The provided test files import modules directly (`from location import Location`, with no path prefix) and are meant to run via `python3 -m unittest test_X` from the same directory, matching how the assignment is graded and how it would be zipped for submission. Splitting the layout would have meant editing the "DO NOT MODIFY" test files just to fix imports, which defeats the point.

```
ex02-vacuum-world/
├── EXERCISE_INSTRUCTIONS.md         # original assignment README from Canvas, unmodified
├── location.py                      # Location: an id and optional dirt (provided)
├── state.py                         # State: all locations + current location id (provided)
├── movement_model.py                # MovementModel: left/right destination pair (provided)
├── transition_model.py              # TransitionModel: how actions change world state (provided)
├── sensor_model.py                  # SensorModel: how world state becomes a percept (provided)
├── simple_reflex_vacuum.py          # Part 1: SimpleReflexVacuum (student-implemented)
├── model_reflex_vacuum.py           # Part 2: ModelReflexVacuum (student-implemented)
├── insufficient_model_reflex_vacuum.py  # provided reference example, deliberately incomplete
├── main.py                          # demonstrates both agents in action
├── scratchpad.py                    # informal exploration script, not graded
├── test_location.py                 # provided, do not modify
├── test_movement_model.py           # provided, do not modify
├── test_sensor_model.py             # provided, do not modify
├── test_state.py                    # provided, do not modify
├── test_transition_model.py         # provided, do not modify
├── test_simple_reflex_vacuum.py     # provided, do not modify (Part 1, required)
└── test_model_reflex_vacuum.py      # provided, do not modify (Part 2, optional)
```

## How to reproduce

```bash
# Run any individual test suite
python3 -m unittest test_simple_reflex_vacuum
python3 -m unittest test_model_reflex_vacuum

# Run everything
python3 -m unittest discover -p "test_*.py"

# See both agents in action
python3 main.py
python3 scratchpad.py
```

No dependencies beyond the Python standard library (`unittest`, `unittest.mock`).

## Notes on the implementation

**`SimpleReflexVacuum`** matches the assignment's description closely: `action(location, dirt)` takes the percept as two plain parameters rather than building a state object, and the conditional logic stands in for RULE-MATCH. No internal state is kept between calls, which is the whole point of a simple reflex agent.

**`ModelReflexVacuum`** keeps `state`, `transition_model`, and `sensor_model` as constructor-provided collaborators (rather than owning that logic itself), and calls `update_state()` at the start of every `action()` call to refresh its internal `is_dirty`/`location` model from the sensor model before deciding on a rule. This mirrors the MODEL-BASED-REFLEX-AGENT structure in AIMA figure 2.12 reasonably closely: sense, update internal state, match a rule, act.

## Known quirks

- `main.py`'s inline comments for Part 2 (`# suck`, `# move right`, `# suck`, `# move left`, `# move right`, `# move left`) don't match the actual runtime output once traced through. The vacuum world in `main.py` starts at location `'B'` (not `'A'` like `scratchpad.py`), and tracing the actual `update_state`/`action` logic against that starting point gives `suck, move_left, suck, move_right, move_left, move_right`, confirmed by actually running the script. The agent logic itself is correct and matches the expected oscillating behavior; only the comments describing it are out of sync with what the code does when run.
- The `InsufficientModelReflexVacuum` in `insufficient_model_reflex_vacuum.py` is provided course reference code (deliberately incomplete, per the assignment) and isn't meant to be modified or graded; it's included here only because the assignment says to submit all provided files alongside new ones.
