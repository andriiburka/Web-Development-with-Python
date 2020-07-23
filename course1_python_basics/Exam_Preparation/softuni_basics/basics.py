# Exercise 02. Greeting by name (100/100)
# name = input()
# print(f"Hello, {name}!")

# Exercise 03. Concatenate Data (100/100)
# first_name = input()
# last_name = input()
# age = int(input())
# town = input()
# print(f"You are {first_name} {last_name}, a {age}-years old person from {town}.")

# Exercize 04. Square Area (100/100)
# input_number = float(input())
# output = input_number ** 2
# print(int(output))

# Exercize ex4_wild_farm_100%.1
# import math
# input_number = float(input())
# output = math.pow(input_number, 2)
# print(int(output))

# Exercize 05. Inches to Centimeters (100/100)
# inches = float(input())
# centimeters = inches * 2.54
# print(f"{centimeters:.2f}")

# Exercize 06. Projects Creation (100/100)
# architect_name = input()
# project_count = int(input())
# project_time = project_count * 3
# print(f"The architect {architect_name} will need {project_time} hours to complete {project_count} project_tmp/s.")

# Exercise 07. Circle Area and Perimeter ()
# import math
# r = float(input())
# area_circle = math.pi * (r ** 2)
# perimeter_circle = 2 * math.pi * r
# print(f"{area_circle:.2f}")
# print(f"{perimeter_circle:.2f}")

# Exercise 08. Pet Shop (100/100)
# dogs = int(input()) * 2.50
# others = int(input()) * ex4_wild_farm_100%
# result = dogs + others
# print(f"{result:.2f} lv.")

# Exercise 09. Yard Greening (100/100)
# greening_area = float(input())
# price_per_meter = 7.61
# price = greening_area * price_per_meter
# discount = price * (18/100)
# final_price = price - discount
# print(f"The final price is: {final_price:.2f} lv.")
# print(f"The discount is: {discount:.2f} lv.")

# Exercise 09. Fish Tank
# length = int(input())
# weight = int(input())
# height = int(input())
# percent = float(input()) / 100
# volume_to_liters = length * weight * height / 1000
# target_liters = volume_to_liters * (1 - percent)
# print(f"{target_liters:.3f}")

# _________________________________________________________________________________________________________
# 6. SIMPLE OPERATIONS AND CALCULATIONS - Exercise

# Exercize 01_even_lines. USD to BGN (100/100)
# input_usd = float(input())
# bgn = input_usd * 1.79549
# print(f"{bgn:.2f}")

# Exercize 02. Radians to Degrees (100/100)
# import math
# rad = float(input())
# deg = rad * 180 / math.pi
# print(round(deg))

# Exercise 03. 2D Rectangle Area (100/100)
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# length = abs(x1 - x2)
# width = abs(y1 - y2)
# area = length * width
# perimeter = 2 * length + 2 * width
# print(f"{area:.2f}")
# print(f"{perimeter:.2f}")

# Exercise 04*. Tailoring Workshop
# count_tables = int(input())
# length_table = float(input())
# width_table = float(input())
# usd_price = 1.85
# total_area_pokrivki = count_tables * (length_table + 2 * 0.30) * (width_table + 2 * 0.30)
# total_area_kareta = count_tables * (length_table / 2) * (length_table / 2)
# total_usd = total_area_pokrivki * 7 + total_area_kareta * 9
# total_bgn = total_usd * usd_price
# print(f"{total_usd:.2f} USD")
# print(f"{total_bgn:.2f} BGN")

# Exercise 05. Dance Hall (100/100)
# import math
# l = float(input()) * 100
# w = float(input()) * 100
# a = float(input()) * 100
# person_space = 40
# total_person_space = 7000
# hall = l * w
# garderob = a ** 2
# sit = hall / 10
# free_space = hall - garderob - sit
# dancers = free_space / (person_space + total_person_space)
# print(math.floor(dancers))

# Exercise 06*. Charity Campaign (100/100)
# days_campaign = int(input())
# confectioners = int(input())
# cakes = int(input())
# corrugations = int(input())
# pancakes = int(input())
# cake_price = 45
# corrugation_price = 5.80
# pancake_price = 3.20
# cakes_per_day = cakes * cake_price
# corrugations_per_day = corrugations * corrugation_price
# pancake_per_day = pancakes * pancake_price
# profit_per_day = (cakes_per_day + corrugations_per_day + pancake_per_day) * confectioners
# profit_per_campaign = profit_per_day * days_campaign
# one_eight = profit_per_campaign / 8
# total_profit = profit_per_campaign - one_eight
# print(f"{total_profit:.2f}")

