import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from tools.reader import read

test_data = read('input_easy.txt')
actual_data = read('input.txt')

def find_n_largest(numbers, n):
    max_val = max(numbers[:len(numbers)-n+1])
    max_index = numbers.index(max_val)
    numbers = numbers[max_index+1:]
    return max_val * pow(10, n-1) + find_n_largest(numbers, n-1) if n > 1 else max_val

def part1(data):
    result = 0
    data = [[int(y) for y in x] for x in data]
    for row in data:
        result += find_n_largest(row, 2)
        
    return result

print(f"Part 1 Test: {part1(test_data)}")
print(f"Part 1 Actual: {part1(actual_data)}")

def part2(data):
    result = 0
    data = [[int(y) for y in x] for x in data]
    for row in data:
        result += find_n_largest(row, 12)
        
    return result


print(f"Part 2 Test: {part2(test_data)}")
print(f"Part 2 Actual: {part2(actual_data)}")