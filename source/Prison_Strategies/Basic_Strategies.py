from Base_Modules.Strategy import Strategy
from Base_Modules.Action import Action_History
from Base_Modules.Action import Prison_Actions as pacts
from random import random

class Prison_Strategy(Strategy[pacts]):
    def Make_Move(self, total_games : int, game_index : int, action_history : Action_History[Prison_Strategy]) -> pacts:
        return list(pacts)[0]

class Random_Strategy(Prison_Strategy):
    def __init__(self, actions, ID=-1, p_coop: float = 0.5):
        super().__init__(ID, actions)
        self.p = p_coop

    def __str__(self):
        return super().__str__() + f" (p_coop={self.p})"

    def Make_Move(self, total_games, game_index, action_history):
        if random() < self.p:
            return pacts.Cooperate
        else:
            return pacts.Betray

class Always_Betray(Prison_Strategy):
    def Make_Move(self, total_games, game_index, action_history):
        return pacts.Betray

class Always_Cooperate(Prison_Strategy):
    def Make_Move(self, total_games, game_index, action_history):
        return pacts.Cooperate

class Patient_Unforgiving(Prison_Strategy):
    def __init__(self, actions, ID=-1, patience : int = 1):
        super().__init__(ID, actions)
        self.patience = patience

    def __str__(self):
        return super().__str__() + f" (patience={self.patience})"

    def Make_Move(self, total_games, game_index, action_history):
        _, enemy_actions = action_history.Get_Ally_Enemy_Actions(self.Get_ID())
        betray_count = 0
        for ea in enemy_actions:
            if ea == pacts.Betray:
                betray_count += 1
                if betray_count >= self.patience:
                    return pacts.Betray
        return pacts.Cooperate

class Copycat(Prison_Strategy):
    def __init__(self, actions, ID=-1, init_action : pacts = pacts.Cooperate):
        super().__init__(ID, actions)
        self.init_action = init_action

    def __str__(self):
        return super().__str__() + f" (1st={self.init_action})"

    def Make_Move(self, total_games, game_index, action_history):
        _, enemy_actions = action_history.Get_Ally_Enemy_Actions(self.Get_ID())
        if len(enemy_actions) > 0:
            return enemy_actions[-1]
        return self.init_action

class Periodic(Prison_Strategy):
    def __init__(self, actions, ID = -1, period=1):
        super().__init__(actions, ID)
        self.period = period

    def __str__(self):
        return super().__str__() + f" (period={self.period})"

    def Make_Move(self, total_games, game_index, action_history):
        self_actions, _ = action_history.Get_Ally_Enemy_Actions(self.ID)
        if len(self_actions) == 0:
            return pacts.Cooperate

        last_action : pacts = self_actions[-1]
        counter = 0
        for a in reversed(self_actions):
            if a == last_action:
                counter += 1
            if counter >= self.period:
                return last_action.Next()
        return last_action

class Forgiving(Prison_Strategy):
    def __init__(self, actions, ID = -1, p_forgive=0.1):
        super().__init__(actions, ID)
        self.p_forgive=p_forgive

    def __str__(self):
        return super().__str__() + f" (p_forgive={self.p_forgive})"

    def Make_Move(self, total_games, game_index, action_history):
        self_actions, enemy_actions = action_history.Get_Ally_Enemy_Actions(self.ID)

        if game_index == 0:
            return pacts.Cooperate

        if self_actions[-1] == pacts.Cooperate:
            return enemy_actions[-1]
        else:
            if random() < self.p_forgive:
                return pacts.Cooperate
            return pacts.Betray