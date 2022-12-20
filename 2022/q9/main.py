import copy
import sys
from tools.reader import read

from enum import Enum


class Direction(Enum):
    RIGHT = 'R'
    DOWN = 'D'
    LEFT = 'L'
    UP = 'U'


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def move(self, direction, distance=1):
        if direction == Direction.RIGHT:
            self.x += distance
        elif direction == Direction.LEFT:
            self.x -= distance
        elif direction == Direction.UP:
            self.y += distance
        elif direction == Direction.DOWN:
            self.y -= distance

    def adjust_to_head(self, head):
        dist = head.distance(self)
        if dist <= 1:
            return
        if dist == 2:
            if head.x == self.x:
                if head.y > self.y + 1:
                    self.y += 1
                elif head.y < self.y - 1:
                    self.y -= 1
            elif head.y == self.y:
                if head.x > self.x + 1:
                    self.x += 1
                elif head.x < self.x - 1:
                    self.x -= 1
        else:
            self.x += 1 if head.x > self.x else -1
            self.y += 1 if head.y > self.y else -1


sys.path.insert(0, '../../tools')

data_easy = read('input_easy.txt', separator=' ', formatter='si')
data_easy2 = read('input_easy2.txt', separator=' ', formatter='si')
data = read('input.txt', separator=' ', formatter='si')


def tail_tracker(lines, num_tails):
    chain = [Point(0, 0), *[Point(0, 0) for i in range(num_tails)]]
    last_tail_tracker = [copy.deepcopy(chain[num_tails])]

    for line in lines:
        direction = Direction(line[0])
        distance = line[1]
        for i in range(distance):
            chain[0].move(direction)  # head
            for t in range(1, len(chain)):
                current_tail = chain[t]
                current_tail.adjust_to_head(chain[t - 1])
            last_tail_tracker.append(copy.deepcopy(chain[num_tails]))

    unique_list = []
    for tail in last_tail_tracker:
        if tail not in unique_list:
            unique_list.append(tail)

    return len(unique_list)


print('Part 1:')
print(tail_tracker(data_easy, 1))
print(tail_tracker(data, 1))

print('\nPart 2:')
print(tail_tracker(data_easy, 9))
print(tail_tracker(data_easy2, 9))
print(tail_tracker(data, 9))
