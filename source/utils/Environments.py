from utils.Action import Act, Actions, Prison_Actions, Action_History
from typing import Type, Generic
from Player import Player

class Environment(Generic[Act]):
    def __init__(self):
        self.total_score : dict[int, int] = {}
        self.action_history = Action_History()

    def Get_Actions() -> Type[Act]:
        return Actions

    def Duel(self) -> dict[int, Act]:
        return ()

class Prison(Environment[Prison_Actions]):
    def __init__(self):
        super().__init__()

    def Get_Actions() -> Type[Prison_Actions]:
        return Prison_Actions

    def Duel(self, *players : Player[Prison_Actions]) ->  dict[int, Prison_Actions]:
        players_actions = {}
        for player in players:
            players_actions[player.Get_ID()] = player.Make_Move(self.action_history)
        self.action_history.append(players_actions)
        return players_actions

    