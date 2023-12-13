import pytest
from game import GameResult, assess_game
from rpsls_rules import GameAction, VICTORY_RULES, LOSS_RULES


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

    assert GameResult.Tie == assess_game(
        agent_action=GameAction.Lizard,
        computer_action=GameAction.Lizard, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)

    assert GameResult.Tie == assess_game(
        agent_action=GameAction.Spock,
        computer_action=GameAction.Spock, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)

@pytest.mark.rock
def test_rock_loses():
    '''
    Rock pierde con Paper 
    '''
    assert GameResult.Loss == assess_game(
        agent_action=GameAction.Rock,
        computer_action=GameAction.Paper, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)
    '''
    Rock pierde con Spock 
    '''
    assert GameResult.Loss == assess_game(
        agent_action=GameAction.Rock,
        computer_action=GameAction.Spock, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)

@pytest.mark.rock
def test_rock_wins():
    '''
    Rock gana a Scissors
    '''
    assert GameResult.Victory == assess_game(
        agent_action=GameAction.Rock,
        computer_action=GameAction.Scissors, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)
    '''
    Rock gana a Lizard
    '''
    assert GameResult.Victory == assess_game(
        agent_action=GameAction.Rock,
        computer_action=GameAction.Lizard, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)

@pytest.mark.paper
def test_paper_loses():
    '''
    Paper pierde con Scissors
    '''
    assert GameResult.Loss == assess_game(
        agent_action=GameAction.Paper,
        computer_action=GameAction.Scissors, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)

    '''
    Paper pierde con Lizard
    '''
    assert GameResult.Loss == assess_game(
        agent_action=GameAction.Paper,
        computer_action=GameAction.Lizard, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)
    
@pytest.mark.paper
def test_paper_wins():
    '''
    Paper gana a Rock
    '''
    assert GameResult.Victory == assess_game(
        agent_action=GameAction.Paper,
        computer_action=GameAction.Rock, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)
    '''
    Paper gana a Spock
    '''
    assert GameResult.Victory == assess_game(
        agent_action=GameAction.Paper,
        computer_action=GameAction.Spock, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)

@pytest.mark.scissors
def test_scissors_loses():
    '''
    Scissors pierde con Rock 
    '''
    assert GameResult.Loss == assess_game(
        agent_action=GameAction.Scissors,
        computer_action=GameAction.Rock, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)
    '''
    Scissors pierde con Spock 
    '''
    assert GameResult.Loss == assess_game(
        agent_action=GameAction.Scissors,
        computer_action=GameAction.Spock, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)

@pytest.mark.scissors
def test_scissors_wins():
    '''
    Scissors gana a Paper 
    '''
    assert GameResult.Victory == assess_game(
        agent_action=GameAction.Scissors,
        computer_action=GameAction.Paper, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)
    '''
    Scissors gana a Lizard 
    '''
    assert GameResult.Victory == assess_game(
        agent_action=GameAction.Scissors,
        computer_action=GameAction.Lizard, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)

@pytest.mark.lizard
def test_lizard_loses():
    '''
    Lizard pierde con Rock 
    '''
    assert GameResult.Loss == assess_game(
        agent_action=GameAction.Lizard,
        computer_action=GameAction.Rock, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)
    '''
    Lizard pierde con Spock 
    '''
    assert GameResult.Loss == assess_game(
        agent_action=GameAction.Lizard,
        computer_action=GameAction.Scissors, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)

@pytest.mark.lizard
def test_lizard_wins():
    '''
    Lizard gana a Paper 
    '''
    assert GameResult.Victory == assess_game(
        agent_action=GameAction.Lizard,
        computer_action=GameAction.Paper, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)
    '''
    Lizard gana a Lizard 
    '''
    assert GameResult.Victory == assess_game(
        agent_action=GameAction.Lizard,
        computer_action=GameAction.Spock, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)

@pytest.mark.spock
def test_lizard_loses():
    '''
    Spock pierde con Rock 
    '''
    assert GameResult.Loss == assess_game(
        agent_action=GameAction.Spock,
        computer_action=GameAction.Paper, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)
    '''
    Spock pierde con Spock 
    '''
    assert GameResult.Loss == assess_game(
        agent_action=GameAction.Spock,
        computer_action=GameAction.Lizard, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)

@pytest.mark.spock
def test_lizard_wins():
    '''
    Spock gana a Paper 
    '''
    assert GameResult.Victory == assess_game(
        agent_action=GameAction.Spock,
        computer_action=GameAction.Rock, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)
    '''
    Spock gana a Lizard 
    '''
    assert GameResult.Victory == assess_game(
        agent_action=GameAction.Spock,
        computer_action=GameAction.Scissors, 
        victory_rules=VICTORY_RULES,
        loss_rules=LOSS_RULES)