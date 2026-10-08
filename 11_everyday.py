"""Everyday recurrences: a doubling penny, a daily pill, the R number and
the Tower of Hanoi. Each one is next = multiplier * now + something."""
#
# 1. a penny that doubles every day for 30 days
penny = 0.01
for day in range(2, 31):
    penny = penny * 2                     # tomorrow is twice today
    if day in (15, 21, 27, 28, 30):
        print(f"day {day:2d}: ${penny:,.2f}")
#
# 2. 100 mg every morning, half cleared by the next morning
level = 0.0
for dose in range(1, 9):
    level = 0.5 * level + 100             # what's left, plus a new dose
    print(f"dose {dose}: peak {level:6.1f} mg")
#
# 3. 1,000 cases, 12 rounds of passing it on
for R in (1.3, 0.8):
    cases = 1000.0
    for _ in range(12):
        cases = R * cases
    print(f"R = {R}: {cases:,.0f} cases after 12 rounds")
#
# 4. Tower of Hanoi: moves(n) = 2 * moves(n - 1) + 1
moves = 0
for n in range(1, 65):
    moves = 2 * moves + 1
    if n in (3, 10, 20, 32, 64):
        years = moves / (365.25 * 24 * 3600)
        print(f"{n:2d} discs: {moves:,} moves, {years:,.1f} years")
