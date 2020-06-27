budget = float(input())
city = input()
nights = int(input())
night_price = 0
two_way_ticket = 0
discount = 0
if city == 'Cairo':
    night_price = (250 * 2) * nights
    two_way_ticket = 600
if city == 'Paris':
    night_price = (150 * 2) * nights
    two_way_ticket = 350
if city == 'Lima':
    night_price = (400 * 2) * nights
    two_way_ticket = 850
if city == 'New York':
    night_price = (300 * 2) * nights
    two_way_ticket = 650
if city == 'Tokyo':
    night_price = (350 * 2) * nights
    two_way_ticket = 700
total = night_price + two_way_ticket
if 1 <= nights <= 4:
    if city == 'Cairo' or city == 'New York':
        total -= total * 0.03
elif 5 <= nights <= 9:
    if city == 'Cairo' or city == 'New York':
        total -= total * 0.05
    elif city == 'Paris':
        total -= total * 0.07
elif 10 <= nights <= 24:
    if city == 'Cairo':
        total -= total * 0.1
    elif city == 'Paris' or city == 'New York' or city == 'Tokyo':
        total -= total * 0.12
elif 25 <= nights <= 49:
    if city == 'Tokyo' or city == 'Cairo':
        total -= total * 0.17
    elif city == 'New York' or city == 'Lima':
        total -= total * 0.19
    elif city == 'Paris':
        total -= total * 0.22
elif nights >= 50:
    total -= total * 0.3
diff = abs(budget - total)
if total < budget:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')