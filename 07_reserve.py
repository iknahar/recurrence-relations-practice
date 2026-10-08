"""An endowment reserve, built one policy year at a time."""
import math
#
A, B, C = 0.0005, 0.000035, 1.097
def q(x):
    h = A + B * C ** x * (C - 1) / math.log(C)
    return 1 - math.exp(-h)
#
age, term, S, i = 45, 20, 100_000.0, 0.04
v = 1 / (1 + i)
alive, annuity, cover = 1.0, 0.0, 0.0
for t in range(term):
    annuity += alive * v ** t             # value of paying 1 a year
    cover += alive * q(age + t) * v ** (t + 1)
    alive *= 1 - q(age + t)
cover += alive * v ** term                # paid out at maturity too
P = S * cover / annuity                   # premium that balances the books
#
V = [0.0]
for t in range(term):
    qt = q(age + t)
    V.append(((V[-1] + P) * (1 + i) - qt * S) / (1 - qt))
print(f"premium {P:,.2f}")
print([round(x) for x in V])
