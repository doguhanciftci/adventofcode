import numpy as np


def part1(filename):
    file = open(filename, 'r')
    start = file.readline().strip()
    file.readline()
    dict = {}
    for line in file:
        key, value = line.split(' -> ')
        dict[key] = value.strip()
    # print(start)
    # print(dict)
    for n in range(40):
        result = ''
        for i in range(len(start) - 1):
            result += start[i] + dict[start[i:i + 2]]
        result += start[-1]
        start = result
        # print(f'After step {n+1}: {result}')
        print(n)
    chars, counts = np.unique(list(result), return_counts=True)
    return max(counts) - min(counts)


# result = part1('ex1.txt')
# print('result is', result)

def part2(filename):
    file = open(filename, 'r')
    start = file.readline().strip()
    file.readline()
    dict = {}
    for line in file:
        key, value = line.split(' -> ')
        dict[key] = value.strip()
    # print(start)
    # print(dict)
    char_counts = {k: start.count(k) for k in dict.values()}
    empty_counts = {v: 0 for v in dict.keys()}
    counts = empty_counts.copy()
    tuples = []
    for i in range(len(start) - 1):
        tuple = start[i:i + 2]
        tuples.append(tuple)
        counts[tuple] += 1
    tuple_dict = {}
    for t in dict.keys():
        mid = dict[t]
        tuple_dict[t] = [t[0] + mid, mid + t[1]]
    for n in range(40):
        new_counts = empty_counts.copy()
        for k, v in counts.items():
            if v == 0:
                continue
            new1, new2 = tuple_dict[k]
            new_counts[new1] += v
            new_counts[new2] += v
            char_counts[dict[k]] += v
        counts = new_counts
        print(f'After step {n + 1}:')
    # chars, counts = np.unique(list(result), return_counts=True)
    return max(char_counts.values()) - min(char_counts.values())


result = part2('input.txt')
print('result is', result)
