days = input()
money_for_next_day = 0

while days != 'Day over':
    days = int(days)
    expenses = 0

    for day in range(1, days + 1):
        while expenses < 60:
            product_price = float(input())
            expenses += product_price

        if expenses >=60:
            continue
        e


if days == 'Day over':
    print('Exit')