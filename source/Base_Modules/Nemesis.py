
class Nemesis_Criterion():
    @classmethod
    def Get_Nemesis(cls, duel_rewards) -> dict[int, dict[int, int]]:
        strategy_nemesis = {}
        for (duel_ids, results) in duel_rewards.items():
            for id in duel_ids:
                enemy_id = ([i for i in duel_ids if i != id])[0]
                if strategy_nemesis.get(id) == None:
                    strategy_nemesis[id] = (enemy_id, {id : float("inf"), enemy_id : -float("inf")})
                strategy_nemesis[id] = cls.Criterion(id, enemy_id, strategy_nemesis[id], results)
        return strategy_nemesis

    @staticmethod
    def Criterion(id : int, enemy_id : int, nemesis : tuple[int, dict[int, int]], new_result : dict[int, int]) -> tuple[int, dict[int, int]]:
        pass

class Nemesis_Worst_Score(Nemesis_Criterion):

    @staticmethod
    def Criterion(id : int, enemy_id : int, nemesis : tuple[int, dict[int, int]], new_result : dict[int, int]):
        if new_result[id] < nemesis[1][id]:
            return (enemy_id, new_result)
        return nemesis
