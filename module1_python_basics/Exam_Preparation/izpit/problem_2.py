# Любо очаква гости за Великден.

# Известно е, че един козунак стига за трима човека,
# като всеки гост ще получи и по 2 яйца.

# Вашата задача е да намерите колко козунака и яйца трябва да купи Любо, както и каква ще е сумата,
# която той трябва да плати и дали бюджета му е достатъчен. При изчисляването на броя козунаци,
# които Любо трябва да закупи, техният брой трябва да се закръгли към по-голямото цяло число.

# Ако парите не му стигат, трябва да се изведе съобщение, колко не му достигат.
# Известно е, че:
# •	Един козунак струва 4лв.
# •	Едно яйце струва 0.45лв.

# Изход
# На конзолата да се отпечатат два реда:
# •	Ако бюджетът е достатъчен:
# o	"Lyubo bought {брои закупени козунаци} Easter bread and {брои закупени яйца} eggs."
# o	"He has {останали пари} lv. left."
# •	Ако  бюджетът НЕ Е достатъчен:
# o	"Lyubo doesn't have enough money."
# o	"He needs {недостигащи пари} lv. more."
# Парите да бъдат форматирани до втората цифра след десетичния знак.

import math
broi_gosti = int(input())
budget = int(input())
cena_1_kozunak = 4
cena_1_qice = 0.45

broi_kozunaci_za_n_choveka = math.ceil(broi_gosti / 3)
broi_qica_za_n_choveka = broi_gosti * 2

suma_kozunaci = cena_1_kozunak * broi_kozunaci_za_n_choveka
suma_qica = cena_1_qice * broi_qica_za_n_choveka

obshto = suma_qica + suma_kozunaci

diff = abs(obshto - budget)
if obshto <= budget:
    print(f'Lyubo bought {math.ceil(broi_kozunaci_za_n_choveka)} Easter bread and {broi_qica_za_n_choveka} eggs.')
    print(f'He has {diff:.2f} lv. left.')
else:
    print("Lyubo doesn't have enough money.")
    print(f'He needs {diff:.2f} lv. more.')
