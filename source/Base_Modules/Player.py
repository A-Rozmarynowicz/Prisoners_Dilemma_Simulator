from Base_Modules.Strategy import Strategy
from Base_Modules.Action import Act, Actions, Action_History
from typing import Type, Generic, Union

class Player(Generic[Act]):
    def __init__(self, ID : int):
        self.ID = ID

    def Get_ID(self) -> int:
        return self.ID

    def Make_Move(self, action_history : Action_History, total_games : int) -> Act:
        return None

class Bot_Player(Player):
    def __init__(self, ID: int, actions: type[Act], strategy: Union[Strategy[Act], Type[Strategy[Act]]]):
        super().__init__(ID=ID)

        if isinstance(strategy, type) and issubclass(strategy, Strategy):
            self.strategy = strategy(actions)
        elif isinstance(strategy, Strategy):
            self.strategy = strategy
        else:
            raise TypeError("strategy must be either a string or Strategy")

    def Make_Move(self, action_history : Action_History, total_games : int) -> Act:
        return self.strategy.Make_Move(ID=self.ID, action_history=action_history, total_games=total_games)