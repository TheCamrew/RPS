import pytest
from rps_game import GameResult, assess_game
from rps_rules import GameAction, VICTORY_RULES, LOSS_RULES


@pytest.mark.draw
def test_draw():
    '''
    Partidas con empate
    '''

    assert GameResult.Tie == assess_game(
        agent_action=GameAction.Rock,
        computer_action=GameAction.Rock, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)

    assert GameResult.Tie == assess_game(
        agent_action=GameAction.Scissors, 
        computer_action=GameAction.Scissors, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)

    assert GameResult.Tie == assess_game(
        agent_action=GameAction.Paper,
        computer_action=GameAction.Paper, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)

@pytest.mark.rock
def test_rock_loses():
    '''
    Rock pierde con Paper 
    '''
    assert GameResult.Victory == assess_game(
        agent_action=GameAction.Paper,
        computer_action=GameAction.Rock, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)

@pytest.mark.rock
def test_rock_wins():
    '''
    Rock gana a Scissors
    '''
    assert GameResult.Loss == assess_game(
        agent_action=GameAction.Scissors,
        computer_action=GameAction.Rock, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)

@pytest.mark.paper
def test_paper_loses():
    '''
    Paper pierde con Scissors
    '''
    assert GameResult.Victory == assess_game(
        agent_action=GameAction.Scissors,
        computer_action=GameAction.Paper, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)

@pytest.mark.paper
def test_paper_wins():
    '''
    Paper gana a Rock
    '''
    assert GameResult.Loss == assess_game(
        agent_action=GameAction.Rock,
        computer_action=GameAction.Paper, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)

@pytest.mark.scissors
def test_scissors_loses():
    '''
    Scissors pierde con Rock 
    '''
    assert GameResult.Victory == assess_game(
        agent_action=GameAction.Rock,
        computer_action=GameAction.Scissors, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)

@pytest.mark.scissors
def test_scissors_wins():
    '''
    Scissors gana a Paper 
    '''
    assert GameResult.Loss == assess_game(
        agent_action=GameAction.Paper,
        computer_action=GameAction.Scissors, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)