from utils.Environments import Prison
from utils.Player import Bot_Player
from Prison_Strategies.Basic_Strategies import *

prison = Prison()
actions = prison.Get_Actions()

random_player_1 = Bot_Player(0, actions, Random_Strategy)
random_player_2 = Bot_Player(1, actions, Always_Betray)

for i in range(10):
    prison.Duel(random_player_1, random_player_2)

print(prison.Get_Total_Rewards())