def sum_negative_nums(nums_li_int):
    return sum([num for num in nums_li_int if num < 0])


def sum_positive_nums(nums_li_int):
    return sum([num for num in nums_li_int if num >= 0])


def hack_nasa_with_css(user_input):
    sum_negatives, sum_positives = sum_negative_nums(user_input), sum_positive_nums(user_input)

    negatives, positives = 'negatives', 'positives'
    if abs(sum_negatives) < abs(sum_positives):
        positives, negatives = negatives, positives
    message = 'The {} are stronger than the {}'.format(negatives, positives)
    print('{}\n{}\n{}'.format(sum_negatives, sum_positives, message))


if __name__ == '__main__':
    list_input = [int(num) for num in input().split()]
    hack_nasa_with_css(user_input=list_input)