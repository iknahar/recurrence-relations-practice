"""When the loop lies: roots, rounding and stability."""
from fractions import Fraction
import numpy as np
#
# x_{n+1} = (10/3) x_n - x_{n-1}, x_0 = 1, x_1 = 1/3
# the exact answer is (1/3)^n, which shrinks forever
x = [1.0, 1 / 3]
for n in range(39):
    x.append(10 / 3 * x[-1] - x[-2])
print("float, n = 40:", x[40])
print("exact, n = 40:", (1 / 3) ** 40)
#
# the same loop with exact fractions never drifts
f = [Fraction(1), Fraction(1, 3)]
for n in range(39):
    f.append(Fraction(10, 3) * f[-1] - f[-2])
print("fraction, n = 40:", float(f[40]))
#
def is_stable(coeffs):
    """a_n = c1 a_{n-1} + ... + ck a_{n-k}. Stable if all |roots| < 1."""
    roots = np.roots([1] + [-c for c in coeffs])
    return bool(np.all(np.abs(roots) < 1)), np.abs(roots).round(4)
#
print(is_stable([10 / 3, -1]))           # roots 3 and 1/3: not stable
print(is_stable([0.5, 0.3]))             # roots 0.85 and 0.35: stable
