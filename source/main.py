from utils.Action import Default_Action_Space
from utils.Strategy import Strategy
from utils.Player import Bot_Player

s = Strategy()
d  = Bot_Player(0, Default_Action_Space, s)

print(d.Make_Move([(Default_Action_Space.Betray, Default_Action_Space.Cooperate)]))