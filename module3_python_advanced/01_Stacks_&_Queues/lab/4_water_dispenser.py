from collections import deque


def start():
    total_liters = int(input())
    people = deque()
    while True:
        cmd = input()
        if cmd.startswith('Start'):

            while people:
                cmd = input()

                if cmd.startswith('End'):
                    break

                if cmd.startswith('refill'):
                    total_liters += int(cmd.split()[1])
                    continue

                elif cmd.isdigit():
                    if total_liters < int(cmd):
                        print(f"{people.popleft()} must wait")
                    else:
                        total_liters -= int(cmd)
                        print(f"{people.popleft()} got water")
                        # трябва да е people[0] вместо people.popleft()
                        # поредното глупаво условие
            print(f"{total_liters} liters left")
            break
        else:
            people.append(cmd)


if __name__ == '__main__':
    start()





# # v.1
# from collections import deque
#
# liters = int(input())
# queue = deque()
# while True:
#     inp = input()
#     if inp == "Start":
#         break
#     else:
#         queue.append(inp)
#
# while True:
#     inp = input()
#     if inp == "End":
#         print(f"{liters} liters left")
#         break
#     else:
#         inp = inp.split()
#         if len(inp) == 1:
#             digit = int(inp[0])
#             if liters - digit >= 0:
#                 print(f"{queue.popleft()} got water")
#                 liters -= digit
#             else:
#                 print(f"{queue.popleft()} must wait")
#                 continue
#         else:
#             value = int(inp[1])
#             liters += value