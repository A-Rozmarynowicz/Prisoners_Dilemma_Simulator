from Base_Modules.Action import Act, Actions, Prison_Actions, Action_History
from Base_Modules.Environments import Environment
from typing import Type, Generic
import random

class Strategy(Generic[Act]):
    def __init__(self, actions : Type[Act], ID : int = -1):
        self.actions = actions
        self.ID = ID

    def Set_ID(self, new_id : int) -> None:
        self.ID = new_id

    def Get_Random_Action(self) -> Act:
        return random.choice(list(self.actions))

    def Make_Move(self, total_games : int, game_index : int, action_history : Action_History[Act], environment:Environment) -> Act:
        return None

    def Get_ID(self) -> int:
        return self.ID

    def __str__(self):
        return f"({self.ID}):" + self.__class__.__name__

    def Reset(self) -> None:
        return