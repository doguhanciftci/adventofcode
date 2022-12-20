import sys
from tools.reader import read
from enum import Enum

sys.path.insert(0, '../../tools')


class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


data_easy = read('input_easy.txt', separator=' ')
data = read('input.txt', separator=' ')


def part1(lines):
    score = 0
    for line in lines:
        opponent = Move(ord(line[0]) - 64)
        me = Move(ord(line[1]) - 87)
        score += me.value
        if opponent == me:
            score += 3
            continue

        if opponent == Move.ROCK and me == Move.PAPER:
            score += 6
        elif opponent == Move.PAPER and me == Move.SCISSORS:
            score += 6
        elif opponent == Move.SCISSORS and me == Move.ROCK:
            score += 6

    return score


def part2(lines):
    score = 0
    for line in lines:
        opponent = Move(ord(line[0]) - 64)
        me = Move(ord(line[1]) - 87)

        if me == Move.ROCK:  # lose
            if opponent == Move.ROCK:
                selection = Move.SCISSORS
            elif opponent == Move.PAPER:
                selection = Move.ROCK
            elif opponent == Move.SCISSORS:
                selection = Move.PAPER
        elif me == Move.PAPER:  # draw
            score += 3
            selection = opponent
        elif me == Move.SCISSORS:  # win
            score += 6
            if opponent == Move.ROCK:
                selection = Move.PAPER
            elif opponent == Move.PAPER:
                selection = Move.SCISSORS
            elif opponent == Move.SCISSORS:
                selection = Move.ROCK
        score += selection.value

    return score

print('Part 1')
print(part1(data_easy))
print(part1(data))

print('\nPart 2')
print(part2(data_easy))
print(part2(data))
