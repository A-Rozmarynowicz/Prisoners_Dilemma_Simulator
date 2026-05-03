from Base_Modules.Environments import Prison
from Base_Modules.Player import Bot_Player
from Prison_Strategies.Basic_Strategies import *
from Base_Modules.Game_Master import Game_Master
from Base_Modules.Action import Action_History

prison = Prison()
actions = prison.Get_Actions()

players = {
    0: Bot_Player(0, actions, Random_Strategy),
    1: Bot_Player(1, actions, Always_Betray),
    2: Bot_Player(2, actions, Always_Cooperate),
}

gm = Game_Master(prison, players=players)

action_history, score = gm.Tournament(10, Game_Master.Game_Type.All_Vs_All, True, 2, False)

print(sorted(score.items(), key=lambda item: -item[1]))