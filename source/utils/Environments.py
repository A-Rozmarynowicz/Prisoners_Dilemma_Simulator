from utils.Action import Act, Actions, Prison_Actions, Action_History
from utils.Player import Player
from typing import Type, Generic
from collections import defaultdict

class Environment(Generic[Act]):
    def __init__(self):
        self.total_score = defaultdict(int)
        self.action_history = Action_History[Act]()

    def Get_Actions(self) -> Type[Act]:
        return Actions

    def Duel(self) -> dict[int, Act]:
        return {}

    def Query_Players_Moves(self) -> dict[int, Act]:
        return {}

    def Reward(self, players_actions : dict[int, Act]) -> dict[int, int]:
        rewards = {}
        for i in players_actions.keys():
            rewards[i] = 0
        return rewards

    def _add_rewards(self, rewards : dict[int, int]) -> None:
        for player in rewards.keys():
            self.total_score[player] += rewards[player]

    def Get_Total_Rewards(self) -> defaultdict:
        return self.total_score

class Prison(Environment[Prison_Actions]):
    def __init__(self):
        super().__init__()

    def Get_Actions(self) -> Type[Prison_Actions]:
        return Prison_Actions

    def Duel(self, *players : Player[Prison_Actions]) ->  dict[int, int]:
        if len(players) != 2:
            raise ValueError("This duel requires exactly 2 players")
        players_actions = self.Query_Players_Moves(*players)
        rewards = self.Reward(players_actions)
        self._add_rewards(rewards)
        return rewards, players_actions

    def Query_Players_Moves(self, *players : Player[Prison_Actions]) ->  dict[int, Prison_Actions]:
        players_actions : dict[int, Act]= {}
        for player in players:
            players_actions[player.Get_ID()] = player.Make_Move(self.action_history)
        self.action_history.Append_Players_Actions(players_actions)
        return players_actions

    def Reward(self, players_actions):
        rewards = {}
        players = list(players_actions.keys())
        p1, p2 = players[0], players[1]
        if players_actions[p1] == Prison_Actions.Cooperate and players_actions[p2] == Prison_Actions.Cooperate:
            rewards[p1] = 3
            rewards[p2] = 3
        elif players_actions[p1] == Prison_Actions.Betray and players_actions[p2] == Prison_Actions.Cooperate:
            rewards[p1] = 5
            rewards[p2] = 0
        elif players_actions[p1] == Prison_Actions.Cooperate and players_actions[p2] == Prison_Actions.Betray:
            rewards[p1] = 0
            rewards[p2] = 5
        elif players_actions[p1] == Prison_Actions.Betray and players_actions[p2] == Prison_Actions.Betray:
            rewards[p1] = 1
            rewards[p2] = 1
        return rewards

