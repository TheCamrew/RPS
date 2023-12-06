import random
from rps_rules import GameAction as RPSGameAction, VICTORY_RULES as RPS_VICTORY_RULES, LOSS_RULES as RPS_LOSS_RULES
from rps_game import GameResult

def rps_agent_random(records = []):
    return RPSGameAction(random.randint(0, len(RPSGameAction) - 1))

def rps_agent_rock(records = []):
    return RPSGameAction.Rock

def rps_agent_paper(records = []):
    return RPSGameAction.Paper

def rps_agent_scissors(records = []):
    return RPSGameAction.Scissors

def rps_agent_human(records = []):

    length = len(RPSGameAction)
    choice = -1

    while choice < 0 or choice >= length:
        game_choices_str = ", ".join([f"{game_action.name}[{game_action.value}]" for game_action in RPSGameAction])
        choice = int(input(f"\nPick a choice ({game_choices_str}): "))

    return RPSGameAction(choice)

def rps_agent_play_wins_oponent_last(records = []):
    out = RPSGameAction.Paper
    if len(records)>0:
        (a, b, result) = records.pop()
        out = RPS_LOSS_RULES[b][0]
    return out

def rps_agent_play_oponent_unused(records = []):
    out = RPSGameAction.Paper
    if len(records) > 1:
        (a, b, result) = records.pop()
        (a2, b2, result2) = records.pop()

        choices = [game_action for game_action in RPSGameAction]

        if b in choices:
            choices.remove(b)
        if b2 in choices:
            choices.remove(b2)

        out = choices[0]
        
    return out

def rps_agent(records = []):
    out = RPSGameAction.Paper
    if len(records) > 1:
        (a, b, result) = records.pop()
        if result == GameResult.Tie:
            out = RPSGameAction(random.randint(0, len(RPSGameAction) - 1))
        elif result == GameResult.Victory:
            out = RPS_LOSS_RULES[RPS_LOSS_RULES[a][0]][0]
        else:
            out = b

    return out


RPS_AGENTS = {
    "random" : rps_agent_random,
    "rock": rps_agent_rock,
    "paper": rps_agent_paper,
    "scissors": rps_agent_scissors,
    "play_wins_oponent_last": rps_agent_play_wins_oponent_last,
    "play_oponent_unused": rps_agent_play_oponent_unused,
    "test": rps_agent
    # "human": rps_agent_human
}
