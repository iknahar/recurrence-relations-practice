"""Second order recurrences with the characteristic equation."""
import numpy as np
#
# a_n = 5 a_{n-1} - 6 a_{n-2}, with a_0 = 2, a_1 = 5
c1, c2 = 5, -6
roots = np.roots([1, -c1, -c2])          # lambda^2 - 5 lambda + 6 = 0
print("roots:", roots)                    # [3. 2.]
#
# fit A and B so the formula matches the two starting values
a0, a1 = 2, 5
M = np.array([[1, 1], roots])            # rows: n = 0 and n = 1
A, B = np.linalg.solve(M, [a0, a1])
print("constants:", A, B)
#
seq = [a0, a1]
for n in range(2, 10):
    seq.append(c1 * seq[-1] + c2 * seq[-2])
formula = [A * roots[0] ** n + B * roots[1] ** n for n in range(10)]
print(seq)
print(np.round(formula).astype(int).tolist())
#
# Fibonacci: the same recipe gives the Binet formula
phi, psi = (1 + 5 ** 0.5) / 2, (1 - 5 ** 0.5) / 2
binet = [round((phi ** n - psi ** n) / 5 ** 0.5) for n in range(15)]
print(binet)
print("ratio F15/F14:", 610 / 377, "phi:", phi)
