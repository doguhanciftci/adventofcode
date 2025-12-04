import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from tools.reader import read

test_data = read('input_easy.txt')
actual_data = read('input.txt')

def findAjs(data, replace):
    result = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '.':
                continue
            adjs = []
            if i > 0:
                adjs.append(data[i-1][j])
                if j > 0:
                    adjs.append(data[i-1][j-1])
                if j < len(data[i])-1:
                    adjs.append(data[i-1][j+1])
            if i < len(data)-1:
                adjs.append(data[i+1][j])
                if j > 0:
                    adjs.append(data[i+1][j-1])
                if j < len(data[i])-1:
                    adjs.append(data[i+1][j+1])
            if j > 0:
                adjs.append(data[i][j-1])

            if j < len(data[i])-1:
                adjs.append(data[i][j+1])
            if adjs.count('@') < 4:
                result += 1
                if replace:
                    data[i][j] = '.'

    return result

def part1(data):
    result = 0
    data = [[y for y in x] for x in data]

    result = findAjs(data, False)
   
    return result

print(f"Part 1 Test: {part1(test_data)}")
print(f"Part 1 Actual: {part1(actual_data)}")

def part2(data):
    result = 0
    data = [[y for y in x] for x in data]
    while True:
        found = findAjs(data, True)
        if found == 0:
            break
        result += found

    return result


print(f"Part 2 Test: {part2(test_data)}")
print(f"Part 2 Actual: {part2(actual_data)}")