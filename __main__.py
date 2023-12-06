from rps_agents import RPS_AGENTS
from rps_rules import VICTORY_RULES as RPS_VICTORY_RULES, LOSS_RULES as RPS_LOSS_RULES
from agent_tester import run

GAMES = 10000

run(RPS_AGENTS, RPS_VICTORY_RULES, RPS_LOSS_RULES, GAMES)