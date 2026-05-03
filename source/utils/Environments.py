from utils.Action import Action
from typing import Type, Generic
from Player import Player

class Environment():
    def __init__(self):
        self.total_score = []
        self.action_history = []

    def Duel(self) ->  tuple:
        return ()

class Prison(Environment):
    def __init__(self):
        super().__init__()

    def Duel(self, player1 : Player, player2 : Player) ->  tuple:
        action1 = player1.Make_Move()
        return ()