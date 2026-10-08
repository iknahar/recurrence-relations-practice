"""Recurrences in dynamic programming: same rule, smarter evaluation."""
from functools import lru_cache
#
calls = 0
def fib_naive(n):
    global calls
    calls += 1
    return n if n < 2 else fib_naive(n - 1) + fib_naive(n - 2)
#
fib_naive(25)
print("naive calls for fib(25):", calls)
#
@lru_cache(maxsize=None)
def fib_memo(n):
    return n if n < 2 else fib_memo(n - 1) + fib_memo(n - 2)
print("fib(90) with a memo:", fib_memo(90))
#
def stairs(n):
    """Ways to climb n stairs taking 1 or 2 at a time."""
    w = [1, 1] + [0] * (n - 1)
    for k in range(2, n + 1):
        w[k] = w[k - 1] + w[k - 2]
    return w[n]
print("ways up 10 stairs:", stairs(10))
