import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from tools.reader import read

test_data = read('input_easy.txt')
actual_data = read('input.txt')

def part1(data):
    result = 0
    current = 50
    for line in data:
        way = line[0]
        distance = int(line[1:])
        current += distance * (1 if way == 'R' else -1)
        
        current = current % 100
        if current == 0:
            result += 1

    return result

print(f"Part 1 Test: {part1(test_data)}")
print(f"Part 1 Actual: {part1(actual_data)}")

def part2(data):
    result = 0
    current = 50
    for line in data:
        way = line[0]
        distance = int(line[1:])

        if distance > 100:
            result += distance // 100
            distance = distance % 100

        current += distance * (1 if way == 'R' else -1)

        if current == 0 or current > 100 or current < 0:
            result += 1
            current = current % 100

    return result

print(f"Part 2 Test: {part2(test_data)}")
print(f"Part 2 Actual: {part2(actual_data)}")