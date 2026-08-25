# Main
# A demonstration of the WumpusWorld and WumpusWorldAgent.
# Carson Hansen

from wumpus_world import WumpusWorld
from wumpus_world_agent import WumpusWorldAgent
from knowledge_base import KnowledgeBase

wumpus_world = WumpusWorld(
    agent_location = (1, 1),
    agent_direction = 'East',
    agent_alive = True,
    wumpus_alive = True,
    wumpus_location = (3, 3),
    gold_location = (4, 3),
    pit_locations = [ (1, 2), (2,3), (4, 4) ]
    )

kb = KnowledgeBase()

agent = WumpusWorldAgent(kb)

action = agent.action(wumpus_world.percept((1, 1)))
action(agent, wumpus_world)

