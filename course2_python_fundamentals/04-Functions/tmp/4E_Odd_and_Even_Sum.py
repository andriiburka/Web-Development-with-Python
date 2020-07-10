def foo(n1):
    odd_sum = 0
    even_sum = 0
    for i in n1:
        if not int(i) % 2 == 0:
            odd_sum += int(i)
        else:
            even_sum += int(i)
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


num = input()
print(foo(num))
