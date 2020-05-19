lower_1 = int(input())
lower_2 = int(input())
upper_1 = int(input()) + lower_1
upper_2 = int(input()) + lower_2

for num1 in range(lower_1, upper_1 + 1):
    for i in range(2, num1):
        if (num1 % i) == 0:
            break                                           # с брейк казваме че този номер няма да се печата !!!
    else:
        for num2 in range(lower_2, upper_2 + 1):
            for i in range(2, num2):
                if (num2 % i) == 0:
                    break                                   # с брейк казваме че този номер няма да се печата !!!
            else:
                print(f'{num1}{num2}')
