"""Iterate a recurrence: a credit card balance, month by month."""
balance = 3000.0          # B0, the starting balance, is part of the rule
rate = 0.02               # 2% interest a month, about 24% a year
payment = 70.0
history = [balance]
for month in range(24):
    balance = balance * (1 + rate) - payment   # the whole recurrence
    history.append(balance)
#
print(f"after 24 months: {history[-1]:,.2f}")
#
# same rule, three different starts, paying 60 a month
for start in (2900, 3000, 3100):
    b = start
    for month in range(60):
        b = b * 1.02 - 60
    print(f"start {start}: after 5 years {b:,.0f}")
