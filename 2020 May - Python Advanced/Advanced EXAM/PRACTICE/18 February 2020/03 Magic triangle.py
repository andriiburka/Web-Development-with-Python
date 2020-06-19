from collections import deque

males = deque(map(int, input().split()[::-1]))
females = deque(map(int, input().split()))

print(males)