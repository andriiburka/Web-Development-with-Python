# # 02.
# username = input()
# password = input()
#
# data_input = input()
# while data_input != password:
#     data_input = input()
#
# print(f'Welcome {username}!')


# 03
# =====================================================================================================================
# number = int(input())
# counter = 1
#
# while counter <= number:
#     print(counter)
#     counter *= 2
#     counter += 1


# 4.	Баланс по сметка
# =====================================================================================================================
# Напишете програма, която пресмята колко общо пари има в сметката, след като направите определен брой вноски.
# На първия ред ще получите колко вноски трябва да се направят.
# На всеки следващ ред ще получавате сумата, която трябва да внесете в сметката, докато не се достигне броят вноски.
# При всяка получена сума на конзолата трябва да се извежда съобщението
# "Increase: " + сумата и тя да се прибавя в сметката.
# Ако получите число по-малко от 0 на конзолата трябва да се изведе "Invalid operation!" и програмата да приключи.
# Когато програмата приключи, трябва да се принтира "Total: " + общата сума в сметката,
# закръглена до втория знак след десетичната запетая.

# payment_count = int(input())
# payment = 0
# counter = 1
# total = 0
#
# while counter <= payment_count:
#     payment = float(input())
#     if payment >= 0:
#         print(f'Increase: {payment:.2f}')
#     else:
#         print('Invalid operation!')
#         break
#     counter += 1
#     total = total + payment
#
# print(f'Total: {total:.2f}')


# 05. Max Number
# =====================================================================================================================
# 05. Най-голямо число
# Напишете програма, която чете n на брой цели числа (n > 0),
# въведени от потребителя, и намира най-голямото измежду тях.
# Първо се въвежда броят числа n, а след това самите n числа по едно на ред.

# import sys
# numbers_count = int(input())
# number_input = 0
# counter = 0
# biggest_number = -sys.maxsize
#
#
# while counter < numbers_count:
#     number_input = int(input())
#     while number_input > biggest_number:
#         biggest_number = number_input
#
#     counter += 1
# print(f'{biggest_number}')


# 06. Min Number
# =====================================================================================================================
# 6.	Най-малко число
# Напишете програма, която чете n на брой цели числа (n > 0), въведени от потребителя, и намира най-малкото измежду тях.
# Първо се въвежда броят числа n, а след това самите n числа по едно на ред.

# import sys
# numbers_count = int(input())
# number_input = 0
# counter = 0
# biggest_number = sys.maxsize
#
#
# while counter < numbers_count:
#     number_input = int(input())
#     while number_input < biggest_number:
#         biggest_number = number_input
#
#     counter += 1
# print(f'{biggest_number}')


# 07. Graduation
# =====================================================================================================================
# 7. Завършване
# Напишете програма, която изчислява средната оценка на ученик от цялото му обучение.

# Вход
# На първия ред е името на ученика
# на всеки следващ ред - неговите годишни оценки.

# Ученикът преминава в следващия клас, ако годишната му оценка е по-голяма или равна на 4.00.
# Ако оценката му е под 4.00, той ще повтори класа.

# При успешно завършване на 12-ти клас да се отпечата:
#  print(f'{student_name} graduated. Average grade: {average_grade:.2f}')

# student_name = input()
# class_grade = 0
# max_classes = 12
# current_class = 1
# total_classes_grade = 0
#
# while current_class <= max_classes:
#     class_grade = float(input())
#     if 4.00 <= class_grade <= 6.00:
#         total_classes_grade += class_grade
#         current_class += 1
#     elif 2.00 <= class_grade < 4.00:
#         current_class += 0
#
# print(f'{student_name} graduated. Average grade: {(total_classes_grade / max_classes):.2f}')


# Ученикът преминава в следващия клас, ако годишната му оценка е по-голяма или равна на 4.00.
# Ако оценката му е под 4.00, той ще повтори класа.


# 8. Завършване - част 2
# Напишете програма, която изчислява средната оценка на ученик от цялото му обучение.
# На първия ред ще получите името на ученика, а на всеки следващ ред - неговите годишни оценки.
# Ученикът преминава в следващия клас, ако годишната му оценка е по-голяма или равна на 4.00.

