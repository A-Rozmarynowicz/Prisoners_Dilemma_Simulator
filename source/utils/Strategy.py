from utils.Action import Act, Actions, Prison_Actions
from typing import Type, Generic
import random


class Strategy(Generic[Act]):
    def __init__(self):
        pass

    def Get_Random_Action(self) -> Act:
        return random.choice(list(Actions))

    def Make_Move(self, ID : int, action_history : list[dict[int, Act]]) -> Act:
        return None

class Prison_Strategy(Strategy[Prison_Actions]):
    def Make_Move(self, ID, action_history) -> Prison_Actions:
        return list(Prison_Actions)[0]

class Random_Strategy(Prison_Strategy):
    def __init__(self):
        super().__init__()

    def Make_Move(self, ID, action_space, action_history):
        return self.Get_Random_Action()

