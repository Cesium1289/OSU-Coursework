# WumpusWorldAgent
# An agent designed to perform in the wumpus world environment.
# Carson Hansen

class WumpusWorldAgent:

    def __init__(self,knowledge_base):
        self.kb = knowledge_base
        self.time = 0

    def turn_left(self, wumpus_world):
        """
        Agent turns left
        """
        wumpus_world.turned_left()
        print("turn left")

    def turn_right(self, wumpus_world):
        """
        Agent turns right
        """
        wumpus_world.turned_right()
        print("turn right")

    def move_forward(self, wumpus_world):
        """
        Agent moves forward
        """
        wumpus_world.moved_forward()
        print("move forward")
    
    def shoot(self, wumpus_world):
        """
        Agent shoots
        """
        wumpus_world.shot()
        print("shot")

    def grab(self,wumpus_world):
        """
        Agent attempts to grab
        """
        wumpus_world.grabbed()
        print("grabbed")

    def climb(self, wumpus_world):
        """
        Agent attempts to climb
        """
        wumpus_world.climbed()
        print("climbed")
    
    def make_percept_sentence(self,wumpus_world):
        """
        Agent makes a percept sentence to assess its surroundings
        """

    def make_action_query(self):
        """
        Make a query actions of what it should do
        """

    def make_action_sentence(self):
        """
        Make a sentence of actions of what the agent should do
        """

    def action(self,wumpus_world):
        """
        Agent tells kb what it sees, asks for an action based on
        what it sees, then returns the action it recieved
        """
        self.kb.tell(wumpus_world)
        action = self.kb.ask(wumpus_world)
        self.kb.tell(action)
        self.time +=1
        return action