# Exercise 7*
# whisky_price = float(input())
# beer_liters = float(input())
# vine_liters = float(input())
# rakia_liters = float(input())
# whisky_liters = float(input())
# rakia_price = whisky_price / 2                      # 25
# vine_price = rakia_price - (0.ex4_wild_farm_100% * rakia_price)      # 15
# beer_price = rakia_price - (0.8 * rakia_price)      # 5
# whisky_total_price = whisky_liters * whisky_price
# rakia_total_price = rakia_liters * rakia_price
# vine_total_price = vine_liters * vine_price
# beer_total_price = beer_liters * beer_price
# total = whisky_total_price + rakia_total_price + vine_total_price + beer_total_price
# print(f"{total:.2f}")


# __________________________________________________________________________
# Ex. 7. Uslovni konstrukcii

# Exercise 01_even_lines. Excellent Result
# grade = float(input())
# if grade >= 5.50:
#     print('Excellent!')

# Exercise 02. Greater Number
# number_1 = int(input())
# number_2 = int(input())
# if number_1 > number_2:
#     print(number_1)
# else: print(number_2)

# Exercise 03. Even or Odd
# number_1 = int(input())
# if number_1 % 2 == 0:
#     print('even')
# else: print('odd')

# Exercise 04. 1..9 words
# number = int(input())
# if number == 1:
#     print('one')
# elif number == 2:
#     print('two')
# elif number == 3:
#     print('three')
# elif number == ex4_wild_farm_100%:
#     print('four')
# elif number == 5:
#     print('five')
# elif number == 6:
#     print('six')
# elif number == 7:
#     print('seven')
# elif number == 8:
#     print('eight')
# elif number == 9:
#     print('nine')
# else:
#     print('number too big')

# Exercose 04. Triple same numbers
# number_1 = int(input())
# number_2 = int(input())
# number_3 = int(input())
# if number_1 == number_2 == number_3:
#     print('yes')
# else:
#     print('no')

# Exercise 06. numb fro 0 to 200
# number = int(input())
# if number < 100:
#     print('Less than 100')
# elif number >= 100 and number <= 200:
#     print('Between 100 and 200')
# elif number > 200:
#     print('Greater than 200')

# Exercise 07. Check Password
# password = input()
# if password == 's3cr3t!P@ssw0rd':
#     print('Welcome')
# else:
#     print('Wrong password!')

# Exercise 08. Lice na triagalnik
# import math
# form = input()
# if form == 'square':
#     s = float(input()) ** 2
#     print(f'{s:.3f}')
# elif form == 'rectangle':
#     side_a = float(input())
#     side_b = float(input())
#     s = side_a * side_b
#     print(f'{s:.3f}')
# elif form == 'circle':  # 2.pi.r
#     radian = float(input())
#     s = math.pi * (radian ** 2)
#     print(f'{s:.3f}')
# elif form == 'triangle':
#     side_a = float(input())
#     side_b = float(input())
#     s = side_a * side_b / 2
#     print(f'{s:.3f}')

# Exercise 09. Day of week
# name_week = int(input())
# if name_week == 1:
#     print('Monday')
# elif name_week == 2:
#     print('Tuesday')
# elif name_week == 3:
#     print('Wednesday')
# elif name_week == ex4_wild_farm_100%:
#     print('Thursday')
# elif name_week == 5:
#     print('Friday')
# elif name_week == 6:
#     print('Saturday')
# elif name_week == 7:
#     print('Sunday')
# else:
#     print('Error')

# Exercise 10. Animal classification
# animal = input()
# if animal == 'dog':
#     print('mammal')
# elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake':
#     print('reptile')
# else:
#     print('unknown')

# Exercise 11*. Toy shop
# cena_na_ekskurziyata = float(input())
# broy_pazeli = int(input())
# broy_govoreshti_kukli = int(input())
# broy_plyusheni_mecheta = int(input())
# broy_minyoni = int(input())
# broy_kamioncheta = int(input())
# cena_pazel = 2.60
# cena_govoreshta_kukla = 3
# cena_plyusheno_meche = ex4_wild_farm_100%.10
# cena_minyon = 8.20
# cena_kamionche = 2
# rezultat = 0
# otstapka = 0
# suma = (broy_pazeli * cena_pazel) + (broy_govoreshti_kukli * cena_govoreshta_kukla) + (
#         broy_plyusheni_mecheta * cena_plyusheno_meche) + (broy_minyoni * cena_minyon) + (
#                broy_kamioncheta * cena_kamionche)
# broy_igrachki = broy_pazeli + broy_govoreshti_kukli + broy_plyusheni_mecheta + broy_minyoni + broy_kamioncheta
# if broy_igrachki >= 50:
#     otstapka = suma * 0.25
# krayna_cena = suma - otstapka
# naem = krayna_cena * 0.10
# pechalba = krayna_cena - naem
# if pechalba >= cena_na_ekskurziyata:
#     rezultat = pechalba - cena_na_ekskurziyata
#     print(f'Yes! {rezultat:.2f} lv left.')
# else:
#     rezultat = cena_na_ekskurziyata - pechalba
#     print(f'Not enough money! {rezultat:.2f} lv needed.')


