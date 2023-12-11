import random
from rps_rules import GameAction as RPSGameAction, VICTORY_RULES as RPS_VICTORY_RULES, LOSS_RULES as RPS_LOSS_RULES
from rps_game import GameResult

def parse_match_by_player(match, player):
    if player == 1:
        a, b, r = match
        
        if r == GameResult.Victory:
            r = GameResult.Loss
        elif r == GameResult.Loss:
            r = GameResult.Victory

        match = (b, a, r)

    return match

def rps_agent_random(records = [], player = None):
    return RPSGameAction(random.randint(0, len(RPSGameAction) - 1))

def rps_agent_rock(records = [], player = None):
    return RPSGameAction.Rock

def rps_agent_paper(records = [], player = None):
    return RPSGameAction.Paper

def rps_agent_scissors(records = [], player = None):
    return RPSGameAction.Scissors

def rps_agent_human(records = [], player = None):

    length = len(RPSGameAction)
    choice = -1

    while choice < 0 or choice >= length:
        game_choices_str = ", ".join([f"{game_action.name}[{game_action.value}]" for game_action in RPSGameAction])
        choice = int(input(f"\nPick a choice ({game_choices_str}): "))

    return RPSGameAction(choice)

def rps_agent_counter_opponent(records=[], player = None):
    if len(records) > 0:
        _, b, _ = parse_match_by_player(records[-1], player)
        return RPS_LOSS_RULES[b][0]
    return rps_agent_random()

def rps_agent_play_oponent_unused(records = [], player = None):
    out = RPSGameAction.Paper
    if len(records) > 1:
        _, b, _ = parse_match_by_player(records[-1], player)
        _, b2, _ = parse_match_by_player(records[-2], player)

        choices = [game_action for game_action in RPSGameAction]

        if b in choices:
            choices.remove(b)
        if b2 in choices:
            choices.remove(b2)

        out = choices[0]
        
    return out

def rps_agent_adv(records = [], player = None):
    out = RPSGameAction.Paper
    if len(records) > 1:
        a, b, result = parse_match_by_player(records[-1], player)
        if result == GameResult.Tie:
            out = RPSGameAction(random.randint(0, len(RPSGameAction) - 1))
        elif result == GameResult.Victory:
            out = RPS_LOSS_RULES[RPS_LOSS_RULES[a][0]][0]
        else:
            out = b

    return out

def rps_agent_copy_opponent(records=[], player = None):
    if len(records) > 0:
        _, b, _ = parse_match_by_player(records[-1], player)
        return b
    return rps_agent_random()

def rps_agent_win_stay_lose_shift(records=[], player = None):
    if len(records) > 0:
        _, b, result = parse_match_by_player(records[-1], player)
        if result == GameResult.Victory:
            return b
        elif result == GameResult.Loss:
            return RPS_LOSS_RULES[b][0]
    return rps_agent_random()

def rps_agent_alternate(records=[], player = None):
    if len(records) % 2 == 0:
        return RPSGameAction.Rock
    else:
        return RPSGameAction.Paper if len(records) % 4 == 1 else RPSGameAction.Scissors

def rps_agent_probabilistic(records=[], player = None):
    choices = [RPSGameAction.Rock, RPSGameAction.Paper, RPSGameAction.Scissors]
    weights = [0.4, 0.3, 0.3] 
    return random.choices(choices, weights=weights)[0]

def rps_agent_cycle(records=[], player = None):
    if len(records) > 0:
        previous_move = parse_match_by_player(records[-1], player)[1]
        return RPSGameAction((previous_move.value + 1) % len(RPSGameAction))
    return rps_agent_random()

def rps_agent_adv2(records = [], player = None):
    out = RPSGameAction.Paper
    leng = len(records)
    if leng > 0:
        _, b, _ = parse_match_by_player(records[-leng], player)
        out = RPS_LOSS_RULES[b][0]
    return out

def rps_agent_predict(records = [], player = None):

    out = RPSGameAction.Paper
    leng = len(records)

    if leng > 0:
        last_tuple = records[-1]

        first_occ = None
        for i in reversed(range(leng - 1)):

            if records[i] == last_tuple:
                first_occ = i
                break
        
        if first_occ is None or first_occ == leng:
            out = rps_agent_random()
        else:
            a, b, res = parse_match_by_player(records[first_occ + 1], player)

            if res == GameResult.Victory:
                out = a
            elif res == GameResult.Loss:
                out = RPS_LOSS_RULES[b][0]
            else:
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
    "adv2": rps_agent_adv2,
    "counter_opponent": rps_agent_counter_opponent,
    "predict": rps_agent_predict,
    # "human": rps_agent_human
}
