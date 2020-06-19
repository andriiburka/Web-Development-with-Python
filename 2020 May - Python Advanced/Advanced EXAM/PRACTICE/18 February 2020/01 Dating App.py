from collections import deque

males = list(map(int, input().split()))
females = deque(map(int, input().split()))
matches = 0

while males or females:
    # Below or equals to zero
    if males and males[-1] <= 0:
        males.pop()
        continue
    if females and females[0] <= 0:
        females.popleft()
        continue

    # Special case...
    if females and females[0] % 25 == 0:
        females.popleft()
        if females:
            females.popleft()
            continue
    elif males and males[-1] % 25 == 0:
        males.pop()
        if males:
            females.pop()
            continue

    # Matching...
    if females and males:
        first_female, last_male = females[0], males[-1]
        if first_female == last_male:
            females.popleft()
            males.pop()
            matches += 1
        else:
            females.popleft()
            males[-1] -= 2
    else:
        break

print(f"Matches: {matches}")
print(f"Males left: {', '.join(map(str, reversed(males))) if males else 'none'}")
print(f"Females left: {', '.join(map(str, females)) if females else 'none'}")