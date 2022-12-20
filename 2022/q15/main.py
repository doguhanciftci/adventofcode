import copy
import sys
from tools.reader import read
import numpy as np

from enum import Enum

sys.path.insert(0, '../../tools')

data_easy = read('input_easy.txt', separator=': ')
data = read('input.txt', separator=': ')


class Beacon:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Beacon({self.x}, {self.y})"


def manhattan_distance(obj1, obj2):
    return abs(obj1.x - obj2.x) + abs(obj1.y - obj2.y)


class Sensor:
    def __init__(self, x, y, beacon):
        self.x = x
        self.y = y
        self.beacon = beacon

    def __repr__(self):
        return f"Sensor({self.x}, {self.y}, {self.beacon})"

    def coverage(self, points, row):
        max_distance = manhattan_distance(self, self.beacon)
        i1 = row - self.x
        if 0 <= i1 <= max_distance:
            for j in range(max_distance + 1 - i1):
                points.add(Beacon(self.x + i1, self.y + j))
                points.add(Beacon(self.x + i1, self.y - j))
        i2 = self.x - row
        if 0 <= i2 <= max_distance:
            for j in range(max_distance + 1 - i2):
                points.add(Beacon(self.x - i2, self.y + j))
                points.add(Beacon(self.x - i2, self.y - j))

        # for i in range(max_distance + 1):
        #     for j in range(max_distance + 1):
        #         if i + j <= max_distance:
        #             if self.x + i == row:
        #                 points.add(Beacon(self.x + i, self.y + j))
        #                 points.add(Beacon(self.x + i, self.y - j))
        #             if self.x - i == row:
        #                 points.add(Beacon(self.x - i, self.y + j))
        #                 points.add(Beacon(self.x - i, self.y - j))


def get_sensors(lines):
    sensors = []
    for line in lines:
        sensor_x = int(line[0].split('x=')[1].split(',')[0])
        sensor_y = int(line[0].split('y=')[1])

        beacon_x = int(line[1].split('x=')[1].split(',')[0])
        beacon_y = int(line[1].split('y=')[1])
        beacon = Beacon(beacon_y, beacon_x)
        sensor = Sensor(sensor_y, sensor_x, beacon)
        sensors.append(sensor)
    return sensors


def part1(lines, row=10):
    sensors = get_sensors(lines)
    points = set()
    for sensor in sensors:
        sensor.coverage(points, row)
    for sensor in sensors:
        if sensor.beacon in points:
            points.remove(sensor.beacon)
        if sensor in points:
            points.remove(sensor)
    return len(points)


def part2(lines):
    return lines



print('Part 1:')
# print(part1(data_easy, 10))
# print(part1(data, 2000000))

print('\nPart 2:')
print(part2(data_easy))
# print(part2(data))
