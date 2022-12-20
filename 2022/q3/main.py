import sys
from tools.reader import read

# from enum import Enum

sys.path.insert(0, '../../tools')

data_easy = read('input_easy.txt', separator='')
data = read('input.txt')


def get_value(char):
    if 'a' <= char <= 'z':
        return ord(char) - 96
    elif 'A' <= char <= 'Z':
        return ord(char) - 38
    else:
        return 0


def part1(lines):
    result = 0
    for line in lines:
        mid = len(line) // 2
        sack1 = set(line[:mid])
        sack2 = set(line[mid:])
        common = sack1.intersection(sack2).pop()
        result += get_value(common)
    return result


def part2(lines):
    result = 0
    for index in range(0, len(lines), 3):
        sack1 = set(lines[index])
        sack2 = set(lines[index + 1])
        sack3 = set(lines[index + 2])
        common = sack1.intersection(sack2).intersection(sack3).pop()
        result += get_value(common)
    return result


print('Part 1:')
print(part1(data_easy))
print(part1(data))

print('\nPart 2:')
print(part2(data_easy))
print(part2(data))
