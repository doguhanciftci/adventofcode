import numpy as np


def file_to_array(filename):
    file = open(filename, 'r')
    lines = [list(line.strip()) for line in file.readlines()]
    lines = np.array(lines, dtype=int)
    return lines, len(lines), len(lines[0])


def part1(filename):
    lines, row, col = file_to_array(filename)
    risk = 0
    for r in range(row):
        for c in range(col):
            curr = lines[r, c]
            up = lines[r - 1, c] if r > 0 else 9
            down = lines[r + 1, c] if r < row - 1 else 9
            right = lines[r, c + 1] if c < col - 1 else 9
            left = lines[r, c - 1] if c > 0 else 9
            if curr < min(up, down, right, left):
                risk += curr + 1
    return risk


# result = part1('ex1.txt')
# print('result is', result)
#
# result = part1('input.txt')
# print('result is', result)


def part2(filename):
    lines, row, col = file_to_array(filename)
    low_points = []
    for r in range(row):
        for c in range(col):
            curr = lines[r, c]
            up = lines[r - 1, c] if r > 0 else 9
            down = lines[r + 1, c] if r < row - 1 else 9
            right = lines[r, c + 1] if c < col - 1 else 9
            left = lines[r, c - 1] if c > 0 else 9
            if curr < min(up, down, right, left):
                low_points.append((r, c, curr))

    def check(rowIndex, colIndex, compareValue):
        if not (-1 < rowIndex < row and -1 < colIndex < col):
            return False
        elem = lines[rowIndex, colIndex]
        if elem != 9 and elem > compareValue:
            basin[rowIndex, colIndex] = elem
            return True
        return False

    def traverse(curr_r, curr_c, curr_value, direction):
        if direction == 'right':
            if (check(curr_r, curr_c + 1, curr_value)):
                traverse(curr_r, curr_c + 1, lines[curr_r, curr_c + 1], 'right')
                traverse(curr_r, curr_c + 1, lines[curr_r, curr_c + 1], 'up')
                traverse(curr_r, curr_c + 1, lines[curr_r, curr_c + 1], 'down')
            # traverseHorizontal(range(curr_c + 1, col), curr_r, curr_value)
        elif direction == 'left':
            if (check(curr_r, curr_c - 1, curr_value)):
                traverse(curr_r, curr_c - 1, lines[curr_r, curr_c - 1], 'left')
                traverse(curr_r, curr_c - 1, lines[curr_r, curr_c - 1], 'up')
                traverse(curr_r, curr_c - 1, lines[curr_r, curr_c - 1], 'down')
            # traverseHorizontal(range(curr_c - 1, -1, -1), curr_r, curr_value)
        elif direction == 'up':
            if (check(curr_r - 1, curr_c, curr_value)):
                traverse(curr_r - 1, curr_c, lines[curr_r - 1, curr_c], 'left')
                traverse(curr_r - 1, curr_c, lines[curr_r - 1, curr_c], 'right')
                traverse(curr_r - 1, curr_c, lines[curr_r - 1, curr_c], 'up')
            # traverseVertical(range(curr_r - 1, -1, -1), curr_c, curr_value)
        elif direction == 'down':
            if (check(curr_r + 1, curr_c, curr_value)):
                traverse(curr_r + 1, curr_c, lines[curr_r + 1, curr_c], 'left')
                traverse(curr_r + 1, curr_c, lines[curr_r + 1, curr_c], 'right')
                traverse(curr_r + 1, curr_c, lines[curr_r + 1, curr_c], 'down')
            # traverseVertical(range(curr_r + 1, row), curr_c, curr_value)
        else:
            return

    lengths = []
    for i in range(len(low_points)):
        r, c, curr = low_points[i]
        basin = np.zeros(lines.shape) - 100
        basin[r, c] = curr
        traverse(r, c, curr, 'right')
        traverse(r, c, curr, 'left')
        traverse(r, c, curr, 'up')
        traverse(r, c, curr, 'down')
        print(basin)
        lengths.append(len(basin[basin > -1]))
        print()
    print(lengths)
    lengths.sort()
    result = 1
    for l in lengths[len(lengths) - 3:]:
        result *= l
    return result


result = part2('input_easy.txt')
print('result is', result)

result = part2('input.txt')
print('result is', result)
