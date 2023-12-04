import random
from enum import IntEnum

class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

class GameResult(IntEnum):
    Victory = 0
    Loss = 1
    Tie = 2

VICTORY_DIC = {
    GameAction.Paper: GameAction.Rock,
    GameAction.Scissors: GameAction.Paper,
    GameAction.Rock: GameAction.Scissors
}

LOSS_DIC = {
    GameAction.Rock: GameAction.Paper,
    GameAction.Paper: GameAction.Scissors,
    GameAction.Scissors: GameAction.Rock
}

actions = []

def get_computer_action():
    return GameAction(random.randint(0, len(GameAction) - 1))

def get_agent_action():
    return GameAction.Paper

def assess_game(computer_action, agent_action):
    if VICTORY_DIC[agent_action] == computer_action:
        return GameResult.Victory
    elif LOSS_DIC[agent_action] == computer_action:
        return GameResult.Loss
    else:
        return GameResult.Tie


def play_round():
    computer_action = get_computer_action()
    agent_action = get_agent_action()
    result = assess_game(computer_action, agent_action)
    actions.append((computer_action, agent_action, result))

if __name__ == "__main__":
    play_round()

