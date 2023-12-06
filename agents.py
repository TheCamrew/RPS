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

def rps_agent_counter_opponent(records=[]):
    if len(records) > 0:
        (_, b, _) = records[-1]
        return RPS_LOSS_RULES[b][0]
    return rps_agent_random()

def rps_agent_play_oponent_unused(records = []):
    out = RPSGameAction.Paper
    if len(records) > 1:
        (_, b, _) = records[-1]
        (_, b2, _) = records[-2]

        choices = [game_action for game_action in RPSGameAction]

        if b in choices:
            choices.remove(b)
        if b2 in choices:
            choices.remove(b2)

        out = choices[0]
        
    return out

def rps_agent_adv(records = []):
    out = RPSGameAction.Paper
    if len(records) > 1:
        (a, b, result) = records[-1]
        if result == GameResult.Tie:
            out = RPSGameAction(random.randint(0, len(RPSGameAction) - 1))
        elif result == GameResult.Victory:
            out = RPS_LOSS_RULES[RPS_LOSS_RULES[a][0]][0]
        else:
            out = b

    return out

def rps_agent_copy_opponent(records=[]):
    if len(records) > 0:
        (_, b, _) = records[-1]
        return b
    return rps_agent_random()

def rps_agent_win_stay_lose_shift(records=[]):
    if len(records) > 0:
        (_, b, result) = records[-1]
        if result == GameResult.Victory:
            return b
        elif result == GameResult.Loss:
            return RPS_VICTORY_RULES[b][0]
    return rps_agent_random()

def rps_agent_alternate(records=[]):
    if len(records) % 2 == 0:
        return RPSGameAction.Rock
    else:
        return RPSGameAction.Paper if len(records) % 4 == 1 else RPSGameAction.Scissors

def rps_agent_probabilistic(records=[]):
    choices = [RPSGameAction.Rock, RPSGameAction.Paper, RPSGameAction.Scissors]
    weights = [0.4, 0.3, 0.3] 
    return random.choices(choices, weights=weights)[0]

def rps_agent_cycle(records=[]):
    if len(records) > 0:
        previous_move = records[-1][1]
        return RPSGameAction((previous_move.value + 1) % len(RPSGameAction))
    return rps_agent_random()

def rps_agent_adv2(records = []):
    out = RPSGameAction.Paper
    leng = len(records)
    if leng > 0:
        (_, b, _) = records[-leng]
        out = RPS_LOSS_RULES[b][0]
    return out


RPS_AGENTS = {
    "random" : rps_agent_random,
    "rock": rps_agent_rock,
    "paper": rps_agent_paper,
    "scissors": rps_agent_scissors,
    "play_oponent_unused": rps_agent_play_oponent_unused,
    "adv": rps_agent_adv,
    "copy_opponent": rps_agent_copy_opponent,
    "win_stay_lose_shift": rps_agent_win_stay_lose_shift,
    "alternate": rps_agent_alternate,
    "probabilistic": rps_agent_probabilistic,
    "cycle": rps_agent_cycle,
    "adv2": rps_agent_adv2
    # "human": rps_agent_human
}
