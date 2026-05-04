

class Reward():
    def __init__(self):
        self.duel_rewards : dict[tuple[int, ...], dict[int, int]] = {}
        self.total_rewards : dict[int, int] = {}

    def Reset(self) -> None:
        self.duel_rewards.clear()
        self.total_rewards.clear()

    def Store_Duel_Rewards(self, rewards : dict[int, int]) -> None:
        ids_tuple = tuple(sorted(rewards))
        if self.duel_rewards.get(ids_tuple) == None:
            self.duel_rewards[ids_tuple] = {}
        for id in ids_tuple:
            if (self.duel_rewards[ids_tuple].get(id) == None):
                self.duel_rewards[ids_tuple][id] = 0
            if self.total_rewards.get(id) == None:
                self.total_rewards[id] = 0
            self.duel_rewards[ids_tuple][id] += rewards[id]

    def Get_Duel_Rewards(self) -> dict[tuple[int, ...], dict[int, int]]:
        return self.duel_rewards

    def Get_Total_Rewards(self) -> dict[int, int]:
        return self.total_rewards
