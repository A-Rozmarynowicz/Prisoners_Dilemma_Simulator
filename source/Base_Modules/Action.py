from enum import Enum
from typing import TypeVar
from typing import Type, Generic
from collections import defaultdict

class Actions(Enum):
    pass

    def __str__(self):
        return self.name

    def Next(self) -> Actions:
        members = list(type(self))
        i = members.index(self)
        return members[(i + 1) % len(members)]

class Prison_Actions(Actions):
    Cooperate = 0
    Betray = 1

Act = TypeVar("Act", bound=Actions)

class Action_History(Generic[Act]):
    def __init__(self, max_memory : int = -1):
        super().__init__()
        self.action_history : dict[int, list[Act]] = {}
        self.max_memory = max_memory

    def Append_Strategy_Actions(self, strategy_actions : dict[int, Act]) -> None:
        if len(self.action_history) != 0:
            for id in strategy_actions.keys():
                if id not in self.action_history.keys():
                    raise ValueError("Action History tried to append an invalid key.")
        for (id, action) in strategy_actions.items():
            self.__get_and_create_action_entry(id)
            self.action_history[id].append(action)
            if len(self.action_history[id]) > self.max_memory and self.max_memory > 0:
                self.action_history[id].pop(0)

    def __get_and_create_action_entry(self, id :int) -> list[Act]:
        if self.action_history.get(id) == None:
            self.action_history[id] = []
        return self.action_history[id]

    def Get_Ally_Enemy_Actions(self, ally_id : int) -> tuple[list[Act], dict[list[Act]]]:
        if len(self.action_history) == 0:
            return ([], {})
        ally_actions = self.__get_and_create_action_entry(ally_id)
        enemy_actions = {}
        for i in self.action_history:
            if i==ally_id:
                continue
            enemy_actions[i] = self.__get_and_create_action_entry(i)

        return (ally_actions, enemy_actions)

    def Get_Strategy_All_Actions(self, strategy_ID : int) -> list[Act]:
        return self.action_history[strategy_ID]

    def Get_Action_History(self) -> dict[int, list[Act]]:
        return self.action_history

class Action_History_1v1(Action_History, Generic[Act]):
    def Get_Ally_Enemy_Actions(self, ally_id) -> tuple[list[Act], list[Act]]:
        a, e = super().Get_Ally_Enemy_Actions(ally_id)
        if len(e) != 0:
            e = list(e.values())[0]
        return a, e

class Duel_Matrix(Generic[Act]):
    def __init__(self, duel_size : int, max_memory : int = -1):
        super().__init__()
        self.duel_matrix : dict[tuple[int, ...], Action_History[Act]] = {}
        self.max_memory = max_memory
        self.duel_size = duel_size

    def Append_Strategy_Actions(self,  strategy_actions : dict[int, Act]) -> None:
        if len(self.duel_matrix) != 0:
            assert(len(next(iter(self.duel_matrix))) ==  len(strategy_actions))
        sorted_indices = tuple(sorted(strategy_actions.keys()))
        if self.duel_matrix.get(sorted_indices) == None:
            self.duel_matrix[sorted_indices] = self._create_action_history_object()
        self.duel_matrix[sorted_indices].Append_Strategy_Actions(strategy_actions)

    def Get_Action_History(self, strategy_ids : tuple) -> Action_History:
        strategy_ids_tuple = tuple(sorted(strategy_ids))
        if self.duel_matrix.get(strategy_ids_tuple) == None:
            self.duel_matrix[strategy_ids_tuple] = self._create_action_history_object()
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

    def _create_action_history_object(self) -> Action_History:
        if self.duel_size == 2:
            return Action_History_1v1[Act](max_memory=self.max_memory)
        else:
            return Action_History[Act](max_memory=self.max_memory)