# Ако ученикът бъде скъсан повече от един път, то той бива изключен и програмата приключва,
# като се отпечатва името на ученика и в кой клас е изключен.

#  При успешно завършване на 12-ти клас да се отпечата :
# "{име на ученика} graduated. Average grade: {средната оценка от цялото обучение}"

# В случай, че ученикът е изключен от училище, да се отпечата:
# "{име на ученика} has been excluded at {класа, в който е бил изключен} grade"
# Стойността трябва да бъде форматирана до втория знак след десетичната запетая.


# student_name = input()
# class_grade = 0
# max_classes = 12
# current_class = 1
# total_classes_grade = 0
# mistakes = 0
# mistakes_bool = False
#
# while current_class <= max_classes:
#
#     if mistakes == 2:
#         mistakes_bool = True
#         break
#     else:
#         if mistakes < 2:
#             class_grade = float(input())
#             if 4.00 <= class_grade <= 6.00:
#                 total_classes_grade += class_grade
#                 current_class += 1
#             elif 2.00 <= class_grade < 4.00:
#                 mistakes += 1
#
# if mistakes_bool:
#     print(f'{student_name} has been excluded at {current_class} grade')
# else:
#     print(f'{student_name} graduated. Average grade: {(total_classes_grade / max_classes):.2f}')


# 09. Преместване (Задачи от изпита)
# =====================================================================================================================
# На осемнадесетия си рожден ден Хосе взел решение, че ще се изнесе да живее на квартира.
# Опаковал багажа си в кашони и намерил подходяща обява за апартамент под наем.
# Той започва да пренася своя багаж на части, защото не може наведнъж.
# Има ограничено свободно пространство в новото си жилище, където може да разположи вещите,
# така че мястото да бъде подходящо за живеене.
# Напишете програма, която изчислява свободния обем от жилището на Хосе, който остава, след като пренесе багажа си.
# Всеки кашон е с точни размери:  1m x 1m x 1m.

# Вход
# Потребителят въвежда следните данни на отделни редове:
# 1.	Широчина на свободното пространство - цяло число;
# 2.	Дължина на свободното пространство - цяло число;
# 3.	Височина на свободното пространство - цяло число;
# 4.	На следващите редове (до получаване на команда "Done") - брой кашони, които се пренасят в квартирата - цели числа
# Програмата трябва да приключи прочитането на данни при команда "Done" или ако свободното място свърши.

# Изход
# Да се отпечата на конзолата един от следните редове:
# -	Ако стигнете до командата "Done" и има още свободно място:
# "{брой свободни куб. метри} Cubic meters left."
# -	Ако свободното място свърши преди да е дошла команда "Done":
# "No more free space! You need {брой недостигащи куб. метри} Cubic meters more."

# width_free_space = int(input())
# length_free_space = int(input())
# height_free_space = int(input())
# total_ap_volume = width_free_space * length_free_space * height_free_space
#
# box_volume = input()
# total_box_volume = 0
# difference = 0
# is_free = True
#
# while not box_volume == 'Done':
#     box_volume = int(box_volume)
#     total_box_volume += box_volume
#     if total_box_volume > total_ap_volume:
#         is_free = False
#         break
#     box_volume = input()
#
# if is_free:
#     difference = total_ap_volume - total_box_volume
#     print(f'{difference} Cubic meters left.')
# elif not is_free:
#     difference = total_box_volume - total_ap_volume
#     print(f'No more free space! You need {difference} Cubic meters more.')


# УПРАЖНЕНИЯ - while
# =====================================================================================================================
# =====================================================================================================================
# 01_even_lines. Old Books
# Ани отива до родния си град след много дълъг период извън страната.
# Прибирайки се вкъщи, тя вижда старата библиотека на баба си и си спомня за любимата си книга.
# Програма, в която тя въвежда търсената от нея книга (текст) и
# капацитета на библиотеката (цяло число).
# Докато Ани не намери любимата си книга или не провери всички в библиотеката,
# програмата трябва да чете всеки път на нов ред името на всяка следваща книга (текст).

