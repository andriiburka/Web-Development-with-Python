salary = float(input())
month_expenses = float(input())
increase_sal_monthly = float(input())
needed = float(input())
months = int(input())
all_salaries = 0

all_expenses = month_expenses * months

for month in range(months):
    all_salaries += salary
    salary += increase_sal_monthly
result = all_salaries - all_expenses

if result >= needed:
    print("Have a nice ride!")
else:
    print("Work harder!")
