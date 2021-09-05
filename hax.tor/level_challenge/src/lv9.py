import z3
from z3 import Solver
all_attacker = z3.Real('x')
n = Solver()

n.add((1/6)*all_attacker-(1/8)*all_attacker==120)

n.check()
print(n.model())
# output = [x = 6000000000000000000/2083333333333333]
print(round(6000000000000000000/2083333333333333))