from rps_game import GameResult, play_round
from agents import *
from rps_rules import VICTORY_RULES as RPS_VICTORY_RULES, LOSS_RULES as RPS_LOSS_RULES, GameAction as RPSRules


GAMES = 10000

def temp(agent_action, computer_action, victory_rules, loss_rules):
    records = []
    for i in range(GAMES):
        (a,b, result) = play_round(agent_action, computer_action, victory_rules, loss_rules)
        records.append(result)
    
    return records

def get_stats(records):

    victories = records.count(GameResult.Victory)
    lost = records.count(GameResult.Loss)
    tie = records.count(GameResult.Tie)

    return (victories, lost, tie)

def get_percentages(stats):
    (victories, lost, tie)  = stats
    return (victories / GAMES, lost / GAMES, tie / GAMES)


def test_agents(agent_action, computer_action, victory_rules, loss_rules):
    records = temp(agent_action, computer_action, victory_rules, loss_rules)
    (victories, lost, ties) = get_stats(records)
    (victories_perc, lost_perc, ties_perc) = get_percentages((victories, lost, ties))
    print(f"Agent { agent_action.__name__} has {victories} victories, {ties} ties and {lost} lost against {computer_action.__name__}")
    print(f"With {victories_perc * 100}% winrate")
    return (victories, lost, ties)

test_agents(rps_agent_paper, rps_agent_random, RPS_VICTORY_RULES, RPS_LOSS_RULES)
    