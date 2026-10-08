"""Euler steps turn y' = -y into the recurrence y_{n+1} = (1 - h) y_n."""
import math
#
for h in (0.5, 1.5, 2.5):
    y, t, path = 1.0, 0.0, []
    while t < 10:
        path.append(round(y, 3))
        y = (1 - h) * y                   # one Euler step
        t += h
    print(f"h = {h}: multiplier {1 - h:+.1f} ->", path[:6])
print("true y(10):", math.exp(-10))
