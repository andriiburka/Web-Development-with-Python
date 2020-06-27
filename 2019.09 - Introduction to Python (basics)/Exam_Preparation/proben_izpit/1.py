# Задача 1. Пътуване до море
# Група туристи решили да си направят лятна екскурзия до морето. Те тръгват от село Чушкопек.
# Да се напише програма, която пресмята общата сума в левове, която е необходима на туристите за тази екскурзия.
#
# Разстоянието до морето е 210 километра, а цялата екскурзия е с продължителност 3 дни.
# Тяхната кола изразходва средно по 7 литра на всеки 100 километра, а цената на бензина е 1,85 лв. за един литър.
# За всеки ден от техния престой те харчат пари за храна и сувенири.
# Общата цена за хотел е Z лв. на ден.
# Като група, първия ден те получават 10% намаление за престоя, втория ден - 15% намаление, а третия ден - 20%.


# Изход
# На конзолата се отпечатва 1 ред:
# "Money needed: {total money}"
# където {total money} e сумата на общия разход на групата, форматирана до втория знак след десетичната запетая.

# 100
# 50
# 500

pari_hrana_1den = float(input())
pari_suveniri_1den = float(input())
pari_hotel_1den = float(input())
days = 3

rastoqnie_do_moreto = 210 * 2
dni_ekskurziq = 3

nujno_kolichestvo_benzin = rastoqnie_do_moreto / 100 * 7
cena_benzin = nujno_kolichestvo_benzin * 1.85

harch = (dni_ekskurziq * pari_hrana_1den) + (dni_ekskurziq * pari_suveniri_1den)

den_1 = pari_hotel_1den - pari_hotel_1den * 0.10
den_2 = pari_hotel_1den - pari_hotel_1den * 0.15
den_3 = pari_hotel_1den - pari_hotel_1den * 0.20

obshto = cena_benzin + harch + den_1 + den_2 + den_3


print(f'Money needed: {obshto:.2f}')