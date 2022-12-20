def shoot(dx, dy, xmin, xmax, ymin, ymax):
    x, y = 0, 0
    top_y = 0
    while True:
        x += dx
        y += dy
        if y > top_y:
            top_y = y
        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1
        dy -= 1
        # print(x, y, dx, dy)
        if xmin <= x <= xmax and ymin <= y <= ymax:
            return top_y
        if x >= xmax:
            return -1
        if y < ymin:
            return -1


xmin = 150
xmax = 193
ymin = -136
ymax = -86


def part1():
    tops = []

    for dx in range(-300, 300):
        for dy in range(-300, 300):
            top = shoot(dx, dy, xmin, xmax, ymin, ymax)
            if top >= 0:
                tops.append((dx, dy, top))

    print(tops)
    print('len:', len(tops))
    print('minx:', min(tops, key=lambda x: x[0])[0])
    print('maxx:', max(tops, key=lambda x: x[0])[0])
    print('miny:', min(tops, key=lambda x: x[1])[1])
    print('maxy:', max(tops, key=lambda x: x[1])[1])
    print(max(tops, key=lambda x: x[2]))


part1()


def part2():
    result = 0
    for dx, dy in velocities:
        top = shoot(dx, dy, xmin, xmax, ymin, ymax)
        if top >= 0:
            result += 1
    print(result)
