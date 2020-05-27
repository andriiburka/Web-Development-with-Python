<h1>**€rror 404**</h1>
==
<p>Възнаграждение за усърдния труд не беше намерено</p>


[link]
(https://pay.revolut.com/money-request/vwR9Oifyuf)


```Python
def solve():
    intersections = []
    for _ in range(int(input())):
        usr_inp = input().split('-')
        li = []
        for i1 in range(len(usr_inp)):
            start, end = [start_end for start_end in list(map(int, usr_inp[i1].split(',')))]
            tmp = []
            [tmp.append(num) for num in range(start, end + 1)]
            li.append(tmp)
        intersections.append([intersection for intersection in set(li[0]).intersection(set(li[1]))])
    lengths = [len(current_intersection) for current_intersection in intersections]
    max_len_index = lengths.index(max(lengths))
    print(f"Longest intersection is {intersections[max_len_index]} with length {len(intersections[max_len_index])}")


if __name__ == '__main__':
    solve()
```