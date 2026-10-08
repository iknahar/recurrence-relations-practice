"""Let SymPy solve recurrences symbolically."""
from sympy import Function, Rational, rsolve, simplify, symbols
#
n = symbols("n", integer=True)
a = Function("a")
#
rate = Rational(102, 100)                 # exact 1.02, no float rounding
first = rsolve(a(n + 1) - rate * a(n) + 70, a(n), {a(0): 3000})
print("balance:", simplify(first))
#
fib = rsolve(a(n + 2) - a(n + 1) - a(n), a(n), {a(0): 0, a(1): 1})
print("fibonacci:", fib)
print("check n = 10:", simplify(fib.subs(n, 10)))
#
second = rsolve(a(n) - 5 * a(n - 1) + 6 * a(n - 2), a(n),
                {a(0): 2, a(1): 5})
print("5, -6 recurrence:", second)
