import numpy as np


def part1(filename):
    print(filename)
    file = open(filename, 'r')
    lst = [line.strip().split(' -> ') for line in file.readlines()]
    print(lst)
    points = np.zeros((1000, 1000))
    for l in lst:
        x1, y1 = l[0].split(',')
        x2, y2 = l[1].split(',')
        if int(x1) > int(x2):
            maxX = int(x1)
            minX = int(x2)
        else:
            maxX = int(x2)
            minX = int(x1)

        if int(y1) > int(y2):
            maxY = int(y1)
            minY = int(y2)
        else:
            maxY = int(y2)
            minY = int(y1)
        print(f'({x1}, {y1}), ({x2}, {y2})')
        if maxX == minX or maxY == minY:
            for x in range(minX, maxX + 1):
                for y in range(minY, maxY + 1):
                    points[x][y] += 1
    print(points)
    danger_zone = points[points > 1]
    return len(danger_zone)


#
# result = part1('ex1.txt')
# print('result:', result)
#
# result = part1('input.txt')
# print('result:', result)

def part2(filename):
    file = open(filename, 'r')
    lst = [line.strip().split(' -> ') for line in file.readlines()]
    points = np.zeros((1000, 1000))
    for l in lst:
        x1, y1 = l[0].split(',')
        x2, y2 = l[1].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        if x1 > x2:
            maxX = x1
            minX = x2
        else:
            maxX = x2
            minX = x1

        if y1 > y2:
            maxY = y1
            minY = y2
        else:
            maxY = y2
            minY = y1
        # print(f'({x1}, {y1}), ({x2}, {y2})')
        for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                if maxX == minX or maxY == minY:
                    points[y][x] += 1
                elif abs(x - x1) == abs(y - y1):
                    points[y][x] += 1
                elif abs(x - x2) == abs(y - y2):
                    points[y][x] += 1



    # print(points)
    danger_zone = points[points > 1]
    return len(danger_zone)

# result = part2('ex1.txt')
# print('result:', result)

result = part2('input.txt')
print('result:', result)
