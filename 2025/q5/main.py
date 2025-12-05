import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from tools.reader import read

test_data = read("input_easy.txt")
actual_data = read("input.txt")


def get_ranges_and_ids(data):
    ranges = []
    ids = []
    line_received = False
    for line in data:
        if line == "":
            line_received = True
            continue
        if line_received:
            ids.append(int(line))
        else:
            ranges.append([int(x) for x in line.split("-")])
    return ranges, ids


def part1(data):
    result = 0
    ranges, ids = get_ranges_and_ids(data)
    for id in ids:
        for r in ranges:
            if r[0] <= id <= r[1]:
                result += 1
                break
    return result


print(f"Part 1 Test: {part1(test_data)}")
print(f"Part 1 Actual: {part1(actual_data)}")


def part2(data):
    ranges, ids = get_ranges_and_ids(data)
    ranges.sort()
    while True:
        merged = False
        for i in range(len(ranges) - 1):
            if ranges[i][1] >= ranges[i + 1][0] - 1:
                ranges[i][1] = max(ranges[i][1], ranges[i + 1][1])
                del ranges[i + 1]
                merged = True
                break
        if not merged:
            break

    result = 0
    for r in ranges:
        result += r[1] - r[0] + 1
    
    return result

print(f"Part 2 Test: {part2(test_data)}")
print(f"Part 2 Actual: {part2(actual_data)}")
