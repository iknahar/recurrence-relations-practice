"""A life table is a recurrence: survivors forward, expectancy backward."""
import math
#
A, B, C = 0.0005, 0.000035, 1.097         # illustrative Gompertz-Makeham
def q(x):
    h = A + B * C ** x * (C - 1) / math.log(C)
    return min(1.0, 1 - math.exp(-h))     # chance of dying between x, x+1
#
TOP = 110
l = [100_000.0]                           # the radix: 100,000 births
for x in range(TOP):
    l.append(l[-1] * (1 - q(x)))          # l_{x+1} = l_x (1 - q_x)
#
e = [0.0] * (TOP + 1)                     # nobody is left at TOP
for x in range(TOP - 1, -1, -1):          # walk backwards from the end
    e[x] = (1 - q(x)) * (1 + e[x + 1])    # e_x = p_x (1 + e_{x+1})
#
for age in (0, 30, 65, 90):
    print(f"age {age:3d}: alive {l[age]:9,.0f}  years left {e[age]:5.1f}")
