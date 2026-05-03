from utils.Action import Action
from typing import Type, Generic
import random


class Strategy(Generic[Action]):
    def __init__(self, action_space: Type[Action]):
        self.action_space = action_space

    def Get_Random_Action(self) -> Action:
        return random.choice(list(self.action_space))

    def Get_Action_Space(self) -> Type[Action]:
        return self.action_space

    # def Make_Move(self, action_history : list[tuple[Action, ...]]) -> Action:
    #     return list(self.action_space)[0]

class Random_Strategy(Strategy):
    def __init__(self):
        super().__init__()

