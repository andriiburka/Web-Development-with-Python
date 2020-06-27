
import math
kind_sushi = input()
restaurant_name = input()
broi_porcii = int(input())
porychka_simvol = input()

total_price = 0

if restaurant_name in ("Sushi Zone", "Sushi Time", "Sushi Bar", "Asian Pub"):
    if restaurant_name == 'Sushi Zone':
        if kind_sushi == 'sashimi':
            price = 4.99
        elif kind_sushi == 'maki':
            price = 5.29
        elif kind_sushi == 'uramaki':
            price = 5.99
        elif kind_sushi == 'temaki':
            price = 4.29

    elif restaurant_name == 'Sushi Time':
        if kind_sushi == 'sashimi':
            price = 5.49
        elif kind_sushi == 'maki':
            price = 4.69
        elif kind_sushi == 'uramaki':
            price = 4.49
        elif kind_sushi == 'temaki':
            price = 5.19

    elif restaurant_name == 'Sushi Bar':
        if kind_sushi == 'sashimi':
            price = 5.25
        elif kind_sushi == 'maki':
            price = 5.55
        elif kind_sushi == 'uramaki':
            price = 6.25
        elif kind_sushi == 'temaki':
            price = 4.75

    elif restaurant_name == 'Asian Pub':
        if kind_sushi == 'sashimi':
            price = 4.50
        elif kind_sushi == 'maki':
            price = 4.80
        elif kind_sushi == 'uramaki':
            price = 5.50
        elif kind_sushi == 'temaki':
            price = 5.50

    total_price += price * broi_porcii
    if porychka_simvol == "Y":
        total_price += total_price * 0.20
else:
    print(f'{restaurant_name} is invalid restaurant!')
    exit()

print(f'Total price: {math.ceil(total_price)} lv.')