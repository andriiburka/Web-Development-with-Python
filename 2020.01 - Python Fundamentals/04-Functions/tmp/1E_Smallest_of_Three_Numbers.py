# v2.0


def foo(n1, n2, n3):
    li.append(n1)
    li.append(n2)
    li.append(n3)
    return min(li)


a = int(input())
b = int(input())
c = int(input())
li = []
print(foo(a, b, c))


# v1.0
# def SMALLEST_NUM(unsorted_list):
#     return min(unsorted_list)
#
#
# if __name__ == '__main__':
#     numbers = []
#     number_1 = numbers.append(int(input()))
#     number_2 = numbers.append(int(input()))
#     number_3 = numbers.append(int(input()))
#     print(SMALLEST_NUM(numbers))