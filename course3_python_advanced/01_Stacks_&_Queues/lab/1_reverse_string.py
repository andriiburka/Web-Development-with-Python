def reverse_func(li):
    while li:
        print(li.pop(), end='')


if __name__ == "__main__":
    reverse_func(
        li=list(input())
    )
