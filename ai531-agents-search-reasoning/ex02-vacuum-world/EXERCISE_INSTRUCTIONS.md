# Exercise 2: Vacuum-Cleaner World

Demonstrate your comprehension of the canonical simple reflex agent design and
the model-based reflex agent design. Build agents that can operate within
a two-location Vacuum-Cleaner World.

## What to Do

Implement a simple reflex agent action function, and implement a complete
model-based reflex agent. Your implementations should honor the specficiations of
the SIMPLE-REFLEX-AGENT function and the MODEL-BASED-REFLEX-AGENT function found
in the AIMA book. Use the concept of a two-location Vacuum-Cleaner World as the
domain of your implementations.

## Instructions

There are two parts to this exercise.

### Part 1

Complete the implementation of SimpleReflexVacuum found in
_simple_reflex_vacuum.py_, and lean on the test suite in
_test_simple_reflex_vacuum.py_ to guide your implementation. You will implement
actuator functions, `suck`, `move_left`, and `move_right`, and the agent function,
named `action`. The `action` function should adhere to the spirit
of the SIMPLE-REFLEX-AGENT and REFLEX-VACUUM-AGENT functions specified by Russell
& Norvig (AIMA Figures 2.8 and 2.10).

Notice that REFLEX-VACUUM-AGENT has two parameters. The `action` function should
receive its _percept_ in the form of two parameters: one representing the id of
the perceived location, and one representing whether there is dirt or not.

The implementation can be a simple `if`-`elif` conditional statement, and it need
not transform the percept into a full-fledged state object with an
INTERPRET-INPUT subroutine as shown in the SIMPLE-REFLEX-AGENT function
specification. The conditional statement shall represent the RULE-MATCH
subroutine found in the specification. Lastly, the `action` function should return
a function representing the rational action, such as the SimpleReflexVacuum's
`suck` function.

In a real robot vacuum, the actuator functions may affect hardware, such as
turning on a motor, and therefore have side effects. Your actuator functions
should simulate the side effect of affecting hardware by producing the side
effect of printing. That way, when demonstrating the use of your agent, you can
see some printed output when an action executed.

You'll know this is complete when the tests found in _test_simple_reflex_vacuum.py_
all pass. Run the test suite with `python3 test_simple_reflex_vacuum.py`. Then,
illustrate the use of a SimpleReflexVacuum in _main.py_. The good news is, we
have provided some code for you in _main.py_ that demonstrates the use of a
SimpleReflexVacuum, and this code should run without error when your
SimpleReflexVacuum is complete. Use the provided code in _main.py_ as a starting
point to illustrate your SimpleReflexVacuum in action.

### Part 2

**Note**: For Part 2, you do not necessarily need to pass the tests
in _test_model_reflex_vacuum.py_.

Complete your own implementation of a ModelReflexVacuum in
_model_reflex_vacuum.py_, that illustrates a model-based reflex agent operating
within a two-location Vacuum-Cleaner World. This is challenging, because it
requires analysis and creativity 😱😱😱. But if you embrace this challenge with
rigor, I promise that you will have a deeper understanding of two things:

1. How does a model-based reflex agent differ from a simple reflex agent, really?
2. What does it mean for a model-based reflex agent to keep track of the world?

Consider using your SimpleReflexVacuum class as a starting point for your
ModelReflexVacuum. But do not be too attached to the code of a SimpleReflexVacuum -
the ModelReflexVacuum will be different!

Next, study the Vacuum-Cleaner World concept, and the model-based reflex agent
design in the AIMA book. Study the prose of section 2.4.3, the diagram in figure
2.11, and especially the specification of the action-producing
MODEL-BASED-REFLEX-AGENT agent function in figure 2.12.

How might you build a model-based reflex agent as a vacuum cleaner, that genuinely
incorporates a transition model, sensor model, rules and actions, and updates
the internally-modeled state of the two-location vacuum-cleaner world?

Start simple, and then _rigorously_ compare your implementation to the
MODEL-BASED-REFLEX-AGENT function. Do your best to:

1. Implement a ModelReflexAgent that honors the MODEL-BASED-REFLEX-AGENT spec.
2. Learn how the MODEL-BASED-REFLEX-AGENT spec manifests as real code.

The hardest part will be deciding how to balance the pragmatic utility of your code
while still authentically honoring the MODEL-BASED-REFLEX-AGENT specification.
For example, instead of actually implementing a RULE-MATCH(state, rules)
subroutine, you might just write an `if`-`elif` statement that relies on the world
state and conditional rules, and feel that this is a pragmatic and authentic
representation of this requirement in the specification.

Our #1 tip is to think of this as an exploratory hacking experiment. Ask yourself,
"Ok, how do I implement a model-based reflex agent vacuum?" You will need to write,
delete and rewrite lots of code. The process should be messy, but it will encourage
you to think about the model-based reflex agent deeply and concretely.

When you are satisfied with your ModelReflexAgent implementation, be sure to
demonstrate the use of your ModelReflexAgent in _main.py_. Your code should
demonstrate how invoking the action-producing agent function multiple times
produces a different action based on the state of the world changing.

### Some Ideas for Part 2

See the example usage of an imaginary ModelReflexVacuum in _scratchpad.py_ to
give you ideas about how a ModelReflexVacuum might be used, and what your code
in _main.py_ might do. Notice how the `action` function is called multiple times
and returns a different action each time. The source code for a Location, State,
TransitionModel and SensorModel are all provided to you - but you are not required
to use them. If you do use them, feel free to modify them as you see fit. Reading
their unit tests may help you understand their utility, or give you ideas for your
own implementation.

An example, albeit insufficient, implementation is the
InsufficientModelReflexVacuum shown in _insufficient_model_reflex_vacuum.py_.
It has some good ideas, but is only a start. It only begins to honor the
MODEL-BASED-REFLEX-AGENT specification, but falls short of doing so correctly.
You could use this code for ideas or even your own starting point for your
ModelReflexVacuum, though much still needs to change.

A unit test for a complete ModelReflexVacuum is in _test_model_reflex_vacuum.py_.
You are *not* required to pass these tests. But reading the docstring description
for each test may give you some great ideas for your own implementation.

That said, if you wish, you can build your ModelReflexVacuum by engaging in a
test-driven approach by using the test suite in _test_model_reflex_vacuum.py_.
You can try commenting out all but the first test in _test_model_reflex_vacuum.py_,
implementing code that gets the test to pass, and then moving on to get the next
test to pass, and so on.

&copy; 2023 Yong Joseph Bakos. All rights reserved.
