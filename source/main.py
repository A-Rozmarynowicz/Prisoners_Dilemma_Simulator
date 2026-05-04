from Base_Modules.Environments import Prison
from Prison_Strategies.Basic_Strategies import *
from Base_Modules.Game_Master import Game_Master
from Base_Modules.Action import Action_History, Prison_Actions, Duel_Matrix
import pandas as pd

prison = Prison()
actions = prison.Get_Actions()

strategies = {
    0: Random_Strategy(0, actions),
    1: Always_Cooperate(1, actions),
    2: Always_Betray(2, actions),
    3: Random_Strategy(3, actions, p_coop=0.1),
    4 : Patient_Unforgiving(4, actions),
}

gm = Game_Master(prison, strategies=strategies, duel_size=2)

duel_matrix, rewards = gm.Tournament(4, Game_Master.Game_Type.All_Vs_All, True)
rewards.Sort_Total_Rewards()

total_rewards = rewards.Get_Total_Rewards()
rewards_per_name = {str(strategies[i]):total_rewards[i] for i in strategies.keys()}
rewards_per_name = pd.DataFrame(rewards_per_name, index=strategies.keys())

duel_rewards = rewards.Get_All_Duel_Rewards()


winner = next(iter(rewards.Get_Total_Rewards()))

players = [str(s) for s in strategies.values()]

print(players)

# Initialize matrix with NaN
df = pd.DataFrame(index=players, columns=players, dtype=object)

for (p1, p2), scores in duel_rewards.items():
    df.loc[str(strategies[p2]), str(strategies[p1])] = (scores[p1], scores[p2])

print(df)

# # for ah1 in duel_matrix.Get_All_Duels_Of_Strategy(1):
# #     print(ah1.Get_Action_History())
# #     print("\n")


# %%
