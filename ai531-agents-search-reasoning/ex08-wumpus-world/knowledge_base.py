# KnowledgeBase
# A knowledge base for a knowledge-based agent.
# Carson Hansen

from wumpus_world_agent import WumpusWorldAgent

class KnowledgeBase:

    def __init__(self):
        pass

    def tell(self, wumpus_world):
        """
        Agent tells the kb what it sees
        """
        pass

    def ask(self, wumpus_world):
        """
        Agent asks what it should do and the kb provides an action
        """
        return WumpusWorldAgent.climb