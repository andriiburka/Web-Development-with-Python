
'''

You need 1000 leva for the journey and you have 4 months.
Month 1
Every month you can save 1000 * 25% => 250 lv. So, to the end of the 1st month you have 250 lv.
Month 2
To the END of the 2nd month -  'First Month Money' + 250 -> 500 lv.
Month 3
To the begging of the 3th month (odd month) you spent 80 lv. ("Month2-money" * 16% = 80)
for clothes and shoes, on  the END of this month you save 250 lv, so now you have 670 lv.
Month 4
Last month is the fourth month and you save
"Month3-Money" + 167.5 ("Month3-money" * 25% = 167.5) + 25 = 1087.5 lv.
Result
You have 1087.5 – 1000 = 87.5 lv., so you can go to the trip.


You need 3265 leva for the journey and you have 3 months.
+++ Month 1 -------------------------------------------------------
Every month you can save 3265 * 25% => 816.25 lv.
So, to the end of the 1st month you have 816.25 lv.
+++ Month 2 -------------------------------------------------------
To the END of the 2nd month -  816.25 + 816.25 -> 1632.5 lv.
Month 3 -------------------------------------------------------
To the begging of the 3th month (odd month) you spent 261.2 lv. (1632.5 * 16% = 261.2) for clothes and shoes
savings now are 1632.5 - 261.2 = 1371.3
on  the END of this month you save 250 lv, so now you have 2187.55 lv.
Result --------------------------------------------------------
You have 3265 - 2187.55 = 1077.45 = 87.5 lv., so you can NOT go to the trip.
2187.55 <   t.e.
diff = 1077.45
'''

# input
needed_money = float(input())
months = int(input())
savings = 0

for month in range(1, months + 1):
    # vars
    monthly_income = needed_money * 0.25
    month_is_not_first = month > 1
    month_is_odd = month % 2 != 0
    month_is_every_fourth = month % 4 == 0
    spending_for_clothes = savings * 0.16
    bonus = savings * 0.25

    # conditions
    if month_is_odd and month_is_not_first:
        savings -= spending_for_clothes
    if month_is_every_fourth:
        savings += bonus

    # add monthly income
    savings += monthly_income

# result
if savings >= needed_money:
    money = savings - needed_money
    print(f'Bravo! You can go to Disneyland and you will have {money:.2f}lv. for souvenirs.')
else:
    diff = abs(savings - needed_money)
    print(f'Sorry. You need {diff:.2f}lv. more.')