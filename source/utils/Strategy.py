from source.utils.Action import Action
from enum import Enum

class Strategy():
    def __init__(self):
        pass

    def Make_Move(self, action_history : list[tuple[Enum, Enum]]) -> Action:
        return Action.Cooperate

class Random_Strategy(Strategy):
    def __init__(self):
        super().__init__()

