
# Напишете програма, която :
# 1. пресмята колко гости ще събере ресторанта,
# 2. какви ще са приходите му от ергенското парти,
# 3. дали Марто ще може да си позволи да плати на гост изпълнител,
#
# като знаете че:
# •	Ако резервацията е за група с по-малко от 5 човека, куверта за един човек ще е 100 лв.
# •	Ако резервацията е за група с 5 или повече човека, куверта за един човек ще е 70 лв.

# Вход
# От конзолата се чете:
# •	Сумата предвидена за гост изпълнителя - цяло число в интервала [1… 4500]
# •	На всеки следващ ред (до получаване на команда "The restaurant is full") - броят на хората във всяка група.
# Изход
# Да се отпечата на конзолата един от следните редове:
# •	Ако Марто успее да си позволи гост изпълнител:
# "You have {брой гости} guests and {останалата сума} leva left."
# •	Ако Марто не успее да си позволи гост изпълнител:
# "You have {брой гости} guests and {приходи} leva income, but no singer."

suma_za_gost_izpalnitel = int(input())
broi_hora = input()
gosti = 0
obshto = 0

while broi_hora != 'The restaurant is full':
    broi_hora = int(broi_hora)
    gosti += broi_hora

    if broi_hora < 5:
        cena_za_grupa = 100 * broi_hora

    elif broi_hora >= 5:
        cena_za_grupa = 70 * broi_hora

    obshto += cena_za_grupa
    broi_hora = input()

if broi_hora == 'The restaurant is full':
    if obshto >= suma_za_gost_izpalnitel:
        total = abs(suma_za_gost_izpalnitel - obshto)
        print(f'You have {gosti} guests and {total} leva left.')
    else:
        print(f'You have {gosti} guests and {obshto} leva income, but no singer.')


