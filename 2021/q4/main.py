import numpy as np


def part1(filename):
    print(filename)
    file = open(filename, 'r')
    draw = [int(d) for d in file.readline().strip().split(',')]
    print(draw)
    boards = []
    index = 0
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        if index == 0:
            boards.append(np.zeros((5, 5), dtype=int))
        row = [int(l) for l in line.split(' ') if len(l) > 0]
        boards[-1][index] = row
        index = (index + 1) % 5
    # print(boards)
    # print()
    for i in range(len(draw)):
        curr_drawn = draw[i]
        for board in boards:
            board[board == curr_drawn] = -1
            # print(curr_drawn)
            # print(board)
            # print()

            if np.all(board == -1, axis=1).sum() > 0 or np.all(board == -1, axis=0).sum():
                return board[board != -1].sum() * curr_drawn


# result = part1('ex1.txt')
# print('result:', result)
#
# result = part1('input.txt')
# print('result:', result)


def part2(filename):
    print(filename)
    file = open(filename, 'r')
    draw = [int(d) for d in file.readline().strip().split(',')]
    print(draw)
    boards = []
    index = 0
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        if index == 0:
            boards.append(np.zeros((5, 5), dtype=int))
        row = [int(l) for l in line.split(' ') if len(l) > 0]
        boards[-1][index] = row
        index = (index + 1) % 5
    # print(boards)
    # print()
    for i in range(len(draw)):
        curr_drawn = draw[i]
        index = 0
        while index < len(boards):
            board = boards[index]
            board[board == curr_drawn] = -1
            # print(curr_drawn)
            # print(board)
            # print()

            if np.all(board == -1, axis=1).sum() > 0 or np.all(board == -1, axis=0).sum():
                # return board[board != -1].sum() * curr_drawn
                del boards[index]
                if len(boards) == 0:
                    return board[board != -1].sum() * curr_drawn
                continue
            index += 1


result = part2('input_easy.txt')
print('result:', result)

result = part2('input.txt')
print('result:', result)
