import copy
import sys
from tools.reader import read
import numpy as np

from enum import Enum

sys.path.insert(0, '../../tools')

data_easy = read('input_easy.txt', separator=' -> ')
data = read('input.txt', separator=' -> ')


def between(p1, p2):
    if p1.x == p2.x:
        return [Point(p1.x, y) for y in range(min(p1.y, p2.y) + 1, max(p1.y, p2.y))]
    elif p1.y == p2.y:
        return [Point(x, p1.y) for x in range(min(p1.x, p2.x) + 1, max(p1.x, p2.x))]
    else:
        raise Exception('Points are not aligned')


def split_line(line):
    x, y = line.split(',')
    return int(x), int(y)


class Type(Enum):
    ROCK = '#'
    SAND = '.'
    EMPTY = ' '


class Point:
    def __init__(self, x, y, type=Type.ROCK):
        self.x = x
        self.y = y
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.type = type

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def get_rocks1(lines):
    rocks = []
    for line in lines:
        for i in range(len(line) - 1):
            start = Point(*split_line(line[i]))
            end = Point(*split_line(line[i + 1]))
            rocks.extend([start, end])
            rocks.extend(between(start, end))

    bottom_line = max([p.y for p in rocks])
    most_left = min([p.x for p in rocks])
    start_index = 500 - most_left
    rocks = [[p.y, p.x - most_left] for p in rocks]
    max_row = max([p[0] for p in rocks]) + 1
    max_col = max([p[1] for p in rocks]) + 1
    rocks2D = [[None] * max_col] * max_row
    rocks2D = np.array(rocks2D)
    for rock in rocks:
        row, col = rock
        rocks2D[row][col] = Type.ROCK
    return rocks2D, start_index, bottom_line


def traverse_part1(rocks, bottom_line, start_index):
    current_row = 0
    current_column = start_index
    while True:
        if current_row == bottom_line:
            return None, None

        if rocks[current_row + 1][current_column] is None:
            current_row += 1
            continue
        elif rocks[current_row + 1][current_column - 1] is None:
            current_row += 1
            current_column -= 1
            continue
        elif rocks[current_row + 1][current_column + 1] is None:
            current_row += 1
            current_column += 1
            continue
        else:
            return current_row, current_column


def part1(lines):
    rocks, start_index, bottom_line = get_rocks1(lines)
    sands = 0
    while True:
        # sand = produce_a_sand(rocks, bottom_line, part=1)
        row, col = traverse_part1(rocks, bottom_line, start_index)
        if row is None:
            break
        rocks[row][col] = Type.SAND
        sands += 1
    return sands


def get_rocks2(lines):
    rocks = []
    for line in lines:
        for i in range(len(line) - 1):
            start = Point(*split_line(line[i]))
            end = Point(*split_line(line[i + 1]))
            rocks.extend([start, end])
            rocks.extend(between(start, end))

    bottom_line = max([p.y for p in rocks]) + 2
    rocks = [[p.y, p.x] for p in rocks]
    max_row = max([p[0] for p in rocks]) + 1 + 2
    max_col = max([p[1] for p in rocks]) + 1 + 200
    rocks2D = [[None] * max_col] * max_row
    rocks2D = np.array(rocks2D)
    for rock in rocks:
        row, col = rock
        rocks2D[row][col] = Type.ROCK
    rocks2D[bottom_line] = Type.ROCK
    return rocks2D, bottom_line


def traverse_part2(rocks, bottom_line):
    current_row = 0
    current_column = 500
    while True:
        if current_row == bottom_line:
            return None, None

        if rocks[current_row + 1][current_column] is None:
            current_row += 1
            continue
        elif rocks[current_row + 1][current_column - 1] is None:
            current_row += 1
            current_column -= 1
            continue
        elif rocks[current_row + 1][current_column + 1] is None:
            current_row += 1
            current_column += 1
            continue
        else:
            return current_row, current_column


def part2(lines):
    rocks, bottom_line = get_rocks2(lines)
    sands = 0
    while True:
        row, col = traverse_part2(rocks, bottom_line)
        if row == 0 and col == 500:
            sands += 1
            break
        rocks[row][col] = Type.SAND
        sands += 1
    return sands


print('Part 1:')
print(part1(data_easy))
print(part1(data))

print('\nPart 2:')
print(part2(data_easy))
print(part2(data))
