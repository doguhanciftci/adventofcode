import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from tools.reader import read

test_data = read("input_easy.txt")
actual_data = read("input.txt")


def print_data(data):
    for line in data:
        print(line)
    print()

def generate_lines(data):
    result = 0
    data = [list(line) for line in data]
    start_index = data[0].index('S')
    data[1][start_index] = '|'
    for i in range(2, len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '.':
                if data[i-1][j] == '|':
                    data[i][j] = '|'
                pass
            elif data[i][j] == '|':
                pass
            elif data[i][j] == '^' and data[i-1][j] == '|':
                data[i][j - 1] = '|'
                data[i][j + 1] = '|'
                result += 1
            else:
                pass  
    return data, result

def part1(data):
    data, result = generate_lines(data)
    return result


print(f"Part 1 Test: {part1(test_data)}")
print(f"Part 1 Actual: {part1(actual_data)}")


def part2(data):
    data, _ = generate_lines(data)

    timelines = [1 for _ in data[0]]
    for row in data[::-1]:
        for i in range(len(row)):
            if row[i] == '^':
                timelines[i] = timelines[i-1] + timelines[i+1]

    return timelines[data[0].index('S')]


print(f"Part 2 Test: {part2(test_data)}")
print(f"Part 2 Actual: {part2(actual_data)}")
