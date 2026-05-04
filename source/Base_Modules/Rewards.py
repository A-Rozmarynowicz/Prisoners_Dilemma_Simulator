class Reward():
    def __init__(self):
        self.duel_rewards : dict[tuple[int, ...], dict[int, int]] = {}
        self.total_rewards : dict[int, int] = {}

    def Reset(self) -> None:
        self.duel_rewards.clear()
        self.total_rewards.clear()

    def Store_Duel_Rewards(self, rewards : dict[int, int]) -> None:
        ids_tuple = tuple(sorted(rewards))
        self.__get_and_create_duel_reward(ids_tuple)
        for id in ids_tuple:
            self.__get_and_create_total_reward(id)
            self.duel_rewards[ids_tuple][id] += rewards[id]
            self.total_rewards[id] += rewards[id]

    def __get_and_create_duel_reward(self, ids_tuple : tuple[int, ...]) -> dict[int, int]:
        ids_tuple = tuple(sorted(ids_tuple))
        if self.duel_rewards.get(ids_tuple) == None:
            self.duel_rewards[ids_tuple] = {}
        for id in ids_tuple:
            if (self.duel_rewards[ids_tuple].get(id) == None):
                self.duel_rewards[ids_tuple][id] = 0
        return self.duel_rewards[ids_tuple]

    def __get_and_create_total_reward(self, id : int) -> int:
        if self.total_rewards.get(id) == None:
            self.total_rewards[id] = 0
        return self.total_rewards[id]

    def Sort_Total_Rewards(self) -> None:
        self.total_rewards = {k: v for k, v in sorted(self.total_rewards.items(), key=lambda item: -item[1])}

    def Get_Duel_Rewards(self, strategies : tuple[int, ...]) -> dict[int, int]:
        return self.__get_and_create_duel_reward(sorted(strategies))

    def Get_All_Duel_Rewards(self) -> dict[tuple[int, ...], dict[int, int]]:
        return self.duel_rewards

    def Get_Total_Rewards(self) -> dict[int, int]:
        return self.total_rewards
