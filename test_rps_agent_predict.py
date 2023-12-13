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