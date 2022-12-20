import copy
import sys
from tools.reader import read

# from enum import Enum

sys.path.insert(0, '../../tools')

data_easy = read('input_easy.txt', separator='')
data = read('input.txt', separator='')


class Point:
    members = []
    members_list = []
    start = None
    end = None

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.distance = sys.maxsize
        self.added_spt = False
        Point.members_list.append(self)

    def get_neighbours(self):
        neighbors = []
        if self.x > 0:
            neighbors.append(Point.members[self.x - 1][self.y])
        if self.x < len(Point.members) - 1:
            neighbors.append(Point.members[self.x + 1][self.y])
        if self.y > 0:
            neighbors.append(Point.members[self.x][self.y - 1])
        if self.y < len(Point.members[0]) - 1:
            neighbors.append(Point.members[self.x][self.y + 1])
        return neighbors

    def __repr__(self):
        return f'Point({self.x}, {self.y}, {chr(self.value)})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def get_points(lines):
    points = []
    Point.start = None
    Point.end = None
    Point.members_list = []
    row = 0
    for line in lines:
        column = 0
        points.append([])
        for char in line:
            point = Point(row, column, ord(char))
            if char == 'S':
                point.value = ord('a')
                Point.start = point
            elif char == 'E':
                point.value = ord('z')
                Point.end = point
            points[row].append(point)
            column += 1
        row += 1
    Point.members = points
    return points


def distance_from_point(start, comparator=None):
    for p in Point.members_list:
        p.distance = sys.maxsize
        p.added_spt = False
    start.distance = 0
    while True:
        not_included = [point for point in Point.members_list if point.added_spt is False]
        if len(not_included) == 0:
            break
        not_included.sort(key=lambda x: x.distance)
        min_point = not_included[0]
        min_point.added_spt = True
        neighbors = [neighbor for neighbor in min_point.get_neighbours() if
                     comparator(min_point, neighbor) and neighbor.distance == sys.maxsize]
        for neighbor in neighbors:
            neighbor.distance = min_point.distance + 1


def part1(lines):
    get_points(lines)

    def comparator(min_point, neighbor):
        return neighbor.value <= min_point.value + 1

    distance_from_point(Point.start, comparator)
    return Point.end.distance


def part2(lines):
    get_points(lines)

    def comparator(min_point, neighbor):
        return min_point.value <= neighbor.value + 1

    distance_from_point(Point.end, comparator)
    distances = [p.distance for p in Point.members_list if p.value == ord('a')]
    return min(distances)


print('Part 1:')
print(part1(data_easy))
print(part1(data))

print('\nPart 2:')
print(part2(data_easy))
print(part2(data))
