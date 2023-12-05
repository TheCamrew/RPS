import random
from rps_rules import GameAction as RPSGameAction

def agent_random():
    return RPSGameAction(random.randint(0, len(RPSGameAction) - 1))

def agent_paper():
    return RPSGameAction.Paper