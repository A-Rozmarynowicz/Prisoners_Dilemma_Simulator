from Base_Modules.Environments import Environment
from Base_Modules.Strategy import Strategy
from typing import Type
from enum import Enum


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

    def Tournament(self,
                    total_games : int,
                    game_type : "Game_Master.Game_Type",
                    total_games_explicit : bool,
                    duel_size : int,
                    duel_oneself : bool
                    ):
        total_games_param = total_games if total_games_explicit else -1
        match game_type:
            case Game_Master.Game_Type.All_Vs_All:
                for game_index in range(0, total_games):
                    self.All_Vs_All_Match(total_games_param, duel_size, duel_oneself)
        return self.environment.Get_Action_History(), self.environment.Get_Total_Rewards()

    def All_Vs_All_Match(self, total_games_param : int, duel_size : int, duel_oneself : bool):
        inc = 0 if duel_oneself else 1
        ps = self.strategies

        for s0 in range(0, len(ps)):
            for s1 in range(s0+inc, len(ps)):
                self.environment.Duel(total_games_param, ps[list(ps.keys())[s0]], ps[list(ps.keys())[s1]])
