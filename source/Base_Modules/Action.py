from enum import Enum
from typing import TypeVar
from typing import Type, Generic
from collections import defaultdict

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

    def Get_Strategy_All_Actions(self, strategy_ID : int) -> list[Act]:
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

    def Get_All_Duels_Of_Strategy(self, strategy_id : int) -> list[Action_History]:
        all_duels : list[Action_History] = []
        for (strategies_ids, action_history) in self.duel_matrix.items():
            if strategy_id in strategies_ids:
                all_duels.append(action_history)
        return all_duels

    def Get_Action_Statistics_Of_Strategy(self, strategy_id : int) -> dict[Act, int]:
        stats = defaultdict(int)
        for ah in self.Get_All_Duels_Of_Strategy(strategy_id):
            for action in ah.Get_Strategy_All_Actions(strategy_id):
                stats[action] += 1
        return stats