from Base_Modules.Environments import Prison
from Prison_Strategies.Basic_Strategies import *
from Base_Modules.Game_Master import Game_Master
from Base_Modules.Action import Action_History, Prison_Actions, Duel_Matrix

prison = Prison()
actions = prison.Get_Actions()

strategies = {
    0 : Patient_Unforgiving(0, actions),
    # 0: Random_Strategy(0, actions),
    # 2: Always_Betray(2, actions),
    2: Always_Cooperate(2, actions),
    # 3: Random_Strategy(3, actions, p_coop=0.1),
}

gm = Game_Master(prison, strategies=strategies, duel_size=2)

duel_matrix, rewards = gm.Tournament(4, Game_Master.Game_Type.All_Vs_All, True)
rewards.Sort_Total_Rewards()
winner = next(iter(rewards.Get_Total_Rewards()))

print(strategies[winner])

print(duel_matrix.Get_Action_History((0, 2)).Get_Action_History())

# # print(duel_matrix.Get_Action_Statistics_Of_Strategy(1))

# # for ah1 in duel_matrix.Get_All_Duels_Of_Strategy(1):
# #     print(ah1.Get_Action_History())
# #     print("\n")

