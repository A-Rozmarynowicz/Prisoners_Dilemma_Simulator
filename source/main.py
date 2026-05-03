from utils.Action import Prison_Actions
from utils.Strategy import Strategy, Prison_Strategy, Random_Strategy
from utils.Environments import Environment, Prison
from utils.Player import Bot_Player

p = Prison()
actions = p.Get_Actions()

s = Random_Strategy(actions)
d  = Bot_Player(0, s)

print(d.Make_Move([]))