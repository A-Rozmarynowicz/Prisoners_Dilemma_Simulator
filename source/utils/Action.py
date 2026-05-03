from enum import Enum
from typing import TypeVar
from typing import Type, Generic

class Actions(Enum):
    pass

class Prison_Actions(Actions):
    Cooperate = 0
    Betray = 1

Act = TypeVar("Act", bound=Actions)

class Action_History(Generic[Act]):
    def __init__(self):
        super().__init__()
        self.action_history : list[dict[int, Act]] = {}

    def Append_Players_Actions(self, players_actions : dict[int, Act]) -> None:
        self.action_history.append(players_actions)

    def Get_Action(self, history_index : int, player_ID : int) -> Act:
        return self.action_history[history_index][player_ID]