# •	Ако не открие книгата, да се отпечата на два реда:
# o	"The book you search is not here!"
# o	"You checked {брой} books."
# •	Ако открие книгата си, да се отпечата на един ред:
# o	"You checked {брой} books and found it."


# target_book = input()
# lib_size = int(input())
#
# book_counter = 0
# founded = False
#
# while book_counter < lib_size:
#     current_book = input()
#
#     if target_book == current_book:
#         founded = True
#         print(f'You checked {book_counter} books and found it.')
#         break
#     book_counter += 1
#
# if not founded:
#     print('The book you search is not here!')
#     print(f'You checked {book_counter} books.')


# 02. Exam Preparation
# =====================================================================================================================
# 2.	Подготовка за изпит

# Example 1
# 3
# Money - 6
# Story - 4
# Spring Time - 5
# Bus - 6
# Enough
# Average score: 5.25
# Number of problems: 4
# Last problem: Bus

# Example 2
# 2
# Income - 3
# Game Info - 6
# Best Player - 4
# You need a break, 2 poor grades.

# max_fails = int(input())
# problem_name = input()
#
# # Almost undefined
# count_fails = 0
# problem_count = 0
# score = 0
# sum_score = 0
# failed = False
# last_problem = ''
#
# # WHILE START ===============================
# while problem_name != 'Enough':
#     score = int(input())
#     sum_score += score
#     problem_count += 1
#     if score <= 4:
#         count_fails += 1
#         if count_fails >= max_fails:
#             failed = True
#             break
#     # Debug prints
#     # print(f'Problem: {problem_count}')
#     # print(f'fails: {count_fails}')
#     # print(f'Problem_name: {problem_name}')
#     # print(f'Sum score: {sum_score}')
#     last_problem = problem_name
#     problem_name = input()
# # WHILE FINISH ==============================
#
# average_score = sum_score / problem_count
# if not failed:
#     print(f'Average score: {average_score}')
#     print(f'Number of problems: {problem_count}')
#     print(f'Last problem: {last_problem}')
# else:
#     print(f'You need a break, {count_fails} poor grades.')


# 03. Vacation 100/100
# =====================================================================================================================
# # 3. Почивка
# # Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере
# # дали ще успее да събере необходимата сума.
#
# Вход
# От конзолата се четат:
# •	Пари, нужни за екскурзията (needed_money) - реално число (float);
# •	Налични пари (owned_money) - реално число (float).
# needed_money = float(input())
# money_in_pocket = float(input())
# too_much_days_in_spending = False
# enough_money = False
# operation = ''
# days = 0
# count_days_in_spending = 0
# money_io = 0
#
# # След това многократно се четат по два реда:
# # •	Вид действие (command) – текст с две възможности: "spend" или "save";
# # •	Сумата, която ще спести/похарчи - реално число (float).
# while money_in_pocket < needed_money and count_days_in_spending < 5:
#     operation = input()
#     money_io = float(input())
#     days += 1
#
#     # Тя спестява или харчи част от парите си всеки ден.
#     if operation == 'save':
#         count_days_in_spending = 0
#         money_in_pocket += money_io
#     elif operation == 'spend':
#         count_days_in_spending += 1
#         money_in_pocket -= money_io
#
#         # Ако иска да похарчи повече от наличните си пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева.
#         if money_in_pocket < 0:
#             money_in_pocket = 0
#
#     if count_days_in_spending == 5:
#         too_much_days_in_spending = True
#         break
#
#     if money_in_pocket >= needed_money:
#         enough_money = True
#
# # Debug prints
# # print(f'\nBroi izminali dni: {days}')
# # print(f'Broi dni v harchene: {count_days_in_spending}')
# # print(f'Nalichni money_io: {money_in_pocket}')
#
# # Изход
# # Програмата трябва да приключи при следните случаи:
# # •	Ако 5 последователни дни Джеси САМО харчи, на конзолата да се изпише:
# # o	"You can't save the money."
# # o	"{Общ брой изминали дни}"
# # •	Ако Джеси събере парите за почивката, на конзолата се изписва:
# # o	"You saved the money for {общ брой изминали дни} days."
# if too_much_days_in_spending:
#     print("You can't save the money.")
#     print(days)
# if enough_money:
#     print(f"You saved the money for {days} days.")





