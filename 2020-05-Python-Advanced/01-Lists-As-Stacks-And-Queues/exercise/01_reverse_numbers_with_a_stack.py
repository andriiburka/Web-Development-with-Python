from _collections import deque


def reverse_f(ints):
    nums = deque(ints.split())
    [print(nums.pop(), end=' ') for _ in range(len(nums))]


if __name__ == '__main__':
    reverse_f(ints=input())
