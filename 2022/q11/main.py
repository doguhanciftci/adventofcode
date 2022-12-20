import copy
import sys
from tools.reader import read

# from enum import Enum

sys.path.insert(0, '../../tools')


class Monkey:
    members = []
    level_operation = lambda x: x

    def __init__(self, index, items, operation, test, index_true, index_false):
        self.index = index
        self.items = items
        self.operation = operation
        self.test = test
        self.index_true = index_true
        self.next_true = None
        self.index_false = index_false
        self.next_false = None
        self.inspected = 0
        Monkey.members.append(self)

    def set_next(self):
        self.next_true = Monkey.members[self.index_true]
        self.next_false = Monkey.members[self.index_false]

    def throw_items_part(self):
        for item in self.items:
            self.inspected += 1
            level = self.operation(item)
            level = Monkey.level_operation(level)
            if self.test(level):
                self.next_true.items.append(level)
            else:
                self.next_false.items.append(level)
        self.items = []

    def __repr__(self):
        return f'Monkey({self.index})'


def get_most_inspected():
    inspected = [monkey.inspected for monkey in Monkey.members]
    inspected.sort()
    return inspected[-1] * inspected[-2]


def create_monkeys_easy():
    Monkey.members = []
    Monkey(0, [79, 98], lambda x: x * 19, lambda x: x % 23 == 0, 2, 3)
    Monkey(1, [54, 65, 75, 74], lambda x: x + 6, lambda x: x % 19 == 0, 2, 0)
    Monkey(2, [79, 60, 97], lambda x: x * x, lambda x: x % 13 == 0, 1, 3)
    Monkey(3, [74], lambda x: x + 3, lambda x: x % 17 == 0, 0, 1)
    return 23 * 19 * 13 * 17


def create_monkeys_actual():
    Monkey.members = []
    Monkey(0, [63, 57], lambda x: x * 11, lambda x: x % 7 == 0, 6, 2)
    Monkey(1, [82, 66, 87, 78, 77, 92, 83], lambda x: x + 1, lambda x: x % 11 == 0, 5, 0)
    Monkey(2, [97, 53, 53, 85, 58, 54], lambda x: x * 7, lambda x: x % 13 == 0, 4, 3)
    Monkey(3, [50], lambda x: x + 3, lambda x: x % 3 == 0, 1, 7)
    Monkey(4, [64, 69, 52, 65, 73], lambda x: x + 6, lambda x: x % 17 == 0, 3, 7)
    Monkey(5, [57, 91, 65], lambda x: x + 5, lambda x: x % 2 == 0, 0, 6)
    Monkey(6, [67, 91, 84, 78, 60, 69, 99, 83], lambda x: x * x, lambda x: x % 5 == 0, 2, 4)
    Monkey(7, [58, 78, 69, 65], lambda x: x + 7, lambda x: x % 19 == 0, 5, 1)
    return 7 * 11 * 13 * 3 * 17 * 2 * 5 * 19


def create_monkeys(is_easy):
    if is_easy:
        common_divider = create_monkeys_easy()
    else:
        common_divider = create_monkeys_actual()

    for monkey in Monkey.members:
        monkey.set_next()

    return common_divider


def part1(is_easy):
    create_monkeys(is_easy)
    Monkey.level_operation = lambda x: x // 3
    for i in range(20):
        for monkey in Monkey.members:
            monkey.throw_items_part()

    return get_most_inspected()


def part2(is_easy):
    common_divider = create_monkeys(is_easy)
    Monkey.level_operation = lambda x: x % common_divider
    for i in range(10000):
        for monkey in Monkey.members:
            monkey.throw_items_part()

    return get_most_inspected()


print('Part 1:')
print(part1(True))
print(part1(False))

print('\nPart 2:')
print(part2(True))
print(part2(False))
