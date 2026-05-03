from Base_Modules.Action import Act, Actions, Prison_Actions, Action_History
from typing import Type, Generic
import random

class Strategy(Generic[Act]):
    def __init__(self, ID : int, actions : Type[Act]):
        self.actions = actions
        self.ID = ID

    def Get_Random_Action(self) -> Act:
        return random.choice(list(self.actions))

    def Make_Move(self, total_games : int, game_index : int, action_history : Action_History[Act]) -> Act:
        return None

    def Get_ID(self) -> int:
        return self.ID

    def __str__(self):
        return self.__class__.__name__