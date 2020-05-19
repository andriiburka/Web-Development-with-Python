# Задача 6. Великденска украса
# Каква сметка трябва да плати всеки един клиент на магазина ?
# като се има в предвид,
# че всеки клиент закупил четен брой продукти, ще получи 20% отстъпка от крайната цена.
# След като всички клиенти приключат с покупките,
# трябва да се отпечата средно по колко пари е похарчил всеки човек.

# Вход
# От конзолата първоначално се чете един ред:
# •	Брои на клиентите в магазина – цяло число [1… 100]
# •	След това за всеки един клиент на нов ред до получаване на командата "Finish" се чете:
# o	Покупката която клиента е избрал – текст ("basket", "wreath" или "chocolate bunny")

# Изход
# •	При получаване на командата "Finish" да се отпечата един ред:
# -	"You purchased {броя на покупките} items for {крайната цена} leva."

# •	Накрая, след като всички клиенти приключат с покупките, да се отпечата на един ред
# -	"Average bill per client is: {средно аритметично на парите които е похарчил всеки един клиент} leva."
# ПАРИ:.2f

broi_klienti_v_magazina = int(input())
command = input()
basket = 1.50
wreath = 3.80
chocolate_bunny = 7
total_sum = 0

for klient in range(1, broi_klienti_v_magazina + 1):

    purchased_sum = 0
    purchases_count = 0

    while command != 'Finish':
        if command == 'basket':
            purchased_sum += basket
            purchases_count += 1
        elif command == 'wreath':
            purchased_sum += wreath
            purchases_count += 1
        elif command == 'chocolate bunny':
            purchased_sum += chocolate_bunny
            purchases_count += 1
        command = input()


    if command == 'Finish':
        if purchases_count % 2 > 0:
            print(f'You purchased {purchases_count} items for {purchased_sum:.2f} leva.')
            total_sum += purchased_sum
        elif purchases_count % 2 == 0:
            purchased_sum -= purchased_sum * 0.2
            print(f'You purchased {purchases_count} items for {purchased_sum:.2f} leva.')
            total_sum += purchased_sum
            continue

    command = input()


average = total_sum / broi_klienti_v_magazina
print(f'Average bill per client is: {average:.2f} leva.')