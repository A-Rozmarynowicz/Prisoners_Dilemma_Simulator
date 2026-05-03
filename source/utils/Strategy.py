from utils.Action import Action, Prison_Action_Space
from typing import Type, Generic
import random


class Strategy(Generic[Action]):
    def __init__(self):
        pass

    def Get_Random_Action(self) -> Action:
        return random.choice(list(Action))

    def Make_Move(self, ID : int, action_history : list[tuple[Action, ...]]) -> Action:
        return list(Action)[0]

class Prison_Strategy(Strategy[Prison_Action_Space]):
    pass

class Random_Strategy(Prison_Strategy):
    def __init__(self):
        super().__init__()

    def Make_Move(self, ID, action_space, action_history):
        return self.Get_Random_Action()

