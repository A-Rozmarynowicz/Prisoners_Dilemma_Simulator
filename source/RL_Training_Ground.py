from Base_Modules.Environments import Prison
from Prison_Strategies.Basic_Strategies import *
from Prison_Strategies.Reinforcement_Learning_Strategies import *
from Base_Modules.Game_Master import Game_Master
from Base_Modules.Action import Action_History, Prison_Actions, Duel_Matrix
import pandas as pd
from collections import defaultdict

prison = Prison()
actions = prison.Get_Actions()

def Get_Enemy_Strategies():
    return [
        Random_Strategy(actions=actions),
        Random_Strategy(actions=actions, p_coop=0.1),
        Always_Betray(actions=actions),
        Always_Cooperate(actions=actions),
        Patient_Unforgiving(actions=actions),
        Copycat(actions=actions),
        Periodic(actions=actions, period=1),
        Forgiving(actions=actions),
    ]



def Enumerate_Strategies(strategies_list : list[Strategy]) -> dict[int, Strategy]:
    strategies = {}
    for (i, s) in enumerate(strategies_list):
        strategies[i] = s
        s.Set_ID(i)
    return strategies


lrs = [0.01, 0.1]
gammas = [0.1, 0.5, 0.9, 0.99]
state_sizes = [1, 2, 3, 4, 5]
eps_decays = [0.999, 0.9]
register_enemy_ID_values = [False]

number_of_games_per_epoch = 10
number_of_RL_epochs = 60
total_games_explicit = True
max_action_memory = -1

eps_init = 1.0
eps_min = 0.05

def Raport(lr, gamma, state_size, eps_decay, reg_enemy):
    print(f"lr={lr}, gamma={gamma}, state_size={state_size}, eps_decay={eps_decay}, reg_enemy={reg_enemy}")

def Normal_Tournament(gm : Game_Master, number_of_games, total_games_explicit) -> tuple[Duel_Matrix, object]:
    return gm.Tournament(number_of_games, Game_Master.Game_Type.All_Vs_All, total_games_explicit=total_games_explicit)

def RL_Training(gm : Game_Master, number_of_games, number_of_RL_epochs, total_games_explicit) -> Game_Master:
    for i in range(number_of_RL_epochs):
        gm.Tournament(number_of_games, Game_Master.Game_Type.All_Vs_All, total_games_explicit=total_games_explicit)
        gm.Reset()
        if (i)%1000 == 0:
            print(i)
    return gm

final_scores = {}
i=0
best_score = -float("inf")
best_q_save_path = "best_q_learning_so_far.pkl"

for lr in lrs:
    for gamma in gammas:
        for state_size in state_sizes:
            for eps_decay in eps_decays:
                for register_enemy_ID in register_enemy_ID_values:
                    Raport(lr, gamma, state_size, eps_decay, register_enemy_ID)
                    strategies_list = Get_Enemy_Strategies()
                    q_learning = Q_Learning(actions=actions,
                                            eps=eps_init,
                                            eps_decay=eps_decay,
                                            eps_min=eps_min,
                                            gamma=gamma,
                                            lr=lr,
                                            state_size=state_size,
                                            register_enemy_ID=register_enemy_ID)
                    strategies_list.append(q_learning)
                    strategies = Enumerate_Strategies(strategies_list)
                    gm = Game_Master(environment=prison, strategies=strategies, duel_size=2, max_action_memory=max_action_memory)
                    q_learning.Train()
                    RL_Training(gm=gm, number_of_games=number_of_games_per_epoch, number_of_RL_epochs=number_of_RL_epochs, total_games_explicit=total_games_explicit)
                    q_learning.Eval()
                    duel_matrix, rewards = Normal_Tournament(gm=gm, number_of_games=number_of_games_per_epoch, total_games_explicit=total_games_explicit)
                    rewards.Sort_Total_Rewards()
                    total_q_score = rewards.Get_Total_Reward()[q_learning.Get_ID()]
                    final_scores[i] = {
                        "total_score" : total_q_score,
                        "lr" : lr,
                        "gamma" : gamma,
                        "state_size" : state_size,
                        "eps_decay" : eps_decay,
                        "reg_enemy" : register_enemy_ID,
                        "object" : q_learning
                    }
                    if total_q_score > best_score:
                        best_score = total_q_score
                        print("Achieved best score.")
                        q_learning.Save_Q_Table(filename=best_q_save_path)

                    i+=1
