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
        if len(self.action_history) != 0:
            for id in strategy_actions.keys():
                if id not in self.action_history.keys():
                    raise ValueError("Action History tried to append an invalid key.")
        for (id, action) in strategy_actions.items():
            if self.action_history.get(id) == None:
                self.action_history[id] = [action]
            else:
                self.action_history[id].append(action)

    def Get_All_Strategy_Actions(self, strategy_ID : int) -> list[Act]:
        return self.action_history[strategy_ID]

    def Get_Action_History(self) -> dict[int, list[Act]]:
        return self.action_history

class Duel_Matrix(Generic[Act]):
    def __init__(self):
        super().__init__()
        self.duel_matrix : dict[tuple[int, ...], Action_History[Act]] = {}

    def Append_Strategy_Actions(self,  strategy_actions : dict[int, Act]) -> None:
        if len(self.duel_matrix) != 0:
            assert(len(next(iter(self.duel_matrix))) ==  len(strategy_actions))
        sorted_indices = tuple(sorted(strategy_actions.keys()))
        if self.duel_matrix.get(sorted_indices) == None:
            self.duel_matrix[sorted_indices] = Action_History[Act]()
        self.duel_matrix[sorted_indices].Append_Strategy_Actions(strategy_actions)

    def Get_Action_History(self, strategy_ids : tuple) -> Action_History:
        strategy_ids_tuple = tuple(sorted(strategy_ids))
        if self.duel_matrix.get(strategy_ids_tuple) == None:
            self.duel_matrix[strategy_ids_tuple] = Action_History[Act]()
        return self.duel_matrix[strategy_ids_tuple]