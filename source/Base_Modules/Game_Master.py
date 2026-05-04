from Base_Modules.Environments import Environment
from Base_Modules.Strategy import Strategy
from Base_Modules.Action import Duel_Matrix
from Base_Modules.Rewards import Reward
from enum import Enum
from collections import defaultdict


class Game_Master():
    class Game_Type(Enum):
        All_Vs_All = 0

    def __init__(
            self,
            environment : Environment,
            strategies : list[Strategy],
            duel_size : int,
            max_action_memory : int=-1
    ):
        self.environment : Environment = environment
        self.strategies : dict[int, Strategy] = strategies
        self.duel_size = duel_size
        self.duel_matrix = Duel_Matrix(duel_size=duel_size, max_memory=max_action_memory)
        self.rewards = Reward()

    def Tournament(self,
                    total_games : int,
                    game_type : "Game_Master.Game_Type",
                    total_games_explicit : bool,
                    ):
        total_games_param = total_games if total_games_explicit else -1
        match game_type:
            case Game_Master.Game_Type.All_Vs_All:
                for game_index in range(0, total_games):
                    self.All_Vs_All_Match(total_games_param, game_index, self.duel_size)
        return self.duel_matrix, self.rewards

    def All_Vs_All_Match(self, total_games_param : int, game_index : int, duel_size : int):
        ss = self.strategies

        for s0 in range(0, len(ss)):
            for s1 in range(s0+1, len(ss)):
                id0 = list(ss.keys())[s0]
                id1 = list(ss.keys())[s1]
                rewards, actions = self.environment.Duel(total_games_param,
                                                        game_index,
                                                        self.duel_matrix.Get_Action_History((id0, id1)),
                                                        ss[id0],
                                                        ss[id1])
                self.duel_matrix.Append_Strategy_Actions(actions)
                self.rewards.Store_Duel_Rewards(rewards)
