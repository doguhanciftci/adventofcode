def part1():
    h = 0
    d = 0
    f = open('input.txt', 'r')
    for line in f:
        command, value = line.strip().split(' ')
        if command == 'forward':
            h += int(value)
        elif command == 'down':
            d += int(value)
        elif command == 'up':
            d -= int(value)
        else:
            continue
    f.close()
    print(h, d)
    print(h * d)


def part2():
    h = 0
    d = 0
    a = 0
    f = open('input.txt', 'r')
    for line in f:
        command, value = line.strip().split(' ')
        if command == 'forward':
            h += int(value)
            d += a * int(value)
        elif command == 'down':
            a += int(value)
        elif command == 'up':
            a -= int(value)
        else:
            continue
    f.close()
    print(h, d)
    print(h * d)


part2()