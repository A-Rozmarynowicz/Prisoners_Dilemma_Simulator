from Base_Modules.Environments import Prison
from Prison_Strategies.Basic_Strategies import *
from Base_Modules.Game_Master import Game_Master
from Base_Modules.Action import Action_History, Prison_Actions, Duel_Matrix

ss1 = {
    0 : Prison_Actions.Betray,
    1 : Prison_Actions.Cooperate,
    2 : Prison_Actions.Betray,
}
ss2 = {
    0 : Prison_Actions.Cooperate,
    3 : Prison_Actions.Cooperate,
    4 : Prison_Actions.Cooperate,
}
ss3 = {
    6 : Prison_Actions.Betray,
    7 : Prison_Actions.Betray,
    8 : Prison_Actions.Cooperate,
}

# ah = Action_History()
# ah.Append_Strategy_Actions(ss1)
# ah.Append_Strategy_Actions(ss2)
# ah.Append_Strategy_Actions(ss3)

dm = Duel_Matrix()
dm.Append_Strategy_Actions(ss1)
dm.Append_Strategy_Actions(ss2)
dm.Append_Strategy_Actions(ss3)

print(dm.Get_Action_History((6, 7, 8)).Get_Action_History())

# print(ah.Get_Action_History())

# prison = Prison()
# actions = prison.Get_Actions()

# strategies = {
#     0: Random_Strategy(0, actions),
#     1: Always_Betray(1, actions),
#     2: Always_Cooperate(2, actions),
#     3: Random_Strategy(3, actions, p_coop=0.1),
# }

# gm = Game_Master(prison, strategies=strategies)

# action_history, score = gm.Tournament(10, Game_Master.Game_Type.All_Vs_All, True, 2, False)
# score = asc = {k: v for k, v in sorted(score.items(), key=lambda item: -item[1])}

# winner = next(iter(score.keys()))

# print(str(strategies[winner]))
# print(score)
