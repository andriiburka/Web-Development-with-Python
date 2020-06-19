from collections import deque

males = list(map(int, input().split()))
females = deque(map(int, input().split()))
matches = 0

while males:
    f, m = females[0], males[-1]
    if f <= 0:
        females.popleft()
        continue
    if m <= 0:
        males.pop()
        continue

    if females and f % 25 == 0:
        females.popleft()
        females.popleft()
        if not females:
            break
    if males and m % 25 == 0:
        males.pop()
        males.pop()
        if not females:
            break

    if f == m:
        females.popleft()
        males.pop()
        matches += 1
    else:
        females.popleft()
        males[-1] -= 2


print(f"Matches: {matches}")
print(f"Males left: {', '.join(map(str, males)) if males else 'none'}")
print(f"Females left: {', '.join(map(str, females)) if females else 'none'}")
