import random
from rpsls_rules import GameAction, VICTORY_RULES, LOSS_RULES
from game import GameResult, parse_match_by_player

def rpsls_agent_random(records = [], player = None):
    return GameAction(random.randint(0, len(GameAction) - 1))

def rpsls_agent_rock(records = [], player = None):
    return GameAction.Rock

def rpsls_agent_paper(records = [], player = None):
    return GameAction.Paper

def rpsls_agent_scissors(records = [], player = None):
    return GameAction.Scissors

def rpsls_agent_lizard(records = [], player = None):
    return GameAction.Lizard

def rpsls_agent_spock(records = [], player = None):
    return GameAction.Spock

def rpsls_agent_human(records = [], player = None):

    length = len(GameAction)
    choice = -1

    while choice < 0 or choice >= length:
        game_choices_str = ", ".join([f"{game_action.name}[{game_action.value}]" for game_action in GameAction])
        choice = int(input(f"\nPick a choice ({game_choices_str}): "))

    return GameAction(choice)

def rpsls_agent_counter_opponent(records=[], player = None):
    if len(records) > 0:
        _, b, _ = parse_match_by_player(records[-1], player)
        return LOSS_RULES[b][0]
    return rpsls_agent_random()

def rpsls_agent_play_oponent_unused(records = [], player = None):
    out = GameAction.Paper
    if len(records) > 1:
        _, b, _ = parse_match_by_player(records[-1], player)
        _, b2, _ = parse_match_by_player(records[-2], player)

        choices = [game_action for game_action in GameAction]

        if b in choices:
            choices.remove(b)
        if b2 in choices:
            choices.remove(b2)

        out = choices[0]
        
    return out

def rpsls_agent_adv(records = [], player = None):
    out = GameAction.Paper
    if len(records) > 1:
        a, b, result = parse_match_by_player(records[-1], player)
        if result == GameResult.Tie:
            out = GameAction(random.randint(0, len(GameAction) - 1))
        elif result == GameResult.Victory:
            out = LOSS_RULES[LOSS_RULES[a][0]][0]
        else:
            out = b

    return out

def rpsls_agent_copy_opponent(records=[], player = None):
    if len(records) > 0:
        _, b, _ = parse_match_by_player(records[-1], player)
        return b
    return rpsls_agent_random()

def rpsls_agent_win_stay_lose_shift(records=[], player = None):
    if len(records) > 0:
        _, b, result = parse_match_by_player(records[-1], player)
        if result == GameResult.Victory:
            return b
        elif result == GameResult.Loss:
            return LOSS_RULES[b][0]
    return rpsls_agent_random()

def rpsls_agent_alternate(records=[], player = None):
    out = GameAction(0)

    leng = len(records)

    if leng > 0: 
        out = GameAction(leng % len(GameAction))
    
    return out


def rpsls_agent_probabilistic(records=[], player = None):
    choices = list(GameAction)
    weights = [0.4, 0.3, 0.3, 0.6, 0.2] 
    return random.choices(choices, weights=weights)[0]

def rpsls_agent_cycle(records=[], player = None):
    if len(records) > 0:
        previous_move = parse_match_by_player(records[-1], player)[1]
        return GameAction((previous_move.value + 1) % len(GameAction))
    return rpsls_agent_random()

def rpsls_agent_adv2(records = [], player = None):
    out = GameAction.Paper
    leng = len(records)
    if leng > 0:
        _, b, _ = parse_match_by_player(records[-leng], player)
        out = LOSS_RULES[b][0]
    return out

def rpsls_agent_predict(records = [], player = None):

    out = GameAction.Paper
    leng = len(records)

    if leng > 0:
        last_tuple = records[-1]

        first_occ = None
        for i in reversed(range(leng - 1)):

            if records[i] == last_tuple:
                first_occ = i
                break
        
        if first_occ is None or first_occ == leng:
            out = rpsls_agent_random()
        else:
            a, b, res = parse_match_by_player(records[first_occ + 1], player)

            if res == GameResult.Victory:
                out = a
            elif res == GameResult.Loss:
                out = LOSS_RULES[b][0]
            else:
                out = LOSS_RULES[b][0]

    return out


RPSLS_AGENTS = {
    "random" : rpsls_agent_random,
    "rock": rpsls_agent_rock,
    "paper": rpsls_agent_paper,
    "scissors": rpsls_agent_scissors,
    "lizard": rpsls_agent_lizard,
    "spok": rpsls_agent_spock,
    "play_oponent_unused": rpsls_agent_play_oponent_unused,
    "adv": rpsls_agent_adv,
    "copy_opponent": rpsls_agent_copy_opponent,
    "win_stay_lose_shift": rpsls_agent_win_stay_lose_shift,
    "alternate": rpsls_agent_alternate,
    "probabilistic": rpsls_agent_probabilistic,
    "cycle": rpsls_agent_cycle,
    "adv2": rpsls_agent_adv2,
    "counter_opponent": rpsls_agent_counter_opponent,
    "predict": rpsls_agent_predict,
    # "human": rpsls_agent_human
}
