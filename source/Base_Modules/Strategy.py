from Base_Modules.Action import Act, Actions, Prison_Actions
from typing import Type, Generic
import random

class Strategy(Generic[Act]):
    def __init__(self, ID : int, actions : Type[Act]):
        self.actions = actions
        self.ID = ID

    def Get_Random_Action(self) -> Act:
        return random.choice(list(self.actions))

    def Make_Move(self, ID : int, action_history : list[dict[int, Act]], total_games : int) -> Act:
        return None

    def Get_ID(self) -> int:
        return self.ID

    def __str__(self):
        return "Base Strategy"