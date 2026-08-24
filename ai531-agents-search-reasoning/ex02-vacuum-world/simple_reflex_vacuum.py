# SimpleReflexVacuum: A robot vacuum cleaner modeled as a simple reflex agent.
# Your implementation should pass the tests in test_simple_reflex_vacuum.py.
# Carson Hansen


class SimpleReflexVacuum:

    def __init__(self):
        pass
    def suck(self):
        print("side effect: cause hardware to suck")

    def move_left(self):
        print("side effect: cause hardware to move left")

    def move_right(self):
        print("side effect: cause hardware to move right")
    
    def action(self, location, dirt):
        if dirt:
            return self.suck
        elif location == "A":
            return self.move_right
        elif location == "B":
            return self.move_left
        else:
            return None
