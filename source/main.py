from utils.Action import Default_Action_Space
from utils.Strategy import Strategy

d = Strategy(Default_Action_Space)
print(d.Make_Move([(1, 2)]))