t_shirt_price = float(input())
needed = float(input())
shirt_price = t_shirt_price * 0.75
socks_price = shirt_price * 0.20
sneakers_price = (t_shirt_price + shirt_price) * 2
total = t_shirt_price + shirt_price + socks_price + sneakers_price
total -= total * 0.15
if total >= needed:
    print('Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {total:.2f} lv.')
else:
    diff = abs(total - needed)
    print('No, he will not earn the world-cup replica ball.')
    print(f'He needs {diff:.2f} lv. more.')
