from Base_Modules.Environments import Prison
from Base_Modules.Player import Bot_Player
from Prison_Strategies.Basic_Strategies import *
from Base_Modules.Game_Master import Game_Master

prison = Prison()
actions = prison.Get_Actions()

random_player_1 = Bot_Player(0, actions, Random_Strategy)
# random_player_2 = Bot_Player(1, actions, Always_Betray)
p3 = Bot_Player(2, actions, Always_Cooperate)

gm = Game_Master(prison, 10, True, Game_Master.Game_Type.All_Vs_All, 2, False, [random_player_1, p3])

print(gm.Tournament())