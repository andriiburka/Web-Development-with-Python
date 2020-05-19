'''
2. Crocs

draw
width – N * 5
height – N * 4 + 2
header rows = int(N / 2)


Input
odd integer number.

Output
correctly-drawn croc shoe

The head lines (first and last several lines) are exactly N / 2 (integer division) by count.

Constraints
 The integer N will always be an odd number in range [0, 100].
 Allowed time / memory: 100ms / 16MB.

START: 15:43
END:

       _3_   _3_    --------- 15 chr
    _3_   _3_   _3_
1      ######### ------------ header_footer()
2   ###         ### --------- empty_inside()
3   ### # # # # ###
4   ###  # # #  ###
5   ### # # # # ###
6   ###  # # #  ###
7   ### # # # # ###
8   ###         ###
9   ###############
10  ### # # # # ###
11  ###############
12  ### # # # # ###
13  ###############
14     #########

for row in (1, odd_in + 1):
    if not row % 2 == 0:    # odd number
        1_0()
    else:    # even number


    __5__     __5__     __5__
         __5__     __5__
1        ###############_______________1
2        ###############               1
3   #####               #####_____________2
4   ##### # # # # # # # #####_______________3---------- 1
5   #####  # # # # # #  #####               3
6   ##### # # # # # # # #####-------------------------- 2
7   #####  # # # # # #  #####
8   ##### # # # # # # # #####-------------------------- 3
9   #####  # # # # # #  #####
10  ##### # # # # # # # #####-------------------------- 4
11  #####  # # # # # #  #####
12  ##### # # # # # # # #####-------------------------- 5
13  #####               #####       empty_inside()
14  #########################
15  ##### # # # # # # # #####
16  #########################
17  ##### # # # # # # # #####
18  #########################
19  ##### # # # # # # # #####
20  #########################
21       ###############
22       ###############

'''
import math as m


def header_footer():
    header_list = []
    header_list.append(" " * odd_in)
    header_list.append(("#" * odd_in) * 3)
    header_list.append(" " * odd_in)
    for row in range(1, n_rows + 1):
        print(''.join(header_list))


def empty_inside():
    empty_inside = []
    empty_inside.append("#" * odd_in)
    empty_inside.append((" " * odd_in) * 3)
    empty_inside.append("#" * odd_in)
    print(''.join(empty_inside))


def hash_space():
    space_hash_list = []
    space_hash_list.append('#' * odd_in + ' ')
    for char in range(1, odd_in * 3):
        if char % 2 == 1:
            space_hash_list.append('#')
        else:
            space_hash_list.append(' ')
    space_hash_list.append('#' * odd_in)
    print(''.join(space_hash_list))


def space_hash():
    hash_space_list = []
    hash_space_list.append('#' * odd_in + ' ')
    for char in range(1, odd_in * 3 - 1):
        if char % 2 == 0:
            hash_space_list.append('#')
        else:
            hash_space_list.append(' ')
    hash_space_list.append(' ' + '#' * odd_in)
    print(''.join(hash_space_list))


def full_line():
    print('#' * horizontal_line)


def mosaic1():
    count_block_1 = 0
    for r in range(1, odd_in + 1):
        count_block_1 += 1
        hash_space()
        for char in range(1):
            count_block_1 += 1
            if count_block_1 > odd_in + (odd_in - 1):
                continue
            else:
                space_hash()


def mosaic2():
    count_block_2 = 0
    for row in range(1, odd_in):  # rows
        count_block_2 += 1
        full_line()

        for char in range(1):  # chars '#'
            if count_block_2 > m.floor(odd_in / 2 + 1):
                break
            else:
                hash_space()


odd_in = int(input())
horizontal_line = odd_in * 5
vertical_line = odd_in * 4 + 2
n_rows = int(odd_in / 2)

header_footer()
empty_inside()
mosaic1()
empty_inside()
mosaic2()
header_footer()
