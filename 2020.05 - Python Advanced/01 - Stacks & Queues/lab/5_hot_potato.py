from collections import deque


def start(people, step):
    index = 0
    while people:
        person = people.popleft()
        index += 1

        if index == step:
            index = 0
            if people:
                print(f"Removed {person}")
            else:
                print(f"Last is {person}")
        else:
            people.append(person)


if __name__ == '__main__':
    start(people=deque(input().split()), step=int(input()))