import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from tools.reader import read

data = read('input.txt')

elfs = []
index = 0
for d in data:
    if d == '':
        index += 1
        continue

    try:
        elfs[index].append(int(d))
    except IndexError:
        elfs.append([int(d)])

sums = [sum(elf) for elf in elfs]


# Part 1:
print('Part 1:', max(sums))

# Part 2:
sums.sort()
print('Part 2:', sum(sums[-3:]))
