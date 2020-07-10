# Задача 3. Боядисване на яйца
# С наближаването на Великденските празници, цех за боядисване на яйца,
# започва да боядисва различни размери яйца, които след това продава на партиди.
#
# В таблицата са показани размерите на яйцата, различните бои
# и каква е цената за продажба на една партида яйца, зависеща от размерите и цвета боя.
#           Red	    Green   Yellow
# Large     16 лв.	12 лв.	9 лв.
# Medium	13 лв.	9 лв.	7 лв.
# Small     9 лв.	8 лв.	5 лв.
#
# Напишете програма, която изчислява какви ще са приходите на цеха от продажбите,
# като знаете размера на яйцата и техният цвят.
#
# С 35% от крайната цена ще бъдат покрити производствени разходи.

egg_size = input()
egg_color = input()
broi_partidi = int(input())

partida_price = 0
if egg_size == 'Large':
    if egg_color == 'Red':
        partida_price += 16
    if egg_color == 'Green':
        partida_price += 12
    if egg_color == 'Yellow':
        partida_price += 9
if egg_size == 'Medium':
    if egg_color == 'Red':
        partida_price += 13
    if egg_color == 'Green':
        partida_price += 9
    if egg_color == 'Yellow':
        partida_price += 7
if egg_size == 'Small':
    if egg_color == 'Red':
        partida_price += 9
    if egg_color == 'Green':
        partida_price += 8
    if egg_color == 'Yellow':
        partida_price += 5

price = partida_price * broi_partidi
price -= price * 0.35
print(f'{price:.2f} leva.')    # 72.80
    # Изход
# На конзолата трябва да се отпечата един ред:
# "{крайната цена} leva."
# Резултатът да се форматира до втората цифра след десетичния знак.
