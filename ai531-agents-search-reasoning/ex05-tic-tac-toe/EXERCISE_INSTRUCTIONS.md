# Exercise 5: Tic-Tac-Toe

Demonstrate your comprehension of adversarial search and the minimax algorithm.
Build an agent that can play tic-tac-toe.

## What to Do

Implement a TicTacToe agent that is a goal-based, game-playing agent, and
implement an agent function that uses the minimax algorithm to produce a game
action. Your implementation should honor the specficiations of the Game concept
in the AIMA book. Your implementation should honor the specification of the
MINIMAX-SEARCH function and, optionally, the ALPHA-BETA-SEARCH function found in
the AIMA book. Use the concept of a tic-tac-toe game as an adversarial search
problem for the domain of your implementation.

## Instructions

Complete the implementation of MinimaxTicTacToeAgent found in
*minimax_tic_tac_toe_agent.py*, and the TicTacToeGame `utility` method found in
*tic_tac_toe_game.py*.

### Play the Game

First, play the game against an agent that chooses a move at random.

`python3 scratchpad.py`

If you take a look at *scratchpad.py*, you will find an example of instantiating
a Game, a HumanTicTacToeAgent and a RandomTicTacToeAgent. A game loop begins, and
each agent is asked to choose an action. That action is then used to produce a
new game state.

Take a look at *human_tic_tac_toe_agent.py* and *random_tic_tac_toe_agent.py*.

Your goal is to implement an agent that is far more diabolical than the
RandomTicTacToeAgent.

### The Game Model

You are provided with an *incomplete* implementation of a Game, following the
specification in the AIMA text. The Game class encapsulates the state model,
transition model, the state space graph, and other game mechanics. Take a look at
*tic_tac_toe_game.py* and *test_tic_tac_toe_game.py*. You will need to implement
the `utility` method.

We do not recommend modifying other parts of the Game class, and the tests in
*test_tic_tac_toe_game.py* should still pass after you complete your implementation
of the Game `utility` method.

### MinimaxTicTacToeAgent

Complete the implementation of MinimaxTicTacToeAgent found in
*minimax_tic_tac_toe_agent.py*, and use the test suite in
*test_minimax_tic_tac_toe_agent.py* to verify the basics of your
implementation. The agent should reflect the architecture of a goal-based,
game-playing, agent that uses adversarial search to produce an individual action
when asked, via the `action` method. Your implementation should honor the
MINIMAX-SEARCH funcion specified in the AIMA book.

In game-playing agents, actions are "game moves." Your agent will not have specific,
individual actuator methods for each of the nine possible moves on a Tic Tac Toe
board. Instead, a move is represented as an integer, which represents a location
on the Tic Tac Toe Board.

```
0 | 1 | 2
3 | 4 | 5
6 | 7 | 8
```

Your agent's `action` method should, ultimately, return an integer.

### Demonstrate Your MinimaxTicTacToeAgent

If you take a look at *scratchpad.py*, you will find an example of instantiating
a Game, and two agents. After you have implemented your MinimaxTicTacToeAgent,
demonstrate the use of your agent in a gameplay workflow. Thankfully, this is
pretty much done for you, in *scratchpad.py*. Do something very similar in
*main.py*, but use your MinimaxTicTacToeAgent instead of the RandomTicTacToeAgent.

You'll know you are done when:

1. All the tests pass. (`python3 -m unittest`)
2. You complete an implementation of the Game `utility` method.
3. Your MinimaxTicTacToeAgent `action` method produces an action using minimax.
4. Running _main.py_ lets you play against your MinimaxTicTacToeAgent.
   (See *scratchpad.py* for inspiration.)

## Notes and Hints

Be sure to review the structure and specification of a game, agent, and minimax
algorithm as specified in the AIMA book.

Read and run *scratchpad.py* to get a sense of how to create and use the different
pieces of the overall game-playing workflow.

Assume the human agent is X and always goes first. Assume the AI agent is O.

&copy; 2023 Yong Joseph Bakos. All rights reserved.
