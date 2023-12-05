from enum import IntEnum
class GameResult(IntEnum):
    Victory = 0
    Loss = 1
    Tie = 2


def assess_game(agent_action, computer_action, victory_rules, loss_rules):
    if computer_action in victory_rules[agent_action]:
        return GameResult.Victory
    elif computer_action in loss_rules[agent_action]:
        return GameResult.Loss
    else:
        return GameResult.Tie


def play_round(agent_action_func, computer_action_func, victory_rules, loss_rules, records = []):
    computer_action = computer_action_func(records)
    agent_action = agent_action_func(records)
    result = assess_game(agent_action, computer_action,victory_rules, loss_rules)
    return (agent_action,computer_action, result)

if __name__ == "__main__":
    from agents import agent_human, agent_random
    from rps_rules import VICTORY_RULES, LOSS_RULES
    (a,b,result) = play_round(agent_human, agent_random, VICTORY_RULES, LOSS_RULES)

    print(result.name)

