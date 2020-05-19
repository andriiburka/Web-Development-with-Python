months = int(input())
electricity_tax = 0
electricity = 0
water = 0
internet = 0
other = 0
average = 0
for month in range(1, months + 1):
    electricity_tax = float(input())
    electricity += electricity_tax
    water += 20
    internet += 15
    percent20 = (electricity + water + internet) * 0.2
    other = electricity + water + internet + percent20
average = (electricity + water + internet + other) / months
print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {average:.2f} lv')

