from Base_Modules.Environments import Prison
from Prison_Strategies.Basic_Strategies import *
from Base_Modules.Game_Master import Game_Master
from Base_Modules.Action import Action_History

prison = Prison()
actions = prison.Get_Actions()

strategies = {
    0: Random_Strategy(0, actions),
    1: Always_Betray(1, actions),
    2: Always_Cooperate(2, actions),
    3: Random_Strategy(3, actions, p_coop=0.1),
}

gm = Game_Master(prison, strategies=strategies)

action_history, score = gm.Tournament(10, Game_Master.Game_Type.All_Vs_All, True, 2, False)
score = asc = {k: v for k, v in sorted(score.items(), key=lambda item: -item[1])}

winner = next(iter(score.keys()))

print(str(strategies[winner]))
print(score)