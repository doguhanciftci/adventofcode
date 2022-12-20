import sys
from tools.reader import read

# from enum import Enum

sys.path.insert(0, '../../tools')

data_easy = read('input_easy.txt', separator=',')
data = read('input.txt', separator=',')


def decode(line):
    start1, end1 = line[0].split('-')
    start2, end2 = line[1].split('-')
    return int(start1), int(end1), int(start2), int(end2)


def part1(lines):
    result = 0
    for line in lines:
        start1, end1, start2, end2 = decode(line)
        if start1 < start2 and end1 >= end2:
            result += 1
        elif start1 > start2 and end1 <= end2:
            result += 1
        elif start1 == start2 or end1 == end2:
            result += 1
    return result


def part2(lines):
    result = 0
    for line in lines:
        start1, end1, start2, end2 = decode(line)
        if start1 < start2 and end1 < start2:
            continue
        elif start1 > start2 and start1 > end2:
            continue
        else:
            result += 1
    return result


print('Part 1:')
print(part1(data_easy))
print(part1(data))

print('\nPart 2:')
print(part2(data_easy))
print(part2(data))
