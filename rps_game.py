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
    agent_action = agent_action_func(records, 0)
    computer_action = computer_action_func(records, 1)
    result = assess_game(agent_action, computer_action,victory_rules, loss_rules)
    return (agent_action,computer_action, result)

if __name__ == "__main__":
    from rps_agents import rps_agent_human, rps_agent_random
    from rps_rules import VICTORY_RULES, LOSS_RULES, GameAction
    a, b, result = play_round(rps_agent_human, rps_agent_random, VICTORY_RULES, LOSS_RULES)

    print(f"You choose {GameAction(a).name} and oponent picked {GameAction(b).name}. It's a {result.name}")