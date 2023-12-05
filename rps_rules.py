from enum import IntEnum
class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

VICTORY_RULES = {
    GameAction.Rock: [GameAction.Scissors],
    GameAction.Paper: [GameAction.Rock],
    GameAction.Scissors: [GameAction.Paper],
}

LOSS_RULES = {
    GameAction.Rock: [GameAction.Paper],
    GameAction.Paper: [GameAction.Scissors],
    GameAction.Scissors: [GameAction.Rock]
}