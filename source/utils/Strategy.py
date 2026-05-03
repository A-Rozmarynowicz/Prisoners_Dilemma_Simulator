from utils.Action import Action_Space, T
from typing import Type, TypeVar, Generic
import random


class Strategy(Generic[T]):
    def __init__(self, action_space: Type[T]):
        self.action_space = action_space

    def Get_Random_Action(self) -> T:
        return random.choice(list(self.action_space))

    def Get_Action_Space(self) -> Type[T]:
        return self.action_space

    def Make_Move(self, action_history : list[tuple[T, ...]]) -> T:
        return list(self.action_space)[0]

class Random_Strategy(Strategy):
    def __init__(self):
        super().__init__()

