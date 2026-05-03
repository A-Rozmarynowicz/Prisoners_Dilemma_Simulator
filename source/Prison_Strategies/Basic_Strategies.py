from utils.Strategy import Strategy
from utils.Action import Prison_Actions

class Prison_Strategy(Strategy[Prison_Actions]):
    def Make_Move(self, ID, action_history) -> Prison_Actions:
        return list(Prison_Actions)[0]

class Always_Betray(Prison_Strategy):
    def Make_Move(self, ID, action_history):
        return Prison_Actions.Betray

class Random_Strategy(Prison_Strategy):
    def Make_Move(self, ID, action_history):
        return self.Get_Random_Action()

