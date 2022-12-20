def part1():

    f = open('input.txt', 'r')

    line = f.readline().strip()
    print(line)
    measurement = int(line)

    result = 0

    for line in f:
        line = line.strip()
        print(line)
        try:
            next_measurement = int(line)
        except ValueError:
            continue
        if next_measurement > measurement:
            result += 1
        measurement = next_measurement

    f.close()

    print(f'\nResult is: {result}')

part1()

def part2():
    f = open('input.txt', 'r')

    measurements = []

    for line in f:
        line = int(line.strip())
        measurements.append(line)
    print(measurements)

    windows = [0] * (len(measurements) - 2)
    n = len(measurements)
    for index in range(n):
        m = measurements[index]
        if index > 1:
            windows[index - 2] += m
        if 0 < index < n - 1:
            windows[index - 1] += m
        if index < n - 2:
            windows[index] += m

    print(windows)

    prev = windows[0]
    next = windows[0]
    result = 0
    for w in range(len(windows)):
        if w == 0:
            continue
        next = windows[w]
        if next > prev:
            result += 1
        prev = next

    print(f'\nResult is: {result}')
