# Exercise 8: Wumpus World

**Course:** AI 531 (Agents, Search, and Reasoning), Oregon State University
**Assignment:** Canvas exercise, [course site](https://canvas.oregonstate.edu/courses/2030143) (Canvas requires OSU login; original instructions are preserved in [`EXERCISE_INSTRUCTIONS.md`](EXERCISE_INSTRUCTIONS.md))
**Task:** Implement a knowledge-based agent (per AIMA Chapter 7's `KB-AGENT` specification) that operates in the classic 4x4 wumpus world, along with a simulator representing the actual physical world (its "physics") that the agent perceives and acts within. This exercise's knowledge base is deliberately incomplete: `ask` is stubbed to always return `climb`, since the real propositional-logic reasoning is the subject of a later exercise not attempted here (see below).

Note: this exercise's own `README.md` (preserved as `EXERCISE_INSTRUCTIONS.md`) titles itself "Exercise 7," but Canvas's actual submission naming convention for this assignment is `LASTNAME_exercise08.zip`, and this is Exercise 8 in the course's actual sequence. The stale "Exercise 7" title in the file appears to be left over from reusing a template.

The exercise has three parts:
1. `WumpusWorldAgent`: a goal-based, knowledge-based agent with `kb` and `time` properties, six actuator methods (`turn_left`, `turn_right`, `move_forward`, `shoot`, `grab`, `climb`) that each cause a side effect in the world and print a short message, three stub methods (`make_percept_sentence`, `make_action_query`, `make_action_sentence`) left as `pass` since their real implementation is out of scope for this exercise, and an `action` method following `KB-AGENT`: tell the KB what's perceived, ask the KB what to do, tell the KB what action was taken, increment `time`, return the action.
2. `KnowledgeBase`: minimal for this exercise, `tell` does nothing, `ask` always returns `WumpusWorldAgent.climb` regardless of input. This is intentional per the assignment, not a shortcut.
3. `WumpusWorld`: a simulation of the actual physical 4x4 wumpus world, not a state representation the agent believes in. Computes the five-element percept tuple (`Stench`, `Breeze`, `Glitter`, `Bump`, `Scream`) for a given location, and implements the physical side effects of each action (movement with wall/pit/wumpus collision handling, shooting the arrow along the agent's facing direction, grabbing gold, climbing out at the exit).

## Results

All 3 test suites pass, 134 tests total:

| Test suite | Tests | Result |
|---|---|---|
| `test_wumpus_world` | 108 | pass |
| `test_wumpus_world_agent` | 22 | pass |
| `test_knowledge_base` | 4 | pass |

Both `scratchpad.py` and `main.py` run without error and, as the assignment promises, the agent's very first action is to climb out of the cave (since `KnowledgeBase.ask` always returns `climb`, regardless of the actual percept):

```
$ python3 scratchpad.py
climbed
$ python3 main.py
climbed
```

## Repo layout

Kept flat, same reasoning as prior exercises: the test files import modules directly by name and are meant to run via `python3 -m unittest test_X` from the same directory.

```
ex08-wumpus-world/
├── EXERCISE_INSTRUCTIONS.md      # original assignment README from Canvas, unmodified (titled "Exercise 7," see note above)
├── wumpus_world.py                # simulated physical world: percepts + action side effects (student-implemented)
├── wumpus_world_agent.py          # KB-AGENT-style agent: properties, actuators, agent function (student-implemented)
├── knowledge_base.py              # minimal KB for this exercise: `ask` always returns `climb` (student-implemented)
├── main.py                        # demonstration: instantiate world/kb/agent, take one action
├── scratchpad.py                  # provided demonstration script, not graded
├── test_wumpus_world.py           # provided, do not modify
├── test_wumpus_world_agent.py     # provided, do not modify
└── test_knowledge_base.py         # provided, do not modify
```

## How to reproduce

```bash
# Run any individual test suite
python3 -m unittest test_wumpus_world
python3 -m unittest test_wumpus_world_agent
python3 -m unittest test_knowledge_base

# Run everything
python3 -m unittest discover -p "test_*.py"

# See the agent take one action (it climbs out immediately, per the stubbed KnowledgeBase)
python3 main.py
python3 scratchpad.py
```

No dependencies beyond the Python standard library (`unittest`, `unittest.mock`).

## Notes on the implementation

**`WumpusWorldAgent.action`** follows `KB-AGENT` directly: `tell` the percept, `ask` for an action, `tell` the action taken, increment `time`, return the action. The three `make_*_sentence`/`make_action_query` methods exist as callable stubs only, per the assignment's explicit instruction not to implement their details in this exercise.

**`WumpusWorld`** is a genuine simulation of the physical environment, not a belief state. `percept` computes `Stench` (adjacent to or on the wumpus), `Breeze` (adjacent to any pit), `Glitter` (standing on the gold), `Bump` (facing a boundary wall), and `Scream` (wumpus is dead) independently from the agent's own knowledge. `moved_forward` handles the physical consequences of movement, including that walking into a pit or a still-living wumpus kills the agent. `shot` only kills the wumpus if it's actually in the direction the agent is currently facing. Per the assignment's stated simplification, `Scream` persists forever once the wumpus dies (no time modeling), and `Bump` is recalculated fresh each time rather than modeled as a momentary event.

## Notes on this course's exercise numbering

This course has no Exercise 6 or 7; numbering goes from Exercise 5 (tic-tac-toe, minimax) to Exercise 8 (this one). Those exercise numbers were never assigned in the course, not missing submissions.

The exercise that would logically follow this one (implementing the actual propositional-logic reasoning inside `KnowledgeBase.tell`/`ask`, replacing the `climb`-always stub with real inference) would have been Exercise 9. It was not attempted and isn't included in this repo.
