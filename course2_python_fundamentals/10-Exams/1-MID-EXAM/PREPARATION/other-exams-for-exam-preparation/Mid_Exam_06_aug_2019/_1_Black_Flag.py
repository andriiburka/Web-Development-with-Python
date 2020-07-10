''' РЕШЕНА НА 200/100
- - - - - - - - - - - - - - - - - - - - - - - - УСЛОВИЕ - - - - - - - - - - - - - - - - - - - - - - - -
Black Flag
Create a program that checks IF A TARGET PLUNDER IS REACHED.
-First you will receive how many days the pirating lasts.
-Then you will receive how much the pirates plunder for a day.
-Last you will receive the expected plunder at the end.

Calculate how much plunder the pirates manage to gather. Each day they gather plunder.

Keep in mind that :
-every third day they attack more ships and they add additional plunder to their total gain which is 50% of the daily plunder.
-Every fifth day the pirates encounter a warship and after the battle they lose 30% of their total plunder.

If the gained plunder is more or equal to the target print the following:
"Ahoy! {totalPlunder} plunder gained."

If the gained plunder is less than the target. Calculate the percentage left and print the following:
"Collected only {percentage}% of the plunder."

Both numbers should be formatted to the 2nd decimal place.
Input
•	On the 1st line you will receive the days of the plunder – an integer number in the range [0…100000]
•	On the 2nd line you will receive the daily plunder – an integer number in the range [0…50]
•	On the 3rd line you will receive the expected plunder – a real number in the range [0.0…10000.0]
Output
•	 In the end print whether the plunder was successful or not following the format described above.

- - - - - - - - - - - - - - - - - - - - - - - - ПЛАН - - - - - - - - - - - - - - - - - - - - - - - -
1. Пишем вход:
    (a) Дни пиратстване.
    (b) Дневна печалба.
    (c) Колко планират спечелят за целия период.
2. Създаваме променлива в която ще добавяме и премахваме печалбата на пиратите
    (d) Обща печалба = 0
3. Изпечатай дните от 1 до (а)
    - Ден 1: добавяме (b) към общата печалба, Ден 2 - добавяме (b) към общата печалба... и т.н.
    - Ако денят е трети или един от всеки трети ден ==>     if for_loop_day % 3 == 0
            - към общата печалба добави 50% от (b).
    - Ако денят е пети или един от всеки пети ден ==>       if for_loop_day % 5 == 0
        - от общата печалба премахни 30%.
4. IF-ELSE проверка за това дали целта е постигната.
    - Ако да то изпринтирай еди си какво с 2 нули в края.
    - Ако НЕ то изчисли колко процента е разликата (виж ПОДСКАЗКА 2)
        - като получим процентите. Махаме ги от 100 и получаваме краен резултат в проценти


- - - - - - - - - - - - - - - - - - - - - - - - ПОДСКАЗКИ - - - - - - - - - - - - - - - - - - - - - - - -
#1 - 30% ot 110
money = 110
percents_to_remove = 30
sum_minus_percents = money * (percents_to_remove/100)
print(f'The sum of 110 lv - 30% = {sum_minus_percents:.0f} lv.')

#2 - 20 ot 200 = ? %
result = 20
target = 200
percentage = (result / target) * 100
print(f'The {result} is {percentage:.0f}% of {target}') # 10%

'''
#1
days = int(input())
daily_plunder = int(input())
target_sum = float(input())
#2
total_sum_of_plunders = 0
#3
for current_day in range(1, days + 1):
    total_sum_of_plunders += daily_plunder
    if current_day % 3 == 0:
        total_sum_of_plunders += (daily_plunder / 2)
    if current_day % 5 == 0:
        total_sum_of_plunders -= (total_sum_of_plunders * (30 / 100))
#4
if total_sum_of_plunders >= target_sum:
    print(f'Ahoy! {total_sum_of_plunders:.2f} plunder gained.')
else:
    percentage = abs(((target_sum - total_sum_of_plunders)/target_sum * 100)-100)
    print(f'Collected only {percentage:.2f}% of the plunder.')