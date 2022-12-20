import numpy as np

input_easy = '''5483143223
                2745854711
                5264556173
                6141336146
                6357385478
                4167524645
                2176841721
                6882881134
                4846848554
                5283751526'''

input = '''2344671212
            6611742681
            5575575573
            3167848536
            1353827311
            4416463266
            2624761615
            1786561263
            3622643215
            4143284653'''


def tryToAdd(grid, x_param, y_param):
    if 0 <= x_param <= 9 and 0 <= y_param <= 9:
        grid[x_param, y_param] += 1


def part1(input, step):
    grid = [list(i.strip()) for i in input.split('\n')]
    grid = np.array(grid, dtype=int)
    flashes = 0
    for s in range(step):
        grid += 1
        flashed_x = []
        flashed_y = []
        while len(grid[grid > 9]) > 0:
            arr_x, arr_y = np.where(grid > 9)
            flashed_x += list(arr_x)
            flashed_y += list(arr_y)
            for i in range(len(arr_x)):
                x = arr_x[i]
                y = arr_y[i]
                grid[x, y] -= 10
                flashes += 1
                tryToAdd(grid, x - 1, y - 1)
                tryToAdd(grid, x - 1, y)
                tryToAdd(grid, x - 1, y + 1)
                tryToAdd(grid, x, y - 1)
                tryToAdd(grid, x, y + 1)
                tryToAdd(grid, x + 1, y - 1)
                tryToAdd(grid, x + 1, y)
                tryToAdd(grid, x + 1, y + 1)
        if len(flashed_x) > 0:
            grid[flashed_x, flashed_y] = 0
        print('step ', s)
        print(grid)
        if np.count_nonzero(grid) == 0:
            return s + 1
    print()
    return flashes


# result = part1(input_easy, 100)
# print('result is', result)

result = part1(input, 10000)
print('result is', result)
