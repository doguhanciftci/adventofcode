def part1(filename):
    file = open(filename, 'r')
    map = {}
    for line in file:
        k, v = line.strip().split('-')
        dest = map.get(k, [])
        dest.append(v)
        map[k] = dest
    print(map)

    print(filename)


result = part1('input_easy.txt')
print('result is', result)
