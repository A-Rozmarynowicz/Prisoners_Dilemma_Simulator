from utils.Action import Action, Action_Space, Prison_Action_Space
from typing import Type, Generic
from Player import Player

class Environment(Generic[Action]):
    def __init__(self):
        self.total_score : list[tuple[int, ...]] = []
        self.action_history : list[tuple[Action, ...]] = []

    def Get_Action_Space() -> Type[Action]:
        return Action_Space

    def Duel(self) -> tuple[Action, ...]:
        return ()


class Prison(Environment[Prison_Action_Space]):
    def __init__(self):
        super().__init__()

    def Get_Action_Space() -> Type[Prison_Action_Space]:
        return Prison_Action_Space

    def Duel(self, *players : Player[Prison_Action_Space]) ->  tuple[Prison_Action_Space, ...]:
        actions : tuple[Action, ...] = ()
        for player in players:
            actions = actions + (player.Make_Move(self.action_history), )
        self.action_history.append(actions)
        return actions
