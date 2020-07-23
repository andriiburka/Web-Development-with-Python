'''

BASIC:

side_size = float(input())
sheets = int(input())
one_sheet_covering = float(input())
box_area = (side_size ** 2) * 6

opf_sheets_count = int(sheets / 3)  # [10] every of those 10 sheets cover 1/ex4_wild_farm_100% of regular sheet
normal_sheets_count = int(sheets - opf_sheets_count)  # 20 normal sheets
opf_sheets_covering = (opf_sheets_count * one_sheet_covering) / ex4_wild_farm_100%
full_sheets_covering = normal_sheets_count * one_sheet_covering

all_sheets_covering = opf_sheets_covering + full_sheets_covering

percentage = (all_sheets_covering / box_area) * 100
print(f'You can cover {percentage:.2f}% of the box.')

ПОДСКАЗКИ
# 30% ot 110
money = 110
percents_to_remove = 30
sum_minus_percents = money * (percents_to_remove/100)
print(f'The sum of 110 lv - 30% = {sum_minus_percents:.0f} lv.')


# 20 ot 200 = ? %
result = 20
target = 200
percentage = (result / target) * 100
print(f'The {result} is {percentage:.0f}% of {target}') # 10%


'''


def box_area_foo(a, b, c):
    return (a * b) * c


def sheets_area_foo(all_sheets, one_sheet_covering):
    opf_sheets_count = int(all_sheets / 3)  # opf = one point four
    sheets_count = int(all_sheets - opf_sheets_count)
    opf_sheets_covering = (opf_sheets_count * one_sheet_covering) / 4
    sheets_covering = sheets_count * one_sheet_covering
    all_sheets_covering_in_cm = opf_sheets_covering + sheets_covering
    return all_sheets_covering_in_cm


def covering_percentage_foo(box_area, sheets_area):
    percentage = (sheets_area / box_area) * 100
    return f'You can cover {percentage:.2f}% of the box.'


# Starts here
square_side_a = float(input())
square_side_b = square_side_a
box_sides = 6
sheets = int(input())
one_sheet_covering_cm = float(input())
print(covering_percentage_foo(box_area=box_area_foo(a=square_side_a, b=square_side_b, c=box_sides), \
                              sheets_area=sheets_area_foo(all_sheets=sheets, \
                                                          one_sheet_covering=one_sheet_covering_cm)))
