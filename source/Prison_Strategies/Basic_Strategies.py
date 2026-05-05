from Base_Modules.Strategy import Strategy
from Base_Modules.Action import Action_History
from Base_Modules.Action import Prison_Actions as pacts
from random import random, choice
from collections import defaultdict
import pickle

class Prison_Strategy(Strategy[pacts]):
    def Make_Move(self, total_games : int, game_index : int, action_history : Action_History[Prison_Strategy], environment) -> pacts:
        return list(pacts)[0]

class Random_Strategy(Prison_Strategy):
    def __init__(self, actions, ID=-1, p_coop: float = 0.5):
        super().__init__(ID, actions)
        self.p = p_coop

    def __str__(self):
        return super().__str__() + f" (p_coop={self.p})"

    def Make_Move(self, total_games, game_index, action_history, environment):
        if random() < self.p:
            return pacts.Cooperate
        else:
            return pacts.Betray

class Always_Betray(Prison_Strategy):
    def Make_Move(self, total_games, game_index, action_history, environment):
        return pacts.Betray

class Always_Cooperate(Prison_Strategy):
    def Make_Move(self, total_games, game_index, action_history, environment):
        return pacts.Cooperate

class Patient_Unforgiving(Prison_Strategy):
    def __init__(self, actions, ID=-1, patience : int = 1):
        super().__init__(ID, actions)
        self.patience = patience

    def __str__(self):
        return super().__str__() + f" (patience={self.patience})"

    def Make_Move(self, total_games, game_index, action_history, environment):
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

    def Make_Move(self, total_games, game_index, action_history, environment):
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

    def Make_Move(self, total_games, game_index, action_history, environment):
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

    def Make_Move(self, total_games, game_index, action_history, environment):
        self_actions, enemy_actions = action_history.Get_Ally_Enemy_Actions(self.ID)

        if game_index == 0:
            return pacts.Cooperate

        if self_actions[-1] == pacts.Cooperate:
            return enemy_actions[-1]
        else:
            if random() < self.p_forgive:
                return pacts.Cooperate
            return pacts.Betray

class Reinforcement_Learning(Prison_Strategy):
    def __init__(self, actions, ID = -1, eps=0.9, eps_decay=0.999, eps_min=0.005, gamma=0.99, lr=0.1, state_size=5, register_enemy_ID=False):
        super().__init__(actions, ID)
        self.q_table = defaultdict(float)
        self.eps = eps
        self.eps_init = eps
        self.eps_decay = eps_decay
        self.eps_min = eps_min
        self.gamma=gamma
        self.lr=lr
        self.state_size = state_size
        self.last_action = pacts.Cooperate
        self.last_state = tuple()
        self.eval = False
        self.register_enemy_ID = register_enemy_ID

    def Save_Q_Table(self, filename : str) -> None:
        with open(filename, "wb") as f:
            pickle.dump(self.q_table, f)

    def Load_Q_Table(self, filename : str) -> None:
        with open(filename, "rb") as f:
            self.q_table = pickle.load(f)

    def Eval(self) -> None:
        self.eval = True

    def Train(self) -> None:
        self.eval = False

    def Reset(self):
        self.eps = self.eps_init
        self.q_table = defaultdict(float)
        self.last_action = pacts.Cooperate
        self.last_state = tuple()
        self.eval = False

    def Create_Q_Key(self, s, a, eID) -> tuple:
        return s + (eID,) + (a,) if self.register_enemy_ID else s + (a,)

    def Update_Q_Table(self, last_state : tuple, new_state : tuple, last_action : pacts, last_reward : float, enemy_ID : int) -> None:
        max_current_state_q = -float("inf")
        for a in list(pacts):
            max_current_state_q = max(max_current_state_q, self.q_table[self.Create_Q_Key(s=new_state, a=a, eID=enemy_ID)])
        delta = last_reward + self.gamma*max_current_state_q - self.q_table[self.Create_Q_Key(s=last_state, a=last_action,eID=enemy_ID)]
        self.q_table[self.Create_Q_Key(s=last_state, a=last_action, eID=enemy_ID)] += self.lr*delta

    def Choose_Action(self, state : tuple, enemy_ID : int) -> pacts:
        sa_reward = {}
        for a in list(pacts):
            sa_reward[a] = self.q_table[self.Create_Q_Key(state, a, enemy_ID)]

        if random() < self.eps and not self.eval:
            action = choice(list(pacts))
        else:
            action = max(sa_reward, key=sa_reward.get)

        return action

    def Make_Move(self, total_games, game_index, action_history, environment):
        self_actions, enemy_actions = action_history.Get_Ally_Enemy_Actions(self.ID)

        if game_index == 0:
            self.last_action = choice(list(pacts))
            self.last_state = tuple()
            return self.last_action

        state = tuple()
        for i in range(min(self.state_size, len(enemy_actions))):
            state = state + (enemy_actions[-i-1],)
        for i in range(min(self.state_size, len(enemy_actions))):
            state = state + (self_actions[-i-1], )

        action = self.Choose_Action(state=state)

        if not self.eval:
            enemy_id = [i for i in action_history.Get_Action_History().keys() if i != self.ID][0]
            last_reward = environment.Reward({
                self.ID : self_actions[-1],
                enemy_id : enemy_actions[-1]
                })[0]
            self.Update_Q_Table(self.last_state, state, self.last_action, last_reward=last_reward)

        self.last_state = state
        self.last_action = action

        self.eps = max(self.eps_min, self.eps*self.eps_decay)

        return action


