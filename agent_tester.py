import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

import numpy as np

from rps_game import GameResult, play_round
from agents import RPS_AGENTS
from rps_rules import VICTORY_RULES as RPS_VICTORY_RULES, LOSS_RULES as RPS_LOSS_RULES

GAMES = 10000

def get_stats(results):

    victories = results.count(GameResult.Victory)
    lost = results.count(GameResult.Loss)
    tie = results.count(GameResult.Tie)

    return (victories, lost, tie)

def get_percentages(stats):
    victories, lost, tie  = stats
    return (victories / GAMES, lost / GAMES, tie / GAMES)

def play_matches(agent_action, computer_action, victory_rules, loss_rules):
    results = []
    records = []
    for i in range(GAMES):
        (a,b, result) = play_round(agent_action, computer_action, victory_rules, loss_rules, records)
        records.append((a, b, result))
        results.append(result)
    
    print(len(records))
    return results

def test_agents(agent_action, computer_action, victory_rules, loss_rules):
    results = play_matches(agent_action, computer_action, victory_rules, loss_rules)
    victories, lost, ties = get_stats(results)
    victories_perc, _, _ = get_percentages((victories, lost, ties))
    print(f"Agent { agent_action.__name__} has {victories} victories, {ties} ties and {lost} lost against {computer_action.__name__}")
    print(f"With {victories_perc * 100}% winrate")
    return (victories, lost, ties)


def match_agents(agents, victory_rules, loss_rules): 
    matches = []

    for i, a in enumerate(agents):
        for j in range(i, len(agents)):
            b = list(agents.keys())[j]
            if a != b:
                victories,lost, ties = test_agents(agents[a], agents[b], victory_rules, loss_rules)
                matches.append({
                    'a':a,
                    'b':b,
                    GameResult.Victory: victories    ,
                    GameResult.Loss: lost,
                    GameResult.Tie: ties   
                }) 

    return matches

def run(agents, victory_rules, loss_rules):
    matches = match_agents(agents, victory_rules, loss_rules)
    
    # display_winrate(matches)
    display_stacked_bar(matches)
    display_matches(matches)

def sum_data(matches):
    data = {}

    for match in matches:
        if match['a'] in data:
            data[match['a']][GameResult.Victory] += match[GameResult.Victory]
            data[match['a']][GameResult.Loss] += match[GameResult.Loss]
            data[match['a']][GameResult.Tie] += match[GameResult.Tie]
        else:
            data[match['a']] = {}
            data[match['a']][GameResult.Victory] = match[GameResult.Victory]
            data[match['a']][GameResult.Loss] = match[GameResult.Loss]
            data[match['a']][GameResult.Tie] = match[GameResult.Tie]
        
        if match['b'] in data:
            data[match['b']][GameResult.Victory] += match[GameResult.Loss]
            data[match['b']][GameResult.Loss] += match[GameResult.Victory]
            data[match['b']][GameResult.Tie] += match[GameResult.Tie]
        else:
            data[match['b']] = {}
            data[match['b']][GameResult.Victory] = match[GameResult.Loss]
            data[match['b']][GameResult.Loss] = match[GameResult.Victory]
            data[match['b']][GameResult.Tie] = match[GameResult.Tie]


    return data

def filter_data(matches, num_keys, key):
    return [round((matches[value][key] / (GAMES * (num_keys - 1))), 3) for value in matches]

def display_winrate(matches):
    data = sum_data(matches)

    agents = data.keys()

    victories = filter_data(data, len(agents), GameResult.Victory)
   

    fig, ax = plt.subplots()
    fig.autofmt_xdate()

    ax.bar(agents, victories, color = "forestgreen")

    plt.show()

def display_stacked_bar(matches):
    data = sum_data(matches)
    agents = data.keys()

    victories = filter_data(data, len(agents), GameResult.Victory)
    ties = filter_data(data, len(agents), GameResult.Tie)
    lost = filter_data(data, len(agents), GameResult.Loss)

    fig, ax = plt.subplots()
    fig.autofmt_xdate()

    bottom = np.zeros(len(agents))

    bars_victories = ax.bar(agents, victories, color="forestgreen", bottom=bottom)
    bottom += victories

    bars_ties = ax.bar(agents, ties, color="khaki", bottom=bottom)
    bottom += ties

    bars_lost = ax.bar(agents, lost, color="lightcoral", bottom=bottom)

    for bars, data_values in zip([bars_victories, bars_ties, bars_lost], [victories, ties, lost]):
        for bar, value in zip(bars, data_values):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height / 2 + bar.get_y(), str(value),
                    ha='center', va='center', color='black')


    plt.show()


def display_matches(matches):

    agents = sorted(list(set([item['a'] for item in matches] + [item['b'] for item in matches])))

    extended_data = matches.copy()

    for data in matches:
        extended_data.append({
            'a': data['b'], 
            'b': data['a'], 
            GameResult.Victory: data[GameResult.Loss], 
            GameResult.Loss: data[GameResult.Victory], 
            GameResult.Tie: data[GameResult.Tie]
        })
    
    num_agents = len(agents)
    wins_matrix = np.full((num_agents, num_agents), -1, dtype=float)

    for item in extended_data:
        i = agents.index(item['a'])
        j = agents.index(item['b'])

        if wins_matrix[i, j] < 0:
            wins_matrix[i, j] = 0
        if wins_matrix[j, i] < 0:
            wins_matrix[j, i] = 0

        wins_matrix[i, j] += item[GameResult.Victory]
        wins_matrix[j, i] += item[GameResult.Loss]

    wins_matrix = wins_matrix / (GAMES * 2)
        
    fig, ax = plt.subplots()

    cax = ax.matshow(wins_matrix, cmap='RdYlGn', vmin=0, vmax=1)

    ax.set_xticks(np.arange(num_agents))
    ax.set_yticks(np.arange(num_agents))

    ax.set_xticklabels(agents, rotation=45, ha='right')
    ax.xaxis.set_ticks_position('bottom')

    ax.set_yticklabels(agents)

    for i in range(num_agents):
        for j in range(num_agents):
            if wins_matrix[i, j] >= 0:
                ax.text(j, i, f"{wins_matrix[i, j]:.3f}", ha='center', va='center', color='black')
            else:
                ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, fill=True, edgecolor='black', facecolor='grey'))
         
    plt.xlabel('Opponent')
    plt.ylabel('Agent')
    plt.title('Wins Between AI Agents')

    fig.colorbar(cax)

    plt.show()



run(RPS_AGENTS, RPS_VICTORY_RULES, RPS_LOSS_RULES)

