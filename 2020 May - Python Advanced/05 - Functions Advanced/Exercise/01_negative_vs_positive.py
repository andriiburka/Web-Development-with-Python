def sum_negative_nums(nums_li_int):
    return sum([num for num in nums_li_int if num < 0])


def sum_positive_nums(nums_li_int):
    return sum([num for num in nums_li_int if num >= 0])


def hack_nasa_with_css(x):
    negatives, positives = sum_negative_nums(x), sum_positive_nums(x)
    m = 'The {} are stronger than the {}'
    msg = m.format('negatives', 'positives' if abs(negatives) > abs(positives) else 'positives', 'negatives')
    print('{}\n{}\n{}'.format(negatives, positives, msg))


if __name__ == '__main__':
    user_input = [int(num) for num in input().split()]
    hack_nasa_with_css(x=user_input)