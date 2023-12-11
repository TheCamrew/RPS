from rps_agents import RPS_AGENTS
from rps_rules import VICTORY_RULES as RPS_VICTORY_RULES, LOSS_RULES as RPS_LOSS_RULES

from rpsls_agents import RPSLS_AGENTS
from rpsls_rules import VICTORY_RULES as RPSLS_VICTORY_RULES, LOSS_RULES as RPSLS_LOSS_RULES

from agent_tester import run

choice = -1

GAMES = -1

while choice < 0 or choice > 2: 
    try:
        choice = int(input("Elegir modo de juego RPS[0] o RPSLS[1]: "))
    except ValueError:
        print("Valor invalido")


while GAMES < 0 : 
    try:
        GAMES = int(input("En cuantas partidas se van a enfrentar los agentes (recomendadas 10000): "))
    except ValueError:
        print("Valor invalido")
    

if choice == 0:
    run(RPS_AGENTS, RPS_VICTORY_RULES, RPS_LOSS_RULES, GAMES)
else:
    run(RPSLS_AGENTS, RPSLS_VICTORY_RULES, RPSLS_LOSS_RULES, GAMES)