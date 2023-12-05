from rps_game import GameResult, play_round
from agents import RPS_AGENTS
from rps_rules import VICTORY_RULES as RPS_VICTORY_RULES, LOSS_RULES as RPS_LOSS_RULES

GAMES = 10000

def play_matches(agent_action, computer_action, victory_rules, loss_rules):
    results = []
    records = []
    for i in range(GAMES):
        (a,b, result) = play_round(agent_action, computer_action, victory_rules, loss_rules, records)
        records.append((a,b, result))
        results.append(result)
    
    return results

def get_stats(results):

    victories = results.count(GameResult.Victory)
    lost = results.count(GameResult.Loss)
    tie = results.count(GameResult.Tie)

    return (victories, lost, tie)

def get_percentages(stats):
    (victories, lost, tie)  = stats
    return (victories / GAMES, lost / GAMES, tie / GAMES)


def test_agents(agent_action, computer_action, victory_rules, loss_rules):
    results = play_matches(agent_action, computer_action, victory_rules, loss_rules)
    (victories, lost, ties) = get_stats(results)
    (victories_perc, lost_perc, ties_perc) = get_percentages((victories, lost, ties))
    print(f"Agent { agent_action.__name__} has {victories} victories, {ties} ties and {lost} lost against {computer_action.__name__}")
    print(f"With {victories_perc * 100}% winrate")
    return (victories, lost, ties)


def match_agents(agents, victory_rules, loss_rules): 
    matches = {}
    for a in agents:
        matches[a] = {}
        for b in agents:
            (victories, lost, ties) = test_agents(agents[a], agents[b], victory_rules, loss_rules)
            matches[a][b] = (victories, lost, ties)
    
    return matches

