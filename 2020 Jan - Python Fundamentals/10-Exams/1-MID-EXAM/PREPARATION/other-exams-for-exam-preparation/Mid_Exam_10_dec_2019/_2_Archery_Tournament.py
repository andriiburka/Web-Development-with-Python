integers = list(map(int, input().split('|')))
second_integers = []

while True:
    judge_command = list(map(str, input().split('@')))
    if judge_command[0] == 'Game over':
        break
    else:
        index = int(judge_command[1])
        length = int(judge_command[2])

        if judge_command[0] == 'Shoot Left':
            action = index - length
            a = integers.pop(action)
            integers.insert(action + 1, abs(a - 5))

        elif judge_command[0] == 'Shoot Right'
            if index + 1 == length:

                action = index + length
            for i in range(index + 1):
                if integers[i] == length:
                    index = 0 + length
                    b = integers.pop(index - 1)
                    integers.insert(index, index - 5)

print(integers)
