from enum import Enum
from typing import Type, TypeVar, Generic
import random


class Action_Space(Enum):
    pass

class Default_Action_Space(Action_Space):
    Cooperate = 0
    Betray = 1

T = TypeVar("T", bound=Action_Space)

class Action_Manager(Generic[T]):
    def __init__(self, action_space: Type[T]):
        self.action_space = action_space

    def Get_Random_Action(self) -> T:
        return random.choice(list(self.action_space))

    def Get_Action_Space(self) -> Type[T]:
        return self.action_space