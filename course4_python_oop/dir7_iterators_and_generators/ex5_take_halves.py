def solution():
    def integers():
        curr_number = 1
        while True:
            yield curr_number
            curr_number += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, sequence):
        numbers = []
        for num in sequence:
            if len(numbers) == n:
                return numbers
            numbers.append(num)

    return take, halves, integers
