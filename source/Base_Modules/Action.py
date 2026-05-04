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
        self.action_history : dict[int, list[Act]] = {}

    def Append_Strategy_Actions(self, strategy_actions : dict[int, Act]) -> None:
        for (id, action) in strategy_actions.items():
            if self.action_history.get(id) == None:
                self.action_history[id] = [action]
            else:
                self.action_history[id].append(action)

    def Get_All_Strategy_Actions(self, strategy_ID : int) -> list[Act]:
        return self.action_history[strategy_ID]

class Duel_Matrix(Generic[Act]):
    def __init__(self):
        super().__init__()
        self.duel_matrix : dict[tuple[int, ...], Action_History[Act]] = {}

    def Append_Strategy_Actions(self,  strategy_actions : dict[int, Act]) -> None:
        sorted_indices = tuple(sorted(strategy_actions.keys()))
        if self.duel_matrix.get(sorted_indices) == None:
            self.duel_matrix[sorted_indices] = Action_History[Act]()
        self.duel_matrix[sorted_indices].Append_Strategy_Actions(strategy_actions)