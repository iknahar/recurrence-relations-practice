"""First order linear recurrence: closed form, checked against the loop."""
import math
#
def loop_balance(b0, r, pay, n):
    b = b0
    for _ in range(n):
        b = b * (1 + r) - pay
    return b
#
def closed_balance(b0, r, pay, n):
    fixed = pay / r                      # the balance that never moves
    return (1 + r) ** n * (b0 - fixed) + fixed
#
for n in (1, 12, 60, 98):
    a = loop_balance(3000, 0.02, 70, n)
    b = closed_balance(3000, 0.02, 70, n)
    print(f"month {n:3d}  loop {a:10.4f}  formula {b:10.4f}")
#
def months_to_zero(b0, r, pay):
    if pay <= r * b0:                    # interest eats the whole payment
        return math.inf
    return -math.log(1 - r * b0 / pay) / math.log(1 + r)
#
for pay in (150, 100, 70, 65, 61, 60):
    print(f"pay {pay:3d}: {months_to_zero(3000, 0.02, pay):6.1f} months")
#
# short versions for one card: $3,000 owed, 2% a month, $70 paid
def by_loop(n):
    b = 3000.0
    for _ in range(n):
        b = b * 1.02 - 70
    return b
#
def by_formula(n):
    return 3500 - 500 * 1.02 ** n
#
print(by_loop(98), by_formula(98))   # both about 18.34
