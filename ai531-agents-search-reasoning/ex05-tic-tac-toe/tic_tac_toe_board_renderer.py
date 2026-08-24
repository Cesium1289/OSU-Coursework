# TicTacToeBoardRenderer
# A class that encapsulates the work of 'drawing' the board state for a TicTacToeGame.

class TicTacToeBoardRenderer:

    def render(self, state):
        result = ""
        result += f"{self.render_location(state[0])} | {self.render_location(state[1])} | {self.render_location(state[2])}\n"
        result += f"{self.render_location(state[3])} | {self.render_location(state[4])} | {self.render_location(state[5])}\n"
        result += f"{self.render_location(state[6])} | {self.render_location(state[7])} | {self.render_location(state[8])}\n"
        return result

    def render_location(self, value):
        return ' ' if value is None else value
