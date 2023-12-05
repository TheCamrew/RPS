import random
from rps_rules import GameAction as RPSGameAction

def rps_agent_random(records = []):
    return RPSGameAction(random.randint(0, len(RPSGameAction) - 1))

def rps_agent_paper(records = []):
    return RPSGameAction.Paper

def rps_agent_human(records = []):

    length = len(RPSGameAction)
    choice = -1

    while choice < 0 or choice >= length:
        game_choices_str = ", ".join([f"{game_action.name}[{game_action.value}]" for game_action in RPSGameAction])
        choice = int(input(f"\nPick a choice ({game_choices_str}): "))

    return RPSGameAction(choice)
