from Base_Modules.Environments import Environment
from Base_Modules.Strategy import Strategy
from Base_Modules.Action import Duel_Matrix
from enum import Enum
from collections import defaultdict


class Game_Master():
    class Game_Type(Enum):
        All_Vs_All = 0

    def __init__(
            self,
            environment : Environment,
            strategies : list[Strategy],
    ):
        self.environment : Environment = environment
        self.strategies : dict[int, Strategy] = strategies
        self.duel_matrix = Duel_Matrix()
        self.total_rewards = defaultdict(int)

    def Tournament(self,
                    total_games : int,
                    game_type : "Game_Master.Game_Type",
                    total_games_explicit : bool,
                    duel_size : int,
                    ):
        total_games_param = total_games if total_games_explicit else -1
        match game_type:
            case Game_Master.Game_Type.All_Vs_All:
                for game_index in range(0, total_games):
                    self.All_Vs_All_Match(total_games_param, game_index, duel_size)
        return self.duel_matrix, self.total_rewards

    def All_Vs_All_Match(self, total_games_param : int, game_index : int, duel_size : int):
        ss = self.strategies

        for s0 in range(0, len(ss)):
            for s1 in range(s0+1, len(ss)):
                rewards, actions = self.environment.Duel(total_games_param,
                                                        game_index,
                                                        self.duel_matrix.Get_Action_History((s0, s1)),
                                                        ss[list(ss.keys())[s0]],
                                                        ss[list(ss.keys())[s1]])
                self.duel_matrix.Append_Strategy_Actions(actions)
                for (id, r) in rewards.items():
                    self.total_rewards[id] += r
