# 2. Космически кораб
# Георги трябва да построи космически кораб, който да събира част от екипажа му.
# За целта, той трябва да го направи така, че да има място за поне трима астронавти, но за не повече от 10.
#
# Всеки астронавт се нуждае от малка стая, която да е с размери: 2 метра ширина,
# 2 метра дължина и с 40 см по-висока от средната височина на астронавтите.
#
# Напишете програма, която изчислява обема на кораба,
# колко астронавта ще събере и принтира на конзолата дали  той е достатъчно голям.

import math

shirochina_korab = float(input())
daljina_korab = float(input())
visochina_korab = float(input())
sredna_visochina_astronavtite = float(input())

obem_raketa = shirochina_korab * daljina_korab * visochina_korab

obem_staq = (sredna_visochina_astronavtite + 0.40) * 2 * 2
obshto_mqsto = obem_raketa / obem_staq


if 3 <= obshto_mqsto <= 10:
    print(f'The spacecraft holds {math.floor(obshto_mqsto)} astronauts.')
elif obshto_mqsto < 3:
    print('The spacecraft is too small.')
elif obshto_mqsto > 10:
    print('The spacecraft is too big.')

# Изход
# Да се отпечата на конзолата един ред:
# •	Ако броят на астронавтите е между 3 и 10:
# "The spacecraft holds {броя на астронавтите} astronauts."
# •	Ако  броят на астронавтите е по-малък от 3:
#  "The spacecraft is too small."
# •	Ако  броят на астронавтите е по-голям от 10:
# "The spacecraft is too big."