from utils.Action import Action
from typing import Type, Generic
import random


class Strategy(Generic[Action]):
    def __init__(self):
        pass

    def Get_Random_Action(self, action_space : Type[Action]) -> Action:
        return random.choice(list(action_space))

    def Make_Move(self, ID : int, action_space : Type[Action], action_history : list[tuple[Action, ...]]) -> Action:
        return list(action_space)[0]

class Random_Strategy(Strategy):
    def __init__(self):
        super().__init__()

    def Make_Move(self, ID, action_space, action_history):
        return self.Get_Random_Action()

