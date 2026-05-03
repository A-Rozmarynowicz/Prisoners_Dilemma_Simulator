from Strategy import Strategy
from Action import Action

class Player():
    def __init__(self):
        pass

    def Make_Move(self) -> Action:
        return Action.Cooperate

class Bot_Player(Player):
    def __init__(self, strategy : Strategy):
        super().__init__()
        self.strategy = strategy

    def Make_Move(self, action_history : list) -> Action:
        return self.strategy.Make_Move(action_history)