# 04. Walking - НЕ Е РЕШЕНА ОТ МЕН, ТРЯБВА ДА СЕ ПОМЪЧА ДА Я РЕША
# =====================================================================================================================
# 04. Стъпки
# Габи иска да започне здравословен начин на живот и си е поставила за цел да върви 10 000 стъпки всеки ден.
# Някои дни обаче е много уморена от работа и ще иска да се прибере преди да постигне целта си.

# Примерен вход и изход
# 1000
# 1500
# 2000
# 6500
# Goal reached!
# Good job!

# 1500
# 3000
# 250
# 1548
# 2000
# Going home
# 2000
# Goal reached!
# Good job!

# 1500
# 300
# 2500
# 3000
# Going home
# 200
# 2500 more steps to reach goal.

# NE E RESHENO OT MEN !!!
# target_steps = 10000
# sum_steps = 0
#
# while sum_steps < 10000:
#     command = input()
#     if command == "Going home":
#         final_steps = int(input())
#         sum_steps += final_steps
#         break
#     else:
#         current_steps = int(command)
#         sum_steps += current_steps
#
#     if sum_steps >= target_steps:
#         break
#
# if sum_steps >= target_steps:
#     print("Goal reached! Good job!")
# else:
#     print(f"{target_steps - sum_steps} more steps to reach goal.")






# 05. Coins
# =====================================================================================================================
# 5.	Монети
# Производителите на кафе-автомати искали да направят машините си да връщат възможно най-малко монети ресто.
#
# Напишете програма, която
# ПРИЕМА СУМА - РЕСТО което трябва да се върне и
# изчислява с колко най-малко монети може да стане това.

# Примерен вход и изход
# Вход	    Изход	Обяснения
# 1.23	    4	    Рестото ни е 1 лев и 23 стотинки. Машината ни го връща с 4 монети:
#                   монета от 1 лев,
#                   монета от 20 стотинки,
#                   монета от 2 стотинки
#                   монета от 1 стотинка.

# 2	        1	    Рестото ни е 2 лева. Машината ни го връща с 1 монета от 2 лева.

# 0.56	    3	    Рестото ни е 56 стотинки. Машината ни го връща с 3 монети:
#                   монета от 50 стотинки,
#                   монета от 5 стотинки и
#                   монета от 1 стотинка.

# 2.73	    5	    Рестото ни е 2 лева и 73 стотинки. Машината ни го връща с 5 монети:
#                   монета от 2 лева,
#                   монета от 50 стотинки,
#                   монета от 20 стотинки,
#                   монета от 2 стотинки и
#                   монета от 1 стотинка.


# import math as m
# money = float(input()) * 100
# money = m.floor(money)
# coins = 0
#
# while money > 0:
#     if money / 200 >= 1:
#         money -= 200
#         coins += 1
#     else:
#         if money / 100 >= 1:
#             money -= 100
#             coins += 1
#         else:
#             if money / 50 >= 1:
#                 money -= 50
#                 coins += 1
#             else:
#                 if money / 20 >= 1:
#                     money -= 20
#                     coins += 1
#                 else:
#                     if money / 10 >= 1:
#                         money -= 10
#                         coins += 1
#                     else:
#                         if money / 5 >= 1:
#                             money -= 5
#                             coins += 1
#                         else:
#                             if money / 2 >= 1:
#                                 money -= 2
#                                 coins += 1
#                             else:
#                                 if money / 1 >= 1:
#                                     money -= 1
#                                     coins += 1
#
# print(coins)



# 06. Cake - НЕ Е РЕШЕНО ОТ МЕН
# =====================================================================================================================

# length = int(input())
# width = int(input())
#
# cake_size = length * width
#
# is_over = False
#
# count_peaces = input()
#
# while count_peaces != 'STOP':
#     count_peaces = int(count_peaces)
#     cake_size -= count_peaces
#
#     if cake_size <= 0:
#         is_over = True
#         print(f"No more cake left! You need {abs(cake_size)} pieces more.")
#         break
#
#     count_peaces = input()
#
# if not is_over:
#     print(f"{cake_size} pieces are left.")

























