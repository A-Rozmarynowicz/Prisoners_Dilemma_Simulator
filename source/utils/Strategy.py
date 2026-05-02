from source.utils.Action import Action

class Strategy():
    def __init__(self):
        pass

    def Make_Move() -> Action:
        return Action.Cooperate

class Random_Strategy(Strategy):
    def __init__(self):
        super().__init__()

    