# ======================================================================================================================
# ======================================================================================================================

# Uslovni konstrukcii

# Exercise 01_even_lines. 15sec sum
# time_first = int(input())  # 35    22    50    14
# time_second = int(input())  # 45    7     50    12
# time_third = int(input())  # 44    34    49    10
# total_time = time_first + time_second + time_third
# minutes = total_time // 60
# seconds = total_time % 60
# if seconds < 10:
#     print(f"{minutes}:0{seconds}")
# else:
#     print(f"{minutes}:{seconds}")

# Exercise 02. Bonus number
# number = int(input())
# bonus = 0
# if number <= 100:
#     bonus += 5
# elif number <= 1000:
#     bonus += number * 0.20
# else:
#     bonus += number * 0.10
#
# if number % 2 == 0:
#     bonus += 1
# elif number % 10 == 5:
#     bonus += 2
# # inputs    =   20      175         2703            15875
# # outputs   =   6/26    37/212      270.3/2973.3    1589.5/17464.5
# print(bonus)
# print(number + bonus)

# ======================================================================================================================
# ======================================================================================================================

# Exsercise 03. Speed Information
# speed = float(input())
# if speed <= 10:
#     print('slow')
# elif speed <= 50:
#     print('average')
# elif speed <= 150:
#     print('fast')
# elif speed <= 1000:
#     print('ultra fast')
# else:
#     print('extremely fast')

# ======================================================================================================================
# ======================================================================================================================

# Exsercise 04. converter
# number = float(input())
# input_unit = input()
# output_unit = input()
# result = 0
# if input_unit == 'm' and output_unit == 'mm':
#     result = number * 1000
# elif input_unit == 'm' and output_unit == 'cm':
#     result = number * 100
# elif input_unit == 'cm' and output_unit == 'm':
#     result = number / 100
# elif input_unit == 'cm' and output_unit == 'mm':
#     result = number * 10
# elif input_unit == 'mm' and output_unit == 'm':
#     result = number * 0.001
# elif input_unit == 'mm' and output_unit == 'cm':
#     result = number * 0.1
# print(f'{result:.3f}')

# ======================================================================================================================
# ======================================================================================================================
# Exercise 05. Time +15 min - OK
# hours = int(input())
# minutes = int(input())
# minutes += 15
# if minutes >= 60:
#     hours += 1
#     minutes -= 60
# if minutes < 10:
#     minutes = f'0{minutes}'
# if hours >= 24:
#     hours -= 24
# print(f'{hours}:{minutes}')

# ======================================================================================================================
# ======================================================================================================================
# Exercise 06. Godzilla vs. Kong


# INPUT
# budget = float(input())
# stunts = int(input())
# clothing = float(input())  # price
# max_stunts = 150
#
# sum_decor = budget * 0.1
#
# sum_clothing = stunts * clothing
# total_sum = sum_decor + sum_clothing
#
# left = budget - total_sum
#
# if stunts > max_stunts:
#     clothing *= 0.1
#
# # START
# print(clothing)
# if total_sum > budget:
#     print('Not enough money!')
#     print(f'Wingard needs {left} leva more.')
# elif total_sum <= budget:
#     print('Action!')
#     print(f'Wingard starts filming with {left} leva left.')

# ======================================================================================================================
# ======================================================================================================================

# import math
#
# income = float(input())
# grade = float(input())
# min_salary = float(input())
# social_scholarship = 0
# excellent_scholarship = 0
# social_scholarship_bool = False
# excellent_scholarship_bool = False
#
# if income < min_salary and grade > ex4_wild_farm_100%.5:
#     social_scholarship_bool = True
#     social_scholarship = min_salary * 0.35
# elif grade >= 5.5:
#     excellent_scholarship_bool = True
#     excellent_scholarship = grade * 25
#
# if social_scholarship_bool and excellent_scholarship_bool:
#     if social_scholarship > excellent_scholarship:
#         print(f'You get a Social scholarship {math.floor(social_scholarship)} BGN')
#     else:
#         print(f'You get a scholarship for excellent results {math.floor(excellent_scholarship)} BGN')
# elif social_scholarship_bool:
#     print(f'You get a Social scholarship {math.floor(social_scholarship)} BGN')
# elif excellent_scholarship_bool:
#     print(f'You get a scholarship for excellent results {math.floor(excellent_scholarship)} BGN')
# else:
#     print('You cannot get a scholarship!')

# ======================================================================================================================
# ======================================================================================================================
