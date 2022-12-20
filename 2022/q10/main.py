import copy
import sys
from tools.reader import read

# from enum import Enum

sys.path.insert(0, '../../tools')

data_easy = read('input_easy.txt', separator=' ', formatter='si')
data = read('input.txt', separator=' ', formatter='si')


def get_cycles(lines):
    cycles = [1]
    for line in lines:
        last = cycles[-1]
        cycles.append(last)
        if len(line) == 2:
            cycles.append(last + line[1])
    return cycles


def part1(lines):
    cycles = get_cycles(lines)
    result = 0
    for i in [20, 60, 100, 140, 180, 220]:
        result += i * cycles[i - 1]
    return result


def part2(lines):
    cycles = get_cycles(lines)
    print(len(cycles))
    print(cycles)
    for i in range(len(cycles)):
        # print(i, cycles[i])
        if cycles[i] - 1 <= i % 40 <= cycles[i] + 1:
            print('#', end='')
        else:
            print('.', end='')
        if i + 1 in [40, 80, 120, 160, 200, 240]:
            print()


print('Part 1:')
# print(part1(data_easy))
# print(part1(data))

print('\nPart 2:')
# print(part2(data_easy))
print(part2(data))
