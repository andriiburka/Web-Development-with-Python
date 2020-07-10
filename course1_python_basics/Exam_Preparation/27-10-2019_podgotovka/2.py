# Задача 2. Коледен базар
# Коледа наближава и Коледният базар на книгата отваря врати.
# Организаторите искат да дарят определена сума от продажба на следните жанрове книги: фентъзи, хорър, романтика.
# Да се напише програма, която изчислява дали организаторите са успели са съберат желаната сума от продажба на книги,
# като се има предвид, че с 20 процента от изкараната сума, се заплаща ДДС. Книгите от всеки жанр имат различна цена:
# •	Фентъзи – 14.90 лв.
# •	Хорър – 9.80 лв.
# •	Романтика – 4.30 лв.
# Ако след заплащане на ДДС, целта е достигната, продавачите ще получат 10% възнаграждение от парите надвишаващи целта.
# Сумата за възнаграждение трябва да е закръглена към най-близкото цяло число надолу.
# Останалите пари, се добавят към основната сума за даряване.


needed_money = float(input())
num_fantasy = int(input())
num_horror = int(input())
num_romantic = int(input())
price_fantasy
price_horror
price_


# Обяснения
# Сумата от продажбата => 15 * 14.90 + 10 * 9.80 + 5 * 4.30 = 343лв
# 20% ДДС от 343 = 68.60 лв.
# Сума след заплащане на ДДС -> 274.40 лв.
# Понеже 274.40 > 200, служителите получават 10% от сумата над целта 274.40 – 200 = 74.40 лв.
# 10% от 74.10 = 7 лв. за продавачите.
# 74.40 – 7 = 67.40 лв. които добавяме към сумата за даряване. 200 + 67.40 = 267.40лв. - крайната сума, която ще бъде дарена.

# Изход
# Отпечатването на конзолата зависи от резултата:
# •	Ако е събрана сумата от Коледният базар :
# o	" {дарена сума} leva donated."
# o	"Sellers will receive {възнаграждение} leva."
# •	Ако НЕ е достигната сумата:
# o	"{парите нужни до достигане на целта} money needed."
# Дарената/Недостигаща сума трябва да се форматира до втория знак след десетичната запетая.