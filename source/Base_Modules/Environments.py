from Base_Modules.Strategy import Strategy
from Prison_Strategies.Basic_Strategies import Prison_Strategy
from Base_Modules.Action import Act, Actions, Prison_Actions, Action_History
from typing import Type, Generic
from collections import defaultdict

class Environment(Generic[Act]):
    def __init__(self):
        self.total_score = defaultdict(int)
        self.action_history = Action_History[Act]()

    def Get_Actions(self) -> Type[Act]:
        return Actions

    def Duel(self, total_games : int, *strategies : Strategy) -> dict[int, Act]:
        return {}

    def Query_Strategies_Moves(self, total_games : int, *strategies : Strategy) -> dict[int, Act]:
        return {}

    def Reward(self, strategies_actions : dict[int, Act]) -> dict[int, int]:
        rewards = {}
        for i in strategies_actions.keys():
            rewards[i] = 0
        return rewards

    def _add_rewards(self, rewards : dict[int, int]) -> None:
        for strategy_id in rewards.keys():
            self.total_score[strategy_id] += rewards[strategy_id]

    def Get_Total_Rewards(self) -> defaultdict:
        return self.total_score

    def Get_Action_History(self) -> Action_History:
        return self.action_history

    def Reset(self) -> None:
        return

class Prison(Environment[Prison_Actions]):
    def __init__(self):
        super().__init__()

    def Get_Actions(self) -> Type[Prison_Actions]:
        return Prison_Actions

    def Duel(self, total_games : int, *strategies : Prison_Strategy) ->  dict[int, int]:
        if len(strategies) != 2:
            raise ValueError("This duel requires exactly 2 players")
        players_actions = self.Query_Strategies_Moves(total_games, *strategies)
        rewards = self.Reward(players_actions)
        self._add_rewards(rewards)
        return rewards, players_actions

    def Query_Strategies_Moves(self, total_games : int, *strategies : Prison_Strategy) ->  dict[int, Prison_Actions]:
        strategies_actions : dict[int, Act]= {}
        for strategy in strategies:
            strategies_actions[strategy.Get_ID()] = strategy.Make_Move(self.action_history, total_games=total_games)
        self.action_history.Append_Strategy_Actions(strategies_actions)
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

