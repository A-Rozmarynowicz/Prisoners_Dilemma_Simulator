from utils.Strategy import Strategy
from utils.Action import Act, Actions, Action_History
from typing import Type, Generic

class Player(Generic[Act]):
    def __init__(self, ID : int):
        self.ID = ID

    def Get_ID(self) -> int:
        return self.ID

    def Make_Move(self, action_history : Action_History) -> Act:
        return None

class Bot_Player(Player):
    def __init__(self, ID : int, strategy : Strategy):
        super().__init__(ID=ID)
        self.strategy = strategy

    def Make_Move(self, action_history : Action_History) -> Act:
        return self.strategy.Make_Move(ID=self.ID, action_history=action_history)