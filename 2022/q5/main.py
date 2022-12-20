import sys
from tools.reader import read

# from enum import Enum

sys.path.insert(0, '../../tools')

data_easy = read('input_easy.txt', separator=' ')
data = read('input.txt', separator=' ')

head_data_easy = [
    ['N', 'Z'],
    ['D', 'C', 'M'],
    ['P']
]

head_data = [
    ['G', 'B', 'D', 'C', 'P', 'R'],
    ['G', 'V', 'H'],
    ['M', 'P', 'J', 'D', 'Q', 'S', 'N'],
    ['M', 'N', 'C', 'D', 'G', 'L', 'S', 'P'],
    ['S', 'L', 'F', 'P', 'C', 'N', 'B', 'J'],
    ['S', 'T', 'G', 'V', 'Z', 'D', 'B', 'Q'],
    ['Q', 'T', 'F', 'H', 'M', 'Z', 'B'],
    ['F', 'B', 'D', 'M', 'C'],
    ['G', 'Q', 'C', 'F']
]


def part1(lines, head_param, reverse=True):
    head = head_param.copy()
    for line in lines:
        piece = int(line[1])
        from_ = int(line[3]) - 1
        to_ = int(line[5]) - 1
        moved = head[from_][:piece]
        if reverse:
            moved.reverse()
        head[from_] = head[from_][piece:]
        head[to_] = moved + head[to_]
    result = [line[0] for line in head]
    return ''.join(result)


print('Part 1:')
print(part1(data_easy, head_data_easy))
print(part1(data, head_data))

print('\nPart 2:')
print(part1(data_easy, head_data_easy, False))
print(part1(data, head_data, False))
