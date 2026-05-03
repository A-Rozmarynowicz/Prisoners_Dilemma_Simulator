from utils.Action import Prison_Actions
from utils.Strategy import Strategy, Prison_Strategy, Random_Strategy
from utils.Environments import Environment, Prison
from utils.Player import Bot_Player

prison = Prison()
actions = prison.Get_Actions()

random_player_1 = Bot_Player(0, actions, Random_Strategy)
random_player_2 = Bot_Player(1, actions, Random_Strategy)

for i in range(10):
    prison.Duel(random_player_1, random_player_2)

print(prison.Get_Total_Rewards())