import sys
from tools.reader import read

sys.path.insert(0, '../../tools')

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
