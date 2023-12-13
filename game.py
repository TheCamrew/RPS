from enum import IntEnum
class GameResult(IntEnum):
    Victory = 0
    Loss = 1
    Tie = 2

def parse_match_by_player(match, player):
    if player == 1:
        a, b, r = match
        
        if r == GameResult.Victory:
            r = GameResult.Loss
        elif r == GameResult.Loss:
            r = GameResult.Victory

        match = (b, a, r)

    return match

def assess_game(agent_a_action, agent_b_action, victory_rules, loss_rules):
    if agent_b_action in victory_rules[agent_a_action]:
        return GameResult.Victory
    elif agent_b_action in loss_rules[agent_a_action]:
        return GameResult.Loss
    else:
        return GameResult.Tie

def play_round(agent_a_action_func, agent_b_action_func, victory_rules, loss_rules, records = []):
    agent_a_action = agent_a_action_func(records, 0)
    agent_b_action = agent_b_action_func(records, 1)
    result = assess_game(agent_a_action, agent_b_action,victory_rules, loss_rules)
    return (agent_a_action,agent_b_action, result)

if __name__ == "__main__":
    from rps_agents import rps_agent_human, rps_agent_random
    from rps_rules import VICTORY_RULES, LOSS_RULES, GameAction
    a, b, result = play_round(rps_agent_human, rps_agent_random, VICTORY_RULES, LOSS_RULES)

    print(f"You choose {GameAction(a).name} and oponent picked {GameAction(b).name}. It's a {result.name}")