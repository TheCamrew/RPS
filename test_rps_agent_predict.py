import pytest
from game import GameResult
from rpsls_rules import GameAction, VICTORY_RULES, LOSS_RULES
from rps_agents import rps_agent_predict


@pytest.mark.no_matches
def test_no_matches():
    '''
    Partidas sin jugar siendo jugador 0
    '''
    assert GameAction.Paper == rps_agent_predict([], 0)

    '''
    Partidas sin jugar siendo jugador 1
    '''
    assert GameAction.Paper == rps_agent_predict([], 1)

@pytest.mark.tie_matches
def test_tie_matches():
    '''
    Partida encontrada empatada siendo jugador 0
    '''
    assert GameAction.Scissors == rps_agent_predict([
        (GameAction.Paper, GameAction.Rock, GameResult.Victory),
        (GameAction.Paper, GameAction.Paper, GameResult.Tie),
        (GameAction.Paper, GameAction.Rock, GameResult.Victory)
    ], 0)

    
    assert GameAction.Paper == rps_agent_predict([
        (GameAction.Rock, GameAction.Rock, GameResult.Tie),
        (GameAction.Rock, GameAction.Rock, GameResult.Tie)
    ], 0)

    
    assert GameAction.Rock == rps_agent_predict([
        (GameAction.Scissors, GameAction.Scissors, GameResult.Tie),
        (GameAction.Scissors, GameAction.Scissors, GameResult.Tie)
    ], 0)

    '''
    Partida encontrada empatada siendo jugador 1
    '''
    assert GameAction.Scissors == rps_agent_predict([
        (GameAction.Paper, GameAction.Paper, GameResult.Tie),
        (GameAction.Paper, GameAction.Paper, GameResult.Tie)
    ], 1)

    
    assert GameAction.Paper == rps_agent_predict([
        (GameAction.Rock, GameAction.Rock, GameResult.Tie),
        (GameAction.Rock, GameAction.Rock, GameResult.Tie)
    ], 1)

    
    assert GameAction.Rock == rps_agent_predict([
        (GameAction.Scissors, GameAction.Scissors, GameResult.Tie),
        (GameAction.Scissors, GameAction.Scissors, GameResult.Tie)
    ], 1)

@pytest.mark.victory_matches
def test_victory_matches():
    '''
    Partida encontrada ganada siendo jugador 0
    '''
    assert GameAction.Paper == rps_agent_predict([        
        (GameAction.Paper, GameAction.Scissors, GameResult.Loss),
        (GameAction.Paper, GameAction.Rock, GameResult.Victory),
        (GameAction.Paper, GameAction.Scissors, GameResult.Loss)
    ], 0)

    
    assert GameAction.Paper == rps_agent_predict([        
        (GameAction.Scissors, GameAction.Scissors, GameResult.Tie),
        (GameAction.Paper, GameAction.Rock, GameResult.Victory),
        (GameAction.Scissors, GameAction.Scissors, GameResult.Tie)
    ], 0)

    
    assert GameAction.Rock == rps_agent_predict([        
        (GameAction.Paper, GameAction.Rock, GameResult.Victory),
        (GameAction.Rock, GameAction.Scissors, GameResult.Victory),
        (GameAction.Paper, GameAction.Rock, GameResult.Victory)
    ], 0)

    '''
    Partida encontrada ganada siendo jugador 1
    '''
    assert GameAction.Scissors == rps_agent_predict([        
        (GameAction.Paper, GameAction.Scissors, GameResult.Loss),
        (GameAction.Paper, GameAction.Rock, GameResult.Victory),
        (GameAction.Paper, GameAction.Scissors, GameResult.Loss)
    ], 1)

    
    assert GameAction.Scissors == rps_agent_predict([        
        (GameAction.Scissors, GameAction.Scissors, GameResult.Tie),
        (GameAction.Paper, GameAction.Rock, GameResult.Victory),
        (GameAction.Scissors, GameAction.Scissors, GameResult.Tie)
    ], 1)

    
    assert GameAction.Paper == rps_agent_predict([        
        (GameAction.Paper, GameAction.Rock, GameResult.Victory),
        (GameAction.Rock, GameAction.Scissors, GameResult.Victory),
        (GameAction.Paper, GameAction.Rock, GameResult.Victory)
    ], 1)


@pytest.mark.lost_matches
def test_lost_matches():
    '''
    Partida encontrada perdida siendo jugador 0
    '''
    assert GameAction.Scissors == rps_agent_predict([        
        (GameAction.Paper, GameAction.Scissors, GameResult.Loss),
        (GameAction.Rock, GameAction.Paper, GameResult.Loss),
        (GameAction.Paper, GameAction.Scissors, GameResult.Loss)
    ], 0)

    
    assert GameAction.Scissors == rps_agent_predict([        
        (GameAction.Scissors, GameAction.Scissors, GameResult.Tie),
        (GameAction.Rock, GameAction.Paper, GameResult.Loss),
        (GameAction.Scissors, GameAction.Scissors, GameResult.Tie)
    ], 0)

    
    assert GameAction.Paper == rps_agent_predict([        
        (GameAction.Paper, GameAction.Rock, GameResult.Victory),
        (GameAction.Scissors, GameAction.Rock, GameResult.Loss),
        (GameAction.Paper, GameAction.Rock, GameResult.Victory)
    ], 0)

    '''
    Partida encontrada perdida siendo jugador 1
    '''
    assert GameAction.Paper == rps_agent_predict([        
        (GameAction.Paper, GameAction.Scissors, GameResult.Loss),
        (GameAction.Rock, GameAction.Paper, GameResult.Loss),
        (GameAction.Paper, GameAction.Scissors, GameResult.Loss)
    ], 1)

    
    assert GameAction.Paper == rps_agent_predict([        
        (GameAction.Scissors, GameAction.Scissors, GameResult.Tie),
        (GameAction.Rock, GameAction.Paper, GameResult.Loss),
        (GameAction.Scissors, GameAction.Scissors, GameResult.Tie)
    ], 1)

    
    assert GameAction.Rock == rps_agent_predict([        
        (GameAction.Paper, GameAction.Rock, GameResult.Victory),
        (GameAction.Scissors, GameAction.Rock, GameResult.Loss),
        (GameAction.Paper, GameAction.Rock, GameResult.Victory)
    ], 1)
