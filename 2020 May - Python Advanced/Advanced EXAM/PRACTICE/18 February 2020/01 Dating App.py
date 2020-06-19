''' already 100/100
Issue 1: 57/100
Tests 4, 9, 10, 12, 14: Incorrect answers
Line 42: reversing the list did the job

Issue 2: 92/100
Test for incorrect answer - 13: Incorrect answer
Line 25: Logic error. Wrote females.pop() instead of males.pop()

The dumbest part of the task is: There is no condition that hinting to reverse males list
'''

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
            males.pop()
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










''' 100/100
The diff here is that i reverse 'Males List' at the begin
That's why i'm using deque to popleft() first index
That make sense..
'''

from collections import deque

males = deque(map(int, input().split()[::-1]))
females = deque(map(int, input().split()))
matches = 0

while males or females:

    # Below or equals to zero
    if males and males[0] <= 0:
        males.popleft()
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
    elif males and males[0] % 25 == 0:
        males.popleft()
        if males:
            males.popleft()
            continue

    # Matching...
    if females and males:
        first_female, last_male = females[0], males[0]
        if first_female == last_male:
            females.popleft()
            males.popleft()
            matches += 1
        else:
            females.popleft()
            males[0] -= 2
    else:
        break

print(f"Matches: {matches}")
print(f"Males left: {', '.join(map(str, males)) if males else 'none'}")
print(f"Females left: {', '.join(map(str, females)) if females else 'none'}")
