from Base_Modules.Environments import Prison
from Prison_Strategies.Basic_Strategies import *
from Base_Modules.Game_Master import Game_Master
from Base_Modules.Action import Action_History, Prison_Actions, Duel_Matrix

prison = Prison()
actions = prison.Get_Actions()

strategies = {
    0: Random_Strategy(0, actions),
    1: Always_Betray(1, actions),
    2: Always_Cooperate(2, actions),
    3: Random_Strategy(3, actions, p_coop=0.1),
}

gm = Game_Master(prison, strategies=strategies)

duel_matrix, score = gm.Tournament(4, Game_Master.Game_Type.All_Vs_All, True, 2)
score = asc = {k: v for k, v in sorted(score.items(), key=lambda item: -item[1])}

winner = next(iter(score.keys()))

# print(str(strategies[winner]))
# print(score)

# print(duel_matrix.Get_Action_Statistics_Of_Strategy(1))

# for ah1 in duel_matrix.Get_All_Duels_Of_Strategy(1):
#     print(ah1.Get_Action_History())
#     print("\n")

