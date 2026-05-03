from Base_Modules.Strategy import Strategy
from Base_Modules.Action import Prison_Actions as pacts
from random import random

class Prison_Strategy(Strategy[pacts]):
    def __str__(self):
        return super().__str__() + " -> Prison Strategy"

    def Make_Move(self, ID, action_history, total_games : int) -> pacts:
        return list(pacts)[0]

class Random_Strategy(Prison_Strategy):
    def __init__(self, actions, p_coop: float = 0.5):
        super().__init__(actions)
        self.p = p_coop

    def __str__(self):
        return super().__str__() + f" -> Random (p_coop={self.p})"

    def Make_Move(self, ID, action_history, total_games):
        if random() < self.p:
            return pacts.Cooperate
        else:
            return pacts.Betray

class Always_Betray(Prison_Strategy):
    def __str__(self):
        return super().__str__() + " -> Always Betray"

    def Make_Move(self, ID, action_history, total_games : int):
        return pacts.Betray

class Always_Cooperate(Prison_Strategy):
    def __str__(self):
        return super().__str__() + " -> Always Cooperate"

    def Make_Move(self, ID, action_history, total_games : int):
        return pacts.Cooperate

# class Optimistic_Unforgiving(Prison_Strategy):