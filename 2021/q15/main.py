import copy

import numpy as np


def part1V1(filename):
    file = open(filename, 'r')
    lines = [list(line.strip()) for line in file.readlines()]
    lines = np.array(lines, dtype=int)
    # print(lines)

    max_row, max_col = lines.shape
    start = lines[0][0]
    # (row, col, sum)
    points = {(0, 0, 0)}

    final = []
    iter = 0
    while True:
        if len(points) == 0:
            break
        iter += 1
        print(iter)
        for point in copy.deepcopy(points):
            points.remove(point)
            r, c, s = point
            # print(r, c, s, path)
            if c < max_col - 1:
                right = lines[r, c + 1]
                points.add((r, c + 1, s + right))

            if r < max_row - 1:
                down = lines[r + 1, c]
                points.add((r + 1, c, s + down))

            if c == max_col - 1 and r == max_row - 1:
                final.append(point)
    print(final)
    return min(final, key=lambda x: x[2])[2]


result = part1V1('input.txt')
print('result is', result)
breakpoint()


def part1(filename):
    file = open(filename, 'r')
    lines = [list(line.strip()) for line in file.readlines()]
    lines = np.array(lines, dtype=int)
    # print(lines)

    max_row, max_col = lines.shape
    start = lines[0][0]
    # (row, col, sum)
    points = [(0, 0, 0, [])]

    final = []
    iter = 0
    while True:
        if len(points) == 0:
            break
        print()
        print(iter)
        # for p in points:
        #     print(p)
        new_points = []
        for drow, dcol in set(map(lambda p: p[:2], points)):
            filtered = filter(lambda p: p[0] == drow and p[1] == dcol, points)
            new_points.append(min(filtered, key=lambda x: x[2]))
        points = new_points
        short_points = []
        for p in points:
            prow, pcol, psum, ppath = p
            lst = list(filter(lambda x: (prow, pcol) in x[3] and x[2] < psum, points))
            if len(lst) == 0:
                short_points.append(p)
        points = short_points
        iter += 1
        print(max(points, key=lambda x: x[0])[:3])
        print(max(points, key=lambda x: x[1])[:3])
        for point in copy.deepcopy(points):
            points.remove(point)
            r, c, s, path = point
            # print(r, c, s, path)
            if c < max_col - 1 and (r, c + 1) not in path:
                right = lines[r, c + 1]
                points.append((r, c + 1, s + right, path + [(r, c)]))

            if c > 0 and (r, c - 1) not in path:
                left = lines[r, c - 1]
                points.append((r, c - 1, s + left, path + [(r, c)]))

            if r < max_row - 1 and (r + 1, c) not in path:
                down = lines[r + 1, c]
                points.append((r + 1, c, s + down, path + [(r, c)]))

            if r > 0 and (r - 1, c) not in path:
                up = lines[r - 1, c]
                points.append((r - 1, c, s + up, path + [(r, c)]))

            if c == max_col - 1 and r == max_row - 1:
                final.append(point)
    print(final)
    return min(final, key=lambda x: x[2])[2]


result = part1('input.txt')
print('result is', result)

# result = part1('input.txt')
# print('result is', result)
