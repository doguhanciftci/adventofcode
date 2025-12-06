import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from tools.reader import read

test_data = read("input_easy.txt")
actual_data = read("input.txt")


def part1(data):
    result = 0
    data = [d.split(" ") for d in data]
    data = [[x for x in d if x != ""] for d in data]
    for j in range(len(data[0])):
        operator = data[-1][j]
        current_result = 1 if operator == "*" else 0
        for i in range(len(data) - 1):
            number = int(data[i][j])
            if operator == "*":
                current_result *= number
            else:
                current_result += number
        result += current_result

    return result


print(f"Part 1 Test: {part1(test_data)}")
print(f"Part 1 Actual: {part1(actual_data)}")



def my_reader(filename):
    lines = open(filename, "r")
    return [line.replace("\n", "") for line in lines]


test_data_p2 = my_reader("input_easy.txt")
actual_data_p2 = my_reader("input.txt")


def part2(data):
    result = 0
    data = [[*d] for d in data]
    ops = data[-1]
    all_numbers = [[ops[0]]]
    index = 0
    for i in range(len(ops)):
        if i < len(ops) - 1 and ops[i + 1] != ' ':
            index += 1
            all_numbers.append([ops[i+1]])
            continue
        next_number = ''.join([d[i] for d in data[:-1]])
        all_numbers[index].append(int(next_number))
        
    for numbers in all_numbers:
        operator = numbers[0]
        current_result = 1 if operator == "*" else 0
        for n in range(1, len(numbers)):
            number = numbers[n]
            if operator == '*':
                current_result *= number
            else:
                current_result += number
        result += current_result
    return result


print(f"Part 2 Test: {part2(test_data_p2)}")
print(f"Part 2 Actual: {part2(actual_data_p2)}")