from enum import Enum
from typing import TypeVar

class Action_Space(Enum):
    pass

class Default_Action_Space(Action_Space):
    Cooperate = 0
    Betray = 1

Action = TypeVar("Action", bound=Action_Space)
