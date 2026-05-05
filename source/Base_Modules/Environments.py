from Base_Modules.Strategy import Strategy
from Prison_Strategies.Basic_Strategies import Prison_Strategy
from Base_Modules.Action import Act, Actions, Prison_Actions, Action_History
from typing import Type, Generic

class Environment(Generic[Act]):
    def Get_Actions(self) -> Type[Act]:
        return Actions

    def Duel(self, total_games : int, *strategies : Strategy) -> tuple[dict[int, int], dict[int, Act]]:
        return ()

    def Query_Strategies_Moves(self, total_games : int, game_index : int, action_history : Action_History, *strategies : Strategy) -> dict[int, Act]:
        return {}

    def Reward(self, strategies_actions : dict[int, Act]) -> dict[int, int]:
        rewards = {}
        for i in strategies_actions.keys():
            rewards[i] = 0
        return rewards

class Prison(Environment[Prison_Actions]):
    def Get_Actions(self) -> Type[Prison_Actions]:
        return Prison_Actions

    def Duel(self, total_games : int, game_index : int, action_history : Action_History, *strategies : Prison_Strategy):
        if len(strategies) != 2:
            raise ValueError("This duel requires exactly 2 players")
        strategies_actions = self.Query_Strategies_Moves(total_games, game_index, action_history, *strategies)
        rewards = self.Reward(strategies_actions)
        return rewards, strategies_actions

    def Query_Strategies_Moves(self,
                               total_games : int,
                               game_index : int,
                               action_history : Action_History,
                               *strategies : Prison_Strategy):
        strategies_actions : dict[int, Act]= {}
        for strategy in strategies:
            strategies_actions[strategy.Get_ID()] = strategy.Make_Move(total_games=total_games, game_index=game_index, action_history=action_history, environment=self)
        return strategies_actions

    def Reward(self, strategies_actions):
        rewards = {}
        strategies = list(strategies_actions.keys())
        s1, s2 = strategies[0], strategies[1]
        if strategies_actions[s1] == Prison_Actions.Cooperate and strategies_actions[s2] == Prison_Actions.Cooperate:
            rewards[s1] = 3
            rewards[s2] = 3
        elif strategies_actions[s1] == Prison_Actions.Betray and strategies_actions[s2] == Prison_Actions.Cooperate:
            rewards[s1] = 5
            rewards[s2] = 0
        elif strategies_actions[s1] == Prison_Actions.Cooperate and strategies_actions[s2] == Prison_Actions.Betray:
            rewards[s1] = 0
            rewards[s2] = 5
        elif strategies_actions[s1] == Prison_Actions.Betray and strategies_actions[s2] == Prison_Actions.Betray:
            rewards[s1] = 1
            rewards[s2] = 1
        return rewards

