from utils.Action import Action
from typing import Type, Generic
from Player import Player

class Environment(Generic[Action]):
    def __init__(self):
        self.total_score : list[tuple[int, ...]] = []
        self.action_history : list[tuple[Action, ...]] = []

    def Duel(self) ->  tuple:
        return ()

class Prison(Environment):
    def __init__(self):
        super().__init__()

    def Duel(self, *players : Player) ->  tuple[Action, ...]:
        actions : tuple[Action, ...] = ()
        for player in players:
            actions = actions + (player.Make_Move(self.action_history), )
        return actions

        