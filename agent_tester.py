from rps_game import GameResult, play_round
from display_matches import display_stacked_bar, display_matches, display_variance    

def get_stats(results):

    victories = results.count(GameResult.Victory)
    lost = results.count(GameResult.Loss)
    tie = results.count(GameResult.Tie)

    return (victories, lost, tie)

def get_percentages(stats, games):
    victories, lost, tie  = stats
    return (victories / games, lost / games, tie / games)

def play_matches(agent_action, computer_action, victory_rules, loss_rules, games):
    results = []
    records = []
    for i in range(games):
        (a,b, result) = play_round(agent_action, computer_action, victory_rules, loss_rules, records)
        records.append((a, b, result))
        results.append(result)
    
    return results

def test_agents(agent_action, computer_action, victory_rules, loss_rules, games):
    results = play_matches(agent_action, computer_action, victory_rules, loss_rules, games)
    victories, lost, ties = get_stats(results)
    victories_perc, _, _ = get_percentages((victories, lost, ties), games)
    print(f"Agent { agent_action.__name__} has {victories} victories, {ties} ties and {lost} lost against {computer_action.__name__}")
    print(f"With {victories_perc * 100}% winrate")
    return (victories, lost, ties)


def match_agents(agents, victory_rules, loss_rules, games): 
    matches = []

    for i, a in enumerate(agents):
        for j in range(i, len(agents)):
            b = list(agents.keys())[j]
            if a != b:
                victories,lost, ties = test_agents(agents[a], agents[b], victory_rules, loss_rules, games)
                matches.append({
                    'a':a,
                    'b':b,
                    GameResult.Victory: victories    ,
                    GameResult.Loss: lost,
                    GameResult.Tie: ties   
                }) 

    return matches

def run(agents, victory_rules, loss_rules, games):
    matches = match_agents(agents, victory_rules, loss_rules, games)
    
    display_stacked_bar(matches, games)
    display_matches(matches, games)
    display_variance(matches, games)