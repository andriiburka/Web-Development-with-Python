def create_matrix(r):
    return [list(map(int, input().split())) for r in range(r)]


def expected_output(max_sum, greatest_3x3):
    return '''Sum = {}
{} {} {}
{} {} {}
{} {} {}'''.format(max_sum, *greatest_3x3.values())


rows, cols = list(map(int, input().split()))
matrix = create_matrix(r=rows)
maximal_sum, greatest_3x3_matrix = -50, list()  # the negative matrix dot is max -50

for row in range(rows-2):
    for col in range(cols-2):
        template = {'r1-c1': matrix[row][col], 'r1-c2': matrix[row][col+1], 'r1-c3': matrix[row][col+2],
                    'r2-c1': matrix[row+1][col], 'r2-c2': matrix[row+1][col+1], 'r2-c3': matrix[row+1][col+2],
                    'r3-c1': matrix[row+2][col], 'r3-c2': matrix[row+2][col+1], 'r3-c3': matrix[row+2][col+2]}

        if sum(template.values()) > maximal_sum:
            maximal_sum = sum(template.values())
            greatest_3x3_matrix = template

print(expected_output(max_sum=maximal_sum, greatest_3x3=greatest_3x3_matrix))
