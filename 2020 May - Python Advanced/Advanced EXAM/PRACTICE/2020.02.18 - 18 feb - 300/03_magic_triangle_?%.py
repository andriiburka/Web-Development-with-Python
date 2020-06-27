def get_magic_triangle(n):
    li = []
    for i in range(n):
        tmp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                tmp.append(1)
            else:
                tmp.append(li[i-1][j-1] + li[i-1][j])
        li.append(tmp)
    print(li)


get_magic_triangle(5)