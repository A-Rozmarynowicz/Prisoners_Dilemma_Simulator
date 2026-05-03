from Strategy import Strategy
from utils.Action import Action
from typing import Type, Generic

class Player(Generic[Action]):
    def __init__(self, ID : int, action_space : Type[Action]):
        self.ID = ID
        self.action_space = action_space

    def Make_Move(self, action_history : list[tuple[Action, ...]]) -> Action:
        return Action.Cooperate

class Bot_Player(Player):
    def __init__(self, ID : int, strategy : Strategy):
        super().__init__(ID)
        self.strategy = strategy

    def Make_Move(self, ID : int, action_history : list[tuple[Action, ...]]) -> Action:
        return self.strategy.Make_Move(ID=ID, action_space=self.action_space, action_history=action_history)