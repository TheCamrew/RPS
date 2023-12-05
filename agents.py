import random
from rps_rules import GameAction as RPSGameAction

def agent_random(records):
    return RPSGameAction(random.randint(0, len(RPSGameAction) - 1))

def agent_paper(records):
    return RPSGameAction.Paper

