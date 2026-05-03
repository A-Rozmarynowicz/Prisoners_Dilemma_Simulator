from utils.Action import Prison_Actions
from utils.Strategy import Strategy, Prison_Strategy
from utils.Player import Bot_Player

s = Prison_Strategy()
d  = Bot_Player(0, s)

print(d.Make_Move([]))