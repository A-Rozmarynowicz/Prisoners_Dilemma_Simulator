from Prison_Strategies.Basic_Strategies import Prison_Strategy
from Base_Modules.Action import Prison_Actions as pacts
from random import random, choice
from collections import defaultdict
import pickle

class Q_Learning(Prison_Strategy):
    def __init__(self, actions, ID = -1, eps=0.9, eps_decay=0.999, eps_min=0.005, gamma=0.99, lr=0.1, state_size=2, register_enemy_ID=False, eps_eval = 0.0001):
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
        self.eps_eval = eps_eval

    def Save_Q_Table(self, filename : str) -> None:
        with open(filename, "wb") as f:
            d = {
                "q_table" : self.q_table,
                "state_size" : self.state_size,
                "register_enemy_ID" : self.register_enemy_ID,
                "eps_init" : self.eps_init,
                "eps" : self.eps,
                "eps_decay" : self.eps_decay,
                "eps_min" : self.eps_min,
                "eps_eval" : self.eps_eval,
                "lr" : self.lr,
                "gamma": self.gamma
            }
            pickle.dump(d, f)

    def Load_Q_Table(self, filename : str) -> None:
        with open(filename, "rb") as f:
            data = pickle.load(f)
            for k, v in data.items():
                setattr(self, k, v)

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

        e = self.eps if not self.eval else self.eps_eval

        if random() < e:
            action = choice(list(pacts))
        else:
            action = max(sa_reward, key=sa_reward.get)

        return action

    def Choose_1st_Action(self) -> pacts:
        if len(self.q_table) == 0 or not self.eval:
            return choice(list(pacts))
        max_reward_per_a = defaultdict(float)
        for key in self.q_table.keys():
            if len(key) <= 2 and len(key) > 0:
                max_reward_per_a[key[-1]] = max(max_reward_per_a[key[-1]], self.q_table[key])
        res = max(max_reward_per_a, key=max_reward_per_a.get)
        return res

    def Make_Move(self, total_games, game_index, action_history, environment, **extra_info):
        self_actions, enemy_actions = action_history.Get_Ally_Enemy_Actions(self.ID)

        if game_index == 0:
            self.last_action = self.Choose_1st_Action()
            self.last_state = tuple()
            return self.last_action

        state = tuple()
        for i in range(min(self.state_size, len(enemy_actions))):
            state = state + (enemy_actions[-i-1],)
        for i in range(min(self.state_size, len(enemy_actions))):
            state = state + (self_actions[-i-1], )

        enemy_id = [i for i in action_history.Get_Action_History().keys() if i != self.ID][0]

        action = self.Choose_Action(state=state, enemy_ID=enemy_id)

        if not self.eval:
            last_reward = environment.Reward({
                self.ID : self_actions[-1],
                enemy_id : enemy_actions[-1]
                })[self.ID]
            self.Update_Q_Table(self.last_state, state, self.last_action, last_reward=last_reward, enemy_ID=enemy_id)

        self.last_state = state
        self.last_action = action

        self.eps = max(self.eps_min, self.eps*self.eps_decay)

        return action