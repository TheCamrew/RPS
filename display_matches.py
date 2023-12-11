import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

import numpy as np

from game import GameResult


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

def filter_data(matches, num_keys, key, games):

    return [round((matches[value][key] / (games * (num_keys - 1))), 3) for value in matches]

def display_winrate(matches, games):
    data = sum_data(matches)

    agents = data.keys()

    victories = filter_data(data, len(agents), GameResult.Victory, games)
   

    fig, ax = plt.subplots()
    fig.autofmt_xdate()

    ax.bar(agents, victories, color = "forestgreen")

    plt.show()

def display_stacked_bar(matches, games):

    data = sum_data(matches)
    agents = data.keys()

    victories = filter_data(data, len(agents), GameResult.Victory, games)
    ties = filter_data(data, len(agents), GameResult.Tie, games)
    lost = filter_data(data, len(agents), GameResult.Loss, games)

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

    fig.canvas.manager.set_window_title('Match Results')

    plt.title('Victories, Ties and Lost')
    plt.xlabel('Agents')
    plt.ylabel('Values')

    plt.show()

def display_matches(matches, games):

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

    wins_matrix = wins_matrix / (games * 2)
        
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
         
    plt.xlabel('Loser')
    plt.ylabel('Winner')
    plt.title('Wins Percentage Between Agents')

    fig.colorbar(cax)
    fig.canvas.manager.set_window_title('Wins Percentage Between Agents')

    plt.show()

def display_variance(matches, games):

    data = {}

    for match in matches:
        if match['a'] not in data:            
            data[match['a']] = []
        if match['b'] not in data:            
            data[match['b']] = []
        
        data[match['a']].append(match[GameResult.Victory] / games)
        data[match['b']].append(match[GameResult.Loss] / games)
    

    # Calculate means and standard deviations for each category
    means = [np.mean(values) for values in data.values()]
    std_devs = [np.std(values) for values in data.values()]

    # Create a bar chart with error bars
    plt.bar(range(len(data)), means, yerr=std_devs, align='center', alpha=0.7)
    plt.xticks(range(len(data)), list(data.keys()), rotation=45, ha="right")
    plt.title('Mean and Standard Deviation')
    plt.xlabel('Agents')
    plt.ylabel('Values')
    plt.ylim(0)
    plt.show()
        