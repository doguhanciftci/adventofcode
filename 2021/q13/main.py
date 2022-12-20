import numpy as np


def part1(filename):
    file = open(filename, 'r')
    dots_x = []
    dots_y = []
    folds = []
    for line in file:
        if len(line.strip()) == 0:
            continue
        if line.startswith('fold along'):
            fold_direction, fold_value = line.replace('fold along ', '').strip().split('=')
            folds.append((fold_direction, int(fold_value)))
            continue
        x, y = line.split(',')
        dots_x.append(int(x.strip()))
        dots_y.append(int(y.strip()))
    matrix = np.zeros((max(dots_y) + 1, max(dots_x) + 1))
    matrix[dots_y, dots_x] = 1
    for direction, fold in folds:
        if direction == 'y':
            left = matrix[:fold, :]
            right = matrix[:fold:-1, :]
            matrix = left + right
        else:
            left = matrix[:, :fold]
            right = matrix[:, :fold:-1]
            matrix = left + right
    matrix[matrix > 0] = 1
    for i in range(8):
        print(matrix[:, i * 5:(i + 1) * 5])
        print()
    return np.count_nonzero(matrix)


result = part1('input.txt')
print('result is', result)
