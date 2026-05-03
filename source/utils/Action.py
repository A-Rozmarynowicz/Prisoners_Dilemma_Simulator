from enum import Enum
from typing import Type

import random

class Action_Space(Enum):
    pass

class Default_Action_Space(Action_Space):
    Cooperate = 0
    Betray = 1

class Action_Manager():
    def __init__(self, action_space : Type[Action_Space]):
        self.action_space = action_space

    def Get_Random_Action(self) -> Action_Space:
        return random.choice(list(self.action_space))

    def Get_Action_Space(self) -> Type[Action_Space]:
        return self.action_space