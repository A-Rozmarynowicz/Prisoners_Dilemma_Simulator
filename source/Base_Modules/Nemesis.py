from Base_Modules.Strategy import Strategy

class Nemesis_Criterion():
    @classmethod
    def Get_Nemesis(cls, duel_rewards) -> dict[int, dict[int, int]]:
        strategy_nemesis = {}
        for (duel_ids, results) in duel_rewards.items():
            for id in duel_ids:
                enemy_id = ([i for i in duel_ids if i != id])[0]
                if strategy_nemesis.get(id) == None:
                    strategy_nemesis[id] = (enemy_id, {id : float("inf"), enemy_id : -float("inf")})
                strategy_nemesis[id] = cls.Criterion(id=id, enemy_id=enemy_id, nemesis=strategy_nemesis[id], new_result=results)
        return strategy_nemesis

    @staticmethod
    def Translate_Nemesis_To_Strategy_Names(strategies : dict[int, Strategy], nemesis : dict[int, tuple]) ->  dict[int, dict[int, int]]:
        name_nemesis = {}
        for (id, nem) in nemesis.items():
            enemy, results = nem
            results = {str(strategies[k]):v for k,v in results.items()}
            name_nemesis[str(strategies[id])] = (str(strategies[enemy]), results)
        return name_nemesis

    @staticmethod
    def Criterion(id : int, enemy_id : int, nemesis : tuple[int, dict[int, int]], new_result : dict[int, int]) -> tuple[int, dict[int, int]]:
        pass

class Nemesis_Worst_Score(Nemesis_Criterion):
    @staticmethod
    def Criterion(id : int, enemy_id : int, nemesis : tuple[int, dict[int, int]], new_result : dict[int, int]):
        if new_result[id] < nemesis[1][id]:
            return (enemy_id, new_result)
        return nemesis

class Nemesis_Best_Enemy_Score(Nemesis_Criterion):
    @staticmethod
    def Criterion(id : int, enemy_id : int, nemesis : tuple[int, dict[int, int]], new_result : dict[int, int]):
        if new_result[enemy_id] > nemesis[1][nemesis[0]]:
            return (enemy_id, new_result)
        return nemesis

class Nemesis_Largest_Difference(Nemesis_Criterion):
    @staticmethod
    def Criterion(id : int, enemy_id : int, nemesis : tuple[int, dict[int, int]], new_result : dict[int, int]):
        if (new_result[id] - new_result[enemy_id]) < (nemesis[1][id] - nemesis[1][nemesis[0]]):
            return (enemy_id, new_result)
        return nemesis