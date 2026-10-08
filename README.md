# Recurrence Relations Practice

Practice code for learning recurrence relations with Python, from a simple loop to closed forms, the characteristic equation, stability, AR models, life tables, insurance reserves and dynamic programming.

Every script runs on its own and prints its results. Read the code, run it, then change one number and predict what will happen before you run it again.

## Setup

```bash
pip install -r requirements.txt
```

## Scripts

| file | what it shows |
|---|---|
| `01_iterate.py` | A credit card balance, month by month, and three different starting balances |
| `02_closed_form.py` | The closed form of a first order recurrence, checked against the loop, plus months to pay off |
| `03_characteristic.py` | Second order recurrences with `np.roots`, and Fibonacci through the Binet formula |
| `04_stability.py` | A recurrence that floating point gets badly wrong, the exact fix, and a root based stability check |
| `05_ar_models.py` | AR(1) paths for four values of phi, and the AR(2) stationarity test in both conventions |
| `06_life_table.py` | Survivors forward and life expectancy backward from an illustrative mortality model |
| `07_reserve.py` | An endowment insurance reserve built one policy year at a time |
| `08_dynamic_programming.py` | Naive versus memoised Fibonacci, and the stairs problem |
| `09_sympy_solve.py` | Solving recurrences symbolically with SymPy `rsolve` |
| `10_euler.py` | Euler steps for y' = -y as a recurrence, and when they blow up |

The mortality numbers in `06` and `07` come from a Gompertz-Makeham formula with made-up parameters. They behave like a real life table but are not any country's actual data.

## Exercises

**1.** In `02_closed_form.py`, what monthly payment clears a $3,000 balance at 2% a month in exactly 36 months?

<details><summary>Answer</summary>

Set B(36) = 0 in the closed form and solve for P. P = r × B0 × 1.02³⁶ / (1.02³⁶ − 1), which is about $117.70. Check it with `loop_balance(3000, 0.02, 117.70, 36)`.

</details>

**2.** Solve a(n) = 6a(n−1) − 9a(n−2) with a(0) = 1, a(1) = 6. Careful, the characteristic equation has a repeated root.

<details><summary>Answer</summary>

λ² − 6λ + 9 = 0 gives λ = 3 twice, so a(n) = (A + Bn) × 3ⁿ. a(0) = 1 gives A = 1, and a(1) = 6 gives 3(1 + B) = 6, so B = 1. The answer is a(n) = (1 + n) × 3ⁿ. Confirm with `rsolve` from `09_sympy_solve.py`.

</details>

**3.** Is the AR(2) model with φ₁ = 1.2 and φ₂ = −0.5 stationary? Do the roots come out real or complex?

<details><summary>Answer</summary>

`ar2_stationary(1.2, -0.5)` returns True for both tests. The characteristic roots are 0.6 ± 0.374i, a complex pair of size about 0.707, so the series is stationary and its swings oscillate like a damped wave.

</details>

**4.** In `04_stability.py`, change the starting values to x(0) = 1 and x(1) = 3. Does the float version still go wrong? Why or why not?

<details><summary>Answer</summary>

No. The exact answer is now 3ⁿ, which is the dominant solution. Rounding errors still creep in, but they are small relative to a value that is itself growing by 3 every step. Instability only hurts when you are trying to follow the small solution.

</details>

**5.** Change the interest rate in `07_reserve.py` from 4% to 6%. Does the premium go up or down, and why?

<details><summary>Answer</summary>

It goes down. Each premium earns more interest before the payout is due, so less money needs to be paid in to reach $100,000 by the end.

</details>

**6.** In `10_euler.py`, find the step size h where the Euler steps neither grow nor shrink in size.

<details><summary>Answer</summary>

h = 2. The multiplier is 1 − h = −1, so the values flip between 1 and −1 forever. Any h above 2 grows, and any h between 0 and 2 shrinks.

</details>

## License

MIT
