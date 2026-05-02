from enum import Enum
import random
from typing import TypeVar


class Default_Action_Space(Enum):
    Cooperate = 0
    Betray = 1

    @classmethod
    def dupa():
        pass

class Action_Manager():
    def __init__(self, action_space : Enum):
        self.action_space = action_space

    def Get_Random_Action(self):
        return random.choice(list(self.action_space))

    def Get_Action_Space(self) -> Enum:
        return self.action_space