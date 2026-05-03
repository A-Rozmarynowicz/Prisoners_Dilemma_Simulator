from utils.Action import Act, Actions, Prison_Actions
from typing import Type, Generic
import random


class Strategy(Generic[Act]):
    def __init__(self, actions : Type[Act]):
        self.actions = actions

    def Get_Random_Action(self) -> Act:
        return random.choice(list(self.actions))

    def Make_Move(self, ID : int, action_history : list[dict[int, Act]]) -> Act:
        return None

class Prison_Strategy(Strategy[Prison_Actions]):
    def Make_Move(self, ID, action_history) -> Prison_Actions:
        return list(Prison_Actions)[0]

class Random_Strategy(Prison_Strategy):
    def Make_Move(self, ID, action_history):
        return self.Get_Random_Action()

