import sys
from tools.reader import read

# from enum import Enum

sys.path.insert(0, '../../tools')

data_easy = read('input_easy.txt', separator='')
data = read('input.txt', separator='')


def distinct(lines, limit):
    index = 0
    chars = []
    for char in lines[0]:
        if len(chars) < limit:
            chars.append(char)
        else:
            chars.pop(0)
            chars.append(char)
        char_set = set(chars)

        index += 1
        if len(char_set) == limit:
            break
    return index


print('Part 1:')
print(distinct(data_easy, 4))
print(distinct(data, 4))

print('\nPart 2:')
print(distinct(data_easy, 14))
print(distinct(data, 14))
