from enum import Enum
from typing import Type, TypeVar, Generic
import random


class Action_Space(Enum):
    pass

class Default_Action_Space(Action_Space):
    Cooperate = 0
    Betray = 1

T = TypeVar("T", bound=Action_Space)
