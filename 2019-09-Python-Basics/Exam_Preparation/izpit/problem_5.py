# Задача 5. Великденски козунаци
# Предстои Великден и Деси е решила да изпече домашни козунаци за колегите си.
# Главните продукти, които ще трябват на Деси са: брашно и захар.

# >>> Един пакет захар е 950 грама, а един пакет брашно е 750 грама. <<<

# Напишете програма,
# която изчислява колко пакета захар и брашно трябва да купи Деси,
# за да й стигнат за направата на козунаците,
# като знаете за всеки един козунак по колко грама захар и брашно са изразходени.
# Също намерете кое е най-голямото количество захар и брашно, които са използвани.

# Вход
# От конзолата се чете 1 ред:
# •	 Броят на козунаците – цяло число в интервала [1 ... 100]
# За всеки козунак се чете:
# o	Количество изразходвана захар (грамове) – цяло число в интервала [1 … 10000]
# o	Количество изразходвано брашно (грамове) – цяло число в интервала [1 … 10000]

# Изход
# Да се отпечатат на конзолата 3 реда:
# •	"Sugar: {брой нужни пакети захар}"
# •	"Flour: {брой нужни пакет брашно}"
# •	"Max used flour is {max_gr_flour} grams, max used sugar is {max_gr_sugar} grams."

# Пакетите захар и брашно да бъдат закръглени към най-близкото цяло число нагоре.
import math

broi_kozunaci = int(input())
paket_zahar = 950
paket_brashno = 750

obshto_kolichestvo_zahar = 0
obshto_kolichestvo_brashno = 0

broi_paketi_zahar = 0
broi_paketi_brahsno = 0

max_used_sugar = 0
max_used_flour = 0

for kozunak in range(broi_kozunaci):
    gramove_zahar = int(input())
    gramove_brashno = int(input())
    if gramove_zahar > max_used_sugar:
        max_used_sugar = gramove_zahar
    if gramove_brashno > max_used_flour:
        max_used_flour = gramove_brashno

    obshto_kolichestvo_zahar += gramove_zahar
    broi_paketi_zahar = obshto_kolichestvo_zahar / paket_zahar

    obshto_kolichestvo_brashno += gramove_brashno
    broi_paketi_brahsno = obshto_kolichestvo_brashno / paket_brashno


print(f'Sugar: {math.ceil(broi_paketi_zahar)}')
print(f'Flour: {math.ceil(broi_paketi_brahsno)}')
print(f'Max used flour is {math.ceil(max_used_flour)} grams, max used sugar is \
{math.ceil(max_used_sugar)} grams.')

