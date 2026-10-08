"""AR models are recurrences with noise added each step."""
import numpy as np
#
rng = np.random.default_rng(7)
shocks = rng.normal(0, 1, 120)            # one set of random shocks
for phi in (0.5, 0.9, 1.0, 1.03):
    x = [0.0]
    for t in range(1, 120):
        x.append(phi * x[-1] + shocks[t])
    print(f"phi {phi}: final {x[-1]:8.2f}  spread {np.std(x):6.2f}")
#
def ar2_stationary(phi1, phi2):
    lam = np.roots([1, -phi1, -phi2])     # characteristic form
    z = np.roots([-phi2, -phi1, 1])       # lag polynomial form
    inside = bool(np.all(np.abs(lam) < 1))
    outside = bool(np.all(np.abs(z) > 1))
    return inside, outside, lam.round(3), z.round(3)
#
print(ar2_stationary(0.5, 0.3))           # both tests agree: stationary
print(ar2_stationary(1.5, 0.3))           # both tests agree: not
