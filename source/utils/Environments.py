from utils.Action import Act, Actions, Prison_Actions, Action_History
from utils.Player import Player
from typing import Type, Generic

class Environment(Generic[Act]):
    def __init__(self):
        self.total_score : dict[int, int] = {}
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

class Prison(Environment[Prison_Actions]):
    def __init__(self):
        super().__init__()

    def Get_Actions(self) -> Type[Prison_Actions]:
        return Prison_Actions

    def Duel(self, *players : Player[Prison_Actions]) ->  dict[int, int]:
        players_actions = self.Query_Players_Moves(*players)
        rewards = self.Reward(players_actions)
        return rewards

    def Query_Players_Moves(self, *players : Player[Prison_Actions]) ->  dict[int, Prison_Actions]:
        players_actions : dict[int, Act]= {}
        for player in players:
            players_actions[player.Get_ID()] = player.Make_Move(self.action_history)
        self.action_history.Append_Players_Actions(players_actions)
        return players_actions

    def Reward(self, players_actions):
        return super().Reward(players_actions)
