# Exercise 1: Warmup

**Course:** AI 531 (Agents, Search, and Reasoning), Oregon State University
**Assignment:** Canvas exercise, [course site](https://canvas.oregonstate.edu/courses/2030143) (Canvas requires OSU login; original instructions are preserved in [`EXERCISE_INSTRUCTIONS.md`](EXERCISE_INSTRUCTIONS.md))
**Task:** A warmup exercise to practice the course's tools and workflow (reading a test suite, writing Python, running `unittest`, submitting via Canvas) before the more substantive exercises. Not meant to be a real vacuum agent implementation, just a stubbed-out API surface using `pass`.

## Results

All 6 tests in `test_vacuum.py` pass:

```
python3 -m unittest test_vacuum -v
```

```
test_action ... ok
test_instantiation ... ok
test_move_left ... ok
test_move_right ... ok
test_sense_clean ... ok
test_sense_is_dirty ... ok

Ran 6 tests in 0.001s
OK
```

`vacuum.py` stubs five methods (`move_left`, `move_right`, `is_dirty`, `clean`, `action`), each just a `pass` body, matching what the exercise asks for: an empty API surface, not working behavior. The real implementation work starts in [Exercise 2](../ex02-vacuum-world/).

## Repo layout

Kept flat, same reasoning as Exercise 2: `test_vacuum.py` imports `vacuum` directly and is meant to run via `python3 -m unittest test_vacuum` from the same directory.

```
ex01-warmup/
├── EXERCISE_INSTRUCTIONS.md   # original assignment README from Canvas, unmodified
├── vacuum.py                  # stubbed Vacuum class (student-implemented)
├── main.py                    # informal scratchpad, not graded
└── test_vacuum.py             # provided, do not modify (uncomment tests one at a time)
```

## Extensions (not attempted here)

The assignment lists two optional extensions: adding `can_move_left`/`can_move_right` stub methods with their own tests, and building out a `Location` class ahead of Exercise 2's fuller version. Neither is implemented in this submission; Exercise 2 builds its own `Location` class from scratch instead.
