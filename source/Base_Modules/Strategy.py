from Base_Modules.Action import Act, Actions, Prison_Actions
from typing import Type, Generic
import random

class Strategy(Generic[Act]):
    def __init__(self, actions : Type[Act]):
        self.actions = actions

    def Get_Random_Action(self) -> Act:
        return random.choice(list(self.actions))

    def Make_Move(self, ID : int, action_history : list[dict[int, Act]], total_games : int) -> Act:
        return None