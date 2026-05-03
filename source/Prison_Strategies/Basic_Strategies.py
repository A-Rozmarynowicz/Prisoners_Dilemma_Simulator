from Base_Modules.Strategy import Strategy
from Base_Modules.Action import Prison_Actions

class Prison_Strategy(Strategy[Prison_Actions]):
    def Make_Move(self, ID, action_history, total_games : int) -> Prison_Actions:
        return list(Prison_Actions)[0]

class Random_Strategy(Prison_Strategy):
    def Make_Move(self, ID, action_history, total_games : int):
        return self.Get_Random_Action()

class Always_Betray(Prison_Strategy):
    def Make_Move(self, ID, action_history, total_games : int):
        return Prison_Actions.Betray

class Always_Cooperate(Prison_Strategy):
    def Make_Move(self, ID, action_history, total_games : int):
        return Prison_Actions.Cooperate

