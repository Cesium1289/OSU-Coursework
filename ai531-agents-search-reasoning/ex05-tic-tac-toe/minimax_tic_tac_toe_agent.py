# MinimaxTicTacToeAgent
# A game-playing tic tac toe agent that uses the minimax algorithm to produce
# a rational action.
# Carson Hansen


class MinimaxTicTacToeAgent:

    def __init__(self, game, symbol):
        self.game = game
        self.symbol = symbol

    def action(self, state):
        #no game or state. So no action should occur
        if state is None or self.game is None:
            return None
        
        return self.minimax(self.game,state)

    def minimax(self, game, state):
        """
        find the state that gives the agent the best chance of winning
        """
        best_action = None
        best_value = float("-inf")

        #loop through all the available states
        for a in game.actions(state):
            successor = game.result(state, a)
            v = self.min_value(game, successor)

            #check to see if the new move is better then the existing one
            if v > best_value:
                best_value = v
                best_action = a

        return best_action
        

    def max_value(self, game, state):
        """
        find the max value of a given state
        """
        #check if game has any valid moves left
        if game.is_terminal(state):
            return game.utility(state,self.symbol)
        
        v = float("-inf")

        #loop through all possible moves on current state
        for action in game.actions(state):
            new_state = game.result(state,action)
            v = max(v,self.min_value(game,new_state))
        return v

    def min_value(self, game, state):
        """
        Find the min value of a given state
        """
        #check if game has any valid moves left
        if game.is_terminal(state):
            return game.utility(state,self.symbol)
        
        v = float("inf")

        #loop through all possible moves on current state
        for action in game.actions(state):
            new_state = game.result(state,action)
            v = min(v,self.max_value(game,new_state))
        return v
