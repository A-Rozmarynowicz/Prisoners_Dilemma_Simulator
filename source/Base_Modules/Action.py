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
        self.action_history : list[Duel_Matrix] = []

    def Append_Strategy_Actions(self, strategy_actions : Duel_Matrix) -> None:
        self.action_history.append(strategy_actions)

    def Get_Action(self, history_index : int, strategy_ID : int) -> Act:
        return self.Get_Players_Actions(history_index)[strategy_ID]

    def Get_Strategys_Actions(self, history_index : int) -> Act:
        return self.action_history[history_index]

class Duel_Matrix(Generic[Act]):
    def __init__(self):
        super().__init__()
        self.duel_matrix = dict[tuple[int, ...], tuple(Act, ...)]

    def Set(self, indices_tuple : tuple[int, ...], actions_tuple : tuple[Act, ...]) -> None:
        self.duel_matrix[indices_tuple] = actions_tuple

    def Get(self, indices_tuple : tuple[int, ...]) -> tuple[Act, ...]:
        return self.duel_matrix[indices_tuple]