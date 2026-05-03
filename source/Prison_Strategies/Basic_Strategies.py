from Base_Modules.Strategy import Strategy
from Base_Modules.Action import Action_History
from Base_Modules.Action import Prison_Actions as pacts
from random import random

class Prison_Strategy(Strategy[pacts]):
    def Make_Move(self, total_games : int, game_index : int, action_history : Action_History[Prison_Strategy]) -> pacts:
        return list(pacts)[0]

class Random_Strategy(Prison_Strategy):
    def __init__(self, ID, actions, p_coop: float = 0.5):
        super().__init__(ID, actions)
        self.p = p_coop

    def __str__(self):
        return super().__str__() + f" (p_coop={self.p})"

    def Make_Move(self, total_games, game_index, action_history):
        if random() < self.p:
            return pacts.Cooperate
        else:
            return pacts.Betray

class Always_Betray(Prison_Strategy):
    def Make_Move(self, total_games, game_index, action_history):
        return pacts.Betray

class Always_Cooperate(Prison_Strategy):
    def Make_Move(self, total_games, game_index, action_history):
        return pacts.Cooperate

# class Optimistic_Unforgiving(Prison_Strategy):